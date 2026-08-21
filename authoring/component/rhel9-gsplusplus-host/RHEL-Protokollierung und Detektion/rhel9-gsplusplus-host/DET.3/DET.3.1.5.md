---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.5 - \[Protokollierung\] Störungen der Netzerreichbarkeit

## Control Statement

Detektion für IT-Systeme KANN Störungen der Netzerreichbarkeit protokollieren.

## Control guidance

Eine Störung der Netzerreichbarkeit kann ein Indiz für Überlastungen, Fehler oder Angriffe im Netz sein. Wann eine Störung vorliegt, kann anhand von Schwellwerten, z.B. durch das Ausbleiben eines regelmäßigen Heartbeat-Paketes, getestet werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

NetworkManager und der Kernel protokollieren Link- und Adressänderungen (Carrier, Disconnect, DHCP) im Journal; `auditd` kann zusätzlich Änderungen an der Netzkonfiguration (`/etc/NetworkManager/`, `sethostname`) überwachen. Heartbeat-Ausfälle und Schwellwerte für „Störung der Erreichbarkeit“ sind kein eingebauter Host-Check, sondern Sache eines zentralen Monitorings oder externer Probes.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index).

### Implementation Status: partial

______________________________________________________________________
