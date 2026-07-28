"""Shared helpers for RHEL host control curation."""
from __future__ import annotations

import json
from pathlib import Path

KERNEL_PREFIX = "BSI-Stand-der-Technik-Kernel"
VALID_STATUSES = {"pending", "included", "excluded"}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def walk_controls(controls: list[dict], out: list[dict]) -> None:
    for ctrl in controls:
        out.append(ctrl)
        walk_controls(ctrl.get("controls") or [], out)


def walk_groups(group: dict, out: list[dict]) -> None:
    walk_controls(group.get("controls") or [], out)
    for sub in group.get("groups") or []:
        walk_groups(sub, out)


def load_catalog_controls(catalog_path: Path) -> list[dict]:
    catalog = load_json(catalog_path)
    cat = catalog.get("catalog", catalog)
    controls: list[dict] = []
    for group in cat.get("groups") or []:
        walk_groups(group, controls)
    return controls


def is_kernel_control(control_class: str | None, prefix: str) -> bool:
    if not control_class:
        return False
    return control_class == prefix or control_class.startswith(f"{prefix}-")


def practice_area(control_id: str) -> str:
    return control_id.split(".", 1)[0]


def control_sort_key(control_id: str) -> tuple:
    parts: list[tuple[int, str]] = []
    for segment in control_id.split("."):
        if segment.isdigit():
            parts.append((0, f"{int(segment):08d}"))
        else:
            parts.append((1, segment))
    return tuple(parts)


def compute_candidates(scope: dict, catalog_controls: list[dict]) -> dict[str, dict]:
    prefix = scope["kernel_class_prefix"]
    allow = set(scope["practice_area_allowlist"])
    component_map = scope["component_by_practice_area"]
    missing = allow - set(component_map)
    if missing:
        raise SystemExit(
            f"Scope {scope['id']!r} missing component_by_practice_area for: {sorted(missing)}"
        )

    candidates: dict[str, dict] = {}
    for ctrl in catalog_controls:
        cid = ctrl["id"]
        if practice_area(cid) not in allow:
            continue
        if not is_kernel_control(ctrl.get("class"), prefix):
            raise SystemExit(
                f"Control {cid} is in practice area allowlist but has class {ctrl.get('class')!r}"
            )
        candidates[cid] = {
            "title": (ctrl.get("title") or "").strip(),
            "class": ctrl.get("class"),
            "default_component": component_map[practice_area(cid)],
        }
    return dict(sorted(candidates.items(), key=lambda item: control_sort_key(item[0])))


def default_registry_path(scope: dict) -> str:
    return f"mappings/shared/curation/{scope['id']}.json"


def load_seed_included(root: Path, scope: dict) -> dict[str, dict]:
    rel = scope.get("seed_included_relative_path")
    if not rel:
        return {}
    path = root / rel
    if not path.is_file():
        return {}
    doc = load_json(path)
    seeded: dict[str, dict] = {}
    for cid, mapping in (doc.get("controls") or {}).items():
        entry = {"status": "included", "component": mapping["component"], "tier": mapping.get("tier", 1)}
        for key in ("statement", "implementation_status", "doc_keys", "rule_ids", "use_default_template"):
            if key in mapping:
                entry[key] = mapping[key]
        seeded[cid] = entry
    return seeded


def init_registry_doc(scope: dict, candidates: dict[str, dict], seeded: dict[str, dict]) -> dict:
    controls: dict[str, dict] = {}
    for cid, meta in candidates.items():
        if cid in seeded:
            controls[cid] = {
                "title": meta["title"],
                "status": "included",
                **{k: v for k, v in seeded[cid].items() if k != "status"},
            }
        else:
            controls[cid] = {
                "title": meta["title"],
                "status": "pending",
                "default_component": meta["default_component"],
            }
    return {
        "scope_id": scope["id"],
        "scope_relative_path": f"mappings/shared/scope/{scope['id']}.json",
        "description": (
            "Human curation registry for RHEL host scope. Set status to included or excluded "
            "before generating OSCAL. Included controls require a curated statement or "
            "use_default_template: true."
        ),
        "controls": controls,
    }


def merge_registry(existing: dict, fresh: dict) -> dict:
    """Preserve human edits; add new candidates as pending; refresh titles."""
    merged = dict(fresh)
    merged_controls = dict(fresh["controls"])
    for cid, entry in (existing.get("controls") or {}).items():
        if cid in merged_controls:
            merged_controls[cid] = entry
            if cid in fresh["controls"]:
                merged_controls[cid]["title"] = fresh["controls"][cid]["title"]
        else:
            merged_controls[cid] = entry
    merged["controls"] = dict(sorted(merged_controls.items(), key=lambda item: control_sort_key(item[0])))
    return merged


def validate_registry(scope: dict, registry: dict, candidates: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    controls = registry.get("controls") or {}
    missing = set(candidates) - set(controls)
    extra = set(controls) - set(candidates)
    if missing:
        errors.append(f"Registry missing {len(missing)} candidate controls (run init_registry.py --write)")
    if extra:
        errors.append(f"Registry has {len(extra)} controls not in candidate pool")

    for cid, entry in controls.items():
        status = entry.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{cid}: invalid status {status!r}")
            continue
        if status == "included":
            has_statement = bool((entry.get("statement") or "").strip())
            has_template = bool(entry.get("use_default_template"))
            if not has_statement and not has_template:
                errors.append(
                    f"{cid}: included control needs statement or use_default_template: true"
                )
            if not entry.get("component"):
                errors.append(f"{cid}: included control missing component")
        if status == "excluded" and not (entry.get("exclude_reason") or "").strip():
            errors.append(f"{cid}: excluded control should document exclude_reason")
    return errors


def included_controls(registry: dict) -> list[str]:
    controls = registry.get("controls") or {}
    return sorted(
        (cid for cid, entry in controls.items() if entry.get("status") == "included"),
        key=control_sort_key,
    )


def build_controls_doc(registry: dict) -> dict:
    controls: dict[str, dict] = {}
    for cid in included_controls(registry):
        entry = registry["controls"][cid]
        mapping: dict = {
            "component": entry["component"],
            "tier": entry.get("tier", 2),
        }
        if entry.get("use_default_template"):
            mapping["use_default_template"] = True
        for key in ("statement", "implementation_status", "doc_keys", "rule_ids"):
            if key in entry:
                mapping[key] = entry[key]
        controls[cid] = mapping
    return {"controls": controls}


def build_slice_doc(scope: dict, control_ids: list[str]) -> dict:
    return {
        "id": scope["id"],
        "description": scope["description"],
        "scope_relative_path": f"mappings/shared/scope/{scope['id']}.json",
        "curation_relative_path": default_registry_path(scope),
        "control_ids": control_ids,
    }


def registry_summary(registry: dict) -> dict[str, int]:
    counts = {"pending": 0, "included": 0, "excluded": 0, "other": 0}
    for entry in (registry.get("controls") or {}).values():
        status = entry.get("status")
        if status in counts:
            counts[status] += 1
        else:
            counts["other"] += 1
    return counts
