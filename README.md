# RH-GSplusplus

OSCAL **implementation layer** artifacts mapping **Red Hat products** to the BSI **Grundschutz++**
*Anwenderkatalog* from the [Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek).

**RHEL 9** is the first product. The same model extends to RHEL 10, OpenShift, Ansible Automation
Platform, and other Red Hat products — see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

This repository does **not** recreate the broad multi-framework OSCAL library in
[ComplianceAsCode/oscal-content](https://github.com/ComplianceAsCode/oscal-content).

## Design

- **BSI catalog** = full GS++ ISMS baseline (organizational + technical).
- **`rhel9-gsplusplus-host`** = scoped profile + component definition for controls RHEL can support.
- **ComplianceAsCode `Rule_Id`** props where OpenSCAP rules exist (see mappings in `mappings/shared/controls/`).

Customers import the BSI control layer **and** the Red Hat implementation artifacts into SSP or
compliance tooling.

## Contents

| Path | Purpose |
|------|---------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Architecture, phasing, multi-product roadmap |
| [catalogs/bsi-grundschutz-plus-plus/catalog.json](catalogs/bsi-grundschutz-plus-plus/catalog.json) | Vendored BSI Control Layer resolved Grundschutz++ catalog snapshot |
| [profiles/rhel9-gsplusplus-host/profile.json](profiles/rhel9-gsplusplus-host/profile.json) | Scoped host profile (generated) |
| [component-definitions/rhel9-gsplusplus-host/](component-definitions/rhel9-gsplusplus-host/) | RHEL subsystem component definitions (generated) |
| [mappings/](mappings/) | Mapping source (slices, components, controls, product config) |
| [scripts/generate_component_definition.py](scripts/generate_component_definition.py) | Regenerate profile + component definition |
| [scripts/fetch_bsi_catalog.sh](scripts/fetch_bsi_catalog.sh) | Refresh vendored BSI catalog |

## Prerequisites

- Python 3.10+ (CI uses 3.11)
- [compliance-trestle](https://github.com/oscal-compass/compliance-trestle) — see [requirements.txt](requirements.txt)

```bash
pip install -r requirements.txt
```

## Validate locally

```bash
python3 scripts/generate_component_definition.py --product rhel9
python3 scripts/check_doc_links.py --product rhel9
python3 -m trestle validate -a
```

## CI

- **Validate OSCAL** — regenerate artifacts, fail on git drift, `trestle validate -a`
- **Check documentation links** — HTTP check of all URLs in `mappings/rhel9/docs.json`
- **OpenSCAP smoke** — evaluate audit-related rules from `mappings/rhel9/artifact.json` against `ssg-rhel9-ds.xml`

## Updating the BSI catalog snapshot

```bash
./scripts/fetch_bsi_catalog.sh
```

Then regenerate and bump `artifact_metadata` in `mappings/rhel9/artifact.json` if needed. Update
`third_party/bsi/VERSION` (`upstream_commit`, `catalog_uuid`, `catalog_last_modified`) and the
`catalog_upstream` block in `mappings/rhel9/artifact.json` to match the fetched snapshot.

## License and attribution

Red Hat-authored files are licensed under [LICENSE](LICENSE). The BSI catalog snapshot is
**CC BY-SA 4.0** — see [ATTRIBUTION.md](ATTRIBUTION.md).

## References

- [NIST OSCAL — Component definition](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/)
- [OSCAL Compass / compliance-trestle](https://github.com/oscal-compass/compliance-trestle)
- [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content)
