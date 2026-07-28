# Reference — enrich-component-implementation

## Implementation status

Apply in order — first match wins unless a higher bar is clearly met.

### `implemented`

All must be true:

1. Every **technical** clause in Control Statement is addressed by listed CaC rules and/or Red Hat docs.
2. Every **technical** clause in Control guidance is addressed (time, actor, change detail — as far as OS-level auditing allows).
3. Listed rules have `cce@rhel{N}` for the artifact product.
4. Prose describes the actual mechanism (not a copy of the requirement).

### `partial`

Use when:

- Listed rules cover **part** of guidance (e.g. file watch on `/etc/passwd` but not full IdM lifecycle)
- Audit records lack a field guidance asks for (e.g. "which changes" is implicit in watch, not structured)
- Suggested additional rules in PR would close gaps but are not yet listed
- Product covers detection; institution must cover process (PAM policy, SSSD, directory)

Default when uncertain.

### `alternative`

Use when:

- Red Hat docs describe a supported approach that **does not** map to listed (or any) CaC rule
- Control is met via a different subsystem than the listed rules (document which)

### `planned`

Use when:

- `### Rules:` is empty and no doc-backed mechanism identified
- Rules listed but none apply to target RHEL major

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

When MCP is configured, prefer structured search over raw WebFetch.

1. `GetMcpTools` with pattern `red.?hat|documentation` or server id from user config
2. Query for product + topic (e.g. "RHEL 9 auditd watch rules identity files")
3. Fall back to `docs.json` → WebFetch on empty or error

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
