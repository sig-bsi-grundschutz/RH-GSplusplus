---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.2.9 - \[Konfiguration von Systemen\] Abgesicherter und authentisierter Bootprozess

## Control Statement

Konfiguration für IT-Systeme KANN einen abgesicherten und authentisierten Bootprozess aktivieren.

## Control guidance

Dies empfiehlt sich für eingebettete Systeme (Embedded Systems), indem z.B. der Bootloader die Integrität des Betriebssystems überprüft und es nur dann lädt, wenn es als korrekt eingestuft wurde. Ebenso empfiehlt es sich ein mehrstufiges Boot-Konzept mit kryptographisch sicherer Überprüfung der Einzelschritte zu realisieren, sichere Hardware-Vertrauensanker zu verwenden, bei ARM & UEFI-basierten Systemem jeweils (ARM) Secure Boot zu nutzen.

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
