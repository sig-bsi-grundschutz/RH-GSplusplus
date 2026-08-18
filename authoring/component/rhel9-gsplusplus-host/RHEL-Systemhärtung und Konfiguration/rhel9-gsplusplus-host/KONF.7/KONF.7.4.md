---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.4 - \[Schutz vor Schadcode\] Angriffserkennung anhand von Netzverkehr

## Control Statement

Konfiguration für IT-Systeme KANN Angriffserkennung anhand von Netzverkehr aktivieren.

## Control guidance

Hierbei wird eine netzwerkbasierte Bedrohungsanalyse direkt auf dem IT-System durchgeführt. Dieser Ansatz, oft als Host-based Network Intrusion Detection System (H-NIDS) oder Endpoint Detection and Response (EDR) bezeichnet, ermöglicht eine tiefere Sicht in das Systemverhalten. Statt nur den Datenstrom am Perimeter zu überwachen, kann so die Institution verdächtige Aktivitäten wie das Scannen von Netzwerk-Ports, den Aufbau ungewöhnlicher Verbindungen zu Command-and-Control-Servern oder den Versuch der Datenexfiltration erkennen. Ohne diese Erkennung könnte sich ein Angreifer, der bereits in das Netzwerk eingedrungen ist, unentdeckt von System zu System bewegen oder sensible Daten unbemerkt nach außen senden. Die dezentrale Erkennung auf den Clients kann zudem dabei helfen, interne Lateral-Movement-Versuche zu identifizieren, da der Datenverkehr zwischen den Systemen überwacht wird, selbst wenn er das interne Netzwerk nicht verlässt. Um diese Anforderung umzusetzen, kann die Institution spezialisierte EDR- oder Endpoint-Security-Lösungen nutzen, die eine integrierte Funktion zur Netzwerküberwachung bieten. Es kann ebenfalls eine regelbasierte Erkennung über lokale Host-Firewalls oder Sicherheitsagenten aktiviert werden, die bestimmte Muster im Netzwerkverkehr blockieren oder protokollieren. Bei der Einführung solcher Maßnahmen ist es entscheidend, die Performance des Clients zu berücksichtigen. Daher kann die Konfiguration so optimiert werden, dass sie nur kritische Protokolle oder Ports überwacht, um die Systemressourcen zu schonen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Host-basierte Erkennung von Netzangriffen ist in RHEL nicht als integrierter Dienst enthalten: nftables und firewalld können Logging (`nft log`, rich rules) aktivieren, aber signaturbasierte NIDS erfordert Drittanbieter-Software. Netfilter-Hooks erlauben technische Integration. Erkennung anhand von Netzverkehr auf dem Host selbst ist optional und organisatorisch zu bewerten — typische IDS laufen als separate Appliance oder Agent.

Weitere Informationen: [Netzwerke absichern](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/index).

### Implementation Status: planned

______________________________________________________________________
