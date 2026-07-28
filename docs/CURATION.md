# RHEL host control curation

Release **0.1** does not auto-include every KONF/BER/DET kernel control. The candidate pool comes
from scope rules; **humans decide** what enters the OSCAL profile and what statement is emitted.

## Files

| Path | Role |
|------|------|
| `mappings/shared/scope/rhel-host.json` | Machine-readable **candidate pool** (KONF, BER, DET kernel controls) |
| `mappings/shared/curation/rhel-host.json` | **Human decisions** — pending / included / excluded per control |
| `mappings/shared/slices/rhel-host.json` | Generated: `included` control IDs only |
| `mappings/shared/controls/rhel-host.json` | Generated: mappings for included controls only |
| `mappings/shared/controls/rhel-audit.json` | Seed file for the first curated audit slice (merged at registry init) |

## Workflow

### 1. Initialize or refresh the registry

```bash
python3 scripts/curation/init_registry.py --write
```

Creates `mappings/shared/curation/rhel-host.json` with all candidates as `pending`, except controls
seeded from `rhel-audit.json` (marked `included` with curated statements).

Re-running preserves existing human edits and only adds new catalog controls as `pending`.

### 2. Review progress

```bash
python3 scripts/curation/review_report.py
python3 scripts/curation/review_report.py --markdown docs/review-queue-rhel-host.md
```

### 3. Curate each control

Edit `mappings/shared/curation/rhel-host.json`:

**Include** (RHEL can address, even if only partially):

```json
"KONF.2.1": {
  "title": "...",
  "status": "included",
  "component": "rhel-hardening",
  "tier": 1,
  "statement": "German curated implementation text…",
  "doc_keys": ["security_hardening"],
  "rule_ids": ["optional_openscap_rule"]
}
```

**Include with explicit template** (honest Tier-2 — use sparingly after review):

```json
"use_default_template": true,
"tier": 2
```

**Exclude** (not applicable to RHEL host scope):

```json
"status": "excluded",
"exclude_reason": "Organisatorische Verfahrensregelung; nicht durch das Betriebssystem umsetzbar."
```

### 4. Build mappings and OSCAL

```bash
python3 scripts/build_host_mappings.py --write
python3 scripts/generate_component_definition.py --product rhel9
python3 -m trestle validate -a
```

CI runs `build_host_mappings.py --check` to ensure generated slice/controls match the registry.

## Rules

- **No synthetic bulk answers** — the generator refuses included controls without `statement` or
  `use_default_template: true`.
- **Excluded controls need a reason** — documents why RHEL does not claim them.
- **Pending controls never appear** in the profile or component definition.
- Default component suggestions (`default_component`) come from practice area; override `component`
  when curating.

## Suggested review order

1. Exclude obvious organizational controls (Verfahren, Inventar, SOC-Prozesse).
2. Include OS-core areas: `KONF.2.*`, `KONF.4–7.*`, `BER.3–7.*`, `DET.3.*`.
3. Defer application-layer KONF (`KONF.10–15`) unless the host runs that stack.
4. Add OpenSCAP `rule_ids` only where CaC rules genuinely map.
