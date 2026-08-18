---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.6.5 - \[Rollen und Berechtigungen\] Dynamische Zugriffskontrolle im System

## Control Statement

Konfiguration für IT-Systeme KANN dynamische Zugriffskontrolle im System aktivieren.

## Control guidance

Eine dynamische Zugriffskontrolle (engl. Dynamic Access Control, DAC) bezeichnet ein Verfahren, bei dem Zugriffsentscheidungen nicht ausschließlich auf statischen Berechtigungen (z. B. Benutzerrollen oder ACLs) beruhen, sondern zusätzlich kontextabhängige Bedingungen wie Gerätezustand, Sensitivität der Daten, Standort, Zeitfenster oder Sicherheitsklassifikation auswerten. Dabei bleibt die Policy, also die zugrundeliegende Regelmenge zur Zugriffsbewertung, fest definiert und nachvollziehbar dokumentiert – lediglich die Entscheidung über den konkreten Zugriff erfolgt dynamisch anhand dieser Bedingungen. Ziel ist eine feinere Steuerung des Datenzugriffs auf Basis aktueller Risikosituationen, ohne dass Administratoren Berechtigungen manuell anpassen müssen. Solche Mechanismen können etwa verhindern, dass ein Benutzer sensible Daten von einem nicht verwalteten Endgerät ausliest, während er im internen Netz regulär Zugriff hätte. Da DAC komplex sein kann ist es zweckmäßig, auch auf Funktionen zur Auditierung und Protokollierung der DAC zu achten.

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
