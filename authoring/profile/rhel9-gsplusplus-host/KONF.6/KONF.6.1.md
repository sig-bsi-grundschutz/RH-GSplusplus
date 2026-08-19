---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.6.1 - \[Rollen und Berechtigungen\] Minimal erforderliche Berechtigungen für Anwendungen

## Control Statement

Konfiguration für IT-Systeme SOLLTE erforderliche Berechtigungen für Anwendungen einschränken.

## Control guidance

Ziel ist es, Angriffsflächen zu minimieren und unerwünschte Seiteneffekte zu vermeiden. Durch restriktive Rechtevergabe pro App lässt sich das Risiko für Zugriffe auf sensible Bereiche stark senken. Gleichzeitig trägt dieses Prinzip dazu bei, eine klare Trennung zwischen den einzelnen Systemkomponenten zu bewahren und unkontrollierte Wechselwirkungen zu verhindern. Beispiele sind Lese- und Schreibrechte für Verzeichnisse, insbesondere für Systemverzeichnisse, Berechtigungen zum Zugriff auf Sensoren oder Peripheriegeräte, sowie der Netzzugriff. Um die Umsetzung zu erleichtern können Berechtigungsprofile erstellt werden, die je nach Anwendungsklasse (z. B. Office, Multimedia, Tools) eine Basislinie an Privilegien definieren. Diese Profile können in einer zentralen Verwaltungssoftware (z. B. über Gruppenrichtlinien oder ein Mobile‑Device‑Management) hinterlegt und automatisch auf neue Installationen angewendet werden. Vor der Freigabe einer Softwareinstallation kann ein Reviewprozess etabliert werden, bei dem anhand von Funktionsdokumentationen geprüft wird, welche minimalen Rechte erforderlich sind. Darüber hinaus kann der Einsatz von Sandboxing- oder Virtualisierungstechnologien unterstützen, indem Anwendungen in einer isolierten Umgebung mit genau festgelegten Schnittstellen betrieben werden können. Tools zur Rechteanalyse (etwa zur Ermittlung der tatsächlich genutzten APIs und Dateizugriffe) können helfen, überflüssige Freigaben im Nachgang weiter einzuschränken.

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
