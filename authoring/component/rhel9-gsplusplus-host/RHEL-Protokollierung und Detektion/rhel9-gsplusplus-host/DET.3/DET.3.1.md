---
x-trestle-param-values:
  det.3.1-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1 - \[Protokollierung\] Protokollierung sicherheitsrelevanter Ereignisse

## Control Statement

Detektion für Anwendungen SOLLTE Sicherheitsrelevante Ereignisse mindestens für {{ insert: param, det.3.1-prm1 }} protokollieren.

## Control guidance

Für die Definition eines Sicherheitsrelevanten Ereignisses, siehe Glossar (Namensräume des Grundschutz++). Relevant sind hierbei insbesondere die Protokollierung auf zentralen Diensten und Servern. Dazu gehören auch vorhandene Cloud-Anwendungen oder -Dienste. Hier besteht ein enger Bezug zur Praktik Änderungen und Tests.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL zeichnet sicherheitsrelevante Host-Ereignisse mit dem Kernel-Audit-Subsystem (`auditd`, Paket `audit`) auf; der Dienst muss aktiv sein und kann bereits ab dem Bootloader mit `audit=1` eingeschaltet werden. Welche Syscalls, Dateiwatches und Anmeldeereignisse in `/etc/audit/rules.d/` landen, legt die Institution fest; `systemd-journald` ergänzt Kernel- und Dienstemeldungen. Die geforderte Mindestaufbewahrungsfrist sowie Anwendungs- und Cloud-Ereignisse außerhalb des Hosts bleiben organisatorisch bzw. beim zentralen Log-Aggregator.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
