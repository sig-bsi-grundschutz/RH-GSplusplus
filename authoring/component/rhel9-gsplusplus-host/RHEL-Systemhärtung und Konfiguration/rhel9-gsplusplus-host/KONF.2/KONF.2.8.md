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

Alternative Administrationswege (serielle Konsole, out-of-band-Management) sind auf RHEL konfigurierbar; physische Absicherung, Freigabe und Nutzungsrichtlinien verbleiben bei der Institution.

### Implementation Status: partial

______________________________________________________________________
