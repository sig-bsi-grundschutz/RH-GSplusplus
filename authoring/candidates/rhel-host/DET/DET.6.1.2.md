---
x-trestle-global:
  catalog:
    title: Automatische Alarmierung
x-review-status: included
x-default-component: rhel-audit
---

# DET.6.1.2 — Automatische Alarmierung

## Control Statement

Detektion SOLLTE bei sicherheitskritischen Ereignissen eine Alarmierung von {{ insert: param, det.6.1.2-prm1 }} durch {{ insert: param, det.6.1.2-prm2 }} ausführen.

## Review

auditd/journald können über Plugins (audispd, rsyslog-Aktionen) automatisierte Alarmierung bei sicherheitskritischen Ereignissen auslösen. SIEM Funktionalitäten sind jedoch zu präferieren.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
