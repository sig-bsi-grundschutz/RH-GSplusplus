---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.4 - \[Zugangskonten\] Protokollierung von Änderungen

## Control Statement

Berechtigung SOLLTE Aktionen an Zugangskonten revisionsfähig protokollieren.

## Control guidance

Werden Aktionen an Zugangskonten wie die Erstellung, Veränderung von Metadaten oder Berechtigungen, Aktivierung, Deaktivierung oder Löschung von Zugangskonten automatisch protokolliert, so können Sicherheitsverstöße erkannt und nachgewiesen werden. Siehe auch Praktik Detektion.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Das Audit-Subsystem (`auditd`) kann über `augenrules`-Regeln unter `/etc/audit/rules.d/` mit Watch-Flag `-p wa` (write, attribute change) jeden Schreibzugriff auf `/etc/passwd`, `/etc/shadow`, `/etc/group` und `/etc/gshadow` protokollieren. Da das Erstellen, Ändern von Metadaten oder Berechtigungen, Aktivieren/Deaktivieren (z.B. via `usermod -L`/`-U`, was `/etc/shadow` schreibt) sowie das Löschen eines Zugangskontos stets einen Schreibzugriff auf mindestens eine dieser Dateien auslöst, deckt die Kombination der vier Watch-Regeln alle in der Leitlinie genannten Aktionen ab; jeder Audit-Datensatz enthält dabei Zeitstempel und die ausführende Benutzer-ID (`auid`). Schutz und Aufbewahrung des Audit-Protokolls selbst (Manipulationssicherheit, Remote-Weiterleitung) sind Gegenstand der Praktik Detektion und werden dort behandelt.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Rules:

  - audit_rules_etc_group_open
  - audit_rules_etc_passwd_open
  - audit_rules_etc_shadow_open
  - audit_rules_etc_gshadow_open

### Implementation Status: implemented

______________________________________________________________________
