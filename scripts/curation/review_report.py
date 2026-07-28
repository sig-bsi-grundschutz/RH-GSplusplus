#!/usr/bin/env python3
"""Print curation progress and optionally export a human review queue."""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from registry import (
    compute_candidates,
    control_sort_key,
    load_catalog_controls,
    load_json,
    practice_area,
    registry_summary,
    repo_root,
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
        "--markdown",
        type=Path,
        help="Write pending controls as markdown checklist for review",
    )
    args = parser.parse_args()
    root = repo_root()
    scope = load_json(root / args.scope)
    registry_path = root / f"mappings/shared/curation/{scope['id']}.json"
    if not registry_path.is_file():
        raise SystemExit(f"Missing {registry_path}; run scripts/curation/init_registry.py --write")

    registry = load_json(registry_path)
    candidates = compute_candidates(scope, load_catalog_controls(root / args.catalog))
    summary = registry_summary(registry)
    total = len(candidates)

    print(f"Curation registry: {registry_path.relative_to(root)}")
    print(f"Candidates: {total}")
    print(
        f"  pending={summary['pending']}  included={summary['included']}  "
        f"excluded={summary['excluded']}  reviewed={summary['included'] + summary['excluded']}"
    )
    if summary["pending"]:
        pct = round(100 * (summary["included"] + summary["excluded"]) / total, 1)
        print(f"  review progress: {pct}%")

    by_area: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for cid, entry in registry["controls"].items():
        by_area[practice_area(cid)][entry.get("status", "other")] += 1

    print("\nBy practice area:")
    for area in sorted(by_area):
        counts = by_area[area]
        print(
            f"  {area}: pending={counts.get('pending', 0)} "
            f"included={counts.get('included', 0)} excluded={counts.get('excluded', 0)}"
        )

    if args.markdown:
        lines = [
            "# RHEL host control review queue",
            "",
            f"Scope: `{scope['id']}` — edit `mappings/shared/curation/{scope['id']}.json`",
            "",
            "For each control: set `status` to `included` or `excluded`.",
            "Included controls need a curated `statement` or explicit `use_default_template: true`.",
            "",
            "## Pending controls",
            "",
        ]
        pending = [
            (cid, registry["controls"][cid])
            for cid in sorted(registry["controls"], key=control_sort_key)
            if registry["controls"][cid].get("status") == "pending"
        ]
        current_area = None
        for cid, entry in pending:
            area = practice_area(cid)
            if area != current_area:
                lines.extend(["", f"### {area}", ""])
                current_area = area
            title = entry.get("title") or candidates.get(cid, {}).get("title") or ""
            component = entry.get("default_component") or "?"
            lines.append(f"- [ ] **{cid}** — {title} _(default: {component})_")

        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\nWrote {args.markdown} ({len(pending)} pending controls)")


if __name__ == "__main__":
    main()
