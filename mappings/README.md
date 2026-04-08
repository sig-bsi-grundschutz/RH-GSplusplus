# Control mappings

## `rhel9_gsplusplus_slice.json`

Machine-readable mapping from **BSI Grundschutz++** catalog control IDs (pilot subset) to:

- **implementation_status** — OSCAL-oriented status for the component-definition generator (`partial`, `implemented`, …).
- **statement** — Short Red Hat product positioning text (not a legal interpretation of BSI wording).
- **rule_ids** — Optional ComplianceAsCode / scap-security-guide rule short names for automation (see [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content)).
- **doc_keys** — Keys into the `docs` map (docs.redhat.com URLs).

### Gaps and limitations

The `gaps` array in the JSON file lists known limitations. In particular:

- Organizational controls (**GC.**\*) often remain **`partial`** because RHEL alone cannot satisfy governance without customer process.
- **Rule IDs** are indicative; profile choice (e.g. OSPP, CIS) changes whether a rule exists or is selected.
- OpenSCAP smoke tests in CI use **`oscap_smoke_rules`** — a small subset that is expected to be present in common RHEL 9 data streams.

Regenerate the component definition after editing the mapping:

```bash
python3 scripts/generate_component_definition.py
```

Bump `artifact_metadata.component_definition_last_modified` when you change statements or control coverage so OSCAL document identity tracking stays honest.
