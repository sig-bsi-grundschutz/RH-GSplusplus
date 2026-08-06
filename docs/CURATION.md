# RHEL host control curation (trestle agile authoring)

Human review and OSCAL generation use **[compliance-trestle](https://github.com/oscal-compass/compliance-trestle) agile authoring** — not a parallel JSON registry.

## Layout

| Path | Role |
|------|------|
| `mappings/shared/scope/rhel-host.json` | **Candidate pool** — KONF/BER/DET kernel controls (331) |
| `authoring/profile/rhel9-gsplusplus-host/` | **Profile scope** — one markdown file per included control |
| `authoring/component/rhel9-gsplusplus-host/` | **Implementation answers** — trestle component markdown |
| `authoring/candidates/rhel-host/` | **Review queue** — generated, not assembled (run export script) |
| `profiles/…/profile.json` | Assembled OSCAL profile — regenerated **manually on each PR branch, right before merge** (see Step 3); no CI job assembles or gates on this |
| `component-definitions/…/` | Assembled OSCAL component definition — same as above; `Rule_Id` props are hand-added to this file at the same time (see Step 3) |

## Workflow: adding or updating an implementation answer

The primary way to add or update an implementation answer is the
[`enrich-component-implementation`](../.cursor/skills/enrich-component-implementation/SKILL.md)
skill, not hand-editing markdown. It drafts honest German prose, evaluates coverage, sets
implementation status, and opens a PR — a human never edits the file directly for a first draft.

### 0. Triage the review queue

Before enriching a control, it must be decided `included` in
`authoring/candidates/rhel-host/{area}/{control-id}.md`. Use the
[`review-candidate-controls`](../.cursor/skills/review-candidate-controls/SKILL.md) skill to work
through an area (e.g. `Review BER.5.* candidates`): it classifies each control as
`included`/`excluded`/`pending` and writes a one-line German rationale in `## Review`. This step
only edits candidate markdown — nothing is committed automatically, matching the existing
`Control Selection {AREA}.*` commit history.

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

The skill's own commit only adds the two markdown files — `profiles/…/profile.json` and
`component-definitions/…/component-definition.json` are added later, on the same branch, in
Step 3, right before merge.

**Merge queue discipline:** several of these PRs can be open and reviewed in parallel, but process
Step 3 (assemble + merge) for **one PR at a time, in order**, always rebasing onto the
then-current `main` first. Because those two JSON files are large generated aggregates, letting
several PRs assemble against different, older snapshots of `main` produces large, overlapping
conflicts on rebase (this has happened repeatedly — see the recurring BER.3.x conflicts). Doing it
one at a time keeps each PR's diff to just its own new entry plus the `last-modified` timestamp —
small enough that `git config rerere.enabled true` (already on in this repo) auto-resolves the
repeat conflict shape on sight after the first manual resolution.

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

### 3. Assemble, attach rules, and merge (one PR at a time)

Before merging, rebase the PR branch onto the then-current `main` first — don't run this against a
stale base, or the resulting diff (and any later rebase) is unnecessarily large. Process PRs
**one at a time, in this order**, never in parallel, so each one's assembled diff stays small (new
entry + `last-modified` timestamp) and `rerere` (see below) can absorb the repeat conflict shape.

1. `git rebase main` on the PR branch (resolve any markdown conflicts — rare, since each control
   has its own file).
2. Run `python3 scripts/assemble_oscal.py --product rhel9`. This regenerates
   `profiles/…/profile.json` and `component-definitions/…/component-definition.json` against the
   now-current `main`, including a stub `implemented-requirement` for this control.
3. **Editing `### Rules:` in the component markdown does nothing.** Trestle treats that heading as
   read-only display (`trestle.common.const.RULES_WARNING`) — `component-assemble` never writes
   markdown-list edits back into OSCAL (verified directly: adding a rule bullet and re-running
   `assemble_oscal.py` left the assembled JSON unchanged). If the skill's "Suggested additional CaC
   rules" (or your own review) identifies a rule that should be attached, edit the assembled OSCAL
   file by hand instead:
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

      Keep the existing `implementation-status` prop; add one `Rule_Id` prop per rule (a control
      can have several).
4. Re-run `python3 scripts/assemble_oscal.py --product rhel9 && python3 -m trestle validate -a` to
   confirm the hand-added `Rule_Id` props survive re-assembly (trestle preserves props it doesn't
   manage) and there's no drift or validation error.
5. Commit `profiles/…/profile.json` and `component-definitions/…/component-definition.json` on the
   PR branch, alongside the markdown, and push.
6. Merge the PR, then move on to the next one — rebase it onto the now-updated `main` before
   repeating this step for it.

This manual step is deliberate: a `Rule_Id` claims a specific ComplianceAsCode rule genuinely
covers the control, so it stays a reviewer decision rather than something a script attaches
automatically, and the assembled files stay a reviewer-controlled artifact rather than a CI
output.

**`rerere`:** this repo already has `rerere.enabled = true` (check with
`git config --get rerere.enabled`; if unset, `git config rerere.enabled true`). Because the same
control-insertion conflict shape recurs across PRs, once you've manually resolved it the first
time, `git rebase`/`git rerere status` will offer or auto-apply that resolution on the next PR's
conflict in the same file. Still re-run sub-step 4's validate (above) after any `rerere`-applied
resolution to confirm it produced correct JSON, not just conflict-marker-free JSON.

## Rules

- **No bulk synthetic answers** — only controls with profile + component markdown appear in OSCAL.
- **Candidate pool ≠ profile** — 331 KONF/BER/DET controls are review candidates; inclusion requires explicit profile markdown (the skill creates this automatically when enriching a new control).
- **Subsystems** — `mappings/shared/components/rhel-host.json` defines three components (hardening, identity, audit); `assemble_oscal.py` ensures their skeleton exists in the component definition.
- **Excluded controls** — simply omit from `authoring/profile/`; optional notes in candidate markdown front matter (`x-review-status: excluded`).
- **`Rule_Id` is manually maintained** in `component-definitions/…/component-definition.json` (see Step 3) — it is not derived from markdown.
- **No CI job assembles or gates on the OSCAL output** — Step 3 is a manual, sequential, one-PR-at-a-time process; `rerere` absorbs the repeat conflict shape it produces.

## Suggested review order

1. Mark obvious non-host controls as excluded in candidate front matter (or skip) — use the
   `review-candidate-controls` skill for this pass.
2. Include OS-core areas: `KONF.2.*`, `KONF.4–7.*`, `BER.3–7.*`, `DET.3.*` (exclude e.g. `KONF.2.6` MDM/Endgeräte).
3. Defer application-layer KONF (`KONF.10–15`) unless the host runs that stack.
4. Run the `enrich-component-implementation` skill on the selected controls; assemble, attach `Rule_Id` props by hand, and merge one PR at a time (Step 3) — only attach rules where they genuinely map.

## Reference

- [compliance-trestle-agile-authoring](https://github.com/oscal-compass/compliance-trestle-agile-authoring)
- [review-candidate-controls skill](../.cursor/skills/review-candidate-controls/SKILL.md)
- [enrich-component-implementation skill](../.cursor/skills/enrich-component-implementation/SKILL.md)
- [docs/ARCHITECTURE.md](ARCHITECTURE.md)
