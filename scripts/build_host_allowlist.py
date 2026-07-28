#!/usr/bin/env python3
"""Build or verify RHEL host allowlist slice and control mappings from scope rules."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

KERNEL_PREFIX = "BSI-Stand-der-Technik-Kernel"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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


def compute_allowlist(scope: dict, catalog_controls: list[dict]) -> list[str]:
    prefix = scope["kernel_class_prefix"]
    allow = set(scope["practice_area_allowlist"])
    component_map = scope["component_by_practice_area"]
    missing_components = allow - set(component_map)
    if missing_components:
        raise SystemExit(
            f"Scope {scope['id']!r} missing component_by_practice_area for: {sorted(missing_components)}"
        )

    selected: list[str] = []
    for ctrl in catalog_controls:
        cid = ctrl["id"]
        if practice_area(cid) not in allow:
            continue
        if not is_kernel_control(ctrl.get("class"), prefix):
            raise SystemExit(
                f"Control {cid} is in practice area allowlist but has class {ctrl.get('class')!r}; "
                f"expected {prefix} or {prefix}-*"
            )
        selected.append(cid)

    return sorted(selected, key=_control_sort_key)


def _control_sort_key(control_id: str) -> tuple:
    parts: list[tuple[int, str]] = []
    for segment in control_id.split("."):
        if segment.isdigit():
            parts.append((0, f"{int(segment):08d}"))
        else:
            parts.append((1, segment))
    return tuple(parts)


def load_tier1_overrides(root: Path, scope: dict) -> dict[str, dict]:
    rel = scope.get("tier1_overrides_relative_path")
    if not rel:
        return {}
    path = root / rel
    if not path.is_file():
        return {}
    doc = load_json(path)
    return doc.get("controls") or {}


def build_controls_doc(
    scope: dict,
    control_ids: list[str],
    tier1_overrides: dict[str, dict],
) -> dict:
    component_map = scope["component_by_practice_area"]
    controls: dict[str, dict] = {}
    for cid in control_ids:
        pa = practice_area(cid)
        entry: dict = {
            "component": component_map[pa],
            "tier": 2,
        }
        override = tier1_overrides.get(cid)
        if override:
            entry.update({k: v for k, v in override.items() if k != "component" or v})
            if override.get("component"):
                entry["component"] = override["component"]
            entry["tier"] = override.get("tier", 1)
        controls[cid] = entry
    return {"controls": controls}


def build_slice_doc(scope: dict, control_ids: list[str]) -> dict:
    return {
        "id": scope["id"],
        "description": scope["description"],
        "scope_relative_path": "mappings/shared/scope/rhel-host.json",
        "control_ids": control_ids,
    }


def write_json(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        default="mappings/shared/scope/rhel-host.json",
        help="Scope rules JSON (default: RHEL host)",
    )
    parser.add_argument(
        "--catalog",
        default="catalogs/bsi-grundschutz-plus-plus/catalog.json",
        help="Vendored BSI catalog path",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write slice and controls JSON under mappings/shared/",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if committed slice/controls differ from computed output",
    )
    args = parser.parse_args()
    root = repo_root()
    scope = load_json(root / args.scope)
    catalog_controls = load_catalog_controls(root / args.catalog)
    control_ids = compute_allowlist(scope, catalog_controls)
    tier1 = load_tier1_overrides(root, scope)
    slice_doc = build_slice_doc(scope, control_ids)
    controls_doc = build_controls_doc(scope, control_ids, tier1)

    slice_path = root / "mappings" / "shared" / "slices" / f"{scope['id']}.json"
    controls_path = root / "mappings" / "shared" / "controls" / f"{scope['id']}.json"

    if args.write:
        write_json(slice_path, slice_doc)
        write_json(controls_path, controls_doc)
        print(f"Wrote {slice_path} ({len(control_ids)} controls)")
        print(f"Wrote {controls_path} ({len(controls_doc['controls'])} mappings, {len(tier1)} Tier-1 overrides)")

    if args.check:
        for path, expected in ((slice_path, slice_doc), (controls_path, controls_doc)):
            if not path.is_file():
                print(f"Missing {path}", file=sys.stderr)
                raise SystemExit(1)
            actual = load_json(path)
            if actual != expected:
                print(f"Drift in {path}; run scripts/build_host_allowlist.py --write", file=sys.stderr)
                raise SystemExit(1)
        print(f"Allowlist check OK ({len(control_ids)} controls)")

    if not args.write and not args.check:
        print(json.dumps({"control_count": len(control_ids), "control_ids": control_ids}, indent=2))


if __name__ == "__main__":
    main()
