"""Shared scope and catalog helpers for OSCAL authoring."""
from __future__ import annotations

import json
from pathlib import Path

KERNEL_PREFIX = "BSI-Stand-der-Technik-Kernel"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


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


def catalog_by_id(catalog_path: Path) -> dict[str, dict]:
    return {c["id"]: c for c in load_catalog_controls(catalog_path)}


def is_kernel_control(control_class: str | None, prefix: str = KERNEL_PREFIX) -> bool:
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


def compute_scope_candidates(scope: dict, catalog_controls: list[dict]) -> dict[str, dict]:
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
        candidates[cid] = ctrl
    return dict(sorted(candidates.items(), key=lambda item: control_sort_key(item[0])))


def control_statement_prose(ctrl: dict) -> str:
    for part in ctrl.get("parts") or []:
        if part.get("name") == "statement":
            prose = part.get("prose")
            if prose:
                return prose.strip()
        for sub in part.get("parts") or []:
            if sub.get("prose"):
                return sub["prose"].strip()
    return ""


def profile_control_ids(profile_doc: dict) -> list[str]:
    imports = profile_doc.get("profile", profile_doc).get("imports") or []
    ids: list[str] = []
    for imp in imports:
        for block in imp.get("include-controls") or []:
            ids.extend(block.get("with-ids") or [])
    return sorted(set(ids), key=control_sort_key)
