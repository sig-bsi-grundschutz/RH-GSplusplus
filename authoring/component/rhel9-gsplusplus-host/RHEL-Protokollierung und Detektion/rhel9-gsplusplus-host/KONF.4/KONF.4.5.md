---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.5 - \[Vertrauenswürdige Basisdienste\] Zeitquellen

## Control Statement

Konfiguration für IT-Systeme SOLLTE Zeitquellen autorisieren.

## Control guidance

Eine einheitliche Zeitquelle für die Systemuhr (meist über NTP oder PTP) ist essenziell für die einheitliche Auswertung von Logdateien, sowie für moderne kryptographische Verfahren. Es empfiehlt sich zu definieren, welche NTP-Server von welchen NTP-Clients genutzt werden sollen und ob NTP-Server im Broadcast-Modus oder im Client-Server-Modus arbeiten. Letzteres (Client-Server) ist hierbei Best Practice. In bestimmten Fällen empfiehlt es sich außerdem, dass sich NTP-Server bei der Kommunikation gegenüber Clients authentisieren und demnach NTP-Clients nur authentifizierte NTP-Daten akzeptieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Zeitsynchronisation für die Korrelation von Protokollen erfolgt typischerweise über chrony; die Institution bindet vertrauenswürdige Zeitquellen gemäß Produktdokumentation an.

### Rules:

  - service_chronyd_enabled

### Implementation Status: partial

______________________________________________________________________
