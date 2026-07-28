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

Turn a single trestle **component markdown** file into a reviewed PR with honest
implementation prose, coverage assessment, and optional CaC rule suggestions.

**Input:** path to one file under `authoring/component/{artifact}/`.

**Output:** branch + commit + PR. Human reviews before merge.

## Prerequisites

| Resource | Default path | Override |
|----------|--------------|----------|
| RH-GSplusplus repo | workspace root | — |
| CaC-content clone | `../CaC-content` | env `CAC_CONTENT_ROOT` |
| Product config | `mappings/rhel9/artifact.json` | read `rhel_major` for doc URLs |
| Doc link registry | `mappings/rhel9/docs.json` | — |

Requires `git`, `gh`, network for push/PR.

## Git safety

1. Run `git branch --show-current`. **Never commit on that branch.**
2. Create branch from current HEAD: `cursor/implement-{control-id}`  
   (`control-id` = filename stem, e.g. `BER.2.4`).
3. One file changed per PR unless user explicitly asks otherwise.

## Workflow

Copy and track:

```
- [ ] 1. Read and parse component markdown
- [ ] 2. Load listed CaC rules
- [ ] 3. Gather Red Hat documentation
- [ ] 4. Discover additional CaC rules (suggestions only)
- [ ] 5. Draft German implementation prose
- [ ] 6. Evaluate coverage → set Implementation Status
- [ ] 7. Write markdown (preserve protected sections)
- [ ] 8. Branch, commit, push, open PR
```

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

**Primary:** MCP server `user-Red-Hat-documentation` (or `redhat-documentation-mcp`).

Before calling, run `GetMcpTools` for that server. If unavailable, continue with fallbacks — do not abort.

**Fallback chain:**

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

Record **doc source used** (MCP query, doc key, URL) for the PR body.

### Step 4 — Discover additional rules (PR suggestions only)

Using control statement + guidance as requirement text, search CaC using the
same approach as `CaC-content/.claude/skills/find-rule` (keyword + reference search):

- Keywords from German guidance (translate concepts: audit → auditd, identity → passwd/group)
- Same audit/identity/network domains under `linux_os/guide/`
- Rules with `cce@rhel{N}` for the artifact product

**Do not edit `### Rules:` in markdown.** List discoveries in PR body under
"Suggested additional CaC rules" with one-line rationale each.

### Step 5 — Draft implementation prose

Write **German** prose replacing only the paragraph(s) between the HTML
comments and `### Rules:`.

Requirements:

- Describe **how RHEL implements** the control (mechanism, not restating the requirement)
- Tie prose to **listed** CaC rules (what they check/configure)
- Cite Red Hat docs conceptually (e.g. auditd watch rules, augenrules) — no English paste blocks
- State **honest limits** (org/IAM/process gaps, directory-only changes vs central IdM)
- 2–5 sentences; match tone of existing files in `authoring/component/`

Leave both HTML comments intact.

### Step 6 — Implementation status

Set `### Implementation Status:` using [status criteria](reference.md#implementation-status).

Summary:

| Status | When |
|--------|------|
| `implemented` | Listed rules + Red Hat docs fully cover technical aspects of statement **and** guidance |
| `partial` | Some guidance aspects covered; gaps remain (typical: IAM lifecycle, account identity in log, extra files) |
| `alternative` | Valid product path documented but not matched by listed CaC rules |
| `planned` | No listed rules or no doc-backed mechanism yet |
| `not-applicable` | Guidance is organizational-only; RHEL has no technical hook |

When unsure between `implemented` and `partial`, choose **`partial`**.

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
git add "{path/to/component.md}"
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
(not in `### Rules:` — for maintainer consideration)
- `rule_id` — rationale

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

## Additional resources

- [Status criteria and coverage matrix](reference.md)
- [docs/CURATION.md](../../../docs/CURATION.md) — trestle authoring workflow
- [docs/ARCHITECTURE.md](../../../docs/ARCHITECTURE.md) — tiers, language, Rule_Id bridge
