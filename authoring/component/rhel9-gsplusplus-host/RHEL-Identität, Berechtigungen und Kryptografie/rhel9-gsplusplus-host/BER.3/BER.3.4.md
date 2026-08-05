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

RHELs Audit-Subsystem (`auditd`) kann über `augenrules`-Regeln in `/etc/audit/rules.d/` Watch-Regeln auf die Kontodatenbanken `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow` und `/etc/security/opasswd` setzen (z.B. `-w /etc/passwd -p wa -k audit_rules_usergroup_modification`), sodass jeder schreibende Zugriff – also Erstellung, Änderung von Metadaten/Berechtigungen sowie Deaktivierung oder Löschung eines Zugangskontos – als Audit-Ereignis mit Zeitstempel und ausführendem Prozess/UID protokolliert wird. Die Ereignisse landen im unveränderlichen Audit-Log unter `/var/log/audit/audit.log` und können mit `ausearch`/`aureport` ausgewertet werden. Eine feldweise Differenz ("was genau wurde geändert") liefert die Watch selbst nicht, sondern nur die Tatsache und den Zeitpunkt eines schreibenden Zugriffs auf die jeweilige Datei; für die vollständige Nachvollziehbarkeit inhaltlicher Änderungen sind zusätzlich Konfigurationsmanagement oder zentrale IdM-Audit-Logs heranzuziehen. In zentral verwalteten Umgebungen protokolliert zusätzlich Red Hat IdM Änderungen an Verzeichniskonten serverseitig.

### Implementation Status: alternative

______________________________________________________________________
