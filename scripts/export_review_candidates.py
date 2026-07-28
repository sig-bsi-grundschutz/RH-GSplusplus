#!/usr/bin/env python3
"""Export scope candidate controls as markdown review queue (not assembled into OSCAL)."""
from __future__ import annotations

import argparse
from pathlib import Path

from oscal_scope import (
    compute_scope_candidates,
    control_sort_key,
    control_statement_prose,
    load_catalog_controls,
    load_json,
    practice_area,
    profile_control_ids,
    repo_root,
)


def _profile_included(root: Path, config: dict) -> set[str]:
    profile_path = root / config["profile_output_path"]
    if not profile_path.is_file():
        return set()
    return set(profile_control_ids(load_json(profile_path)))


def _candidate_markdown(
    control_id: str,
    ctrl: dict,
    default_component: str,
    included: bool,
) -> str:
    title = (ctrl.get("title") or "").strip()
    statement = control_statement_prose(ctrl)
    status = "included" if included else "pending"
    lines = [
        "---",
        "x-trestle-global:",
        "  catalog:",
        f"    title: {title}",
        "x-review-status: " + status,
        f"x-default-component: {default_component}",
        "---",
        "",
        f"# {control_id} — {title}",
        "",
        "## Control Statement",
        "",
        statement or "_No statement prose in catalog._",
        "",
        "## Review",
        "",
        "<!-- Human review queue — not assembled into OSCAL until promoted. -->",
        "<!-- x-review-status: pending | included | excluded -->",
        "<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->",
        "<!-- See docs/CURATION.md -->",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", default="rhel9")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    config = load_json(root / "mappings" / args.product / "artifact.json")
    scope = load_json(root / config["scope_relative_path"])
    candidates = compute_scope_candidates(
        scope, load_catalog_controls(root / config["catalog_relative_path"])
    )
    included = _profile_included(root, config)
    out_dir = root / config.get("authoring_candidates_dir", "authoring/candidates/rhel-host")

    pending = [cid for cid in candidates if cid not in included]
    if args.write:
        for cid in candidates:
            ctrl = candidates[cid]
            area = practice_area(cid)
            path = out_dir / area / f"{cid}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            default_comp = scope["component_by_practice_area"].get(area, "")
            path.write_text(
                _candidate_markdown(cid, ctrl, default_comp, cid in included),
                encoding="utf-8",
            )
        print(f"Wrote {len(candidates)} candidate files to {out_dir} ({len(pending)} pending)")
    else:
        print(f"Candidates: {len(candidates)}  in profile: {len(included)}  pending: {len(pending)}")


if __name__ == "__main__":
    main()
