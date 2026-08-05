---
x-trestle-global:
  catalog:
    title: Integritätsprüfung von Patches
x-review-status: included
x-default-component: rhel-audit
---

# DET.5.10.4 — Integritätsprüfung von Patches

## Control Statement

Detektion SOLLTE Patches vor der Installation auf Integrität testen.

## Review

dnf/rpm prüfen Paketintegrität und -signatur (gpgcheck) vor der Installation von Patches, sofern nicht deaktiviert.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
