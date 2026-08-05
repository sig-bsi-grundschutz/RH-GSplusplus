---
x-trestle-global:
  catalog:
    title: Automatisierte Überwachung von Anwendungsupdates
x-review-status: included
x-default-component: rhel-audit
---

# DET.5.10.3 — Automatisierte Überwachung von Anwendungsupdates

## Control Statement

Detektion für Anwendungen KANN den Patchstatus durch {{ insert: param, det.5.10.3-prm1 }} überwachen.

## Review

dnf/yum-basierte Anwendungen werden ebenfalls durch dnf-automatic/Insights-Patch-Monitoring erfasst. Begrenzt auf via RPM bereitgestellte Anwendungen.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
