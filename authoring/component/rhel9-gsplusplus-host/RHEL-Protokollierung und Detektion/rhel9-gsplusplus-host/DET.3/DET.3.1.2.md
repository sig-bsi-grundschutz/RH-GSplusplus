---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.2 - \[Protokollierung\] Ausgeführte Kommandozeilenbefehle

## Control Statement

Detektion für IT-Systeme SOLLTE ausgeführte Kommandozeilenbefehle protokollieren.

## Control guidance

Angreifer nutzen Kommandozeilenfunktionen wie Bash oder Windows PowerShell, um mit Bordmitteln schädliche Befehle auszuführen. Hier sind vor allem Living-off-the-Land-Binaries (LOLBins) und Nutzlasten (Malware Payloads) zu nennen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt konfigurierbare Audit-Regeln (einschließlich privilegierter Befehle und Syscall-Auditing) über auditd bereit; Regelsätze wählt die Institution. Siehe Sicherheitshärtung und OpenSCAP-Inhalte für Beispiele.

### Implementation Status: partial

______________________________________________________________________
