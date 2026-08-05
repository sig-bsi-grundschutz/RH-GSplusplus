---
x-trestle-global:
  catalog:
    title: Kompromittierte Authentifizierungsmittel
x-review-status: included
x-default-component: rhel-identity
---

# BER.5.14 — Kompromittierte Authentifizierungsmittel

## Control Statement

Berechtigung SOLLTE die Sperrung kompromittierter Authentifizierungsmittel verankern.

## Review

Sperrung kompromittierter Zugänge technisch umsetzbar (z. B. usermod -L, Entzug von SSH-Keys/Zertifikaten, SSSD) auch mittels ansible

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
