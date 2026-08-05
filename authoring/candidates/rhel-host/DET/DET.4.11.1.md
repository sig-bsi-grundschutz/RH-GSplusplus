---
x-trestle-global:
  catalog:
    title: Authentifizierungsversuche an externen Schnittstellen
x-review-status: included
x-default-component: rhel-audit
---

# DET.4.11.1 — Authentifizierungsversuche an externen Schnittstellen

## Control Statement

Detektion für Externe Netzanschlüsse KANN Authentifizierungsversuche auf unauthorisierte Verbindungen {{ insert: param, det.4.11.1-prm1 }} überprüfen.

## Review

fail2ban/sshguard überwachen Authentifizierungsversuche auf unautorisierte externe Verbindungen (z. B. SSH-Brute-Force)

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
