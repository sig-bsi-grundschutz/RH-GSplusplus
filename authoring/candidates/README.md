# Review queue (generated)

Run from the repository root:

```bash
python3 scripts/export_review_candidates.py --write
```

This writes one markdown file per KONF/BER/DET kernel candidate (~331 controls). These files are
**not** assembled into OSCAL. Promote a control by adding profile and component markdown under
`authoring/profile/` and `authoring/component/`.

See [docs/CURATION.md](../../docs/CURATION.md).
