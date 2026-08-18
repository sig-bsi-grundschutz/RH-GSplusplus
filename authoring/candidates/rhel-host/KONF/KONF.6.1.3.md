---
x-trestle-global:
  catalog:
    title: Isolierte Arbeitsumgebungen
x-review-status: excluded
x-default-component: rhel-hardening
---

# KONF.6.1.3 — Isolierte Arbeitsumgebungen

## Control Statement

Konfiguration für Endgeräte KANN die Isolation verschiedener Arbeitsumgebungen für verschiedene Verwendungen aktivieren.

## Review

Nicht relevant im Kontext RHEL. Selbst wenn RHEL auf dem Endgerät eingesetzt ist, wäre die Kapselung der Arbeitsumgebung vermutlich unterschiedliche RHEL Systeme, ähnlich wie auf Genu-Client / SINA-Client. GGF könnte man Richtung qemu / kvm argumentieren in RHEL selbst, aber das bietet für den Großteil der Anwendungsfälle vermutlich wenig bis keinen Mehrwert.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
