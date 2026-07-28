#!/usr/bin/env python3
"""Build slice and control mappings from human-curated registry (included controls only)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "curation"))
from registry import (  # noqa: E402
    build_controls_doc,
    build_slice_doc,
    compute_candidates,
    included_controls,
    load_json,
    repo_root,
    validate_registry,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        default="mappings/shared/scope/rhel-host.json",
    )
    parser.add_argument(
        "--catalog",
        default="catalogs/bsi-grundschutz-plus-plus/catalog.json",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write slice and controls JSON from included registry entries",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if generated mappings differ from registry",
    )
    args = parser.parse_args()
    root = repo_root()
    scope = load_json(root / args.scope)
    registry_path = root / f"mappings/shared/curation/{scope['id']}.json"
    if not registry_path.is_file():
        raise SystemExit(f"Missing {registry_path}; run scripts/curation/init_registry.py --write")

    from registry import load_catalog_controls

    candidates = compute_candidates(scope, load_catalog_controls(root / args.catalog))
    registry = load_json(registry_path)
    errors = validate_registry(scope, registry, candidates)
    if errors:
        for err in errors[:20]:
            print(err, file=sys.stderr)
        if len(errors) > 20:
            print(f"... and {len(errors) - 20} more", file=sys.stderr)
        raise SystemExit(1)

    control_ids = included_controls(registry)
    slice_doc = build_slice_doc(scope, control_ids)
    controls_doc = build_controls_doc(registry)

    slice_path = root / "mappings" / "shared" / "slices" / f"{scope['id']}.json"
    controls_path = root / "mappings" / "shared" / "controls" / f"{scope['id']}.json"

    if args.write:
        write_json(slice_path, slice_doc)
        write_json(controls_path, controls_doc)
        print(f"Wrote {slice_path} ({len(control_ids)} included controls)")
        print(f"Wrote {controls_path}")

    if args.check:
        for path, expected in ((slice_path, slice_doc), (controls_path, controls_doc)):
            if not path.is_file():
                print(f"Missing {path}; run scripts/build_host_mappings.py --write", file=sys.stderr)
                raise SystemExit(1)
            actual = load_json(path)
            if actual != expected:
                print(f"Drift in {path}; run scripts/build_host_mappings.py --write", file=sys.stderr)
                raise SystemExit(1)
        pending = sum(1 for e in registry["controls"].values() if e.get("status") == "pending")
        print(
            f"Mappings check OK ({len(control_ids)} included, {pending} pending review, "
            f"{len(candidates)} candidates)"
        )

    if not args.write and not args.check:
        print(f"Included controls: {len(control_ids)}")


if __name__ == "__main__":
    main()
