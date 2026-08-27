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

RHEL zeichnet sicherheitsrelevante Host-Ereignisse mit dem Kernel-Audit-Subsystem (`auditd`, Paket `audit`) auf. Der Dienst muss aktiv sein. Hierzu kann er bereits ab dem Bootloader (grub2) mit `audit=1` eingeschaltet werden. Die Festlegung, welche Ereignisse sicherheitsrelevant sind, sind durch die Institution zu treffen und entsprechende Regeln in `/etc/auditd/rules.d/` zu hinterlegen und mittels `augenrules` in `auditd` zu überführen. Im Verzeichnis `/usr/share/audit/sample-rules/` stehen Beispielhafte Regeln für bestimmte Anforderungen zur Verfügung. `auditd` auf dem OS arbeitet auf Basis der Logdatei-Größe, wodurch eine bestimmte Zeitfrist nicht garantiert werden kann. Um dies zu erreichen empfiehlt sich ein Forwarding (siehe andere DET Anforderungen) an ein zentrales Log-Management und die Sicherstellung der Zeit-Fristen dort. Alternativ kann dieser [Solution](https://access.redhat.com/solutions/661603) gefolgt werden (nicht supportet).

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hcat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - package_audit_installed
  - service_auditd_enabled
  - grub2_audit_argument
  - service_systemd-journald_enabled

### Implementation Status: partial

______________________________________________________________________
