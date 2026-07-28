# Control mappings

Source-of-truth for **human authoring** is under `authoring/` (trestle markdown). Generated OSCAL
lives under `profiles/` and `component-definitions/`. See [docs/CURATION.md](../docs/CURATION.md).

## Layout

| Path | Purpose |
|------|---------|
| `shared/scope/` | Candidate pool rules (KONF/BER/DET kernel controls) |
| `shared/components/` | Subsystem metadata for component-definition skeleton |
| `authoring/profile/` | trestle profile markdown — **controls in scope** |
| `authoring/component/` | trestle component markdown — **implementation prose** |
| `authoring/candidates/` | Review queue (generated, not assembled) |
| `{product}/artifact.json` | Assemble config, BSI upstream refs, CI smoke rules |
| `{product}/docs.json` | Documentation link keys injected at assemble time |

## Regenerate OSCAL

```bash
python3 scripts/assemble_oscal.py --product rhel9
python3 -m trestle validate -a
```

## Retired

- `mappings/shared/curation/` — replaced by trestle authoring
- `scripts/build_host_mappings.py`, `scripts/build_host_allowlist.py`
- Bulk-generated `mappings/shared/controls/rhel-host.json`
