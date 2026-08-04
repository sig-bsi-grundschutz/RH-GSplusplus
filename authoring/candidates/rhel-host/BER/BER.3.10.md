---
x-trestle-global:
  catalog:
    title: Anmeldeversuchsgrenze am System
x-review-status: included
x-default-component: rhel-identity
---

# BER.3.10 — Anmeldeversuchsgrenze am System

## Control Statement

Berechtigung für IT-Systeme SOLLTE weitere Anmeldeversuche nach Erreichen von {{ insert: param, ber.3.10-prm1 }} fehlgeschlagenen Versuchen vorübergehend blockieren.

## Review

konfigurierbar via pam

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
