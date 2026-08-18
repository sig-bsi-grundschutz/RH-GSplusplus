---
x-trestle-global:
  catalog:
    title: Echtzeitscanner
x-review-status: included
x-default-component: rhel-hardening
---

# KONF.7.1 — Echtzeitscanner

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine automatische Prüfung auf Schadcode bei Installation oder Öffnung von Dateien aktivieren.

## Review

RPM-Signatur als alternative. SLSA Level3 Builds. Red Hat does not provide clamav packages. It's not supported by Red Hat. (https://access.redhat.com/solutions/22007) But clamav is available via EPEL. Alternativ andere 3rd Party Lösungen.


<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
