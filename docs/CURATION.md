# RHEL host control curation (trestle agile authoring)

Human review and OSCAL generation use **[compliance-trestle](https://github.com/oscal-compass/compliance-trestle) agile authoring** — not a parallel JSON registry.

## Layout

| Path | Role |
|------|------|
| `mappings/shared/scope/rhel-host.json` | **Candidate pool** — KONF/BER/DET kernel controls (331) |
| `authoring/profile/rhel9-gsplusplus-host/` | **Profile scope** — one markdown file per included control |
| `authoring/component/rhel9-gsplusplus-host/` | **Implementation answers** — trestle component markdown |
| `authoring/candidates/rhel-host/` | **Review queue** — generated, not assembled (run export script) |
| `profiles/…/profile.json` | Assembled OSCAL profile (CI output) |
| `component-definitions/…/` | Assembled OSCAL component definition (CI output) |

## Workflow

### 1. Review candidates (optional export)

```bash
python3 scripts/export_review_candidates.py --write
```

Writes `authoring/candidates/rhel-host/{KONF,BER,DET}/…` with catalog statement text and
`x-review-status: pending` front matter. These files are **not** assembled into OSCAL.

### 2. Include a control in scope

Add or edit markdown under `authoring/profile/rhel9-gsplusplus-host/{area}/{control}.md`.
Use trestle profile conventions (see [trestle authoring tutorial](https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring)).

To bootstrap from the candidate queue, copy a candidate file into the profile tree and adjust.

Regenerate profile markdown from the current OSCAL profile (optional):

```bash
python3 -m trestle author profile-generate -n rhel9-gsplusplus-host \
  -o authoring/profile/rhel9-gsplusplus-host
```

### 3. Write the implementation answer

Edit the matching file under `authoring/component/rhel9-gsplusplus-host/` — section
**“What is the solution and how is it implemented?”**, `Implementation Status`, and
`### Rules:` (OpenSCAP rule short names).

Regenerate component markdown after adding subsystem skeletons:

```bash
python3 -m trestle author component-generate -n rhel9-gsplusplus-host \
  -o authoring/component/rhel9-gsplusplus-host
```

### 4. Assemble and validate

```bash
python3 scripts/assemble_oscal.py --product rhel9
python3 -m trestle validate -a
```

CI runs the same assemble step and fails on drift in `profiles/` and `component-definitions/`.

## Rules

- **No bulk synthetic answers** — only controls with profile + component markdown appear in OSCAL.
- **Candidate pool ≠ profile** — 331 KONF/BER/DET controls are review candidates; inclusion requires explicit profile markdown.
- **Subsystems** — `mappings/shared/components/rhel-host.json` defines three components (hardening, identity, audit); `assemble_oscal.py` ensures their skeleton exists in the component definition.
- **Excluded controls** — simply omit from `authoring/profile/`; optional notes in candidate markdown front matter (`x-review-status: excluded`).

## Suggested review order

1. Mark obvious non-host controls as excluded in candidate front matter (or skip).
2. Include OS-core areas: `KONF.2.*`, `KONF.4–7.*`, `BER.3–7.*`, `DET.3.*`.
3. Defer application-layer KONF (`KONF.10–15`) unless the host runs that stack.
4. Add OpenSCAP `Rule_Id` entries only where CaC rules genuinely map.

## Reference

- [compliance-trestle-agile-authoring](https://github.com/oscal-compass/compliance-trestle-agile-authoring)
- [docs/ARCHITECTURE.md](ARCHITECTURE.md)
