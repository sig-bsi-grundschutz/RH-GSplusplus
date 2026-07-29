---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.4.2 - \[Konfiguration von Systemen\] Externe Cloud-Anbindungen

## Control Statement

Konfiguration für IT-Systeme SOLLTE nicht benötigte Cloud-Anbindungen deaktivieren.

## Control guidance

Eine Cloud-Anbindung ist eine technische Schnittstelle, über die ein IT-System Daten oder Dienste mit einer externen Cloud-Plattform austauscht. Dazu können sowohl direkte API-Integrationen wie die Anmeldung an Cloud-Verzeichnisdienste, aber auch automatische Synchronisationsmechanismen, Hintergrund-Updates über Cloud-Server oder agentenbasierte Remote-Management-Funktionen zählen. Nicht benötigte Anbindungen können dadurch identifiziert werden, dass sie weder für den produktiven Betrieb noch für Wartung, Support oder Sicherheitsfunktionen erforderlich sind. Der Sinn und Zweck dieser Regelung liegt darin, die Angriffsfläche zu reduzieren und unkontrollierte Datenflüsse zu vermeiden. Ein nicht genutzter, aber weiterhin aktiver Cloud-Connector könnte etwa unbemerkt sensible Metadaten an Drittdienste übertragen oder als Einfallstor für Schadsoftware missbraucht werden; die gezielte Deaktivierung kann dagegen unnötige Risiken eliminieren und die Übersichtlichkeit der Systemarchitektur erhöhen.

______________________________________________________________________

## What is the solution and how is it implemented?

Cloud-spezifische Anbindungen wie cloud-init (Instanz-Provisionierung/Metadaten-Abruf) und Hypervisor-/Cloud-Guest-Agenten (z. B. qemu-guest-agent, WALinuxAgent, google-guest-agent) sind auf RHEL als optionale Pakete bzw. systemd-Dienste realisiert und lassen sich über `dnf remove` bzw. `systemctl mask --now` vollständig entfernen oder deaktivieren, wenn ein System nicht in einer entsprechenden Cloud-/Virtualisierungsumgebung betrieben wird oder kein automatisiertes Remote-Management über diesen Kanal benötigt wird. Auf physischen oder eigenständig verwalteten Systemen ist keine dieser Komponenten Teil einer Standardinstallation. Die Entscheidung, welche Cloud-Anbindungen für Betrieb, Wartung oder Support tatsächlich erforderlich sind, trifft die Institution auf Basis ihrer Bereitstellungsarchitektur.

### Implementation Status: partial

______________________________________________________________________
