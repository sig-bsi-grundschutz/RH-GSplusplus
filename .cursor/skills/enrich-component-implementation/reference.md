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
5. Prose describes the actual on-host mechanism (not a copy of the requirement, and not CaC rule
   citations — see [Implementation prose](#implementation-prose)).

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

## Implementation prose

Prose under **What is the solution and how is it implemented?** explains how RHEL implements the
control technically. It is **not** where ComplianceAsCode rules, OpenSCAP scans, or other
audit/check mechanisms are introduced — those belong only in `### Rules:`, the PR body's "Listed
CaC rules reviewed" / "Suggested additional CaC rules", and the coverage matrix.

**DO** — describe the on-host mechanism:

> OpenSSH authentifiziert Fernwartung über PAM angebunden an SSSD/IdM.

**DON'T** — cite or paraphrase a CaC rule as the implementation:

> Die Regel `sshd_enable_pam` stellt sicher, dass SSH PAM nutzt.

Also avoid: rule IDs inline, „wird durch Regel … geprüft“, OpenSCAP/oscap as the subject of the
sentence. Use CaC `description`/`rationale` in Steps 2–3 as research input only; distill the
underlying RHEL behavior into plain German.

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

## Linking the source of truth

Every control's prose should end with a line the reader can click through to verify — not just a
conceptual mention. Format (German label, public URL, one link per distinct source, max ~3):

```markdown
Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening/), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).
```

**Always link the public `docs.redhat.com`/`access.redhat.com` URL, never a `localhost` one** — the
markdown is read by humans without RHOKP access. Derive it per source:

- **`docs.json` hit** — use its `href`/`text` verbatim (already public).
- **RHOKP scraped markdown** — take the frontmatter `source_url` (e.g.
  `http://localhost:8080/documentation/en-us/red_hat_enterprise_linux/9/html-single/{book}/index/`)
  and rewrite the RHOKP base to the public one:
  `{RHOKP_BASE_URL}documentation/en-us/` → `https://docs.redhat.com/en/documentation/`. The path
  segment after that (product/version/html(-single)/book/index) is identical between the offline
  mirror and the public site — verified against the existing `docs.json` `sssd` entry, which is the
  same URL shape. Use the frontmatter `title` (translate to a short German label) as link text if
  no closer `docs.json`-style label exists.
- **RHOKP knowledgebase hit (`search.py`/`fetch_page.py`)** — these are solutions/articles; use the
  public `access.redhat.com` URL, not the local RHOKP path.
- **MCP result** — use whatever public URL/citation the tool call returns directly.
- **CaC rule text only (no doc reachable)** — no link; state the gap in the PR body instead of
  guessing a URL.

This is separate from `mappings/rhel9/docs.json`, which drives **component-level** OSCAL `links`
injected at assemble time (see below) — the inline prose link is for a human reading this specific
control's markdown, and is not itself read by `assemble_oscal.py`.

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
to `component-definitions/{artifact}/component-definition.json`, on the PR branch right before
merge —
[docs/CURATION.md](../../../docs/CURATION.md#3-assemble-attach-rules-and-merge-one-pr-at-a-time).

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

{EDIT: German prose here — technical mechanism only; no CaC rule citations}

### Rules: — UNCHANGED (list items)

### Implementation Status: {EDIT: value}

______________________________________________________________________
```
