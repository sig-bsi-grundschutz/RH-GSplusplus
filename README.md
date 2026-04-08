# RH-GSplusplus

OSCAL **Implementation Layer** artifacts for **Red Hat Enterprise Linux 9** aligned to the full BSI **Grundschutz++** *Anwenderkatalog* from the [Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek). The repository publishes a **profile** that selects **all** catalog controls and a **component definition** with one `implemented-requirement` per control, plus optional curated links to [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) rule IDs where overrides exist.

This repository does not recreate the broad multi-framework OSCAL library in [ComplianceAsCode/oscal-content](https://github.com/ComplianceAsCode/oscal-content).

## Contents

| Path | Purpose |
|------|---------|
| [`catalogs/bsi-grundschutz-plus-plus/catalog.json`](catalogs/bsi-grundschutz-plus-plus/catalog.json) | Vendored BSI Grundschutz++ **catalog** (snapshot for offline validation). |
| [`profiles/rhel9-gsplusplus-full/profile.json`](profiles/rhel9-gsplusplus-full/profile.json) | OSCAL **profile** including **every** Grundschutz++ control (generated). |
| [`component-definitions/rhel9-gsplusplus-full/component-definition.json`](component-definitions/rhel9-gsplusplus-full/component-definition.json) | OSCAL **component definition** for RHEL 9 (generated). |
| [`mappings/rhel9_gsplusplus.json`](mappings/rhel9_gsplusplus.json) | Generator config: defaults, doc URLs, artifact paths, smoke-test rule list. |
| [`mappings/rhel9_gsplusplus_overrides.json`](mappings/rhel9_gsplusplus_overrides.json) | Per-control overrides for **all** catalog controls (docs.redhat.com `doc_keys`, statements; bulk rows from [`scripts/build_gsplusplus_overrides.py`](scripts/build_gsplusplus_overrides.py)). |
| [`scripts/build_gsplusplus_overrides.py`](scripts/build_gsplusplus_overrides.py) | Rebuilds `rhel9_gsplusplus_overrides.json` from the BSI catalog (preserves `CURATED` controls). |
| [`scripts/generate_component_definition.py`](scripts/generate_component_definition.py) | Regenerates **profile** and **component definition** from the catalog + mappings. |
| [`scripts/fetch_bsi_catalog.sh`](scripts/fetch_bsi_catalog.sh) | Refreshes the vendored BSI catalog from GitHub. |

## Prerequisites

- Python 3.10+ recommended (CI uses 3.11).
- [compliance-trestle](https://github.com/oscal-compass/compliance-trestle) — pinned in [`requirements.txt`](requirements.txt).

```bash
pip install -r requirements.txt
```

## Validate locally

```bash
python3 scripts/generate_component_definition.py
python3 -m trestle validate -a
```

After changing the vendored catalog (new control IDs), re-run the generator so the profile `with-ids` list and component stay in sync.

## CI

- **Validate OSCAL** — installs Trestle, regenerates profile + component definition, fails on git drift under `component-definitions/` and `profiles/`, runs `trestle validate -a`.
- **OpenSCAP smoke** — Fedora container, evaluates `oscap_smoke_rules` from `mappings/rhel9_gsplusplus.json` against `ssg-rhel9-ds.xml` (reports uploaded; individual rules may *fail* on an unhardened image).

## Updating the BSI catalog snapshot

```bash
./scripts/fetch_bsi_catalog.sh
```

Update [`third_party/bsi/VERSION`](third_party/bsi/VERSION), bump `artifact_metadata` timestamps in `mappings/rhel9_gsplusplus.json` if document semantics change, then run `python3 scripts/generate_component_definition.py`.

## License and attribution

Red Hat-authored files in this repository are licensed under the terms in [`LICENSE`](LICENSE). The BSI catalog snapshot is subject to **CC BY-SA 4.0**; see [`ATTRIBUTION.md`](ATTRIBUTION.md).

## References

- [NIST OSCAL — Component definition](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/)
- [OSCAL Compass / compliance-trestle](https://github.com/oscal-compass/compliance-trestle)
- [BSI Grundschutz++ README (upstream)](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/blob/main/Anwenderkataloge/Grundschutz++/README.md)
