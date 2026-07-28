# Control mappings

Source-of-truth layout for GS++ → Red Hat product mappings. Generated OSCAL lives under
`profiles/` and `component-definitions/`. See [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md).

## Layout

| Path | Purpose |
|------|---------|
| `shared/slices/` | Phased control ID lists (e.g. `rhel-audit.json` vertical slice) |
| `shared/components/` | Subsystem component metadata (`rhel-audit`, …) |
| `shared/controls/` | Per-slice control mappings: tier, statement, doc_keys, rule_ids |
| `{product}/artifact.json` | Generator config: UUIDs, output paths, defaults, smoke rules |
| `{product}/docs.json` | `doc_key` → `href` + German link `text` for OSCAL output |

## Regenerate OSCAL

```bash
python3 scripts/generate_component_definition.py --product rhel9
python3 -m trestle validate -a
```

Edit **`mappings/shared/controls/`** for curated Tier-1 content and **`shared/slices/`** to change
profile scope. Bump `artifact_metadata` timestamps in `{product}/artifact.json` when output
semantics change.

## Retired

- `rhel9_gsplusplus.json` / `rhel9_gsplusplus_overrides.json` — replaced by layout above
- `scripts/build_gsplusplus_overrides.py` — keyword heuristics retired per architecture doc
