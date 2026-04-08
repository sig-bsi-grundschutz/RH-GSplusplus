# Control mappings

## `rhel9_gsplusplus.json`

Main **generator configuration**: artifact UUIDs and timestamps, paths, default template (used only if an override omits fields — overrides now cover all controls), `docs` map (**docs.redhat.com** URLs), OpenSCAP smoke rules, and `gaps`.

## `rhel9_gsplusplus_overrides.json`

**Per-control data** for every Grundschutz++ catalog control (`647` entries):

- **doc_keys** — Keys into `docs` in `rhel9_gsplusplus.json` so the component definition gets concrete **docs.redhat.com** links.
- **statement** — English implementation narrative (curated for 18 controls; the rest generated from BSI practice area + German title keywords).
- **implementation_status** — Mostly `partial`; curated exceptions (e.g. SELinux) may use `implemented`.
- **rule_ids** — Optional ComplianceAsCode rule short names (currently only on the **curated** subset).

### Regenerating generated overrides

Hand-edits inside `controls` will be **overwritten** if you run the builder. To change bulk behavior, edit [`scripts/build_gsplusplus_overrides.py`](../scripts/build_gsplusplus_overrides.py) (`GROUP_META`, `KEYWORD_RULES`, or `CURATED`), then:

```bash
python3 scripts/build_gsplusplus_overrides.py
python3 scripts/generate_component_definition.py
```

Bump `artifact_metadata.component_definition_last_modified` in `rhel9_gsplusplus.json` when OSCAL output meaningfully changes.

To **preserve** a one-off control: add or update it in the `CURATED` dict in `build_gsplusplus_overrides.py`, then rebuild.
