---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  RHEL-Systemhärtung und Konfiguration:
    - name: var_selinux_state
      values:
        - enforcing
      component-values:
        - enforcing
---

# KONF.7.16 - \[Schutz vor Schadcode\] Anti-Exploit

## Control Statement

Konfiguration für IT-Systeme SOLLTE Systemfunktionen zum Schutz des Systems vor der Ausnutzung bekannter Sicherheitslücken aktivieren.

## Control guidance

Angreifer versuchen häufig, bekannte Sicherheitslücken oder offene Systemfunktionen zur Verbreitung oder Einnistung von Schadcode zu missbrauchen. Funktionen zum Schutz vor der Ausnutzung von Sicherheitslücken (Anti-Exploit) können helfen dies zu verhindern. Beispiele sind Data Execution Prevention (DEP), Defender Exploit Guard (WDEG) oder System Integrity Protection (SIP).

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt prüfbare Anti-Exploit-Funktionen per Default aktiviert bereit: Address Space Layout Randomization (ASLR) über den `sysctl` Wert `kernel.randomize_va_space=2`; NX/XD (Linux DEP), sofern der Kernel-Parameter `noexec=off` nicht gesetzt ist. SMEP (Supervisor Mode Execution Prevention) und SMAP (Supervisor Mode Access Prevention), sofern `nosmep` und `nosmap` nicht in der GRUB-Kommandozeile stehen. Ebenfalls ist im Default SELinux als MAC-Schicht im Zustand `enforcing`. Kernel-KASLR und Stack-Canaries sind zusätzlich über KONF.7.16.1 abbildbar.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - sysctl_kernel_randomize_va_space
  - sysctl_kernel_exec_shield
  - grub2_nosmep_argument_absent
  - grub2_nosmap_argument_absent
  - package_libselinux_installed
  - grub2_enable_selinux
  - selinux_not_disabled
  - selinux_state

### Implementation Status: partial

______________________________________________________________________
