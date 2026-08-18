---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.7.4 - \[Schutz vor Schadcode\] Angriffserkennung anhand von Netzverkehr

## Control Statement

Konfiguration für IT-Systeme KANN Angriffserkennung anhand von Netzverkehr aktivieren.

## Control guidance

Hierbei wird eine netzwerkbasierte Bedrohungsanalyse direkt auf dem IT-System durchgeführt. Dieser Ansatz, oft als Host-based Network Intrusion Detection System (H-NIDS) oder Endpoint Detection and Response (EDR) bezeichnet, ermöglicht eine tiefere Sicht in das Systemverhalten. Statt nur den Datenstrom am Perimeter zu überwachen, kann so die Institution verdächtige Aktivitäten wie das Scannen von Netzwerk-Ports, den Aufbau ungewöhnlicher Verbindungen zu Command-and-Control-Servern oder den Versuch der Datenexfiltration erkennen. Ohne diese Erkennung könnte sich ein Angreifer, der bereits in das Netzwerk eingedrungen ist, unentdeckt von System zu System bewegen oder sensible Daten unbemerkt nach außen senden. Die dezentrale Erkennung auf den Clients kann zudem dabei helfen, interne Lateral-Movement-Versuche zu identifizieren, da der Datenverkehr zwischen den Systemen überwacht wird, selbst wenn er das interne Netzwerk nicht verlässt. Um diese Anforderung umzusetzen, kann die Institution spezialisierte EDR- oder Endpoint-Security-Lösungen nutzen, die eine integrierte Funktion zur Netzwerküberwachung bieten. Es kann ebenfalls eine regelbasierte Erkennung über lokale Host-Firewalls oder Sicherheitsagenten aktiviert werden, die bestimmte Muster im Netzwerkverkehr blockieren oder protokollieren. Bei der Einführung solcher Maßnahmen ist es entscheidend, die Performance des Clients zu berücksichtigen. Daher kann die Konfiguration so optimiert werden, dass sie nur kritische Protokolle oder Ports überwacht, um die Systemressourcen zu schonen.

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
