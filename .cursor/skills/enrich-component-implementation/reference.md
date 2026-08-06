# Reference — enrich-component-implementation

## Implementation status

Evaluate against the **anticipated end state** — i.e. as if every CaC rule identified in Step 2
(already listed) and Step 4 (discovered, CCE-backed matches for the target RHEL major) has been
attached by a reviewer per docs/CURATION.md Step 3 — not the markdown's current `### Rules:`
state, which is empty for every newly-created stub (Step 0 never populates it) regardless of how
strong the actual coverage is. Apply in order — first match wins unless a higher bar is clearly
met.

### `implemented`

All must be true:

1. Every **technical** clause in Control Statement is addressed by CaC rules (listed and/or
   strong Step 4 discoveries) available for the target technology (e.g. RHEL9).
2. Every **technical** clause in Control guidance is addressed (time, actor, change detail — as
   far as OS-level auditing allows).
3. Those rules have `cce@rhel{N}` for the artifact product.
4. The covering rule(s) are cited by ID in the PR body (listed rules reviewed and/or suggested
   additional CaC rules) — a doc-only mechanism claim with no concrete rule ID does not qualify.
5. Prose describes the actual mechanism (not a copy of the requirement).

### `partial`

Use when CaC rules (listed or Step 4 discoveries, expected to be attached) cover only **part** of
the statement/guidance — independent of whether those rules are attached in `### Rules:` yet:

- Rules cover **part** of guidance (e.g. file watch on `/etc/passwd` but not full IdM lifecycle)
- Audit records lack a field guidance asks for (e.g. "which changes" is implicit in watch, not
  structured)
- Product covers detection; institution must cover process (PAM policy, SSSD, directory)

Whether the covering rule is currently listed in `### Rules:` or only discovered in Step 4 does
not change this status — assume it will be attached.

Default when uncertain.

### `alternative`

Use only for a **genuinely different technical approach** than what the statement/guidance
literally asks for — not merely "no CaC rule is attached yet." Example: guidance asks for an
HTTPS-secured channel but the actual implementation uses a TLS-secured gRPC channel instead — same
security intent, different literal mechanism. If a CaC rule directly checks/configures the
mechanism the guidance itself describes, that is `implemented`/`partial`, not `alternative`, even
if the rule isn't attached in `### Rules:` yet.

Use when:

- The control's intent is met via a different subsystem/protocol/technology than what the
  statement/guidance literally specifies (document which, and why it satisfies the same intent)
- No CaC rule targets the literal mechanism described, but Red Hat docs describe a genuinely
  different supported approach that satisfies the same requirement

### `planned`

Use when no CaC rule (listed or discovered) and no doc-backed mechanism address the requirement at
all — not merely because `### Rules:` is currently empty:

- No listed or discovered rule and no doc-backed mechanism identified
- Rules exist but none apply to target RHEL major

### `not-applicable`

Use when:

- Control guidance is purely organizational (policy, personnel, physical)
- No defensible RHEL host technical hook exists

Do not use to avoid writing prose for hard partial cases.

## Coverage matrix

Build one row per **distinct requirement aspect** from statement + guidance.

| Guidance aspect | Covered by | Status |
|-----------------|------------|--------|
| Short German paraphrase of aspect | `rule_id` and/or doc key/URL | Yes / Partial / No |

**Example — BER.2.4:**

| Aspect | Covered by | Status |
|--------|------------|--------|
| Änderungen an Identitäts-Stammdaten protokolieren | `audit_rules_usergroup_modification_passwd`, doc `audit` | Partial |
| Zeitpunkt im Ereignisprotokoll | auditd timestamp (implicit in audit record) | Yes |
| Zugangskonto | audit UID/euid in record; actor for file write | Partial |
| Welche Änderungen | watch on `/etc/passwd` — detects write, not field-level diff | Partial |
| IAM/Verzeichnis-Stammdaten außerhalb lokaler Dateien | not OS-enforced | No — institution |

## CaC rule lookup

```text
{CAC_CONTENT_ROOT}/linux_os/guide/**/{rule_id}/rule.yml
```

Rule directory name **equals** rule ID. Parent aggregate rules (e.g.
`audit_rules_usergroup_modification`) may reference split rules in `warnings:` — use those for suggestions.

## Doc key hints

Expand `mappings/rhel9/docs.json` as new areas are curated. Control ID prefixes:

| Prefix | Typical doc keys |
|--------|------------------|
| `DET.*` | `audit`, `monitoring` |
| `BER.2.*`, `BER.3.*` | `sssd`, `audit`, `security_hardening` |
| `KONF.2.*` | `security_hardening`, `systemd` |
| `KONF.4.*` | `audit` |

Replace `rhel9` in URLs with `rhel10` when `artifact.json` → `product.rhel_major` is 10.

## Red Hat documentation MCP

Preference order (see SKILL.md Step 3 for the full fallback chain):

1. **`rhokp-docs` skill** (local RHOKP, `../rhokp-scraper` repo) — fastest, no network egress.
   Read already-scraped markdown under `output/red_hat_enterprise_linux/{rhel_major}/` directly
   when present; use `scripts/search.py` / `scrape` only if that RHEL major isn't scraped yet and
   the local portal is reachable.
2. **Red Hat documentation MCP** — has repeatedly been slow or silently unreachable in this
   environment. `GetMcpTools` with pattern `red.?hat|documentation` or server id from user config;
   query for product + topic (e.g. "RHEL 9 auditd watch rules identity files"); don't retry more
   than once if it doesn't respond promptly.
3. **`docs.json` → WebFetch** on empty or error from both of the above.

## Rule_Id is not markdown-driven

`### Rules:` in component markdown is populated by trestle at generation time and is **read-only
display** (`trestle.common.const.RULES_WARNING`). `component-assemble` does not read edits to this
list back into the OSCAL component definition — verified empirically: adding a bullet here and
re-running `scripts/assemble_oscal.py` produces no `Rule_Id` prop change. Never tell a reviewer
that editing this list attaches a rule. The only way to attach/change a `Rule_Id` is a manual edit
to `component-definitions/{artifact}/component-definition.json` —
[docs/CURATION.md](../../../docs/CURATION.md#3-attaching-a-cac-rule).

## Protected markdown regions

```markdown
---
frontmatter: UNCHANGED
---

# Title — UNCHANGED

## Control Statement — UNCHANGED

## Control guidance — UNCHANGED

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- comments — UNCHANGED -->

{EDIT: German prose here}

### Rules: — UNCHANGED (list items)

### Implementation Status: {EDIT: value}

______________________________________________________________________
```
