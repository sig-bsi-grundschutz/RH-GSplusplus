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

## Workflow: adding or updating an implementation answer

The primary way to add or update an implementation answer is the
[`enrich-component-implementation`](../.cursor/skills/enrich-component-implementation/SKILL.md)
skill, not hand-editing markdown. It drafts honest German prose, evaluates coverage, sets
implementation status, and opens a PR — a human never edits the file directly for a first draft.

### 1. Run the skill for one control or a set of controls

```
Enrich BER.2.4 for rhel9-gsplusplus-host
Enrich KONF.2.1, KONF.2.2 and DET.3.1.4 for rhel9-gsplusplus-host
```

For a control already in scope with existing component markdown, the skill enriches that file
in place. For a control **not yet in scope**, the skill first creates the profile markdown
(`authoring/profile/…/{control-id}.md`) and a component markdown stub
(`authoring/component/…/{control-id}.md`, status `planned`) — see "Step 0" in
[SKILL.md](../.cursor/skills/enrich-component-implementation/SKILL.md) — before drafting prose.

Each control gets its **own branch and PR** (`cursor/implement-{control-id}`) unless you
explicitly ask the skill to batch several controls into one PR. The PR body includes a coverage
matrix, documentation sources, and any additional CaC rules the skill found but did not attach
(see below).

*(Optional, exploratory)* To see the full unreviewed candidate pool before picking controls to
enrich:

```bash
python3 scripts/export_review_candidates.py --write
```

Writes `authoring/candidates/rhel-host/{KONF,BER,DET}/…` with catalog statement text and
`x-review-status: pending` front matter. These files are **not** assembled into OSCAL and are
purely a browsing aid.

### 2. Review the PR

A human reviews the drafted prose, coverage matrix, and implementation status against the linked
Red Hat documentation. Fix wording directly on the PR branch if needed.

### 3. Attaching a CaC rule

**Editing `### Rules:` in the component markdown does nothing.** Trestle treats that heading as
read-only display (`trestle.common.const.RULES_WARNING`) — `component-assemble` never writes
markdown-list edits back into OSCAL. This was verified directly: adding a rule bullet and
re-running `assemble_oscal.py` left the assembled JSON unchanged.

If the skill's "Suggested additional CaC rules" (or your own review) identifies a rule that
should be attached, a human edits the assembled OSCAL file by hand:

1. Open `component-definitions/rhel9-gsplusplus-host/component-definition.json`.
2. Find the matching entry: `component-definition.components[].control-implementations[].implemented-requirements[]`
   where `control-id` equals the target control (e.g. `"BER.2.4"`).
3. Add one `props` entry per rule:

   ```json
   {
     "name": "Rule_Id",
     "ns": "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd",
     "value": "audit_rules_usergroup_modification_passwd"
   }
   ```

   Keep the existing `implementation-status` prop; add one `Rule_Id` prop per rule (a control can
   have several).
4. Commit this JSON edit on the same PR branch, alongside the markdown changes. It is safe against
   future `assemble_oscal.py` runs — trestle preserves props it doesn't manage.
5. Re-run `python3 scripts/assemble_oscal.py --product rhel9 && python3 -m trestle validate -a`
   locally to confirm no drift or validation errors before merging.

This manual step is deliberate: a `Rule_Id` claims a specific ComplianceAsCode rule genuinely
covers the control, so it stays a reviewer decision rather than something the skill or a script
attaches automatically.

### 4. Merge

CI re-runs `assemble_oscal.py` and fails on drift between `authoring/` + the manually-maintained
`Rule_Id` props and the committed `profiles/` / `component-definitions/` output, so the PR must
already contain the fully assembled result.

## Rules

- **No bulk synthetic answers** — only controls with profile + component markdown appear in OSCAL.
- **Candidate pool ≠ profile** — 331 KONF/BER/DET controls are review candidates; inclusion requires explicit profile markdown (the skill creates this automatically when enriching a new control).
- **Subsystems** — `mappings/shared/components/rhel-host.json` defines three components (hardening, identity, audit); `assemble_oscal.py` ensures their skeleton exists in the component definition.
- **Excluded controls** — simply omit from `authoring/profile/`; optional notes in candidate markdown front matter (`x-review-status: excluded`).
- **`Rule_Id` is manually maintained** in `component-definitions/…/component-definition.json` (see Step 3) — it is not derived from markdown.

## Suggested review order

1. Mark obvious non-host controls as excluded in candidate front matter (or skip).
2. Include OS-core areas: `KONF.2.*`, `KONF.4–7.*`, `BER.3–7.*`, `DET.3.*` (exclude e.g. `KONF.2.6` MDM/Endgeräte).
3. Defer application-layer KONF (`KONF.10–15`) unless the host runs that stack.
4. Run the `enrich-component-implementation` skill on the selected controls; attach `Rule_Id` props by hand (Step 3) only where CaC rules genuinely map.

## Reference

- [compliance-trestle-agile-authoring](https://github.com/oscal-compass/compliance-trestle-agile-authoring)
- [enrich-component-implementation skill](../.cursor/skills/enrich-component-implementation/SKILL.md)
- [docs/ARCHITECTURE.md](ARCHITECTURE.md)
