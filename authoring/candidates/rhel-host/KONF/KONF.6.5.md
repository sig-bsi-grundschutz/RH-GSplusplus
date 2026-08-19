---
x-trestle-global:
  catalog:
    title: Dynamische Zugriffskontrolle im System
x-review-status: excluded
x-default-component: rhel-hardening
---

# KONF.6.5 — Dynamische Zugriffskontrolle im System

## Control Statement

Konfiguration für IT-Systeme KANN dynamische Zugriffskontrolle im System aktivieren.

## Review

SELInux stellt zwar kleine Anteile Bereit um Kontextabhängige Berechtigungsprüfung zu machen (z.B. aus welchem Prozess heraus wird agiert), kann aber keine "dynamik" wie sie im Langtext gefordert ist. Insbesondere Standortdaten etc. sind für solche Entscheidungen in RHEL nicht verfügbar.

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
