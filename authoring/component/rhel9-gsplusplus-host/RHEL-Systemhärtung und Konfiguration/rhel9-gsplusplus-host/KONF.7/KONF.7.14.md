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

RHEL kann den Einsatz signierter Kernel-Module erzwingen — unsignierte Module werden beim Laden abgewiesen (`modprobe`/`kernel` module signing). Kernel-Images und kmod-Pakete stammen im Standard aus signierten Red-Hat-Builds. Dies addressiert das Control Statement ("Code-Signierung im Betriebssystemkern"). Für das Ausführen von vertrauenswürdigen Skripten und Anwendungen (Langtext aus der Control Guidance) sind die Maßnahmen der vorherigen KONF.7.x zu berücksichtigen.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Signing a Kernel](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_assembly_managing-kernel-command-line-parameters-with-uki)

### Rules:

  - kernel_config_module_sig
  - kernel_config_module_sig_all

### Implementation Status: implemented

______________________________________________________________________
