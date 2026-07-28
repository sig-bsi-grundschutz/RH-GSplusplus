# Control mappings

Source-of-truth layout for GS++ → Red Hat product mappings. Generated OSCAL lives under
`profiles/` and `component-definitions/`. See [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) and
[docs/CURATION.md](../docs/CURATION.md).

## Layout

| Path | Purpose |
|------|---------|
| `shared/scope/` | Candidate pool rules (practice areas, kernel class gate) |
| `shared/curation/` | **Human review registry** — pending / included / excluded per control |
| `shared/slices/` | Generated included control ID lists |
| `shared/components/` | Subsystem component metadata |
| `shared/controls/` | Generated mappings for included controls only |
| `{product}/artifact.json` | Generator config |
| `{product}/docs.json` | Documentation link keys |

## Regenerate OSCAL

```bash
python3 scripts/curation/init_registry.py --write      # refresh candidate registry
python3 scripts/curation/review_report.py            # review progress
python3 scripts/build_host_mappings.py --write       # after editing curation
python3 scripts/generate_component_definition.py --product rhel9
python3 -m trestle validate -a
```

Curate controls in **`mappings/shared/curation/rhel-host.json`**. Seed curated audit controls live
in **`mappings/shared/controls/rhel-audit.json`**. Do not bulk-generate synthetic Tier-2 answers.

## Retired

- `scripts/build_host_allowlist.py` — replaced by human curation workflow
- `rhel9_gsplusplus.json` / keyword heuristics — see architecture doc
