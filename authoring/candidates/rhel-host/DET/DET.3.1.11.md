---
x-trestle-global:
  catalog:
    title: Anwendungsspezifische Ereignisse
x-review-status: excluded
x-default-component: rhel-audit
---

# DET.3.1.11 — Anwendungsspezifische Ereignisse

## Control Statement

Detektion für Anwendungen KANN {{ insert: param, det.3.1.11-prm1 }} protokollieren.

## Review

journald/syslog aggregieren beliebige anwendungsspezifische Ereignisse (Inhalt anwendungsabhängig). Dies ist allerdings eine Anwendungsanforderung, keine an den Host.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
