---
name: review-candidate-controls
description: >-
  Triage BSI Grundschutz++ candidate controls under authoring/candidates/rhel-host/{AREA}/ —
  decide included, excluded, or pending, and write a one-line German rationale. Use when the user
  asks to review, triage, or curate candidate controls, mentions "Control Selection" for an area
  (e.g. BER.5.*, KONF.4.*), or wants to work through the review queue described in
  docs/CURATION.md.
---

# Review Candidate Controls

Work through the **review queue** (`authoring/candidates/rhel-host/{AREA}/*.md`, one file per BSI
control) and decide, per control, whether it belongs in scope for a RHEL host. This is the triage
step **before** [`enrich-component-implementation`](../enrich-component-implementation/SKILL.md) —
it only classifies controls, it never writes profile or component markdown.

**Input:** an area or prefix (e.g. `BER.5.*`, `KONF.4`) or an explicit list of control IDs.
**Output:** edited candidate markdown files only (frontmatter `x-review-status` + `## Review`
rationale). Nothing is committed — the human commits, matching the existing history's
`Control Selection {AREA}.*` commits. Do not commit on the user's current branch (see workspace
git-safety rule); if asked to commit, create a separate branch first.

## Workflow

```
- [ ] 1. Resolve target files
- [ ] 2. Read each control's statement + existing review state
- [ ] 3. Classify: included / excluded / pending
- [ ] 4. Write rationale + update x-review-status
- [ ] 5. Summarize decisions for the user
```

### Step 1 — Resolve target files

Glob `authoring/candidates/rhel-host/{area}/{prefix}*.md` for the given area/prefix, or resolve
each explicit control ID to its file (search all three areas: `BER`, `KONF`, `DET`). Process a
whole area/prefix together in one pass, mirroring the existing commit granularity
(`Control Selection BER.4.*`).

Skip files whose `## Review` body already has non-empty rationale text **unless** the user
explicitly asks to re-review them.

### Step 2 — Read each file

Extract per file (see `scripts/export_review_candidates.py` for the generator):

- Control ID and title (`#` heading)
- **Control Statement** body — the only technical content available at this stage (no `## Control
  guidance` section exists yet in candidate files, unlike promoted profile/component markdown)
- Current `x-review-status` (frontmatter) and any existing `## Review` text

### Step 3 — Classify

Ask one question: **does the Control Statement describe something a RHEL host itself can
technically enforce or verify (even partially, even via IdM/Ansible Automation Platform), or is it
inherently a human/organizational process?**

| Decision | When | Example rationale (reuse this register, German, terse) |
|----------|------|----------------------------------------------------------|
| `included` | Statement maps to a local OS mechanism: accounts, permissions, crypto config, auth, logging, package/service state | `Relevant für RHEL`, `UID, accountnamen, relevant`, `Änderung, Löschung von lokalen Accounts` |
| `included` | Technical, but only partially verifiable, or only via central management | `Bei Management via Red Hat IdM oder Ansible Automation Platform kann dies (partiell) geprüft werden.` |
| `excluded` | Statement is a personnel/process/policy/contract matter with no host-level hook, even if it nominally touches the host | `Reines Organisationsthema, kein technischer Impact`, `organisatorischer Prozess`, `Organisatorische Maßnahme` |
| `excluded` | Statement targets central directory services / identity master data rather than the host itself | `Stammdatenprüfung betrifft eher zentrale Verzeichnisdienste und ist rein organisatorisch, selbst wenn es einen RHEL Host betreffen würde` |
| `pending` | Genuinely undecidable without more context (rare — prefer a decision) | Leave a short note on what's missing, e.g. `Je nach Guidance` when the guidance text needed to decide isn't in the candidate file yet |

Bias toward a decision (`included`/`excluded`) over `pending`. Reserve `pending` for cases where
you would otherwise guess.

Cross-reference `docs/CURATION.md`'s "Suggested review order" for area-level defaults (e.g.
`KONF.2.*`, `KONF.4–7.*`, `BER.3–7.*`, `DET.3.*` generally in scope; `KONF.10–15` app-layer,
usually deferred; MDM/Endgeräte controls like `KONF.2.6` excluded).

### Step 4 — Write the decision

Edit only two things per file:

1. Frontmatter `x-review-status:` → `included` | `excluded` | `pending`
2. `## Review` body — replace the (usually empty) line between the heading and the HTML comment
   block with the one-line rationale. Keep it short (matches existing style: sentence fragments,
   no trailing period required). Leave blank if the decision is truly self-evident and you have no
   substantive rationale to add — but prefer adding one, it's the artifact reviewers read later.

**Never touch:** frontmatter `title`/`x-default-component`, the `#` heading, `## Control
Statement`, or the four HTML comment lines at the bottom.

### Step 5 — Summarize

Report a table of `control-id | decision | rationale` for everything touched. Call out any
`included` controls so the user knows they're now candidates for the
`enrich-component-implementation` skill (that skill still needs profile + component markdown
created — this triage step doesn't do that).

## Example invocations

```
Review BER.5.* candidates
```

```
Do Control Selection for KONF.4.*
```

```
Triage DET.3.1, DET.3.2 and DET.3.3
```

## Additional resources

- [docs/CURATION.md](../../../docs/CURATION.md) — full curation workflow, review queue role
- [enrich-component-implementation skill](../enrich-component-implementation/SKILL.md) — next step for `included` controls
