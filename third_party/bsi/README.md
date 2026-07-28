# BSI Stand der Technik — Grundschutz++ catalog (upstream)

This repository vendors a snapshot of the BSI **Control Layer** resolved **Anwenderkatalog Grundschutz++** OSCAL catalog for reproducible validation and offline use.

- **Upstream repository:** [BSI-Bund/Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek)
- **Layer:** `control_layer`
- **Source file:** `control_layer/Grundschutz++/Grundschutz++-resolved_catalog.json`
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

The vendored copy lives at [`catalogs/bsi-grundschutz-plus-plus/catalog.json`](../catalogs/bsi-grundschutz-plus-plus/catalog.json). See [`VERSION`](VERSION) for the pinned upstream commit, catalog UUID, and `last-modified` timestamp this tree was aligned with.

To refresh the snapshot:

```bash
./scripts/fetch_bsi_catalog.sh
```

After fetching, verify `catalog_uuid` and `catalog_last_modified` in `VERSION` and `mappings/rhel9/artifact.json` (`catalog_upstream`) still match the file, then regenerate OSCAL artifacts.
