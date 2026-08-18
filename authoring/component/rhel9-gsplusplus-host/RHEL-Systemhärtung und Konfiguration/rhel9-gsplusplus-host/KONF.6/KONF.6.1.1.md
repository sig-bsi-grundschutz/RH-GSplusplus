---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.1.1 - \[Minimal erforderliche Berechtigungen für Anwendungen\] Datenkapselung

## Control Statement

Konfiguration für IT-Systeme KANN Datenkapselung aktivieren.

## Control guidance

Bei der Datenkapselung, im Englischen als data encapsulation bekannt, handelt es sich um einen Schutzmechanismus, bei dem Daten logisch vor dem Zugriff des restlichen Systems verborgen werden. Hierdurch wird der direkte Zugriff unterbunden und ausschließlich über definierte, sichere Schnittstellen bereitgestellt. Zweck ist es, die Angriffsfläche auf sensible Daten zu verringern und deren Integrität sowie Vertraulichkeit zu wahren. Ohne eine solche Kapselung könnte beispielsweise eine Schadsoftware auf einem Server direkt auf Konfigurationsdateien oder im Arbeitsspeicher gehaltene Anmeldeinformationen anderer Anwendungen zugreifen und diese manipulieren oder ausleiten. Durch eine wirksame Datenkapselung kann die Institution sicherstellen, dass Zugriffe nur über vorab genehmigte und protokollierte Wege erfolgen, was eine unautorisierte Modifikation oder einen unbemerkten Abfluss von Daten erschwert. Technisch erfolgt dies zum Beispiel durch einen abgeschlossenen Speicherbereich auf einem mobilen Gerät für persönliche Informationen wie Kontakte oder Kalender (PIM-Container). Die Kapselung erfordert eine separate Authentisierung vor dem Zugriff auf die gekapstelten Daten und eine vom Betriebssystem unabhängige Daten- & Transportverschlüsselung innerhalb der Kapselung.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL isoliert Anwendungsdaten und Runtime über Container (Podman) mit separaten Namespaces, cgroups und optional Rootless-Modus: Prozess-, Mount- und Netzwerk-Sicht sind pro Container getrennt; Images und Volumes kapseln Dateisystemzugriffe. Für traditionelle Dienste ergänzt SELinux-Domain-Isolation den Datenumfang einzelner Prozesse. Container-Plattform und Sandbox-Regeln sind optional — die Institution wählt Workloads und Grenzen.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: alternative

______________________________________________________________________
