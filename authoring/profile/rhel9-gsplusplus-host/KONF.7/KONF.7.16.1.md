---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.7.16.1 - \[Schutz vor Schadcode\] Anti-Exploit für den Arbeitsspeicher

## Control Statement

Konfiguration für IT-Systeme SOLLTE den Schutz des Arbeitsspeichers vor der Ausnutzung bekannter Sicherheitslücken aktivieren.

## Control guidance

Gelingt es Angreifern Code auf dem System auszuführen, so könnten sie versuchen, über den Arbeitsspeicher des Systems den Schadcode weiter zu verbreiten oder Zugriff auf Daten zu erlangen. Hierzu gehören Angriffe wie Buffer Overflows, Return-Oriented Programming, Heap Spraying, Use-After-Free, Memory Scraping oder Side-Channel-Angriffe wie Spectre und Meltdown. Schutzmaßnahmen hiergegen können durch Software oder durch Hardware umgesetzt sein. Softwarebasiert sind z.B. Address Space Layout Randomization (ASLR), Data Execution Prevention (DEP), Stack Canaries. Hardwarebasiert sind z.B. Trusted Execution Environments (TEE).

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
