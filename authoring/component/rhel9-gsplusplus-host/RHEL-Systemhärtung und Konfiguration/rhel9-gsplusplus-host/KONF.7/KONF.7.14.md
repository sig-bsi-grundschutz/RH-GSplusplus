---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.14 - \[Schutz vor Schadcode\] Code-Signierung im Betriebssystemkern

## Control Statement

Konfiguration für IT-Systeme SOLLTE Code-Signierung im Betriebssystemkern aktivieren.

## Control guidance

Laufende Kernprozesse des Systems können geschützt werden, indem nur signierter Code hierauf zugreifen darf. Beispiele sind unter Windows der der PPL-Schutz (Protected Process Light) des Local Credential Store (LSA-Schutz) oder unter Linux mit SELinux oder dem Secure Computing Mode.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Code-Signierung im Kernel: RHEL erzwingt signierte Kernel-Module — unsignierte Module werden beim Laden abgewiesen (`modprobe`/`kernel` module signing). Kernel-Images und kmod-Pakete stammen aus signierten Red-Hat-Builds. Optional erweitern IMA/EVM die Integritätsprüfung für Dateien und Prozesse; Standard ist Modul-Signierung über den Distribution-Kernel.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
