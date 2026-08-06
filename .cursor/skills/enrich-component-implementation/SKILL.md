---
name: enrich-component-implementation
description: >-
  Enrich RH-GSplusplus trestle component markdown with German implementation
  prose from ComplianceAsCode rules and Red Hat documentation, evaluate coverage,
  set implementation status, and open a PR on a separate branch. Use when
  authoring or updating implementation answers under authoring/component/, or
  when the user asks to document how a GS++ control is implemented on RHEL.
---

# Enrich Component Implementation

Turn one or more trestle **component markdown** files into reviewed PRs with honest
implementation prose, coverage assessment, and optional CaC rule suggestions.

**Input:** one of:
- path to an existing file under `authoring/component/{artifact}/`, or
- one or more **control IDs** (e.g. `BER.2.4` or `KONF.2.1, DET.3.1.4`) for a given artifact
  (default `rhel9-gsplusplus-host`). If the control has no component markdown yet, Step 0 creates
  the stub (profile + component markdown) before enrichment.

**Output:** one branch + commit + PR **per control** (see batching note in Git safety). The skill's
own commit contains only markdown; human reviews before merge, then assembles, attaches CaC rules,
and merges — a separate manual step on the same branch, one PR at a time — see
[docs/CURATION.md](../../../docs/CURATION.md#3-assemble-attach-rules-and-merge-one-pr-at-a-time).

## Prerequisites

| Resource | Default path | Override |
|----------|--------------|----------|
| RH-GSplusplus repo | workspace root | — |
| CaC-content clone | `../CaC-content` | env `CAC_CONTENT_ROOT` |
| Product config | `mappings/rhel9/artifact.json` | read `rhel_major` for doc URLs |
| Doc link registry | `mappings/rhel9/docs.json` | — |
| Scope config (practice-area → component id) | `mappings/shared/scope/rhel-host.json` | — |
| Component titles (component id → directory title) | `mappings/shared/components/rhel-host.json` | — |
| Vendored BSI catalog (statement/guidance text) | `catalogs/bsi-grundschutz-plus-plus/catalog.json` | — |

Requires `git`, `gh`, network for push/PR.

## Git safety

1. Run `git branch --show-current`. **Never commit on that branch.**
2. Create branch from current HEAD: `cursor/implement-{control-id}`
   (`control-id` = filename stem, e.g. `BER.2.4`).
3. One control changed per PR unless the user explicitly asks for a single batch PR. For a
   requested set of controls, repeat Steps 0–8 per control, each on its own branch from the
   original HEAD (not stacked on the previous control's branch).

## Workflow

Copy and track (repeat per control when given a set):

```
- [ ] 0. Resolve target; create profile + component markdown stub if missing
- [ ] 1. Read and parse component markdown
- [ ] 2. Load listed CaC rules
- [ ] 3. Gather Red Hat documentation
- [ ] 4. Discover additional CaC rules (suggestions only)
- [ ] 5. Draft German implementation prose
- [ ] 6. Evaluate coverage → set Implementation Status
- [ ] 7. Write markdown (preserve protected sections)
- [ ] 8. Branch, commit, push, open PR
```

### Step 0 — Resolve target; create stub if missing

Given a control ID, search
`authoring/component/{artifact}/**/{artifact}/**/{control-id}.md`.

**If found:** use it as the target file for Step 1.

**If not found** (new control), create both files before continuing:

1. Look up the control in the vendored catalog (`catalogs/bsi-grundschutz-plus-plus/catalog.json`)
   for its title, statement, and guidance prose. `python3 scripts/export_review_candidates.py`
   (no `--write`) or `--write` can produce this text pre-formatted under
   `authoring/candidates/{scope}/{area}/{control-id}.md` if you want a shortcut.
2. Create `authoring/profile/{artifact}/{area}/{control-id}.md` — copy the frontmatter and
   `# Editable Content` footer structure from a sibling file in the same directory; fill in the
   heading, Control Statement, and Control guidance from the catalog. Heading format:
   `# {control-id} - \[{Group Title}\] {Control Title}` — trestle requires the bracketed group
   title or `assemble_oscal.py` fails with "unable to read group title". Look up `{Group Title}`
   as the sibling `"title"` of the catalog group object whose `"id"` matches the control's parent
   group (e.g. group `{"id": "BER.3", "title": "Zugangskonten", ...}` in
   `catalogs/bsi-grundschutz-plus-plus/catalog.json` → `\[Zugangskonten\]` for any `BER.3.*`
   control).
3. Determine the component: `area` = control ID prefix before the first `.` (e.g. `BER`). Look up
   `component_by_practice_area[area]` in `mappings/shared/scope/rhel-host.json` to get the
   component id, then that id's `title` in `mappings/shared/components/rhel-host.json` to get the
   component directory name.
4. Create `authoring/component/{artifact}/{component-title}/{artifact}/{area}/{control-id}.md` —
   copy frontmatter, heading (including the `\[{Group Title}\]` bracket, same as Step 0.2 above),
   Control Statement, and Control guidance verbatim from the new profile file; leave the two HTML
   comments, an empty prose line, and `### Implementation Status: planned`. Do not add a
   `### Rules:` heading (added later only if a rule is confirmed — see docs/CURATION.md).
5. Run `python3 scripts/assemble_oscal.py --product rhel9` once so the new control's markdown is
   picked up (`include-controls.with-ids` and the component-definition stub) before drafting prose.
   This modifies `profiles/…/profile.json` and `component-definitions/…/component-definition.json`
   locally — **do not stage or commit them** (Step 8 only adds the two markdown files). Discard
   these local changes once you've confirmed the stub exists, e.g.
   `git checkout -- profiles/ component-definitions/`, so the working tree stays clean for Step 8
   and any subsequent control's branch.

Continue to Step 1 with the (now existing) component markdown file.

### Step 1 — Read and parse

Read the target markdown file. Extract:

- **Control ID** — from `#` heading (e.g. `BER.2.4`)
- **Control Statement** — `## Control Statement` body (read-only)
- **Control guidance** — `## Control guidance` body (read-only)
- **Listed rules** — bullet IDs under `### Rules:` (read-only in file)
- **Current prose** — text between HTML comments and `### Rules:`
- **Current status** — line `### Implementation Status: {value}`

Preserve YAML frontmatter (`x-trestle-global`) unchanged.

### Step 2 — Load listed CaC rules

Every brand-new stub from Step 0 has no `### Rules:` heading at all, so this step trivially finds
nothing for those — that's expected, continue to Step 3/4 regardless.

For each rule ID under `### Rules:`:

```
{CAC_CONTENT_ROOT}/linux_os/guide/**/{rule_id}/rule.yml
```

Also search `applications/openshift/**/{rule_id}/rule.yml` if no Linux match.

From each `rule.yml` collect:

- `title`, `description`, `rationale`, `severity`
- `template` name and key vars (if present)
- `identifiers` — confirm `cce@rhel9` (or artifact `rhel_major`) exists
- `ocil` / `fixtext` — remediation hints

If a listed rule is missing, note in PR body; treat as coverage gap.

### Step 3 — Red Hat documentation

**Primary:** the `rhokp-docs` skill (local Red Hat Offline Knowledge Portal), if the
`rhokp-scraper` repo is present in the workspace — read
`../rhokp-scraper/.cursor/skills/rhokp-docs/SKILL.md` and follow it. It's local and much faster
than the MCP server. Check `../rhokp-scraper/output/red_hat_enterprise_linux/{rhel_major}/` for
already-scraped markdown first (`rg` it directly, no server needed); only invoke `scrape`/`search.py`
if that RHEL major isn't scraped yet, and only after confirming the local RHOKP instance is
reachable (`curl -fsS "$RHOKP_BASE_URL"`) — if it's down and nothing relevant is already scraped,
skip to the next source rather than blocking.

**Secondary:** MCP server `user-Red-Hat-documentation` (or `redhat-documentation-mcp`). This has
been unreliable (slow, silently unreachable, or hangs) — before calling, run `GetMcpTools` for
that server; if unavailable or a call doesn't return quickly, don't retry more than once, continue
with the remaining fallbacks instead of blocking.

**Further fallback chain:**

1. **`mappings/rhel9/docs.json`** — pick keys by control area:

   | Control prefix / topic | Doc key |
   |------------------------|---------|
   | `DET.*`, `KONF.4.*`, audit, logging | `audit` |
   | `BER.*`, identity, auth, SSSD | `sssd` |
   | OpenSCAP, compliance scan | `openscap` |
   | General hardening | `security_hardening` |
   | Monitoring | `monitoring` |
   | systemd, services | `systemd` |

2. **WebFetch** — fetch the chosen `href` from `docs.json`.

3. **CaC rule text** — use `description` + `rationale` only if docs unreachable.

Record **doc source used** (RHOKP path, MCP query, doc key, or URL) for the PR body.

### Step 4 — Discover additional rules (PR suggestions only)

Delegate to the `find-rule` skill in the CaC-content clone instead of reimplementing its search:

1. Read `{CAC_CONTENT_ROOT}/.claude/skills/find-rule/SKILL.md` (default `../CaC-content`).
2. Follow it with `$ARGUMENTS` set to the control statement + guidance text,
   scoped to `linux_os/guide/` for RHEL (skip `applications/openshift/`).
3. Take its strong/partial match output and cross-check `identifiers` for `cce@rhel{N}` (artifact's
   `rhel_major`) to confirm applicability.

**Do not edit `### Rules:` in markdown.** List discoveries in PR body under
"Suggested additional CaC rules" with one-line rationale each (reuse the rationale the find-rule
skill produced).

### Step 5 — Draft implementation prose

Write **German** prose replacing only the paragraph(s) between the HTML
comments and `### Rules:`.

Requirements:

- Describe **how RHEL implements** the control (mechanism, not restating the requirement)
- Cite Red Hat docs conceptually (e.g. auditd watch rules, augenrules) — no English paste blocks
- State **honest limits** (org/IAM/process gaps, directory-only changes vs central IdM)
- 2–5 sentences; match tone of existing files in `authoring/component/`
- End with a **"Weitere Informationen:"** line linking the actual doc source(s) used in Step 3, so
  the reader has a source of truth — not just a conceptual mention. See
  [reference.md](reference.md#linking-the-source-of-truth) for the link format and how to derive a
  public URL per source type (RHOKP, MCP, `docs.json`). Skip this line only if no doc source was
  reachable at all (Step 3 fell back to CaC rule text) — never fabricate a URL.

Leave both HTML comments intact.

### Step 6 — Implementation status

Set `### Implementation Status:` using [status criteria](reference.md#implementation-status).

Summary:

| Status | When |
|--------|------|
| `implemented` | CaC rules (listed and/or strong Step 4 discoveries, cited by ID) + Red Hat docs fully cover technical aspects of statement **and** guidance — regardless of whether those rules are attached in `### Rules:` yet |
| `partial` | CaC rules (listed and/or Step 4 discoveries) cover some guidance aspects; gaps remain (typical: IAM lifecycle, account identity in log, extra files) — independent of current `### Rules:` attachment state |
| `alternative` | A genuinely different technical approach satisfies the same intent as the literal statement/guidance (e.g. TLS-secured gRPC instead of a requested HTTPS channel) — not merely "no rule attached yet" |
| `planned` | No listed or discovered rule and no doc-backed mechanism address the requirement at all |
| `not-applicable` | Guidance is organizational-only; RHEL has no technical hook |

When unsure between `implemented` and `partial`, choose **`partial`**. Evaluate against the
anticipated end state (as if Step 4's strong, CCE-backed discoveries are attached by a reviewer
per docs/CURATION.md Step 3), not against the stub's current (often-empty) `### Rules:` list.

Build a coverage matrix (guidance aspect → rule/doc → covered Y/N) for the PR body.
See [reference.md](reference.md#coverage-matrix).

### Step 7 — Write markdown

Edit **only**:

- Prose between comments and `### Rules:`
- `### Implementation Status: {value}`

**Do not change:** frontmatter, `#` title, Control Statement, Control guidance,
`### Rules:` list, HTML comments, separator lines.

### Step 8 — Branch, commit, PR

```bash
git checkout -b cursor/implement-{control-id}
git add "{path/to/component.md}" "{path/to/profile.md if newly created}"
git status --short  # confirm only the markdown files above are staged — never profile.json/component-definition.json
git commit -m "$(cat <<'EOF'
Enrich {control-id} implementation prose and status.

Assisted-by: Cursor
EOF
)"
git push -u origin HEAD
gh pr create --title "Enrich {control-id} component implementation" --body "$(cat <<'EOF'
## Summary
- Updated German implementation prose for `{control-id}`
- Implementation status: `{status}`

## Coverage matrix
| Guidance aspect | Covered by | Status |
|-----------------|------------|--------|
| ... | ... | ... |

## Documentation sources
- ...

## Listed CaC rules reviewed
- `rule_id` — one-line summary

## Suggested additional CaC rules
(not attached in OSCAL — reviewer decides; see "Attaching a rule" below)
- `rule_id` — rationale

## Attaching a rule (reviewer, manual, optional)
Editing `### Rules:` in this markdown has **no effect** on the assembled OSCAL — trestle treats
that heading as read-only display. To actually attach a suggested rule, a reviewer rebases this
branch onto current `main`, runs `assemble_oscal.py`, and adds a `Rule_Id` prop to this control's
`implemented-requirement` entry in `component-definitions/{artifact}/component-definition.json`
directly, then commits it on this branch right before merging. Step-by-step, and why this must
happen one PR at a time:
[docs/CURATION.md](../../../docs/CURATION.md#3-assemble-attach-rules-and-merge-one-pr-at-a-time).

## Gaps / manual verification
- ...

## Test plan
- [ ] Review prose accuracy against docs.redhat.com links
- [ ] Confirm implementation status matches honest coverage
- [ ] Run `python3 scripts/assemble_oscal.py --product rhel9 && python3 -m trestle validate -a`
EOF
)"
```

Return the PR URL to the user.

## Example invocation

```
Enrich authoring/component/rhel9-gsplusplus-host/RHEL-Protokollierung und Detektion/rhel9-gsplusplus-host/BER.2/BER.2.4.md
```

```
Enrich BER.2.4 for rhel9-gsplusplus-host
```

```
Enrich KONF.2.1, KONF.2.2 and DET.3.1.4 for rhel9-gsplusplus-host
```

## Additional resources

- [Status criteria and coverage matrix](reference.md)
- [review-candidate-controls skill](../review-candidate-controls/SKILL.md) — triage step that decides which controls reach this skill
- [docs/CURATION.md](../../../docs/CURATION.md) — trestle authoring workflow
- [docs/ARCHITECTURE.md](../../../docs/ARCHITECTURE.md) — tiers, language, Rule_Id bridge
