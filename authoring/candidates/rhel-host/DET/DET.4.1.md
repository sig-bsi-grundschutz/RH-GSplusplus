---
x-trestle-global:
  catalog:
    title: Überwachung der Protokollierung
x-review-status: included
x-default-component: rhel-audit
---

# DET.4.1 — Überwachung der Protokollierung

## Control Statement

Detektion SOLLTE die Funktionsfähigkeit der Protokollierung überwachen.

## Review

systemd-Statusüberwachung von auditd/rsyslog/journald prüft Funktionsfähigkeit der Protokollierung. Zusätzliche Detektionsmechanismen im SIEM sind denkbar.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
