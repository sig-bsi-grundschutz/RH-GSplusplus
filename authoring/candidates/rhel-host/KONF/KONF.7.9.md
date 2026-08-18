---
x-trestle-global:
  catalog:
    title: Einschränkung der Installation
x-review-status: included
x-default-component: rhel-hardening
---

# KONF.7.9 — Einschränkung der Installation

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Installation von Anwendungen einschränken.

## Review

Paketinstallation per GPG/RHN einschränkbar. Außerdem via SUDO only. Binaries in `.local` im Homeverzeichnis immer möglich. Alternative: RHEL im Image-Mode

<!-- Human review queue — not assembled into OSCAL until promoted. -->
<!-- x-review-status: pending | included | excluded -->
<!-- To include: copy or recreate under authoring/profile/ and add component markdown. -->
<!-- See docs/CURATION.md -->
