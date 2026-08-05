---
x-trestle-global:
  catalog:
    title: Etablierte Algorithmen bei der Schlüsselerzeugung
x-review-status: included
x-default-component: rhel-identity
---

# BER.7.1 — Etablierte Algorithmen bei der Schlüsselerzeugung

## Control Statement

Berechtigung SOLLTE die ausschließliche Verwendung etablierter kryptografischer Algorithmen bei der Schlüsselerzeugung nach {{ insert: param, ber.7.1-prm1 }} verankern.

## Review

RHEL crypto-policies (update-crypto-policies) steuern zulässige Algorithmen bei der Schlüsselerzeugung (openssl, gpg, ssh-keygen)

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
