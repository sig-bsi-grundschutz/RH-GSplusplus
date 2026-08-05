---
x-trestle-global:
  catalog:
    title: Speicherkapazität
x-review-status: included
x-default-component: rhel-audit
---

# DET.3.4 — Speicherkapazität

## Control Statement

Detektion SOLLTE den für die Protokollierung zur Verfügung stehenden Speicherplatz {{ insert: param, det.3.4-prm1 }} überprüfen.

## Review

auditd (space_left/admin_space_left) und Speicherplatz-Monitoring (df/logrotate) prüfen verfügbaren Protokollspeicher

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
