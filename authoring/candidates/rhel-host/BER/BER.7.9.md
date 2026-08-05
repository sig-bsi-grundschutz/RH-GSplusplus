---
x-trestle-global:
  catalog:
    title: Zweckbindung
x-review-status: included
x-default-component: rhel-identity
---

# BER.7.9 — Zweckbindung

## Control Statement

Berechtigung SOLLTE Verstöße gegen die Zweckbindung bei der Schlüsselnutzung untersagen.

## Review

OpenSSL/NSS/GnuTLS erzwingen Zweckbindung anhand von X.509 KeyUsage/ExtendedKeyUsage-Erweiterungen. Ansonsten auch organisatorischer Prozess.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
