---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.8 - \[Konfiguration von Systemen\] Alternative Administrationszugänge

## Control Statement

Konfiguration für IT-Systeme KANN alternative Administrationszugänge installieren.

## Control guidance

Das ist zum Beispiel von Bedeutung bei zentralen Systemen wie Firewalls und Router, bei deren Ausfall eine Fernwartung nicht mehr möglich ist. Hierzu können alternative Werkzeuge, sowie alternative Protokolle, Schnittstellen und Zugangskonten verwendet werden. Alternative Werkzeuge sind z.B. Kommandozeilenwerkzeuge, API-Schnittstellen oder die Konsole virtualisierter oder physischer Server, statt der Grafischen Benutzeroberfläche. Bei Cloud-Diensten kann dies z.B. durch Vorhalten von sowohl Browser-Zugang als auch CLI-Zugang geschehen. Alternative Zugangskonten sind z.B Break-Glass-Accounts, deren Zugangsdaten nur bei Notfällen aus einem Safe entnommen werden.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL unterstützt mehrere von der primären Fernverwaltung unabhängige Administrationswege: Eine serielle Konsole (`ttyS0`, per Kernel-Parameter und `getty`-Unit aktiviert) sowie die Konsole von Virtualisierungs-Hosts (z. B. `virsh console`) bleiben auch dann erreichbar, wenn Netzwerk-Management-Dienste oder die grafische Oberfläche ausgefallen sind; auf physischer Hardware ergänzen herstellerseitige Out-of-Band-Schnittstellen (IPMI/Redfish, iDRAC/iLO) den Zugriff unabhängig vom Betriebssystemzustand. Als alternative Werkzeuge stehen zudem Kommandozeile und systemd-Targets zur Verfügung, um administrative Aufgaben auch ohne grafische Oberfläche durchzuführen. Für den Notfall lässt sich zusätzlich ein separates, lokal authentifiziertes Break-Glass-Konto mit eigenem PAM-Pfad einrichten, dessen Zugangsdaten getrennt verwahrt werden. Welche dieser Mechanismen aktiviert, physisch abgesichert und in eine Notfall-Zugriffsrichtlinie überführt werden, entscheidet die Institution.

### Implementation Status: partial

______________________________________________________________________
