# RH-GSplusplus

OSCAL **Implementation Layer** artifacts for **Red Hat Enterprise Linux** aligned to the BSI **Grundschutz++** user catalog from the [Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek). The goal is machine-readable **component definitions** (and supporting **profiles**) that security planners can import into SSP and GRC tooling, together with traceability toward technical checks in [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content).

This repository is intentionally **narrow**: it does not recreate the full multi-framework OSCAL library maintained upstream in [ComplianceAsCode/oscal-content](https://github.com/ComplianceAsCode/oscal-content).

## Contents

| Path | Purpose |
|------|---------|
| [`catalogs/bsi-grundschutz-plus-plus/catalog.json`](catalogs/bsi-grundschutz-plus-plus/catalog.json) | Vendored BSI Grundschutz++ **catalog** (snapshot for offline validation). |
| [`profiles/rhel9-gsplusplus-slice/profile.json`](profiles/rhel9-gsplusplus-slice/profile.json) | OSCAL **profile** selecting a pilot subset of controls for RHEL 9 authoring. |
| [`component-definitions/rhel9-gsplusplus-slice/component-definition.json`](component-definitions/rhel9-gsplusplus-slice/component-definition.json) | OSCAL **component definition** for RHEL 9 (generated; see below). |
| [`mappings/rhel9_gsplusplus_slice.json`](mappings/rhel9_gsplusplus_slice.json) | Mapping source: statements, implementation status, optional SSG rule IDs, docs.redhat.com links. |
| [`scripts/generate_component_definition.py`](scripts/generate_component_definition.py) | Regenerates the component definition from the mapping. |
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

## CI

- **Validate OSCAL** — installs Trestle, regenerates the component definition, fails on git drift, runs `trestle validate -a`.
- **OpenSCAP smoke** — Fedora container, evaluates a small rule list from `oscap_smoke_rules` against `ssg-rhel9-ds.xml` (reports uploaded; rule results may be *fail* on an unhardened image — the job still produces artifacts).

## Updating the BSI catalog snapshot

```bash
./scripts/fetch_bsi_catalog.sh
```

Record the upstream state in [`third_party/bsi/VERSION`](third_party/bsi/VERSION).

## License and attribution

Red Hat-authored files in this repository are licensed under the terms in [`LICENSE`](LICENSE). The BSI catalog snapshot is subject to **CC BY-SA 4.0**; see [`ATTRIBUTION.md`](ATTRIBUTION.md).

## References

- [NIST OSCAL — Component definition](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/)
- [OSCAL Compass / compliance-trestle](https://github.com/oscal-compass/compliance-trestle)
- [BSI Grundschutz++ README (upstream)](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/blob/main/Anwenderkataloge/Grundschutz++/README.md)
