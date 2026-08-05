---
x-trestle-global:
  catalog:
    title: Monitoring von Zugangsdaten
x-review-status: included
x-default-component: rhel-identity
---

# BER.6.6 — Monitoring von Zugangsdaten

## Control Statement

Berechtigung SOLLTE Zugangsdaten auf Kompromittierung durch {{ insert: param, ber.6.6-prm1 }} überwachen.

## Review

RHEL auditd und logforwarding ermöglichen Überwachung der genutzten Zugangsdaten (wann wurde ein Login durchgeführt) und sind essentiell für ein Monitoring.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
