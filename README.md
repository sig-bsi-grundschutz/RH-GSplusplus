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
- **ComplianceAsCode `Rule_Id`** props where OpenSCAP rules exist (see `authoring/component/` markdown).

Customers import the BSI control layer **and** the Red Hat implementation artifacts into SSP or
compliance tooling.

Human review uses **trestle agile authoring** — see [docs/CURATION.md](docs/CURATION.md).

## Contents

| Path | Purpose |
|------|---------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Architecture, phasing, multi-product roadmap |
| [docs/CURATION.md](docs/CURATION.md) | Human curation workflow (host control review) |
| [catalogs/bsi-grundschutz-plus-plus/catalog.json](catalogs/bsi-grundschutz-plus-plus/catalog.json) | Vendored BSI Control Layer resolved Grundschutz++ catalog snapshot |
| [authoring/profile/rhel9-gsplusplus-host/](authoring/profile/rhel9-gsplusplus-host/) | trestle profile markdown — human scope selection |
| [authoring/component/rhel9-gsplusplus-host/](authoring/component/rhel9-gsplusplus-host/) | trestle component markdown — implementation prose |
| [profiles/rhel9-gsplusplus-host/profile.json](profiles/rhel9-gsplusplus-host/profile.json) | Scoped host profile (assembled from authoring) |
| [component-definitions/rhel9-gsplusplus-host/](component-definitions/rhel9-gsplusplus-host/) | RHEL subsystem component definitions (assembled) |
| [mappings/](mappings/) | Scope rules, component metadata, product config |
| [scripts/assemble_oscal.py](scripts/assemble_oscal.py) | Assemble profile + component-definition from authoring |
| [scripts/export_review_candidates.py](scripts/export_review_candidates.py) | Export candidate review queue markdown |
| [scripts/fetch_bsi_catalog.sh](scripts/fetch_bsi_catalog.sh) | Refresh vendored BSI catalog |

## Prerequisites

- Python 3.10+ (CI uses 3.11)
- [compliance-trestle](https://github.com/oscal-compass/compliance-trestle) — see [requirements.txt](requirements.txt)

```bash
pip install -r requirements.txt
```

## Validate locally

```bash
python3 scripts/assemble_oscal.py --product rhel9
python3 scripts/check_doc_links.py --product rhel9
python3 -m trestle validate -a
```

## CI

- **Validate OSCAL** — assemble from `authoring/`, fail on git drift, `trestle validate -a`
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
