---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.9 - \[Protokollierung\] Fehler der Anwendung

## Control Statement

Detektion für Anwendungen SOLLTE Fehlermeldungen der Anwendung protokollieren.

## Control guidance

Fehlermeldungen können wichtige Hinweise auf technisches Versagen oder menschliches Fehlverhalten liefern. Insbesondere, wenn Fehlermeldungen neuartig sind, oder gehäuft auftreten, können sie Indiz für Probleme sein, die behandlungsbedürftig sind. Denken Sie insbesondere auch an Fehlermeldungen in automatisierten Prozessen, da diese möglicherweise sonst nicht zur Kenntnisnahme gelangen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

`systemd-journald` und optional `rsyslog` nehmen Standardausgabe, Syslog und Unit-Fehler von Diensten entgegen, die als systemd-Units laufen oder nach syslog schreiben. Der Host erzwingt nicht, dass jede Anwendung aussagekräftige Fehlermeldungen erzeugt — das bleibt Implementierung der jeweiligen Software. Häufung und Eskalation neuartiger Fehler sind Aufgabe von Auswertung/SIEM, nicht des einzelnen Hosts.

Weitere Informationen: [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index), [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
