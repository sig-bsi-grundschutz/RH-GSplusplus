---
x-trestle-param-values:
  det.5.10.3-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.10.3 - \[Management von Schwachstellen\] Automatisierte Überwachung von Anwendungsupdates

## Control Statement

Detektion für Anwendungen KANN den Patchstatus durch {{ insert: param, det.5.10.3-prm1 }} überwachen.

## Control guidance

Eine nicht gepatchte Anwendung könnte als Einfallstor für Angreifer dienen, die bekannte Schwachstellen ausnutzen, um sich Zugang zu Systemen oder Daten zu verschaffen. Die Umsetzung kann beispielsweise auf einem Patch Management System (PMS) oder einem Vulnerability Management System (VMS) basieren. Ein Patch-Managementsystem kann beispielsweise so konfiguriert werden, dass es kontinuierlich die Versionen der installierten Software mit einer zentralen Datenbank für verfügbare Updates abgleicht. Auch die Nutzung eines Schwachstellen-Scanners, der im Netzwerk nach ungepatchten Anwendungen sucht, ist eine wirksame Maßnahme. Ein solcher Scanner könnte beispielsweise wöchentlich oder sogar täglich einen Scan durchführen und die Ergebnisse in einem Dashboard visualisieren. Wichtige prozessuale Tipps sind die Einrichtung von Benachrichtigungsworkflows, die sicherstellen, dass kritische Patch-Status-Änderungen sofort an die richtigen Personen eskaliert werden, sowie die Integration der Überwachungsergebnisse in ein zentrales Incident Response System. Dies kann helfen, die Reaktionszeit zu verkürzen, sodass die Anwendungen schnellstmöglich aktualisiert werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Anwendungen, die als RPM aus denselben Repos kommen, sind im selben `dnf`- und Insights-Patchstatus enthalten wie das Basissystem. Spracheigene Pakete (pip, npm, Container-Images, Flatpak) erfasst `dnf-automatic` nicht; dafür braucht die Institution ein gesondertes Vulnerability-/Patch-Management. Damit ist die Anforderung für RPM-ausgelieferte Anwendungen teilweise, für den Rest nicht host-generisch erfüllt.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
