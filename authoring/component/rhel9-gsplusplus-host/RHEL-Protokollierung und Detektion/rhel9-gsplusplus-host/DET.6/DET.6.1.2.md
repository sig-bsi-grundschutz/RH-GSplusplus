---
x-trestle-param-values:
  det.6.1.2-prm1:
  det.6.1.2-prm2:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.6.1.2 - \[Vorfallserkennung\] Automatische Alarmierung

## Control Statement

Detektion SOLLTE bei sicherheitskritischen Ereignissen eine Alarmierung von {{ insert: param, det.6.1.2-prm1 }} durch {{ insert: param, det.6.1.2-prm2 }} ausführen.

## Control guidance

Für die Definition eines sicherheitskritischen Ereignisses, siehe Glossar (Namensräume des Grundschutz++). Bewährt hat sich hierzu der Einsatz eines Security Information and Event Management Systems (SIEM), das die Audit Logs verschiedener Hersteller auf Ereignisse überprüfen und diese korrelieren kann. Passen Sie Schwellwerte und Kriterien so an, dass keine Alarmmüdigkeit (alert fatigue) beim Personal aufkommt.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Der Host kann sicherheitskritische Ereignisse an eine zentrale Senke geben (`audispd`-syslog-Plugin, `rsyslog` mit Aktionen, `systemd-journal-upload`); Alarmierung von Personen oder Rollen übernimmt typischerweise das SIEM oder ein Ticket-Gateway, nicht `auditd` selbst. Mail-`cron` nach AIDE-Lauf (`aide_scan_notification`) ist eine rudimentäre Host-Alarmierung. Schwellwerte gegen Alarmmüdigkeit gehören in die zentrale Korrelation.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening).

### Implementation Status: partial

______________________________________________________________________
