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

Bei mit dem Internet verbundenen Systemen können wir Red Hat Lightspeed entsprechende Benachrichtungen konfiguriert werden. Für nicht verbundene Systeme können nur die mitigierenden Teilkomponenten Benachrichtigung an ein SIEM über die audit oder syslog Komponenten versenden. AIDE kann bei Abweichungen Mail oder Script-Hooks nutzen. `auditd`-Ereignisse lassen sich per `audisp` oder `rsyslog` an ein SIEM schicken.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Red Hat Lightspeed Malware Notification](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/assessing_and_reporting_malware_signatures_on_rhel_systems/malware-svc-additional-concepts#con-mal-enabling-notifications-integrations_malware-svc-additional-collector-alerts).

### Rules:

  - aide_scan_notification
  - rsyslog_remote_loghost
  - service_rsyslog_enabled

### Implementation Status: partial

______________________________________________________________________
