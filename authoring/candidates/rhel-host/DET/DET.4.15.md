---
x-trestle-global:
  catalog:
    title: Ressourcenauslastung von Hostsystemen
x-review-status: included
x-default-component: rhel-audit
---

# DET.4.15 — Ressourcenauslastung von Hostsystemen

## Control Statement

Detektion für Hostsysteme SOLLTE die Ressourcenauslastung anhand von {{ insert: param, det.4.15-prm1 }} überwachen.

## Review

sysstat/sar, node_exporter oder systemd-cgtop überwachen Ressourcenauslastung des Hosts

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
