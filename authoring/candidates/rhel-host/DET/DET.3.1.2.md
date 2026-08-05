---
x-trestle-global:
  catalog:
    title: Ausgeführte Kommandozeilenbefehle
x-review-status: included
x-default-component: rhel-audit
---

# DET.3.1.2 — Ausgeführte Kommandozeilenbefehle

## Control Statement

Detektion für IT-Systeme SOLLTE ausgeführte Kommandozeilenbefehle protokollieren.

## Review

auditd (execve-Regeln) protokolliert ausgeführte Kommandozeilenbefehle. Hier besteht zusätzlich ein Passwort-Leakage Gefahr, wenn Passwörter direkt über die CLI als Parameter mitgegeben werden.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
