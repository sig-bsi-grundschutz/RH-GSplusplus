---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.1 - \[Überwachung von Aktivitäten\] Überwachung der Protokollierung

## Control Statement

Detektion SOLLTE die Funktionsfähigkeit der Protokollierung überwachen.

## Control guidance

Zu den Kriterien kann beispielsweise die Aktivierung oder Deaktkvierung des Loggings auf Systemen, sowie die Datenmenge eingehender Logs in einem bestimmten Zeitraum gehören.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

systemd überwacht, ob `auditd`, `systemd-journald` und optional `rsyslog` aktiv sind; CaC-Regeln fordern genau diesen Enabled-Zustand. `auditd` kann bei vollem Datenträger oder voller Event-Queue Aktionen auslösen (`overflow_action`, `space_left`). Die **Datenmenge** eingehender Logs über einen Zeitraum und das Erkennen eines stillen Logging-Ausfalls ohne Dienstestopp sind Aufgabe von SIEM/Monitoring, nicht einer Host-Regel.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index).

### Implementation Status: partial

______________________________________________________________________
