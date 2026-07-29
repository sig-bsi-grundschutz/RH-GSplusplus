---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.4 - \[Protokollierung\] Systemfehler

## Control Statement

Detektion für IT-Systeme SOLLTE Fehlermeldungen des Systems protokollieren.

## Control guidance

Die Protokollierung von Fehlermeldungen kann eine wesentliche Grundlage für die Früherkennung von Sicherheits- und Stabilitätsproblemen in IT-Systemen bilden. Ohne ein systematisches Logging könnte ein kritischer Hardwaredefekt, eine beschädigte Systemdatei oder ein fehlgeschlagener Sicherheits-Update-Prozess unentdeckt bleiben und dadurch die Integrität oder Verfügbarkeit von IT-Systemen gefährden. Ebenso könnte ein Angreifer, der wiederholt unautorisierte Befehle ausführt oder Dienste fehlerhaft anspricht, unbemerkt bleiben, wenn die resultierenden Fehlermeldungen nicht nachvollzogen werden. Auf technischer Ebene kann es zweckmäßig sein, das native Logging des Betriebssysteme zu aktivieren und so zu konfigurieren, dass Fehlermeldungen konsistent erfasst werden – beispielsweise über Syslog-Dienste oder Windows-Event-Logs. Eine zentrale Log-Sammlung kann helfen, auch bei verteilten Systemen eine einheitliche Auswertung vorzunehmen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL erfasst Systemfehler über das systemd-Journal und das Audit-Subsystem; Aufbewahrung und zentrale Sammlung legt die Institution fest.

### Rules:

  - audit_rules_var_log_journal

### Implementation Status: partial

______________________________________________________________________
