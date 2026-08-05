---
x-trestle-global:
  catalog:
    title: Revisionssicherheit
x-review-status: included
x-default-component: rhel-audit
---

# DET.3.5 — Revisionssicherheit

## Control Statement

Detektion SOLLTE Änderungen am Audit Log revisionssicher dokumentieren.

## Review

auditd Immutable-Modus (-e 2), chattr +a und Remote-Log-Forwarding schützen vor unbemerkten Änderungen am Audit Log

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
