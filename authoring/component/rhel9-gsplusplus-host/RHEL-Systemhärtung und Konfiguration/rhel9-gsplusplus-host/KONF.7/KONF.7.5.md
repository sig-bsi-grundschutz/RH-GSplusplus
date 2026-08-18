---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.5 - \[Schutz vor Schadcode\] Alarmierung

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine Benachrichtigung bei potenziellem Schadcode aktivieren.

## Control guidance

Durch die Aktivierung einer Benachrichtigung kann eine Institution schnell auf verdächtige Aktivitäten reagieren, noch bevor sich der Schadcode vollständig im System etablieren und erheblichen Schaden anrichten könnte. Eine Möglichkeit zur Umsetzung ist der Einsatz von Endpoint Detection and Response (EDR)-Lösungen, die in der Lage sind, Verhaltensanomalien in Echtzeit zu erkennen und sofortige Benachrichtigungen auszulösen. Eine effektive Umsetzung erfordert, dass die Benachrichtigungen sowohl an die Endnutzer als auch an die zuständigen IT-Sicherheitsteams gesendet werden, um eine umfassende und koordinierte Reaktion zu ermöglichen. Dabei können Automatisierungsregeln im Security Information and Event Management (SIEM) die Benachrichtigungen an die richtigen Personen eskalieren und so die Reaktionszeit verkürzen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Benachrichtigung bei potenziellem Schadcode erfordert auf RHEL Integration in Monitoring: AIDE kann bei Abweichungen Mail oder Script-Hooks nutzen; auditd-Ereignisse lassen sich per `audisp` oder rsyslog an SIEM schicken. Kein vorgefertigter Malware-Alarm — die Institution koppelt Integritäts- und Audit-Alerts mit Monitoring (Red Hat Insights, Satellite oder externes SIEM).

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Systemstatus überwachen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index).

### Implementation Status: partial

______________________________________________________________________
