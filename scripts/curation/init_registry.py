#!/usr/bin/env python3
"""Initialize or update the human curation registry from scope candidates."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from registry import (
    compute_candidates,
    init_registry_doc,
    load_catalog_controls,
    load_json,
    load_seed_included,
    merge_registry,
    repo_root,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        default="mappings/shared/scope/rhel-host.json",
        help="Scope rules JSON",
    )
    parser.add_argument(
        "--catalog",
        default="catalogs/bsi-grundschutz-plus-plus/catalog.json",
        help="Vendored BSI catalog path",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write curation registry JSON",
    )
    args = parser.parse_args()
    root = repo_root()
    scope = load_json(root / args.scope)
    candidates = compute_candidates(scope, load_catalog_controls(root / args.catalog))
    seeded = load_seed_included(root, scope)
    registry_path = root / f"mappings/shared/curation/{scope['id']}.json"
    fresh = init_registry_doc(scope, candidates, seeded)

    if registry_path.is_file():
        existing = load_json(registry_path)
        registry = merge_registry(existing, fresh)
        action = "Updated"
    else:
        registry = fresh
        action = "Created"

    if args.write:
        write_json(registry_path, registry)
        summary = {
            status: sum(1 for e in registry["controls"].values() if e.get("status") == status)
            for status in ("pending", "included", "excluded")
        }
        print(f"{action} {registry_path} ({len(registry['controls'])} candidates)")
        print(
            f"  pending={summary['pending']} included={summary['included']} excluded={summary['excluded']}"
        )
    else:
        print(json.dumps(
            {
                "path": str(registry_path.relative_to(root)),
                "candidate_count": len(registry["controls"]),
                "included": sum(
                    1 for e in registry["controls"].values() if e.get("status") == "included"
                ),
            },
            indent=2,
        ))


if __name__ == "__main__":
    main()
