---
x-trestle-global:
  catalog:
    title: Öffentliche Blocklisten
x-review-status: excluded
x-default-component: rhel-audit
---

# DET.4.18 — Öffentliche Blocklisten

## Control Statement

Detektion für E-Mail KANN öffentliche Blocklisten auf Einträge für eigene E-Mail-Server {{ insert: param, det.4.18-prm1 }} überprüfen.

## Review

Sofern Host Mailserver betreibt: Cron-Job mit DNSBL-Abfragen kann eigene IP auf öffentlichen Blocklisten prüfen. Wir behandeln hier nur das RHEL Basis-System und excludieren die Anforderung daher.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
