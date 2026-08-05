---
x-trestle-global:
  catalog:
    title: Automatisierte Feststellung
x-review-status: included
x-default-component: rhel-audit
---

# DET.6.1.1 — Automatisierte Feststellung

## Control Statement

Detektion SOLLTE kritische Vorfälle anhand von {{ insert: param, det.6.1.1-prm1 }} durch {{ insert: param, det.6.1.1-prm2 }} protokollieren.

## Review

auditd-Regeln bzw. SIEM-Integration können kritische Vorfälle automatisiert erkennen und protokollieren. SIEM Funktionalitäten sind jedoch zu präferieren.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
