---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.16.1 - \[Schutz vor Schadcode\] Anti-Exploit für den Arbeitsspeicher

## Control Statement

Konfiguration für IT-Systeme SOLLTE den Schutz des Arbeitsspeichers vor der Ausnutzung bekannter Sicherheitslücken aktivieren.

## Control guidance

Gelingt es Angreifern Code auf dem System auszuführen, so könnten sie versuchen, über den Arbeitsspeicher des Systems den Schadcode weiter zu verbreiten oder Zugriff auf Daten zu erlangen. Hierzu gehören Angriffe wie Buffer Overflows, Return-Oriented Programming, Heap Spraying, Use-After-Free, Memory Scraping oder Side-Channel-Angriffe wie Spectre und Meltdown. Schutzmaßnahmen hiergegen können durch Software oder durch Hardware umgesetzt sein. Softwarebasiert sind z.B. Address Space Layout Randomization (ASLR), Data Execution Prevention (DEP), Stack Canaries. Hardwarebasiert sind z.B. Trusted Execution Environments (TEE).

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL legt den Arbeitsspeicher-Schutz überwiegend in den Kernel-Build: KASLR (`CONFIG_RANDOMIZE_BASE`) randomisiert den Speicherbereich, in dem das Kernel-Image geladen wird, `CONFIG_RANDOMIZE_MEMORY` verschiebt zusätzlich Physmap, vmalloc und vmemmap. Stack-Canaries (`CONFIG_STACKPROTECTOR` und `CONFIG_STACKPROTECTOR_STRONG`, `-fstack-protector-strong`) erkennen Stack-Overflows vor der Ausführung. `CONFIG_STRICT_KERNEL_RWX` macht Kernel-Text und rodata nur lesbar und Nicht-Text nicht ausführbar (W^X). `CONFIG_SLAB_FREELIST_RANDOM` verhindert die Vorhersagbarkeit der Speicheradressen von neuen Pages und erschwert dadurch Heap-Spraying. Im Userspace greifen ASLR über `kernel.randomize_va_space=2` und NX/DEP (ExecShield), sofern `noexec=off` nicht gesetzt ist. `kernel.kptr_restrict` (1 oder 2) blendet Kernelzeiger aus, damit KASLR nicht über `/proc` unterlaufen wird.

Zusätzlich prüfbare GRUB-Parameter härten Allokation und Seitenkanäle: `page_poison=1` beschreibt freigegebene Seiten mit Mustern (Use-after-Free, Datenreste); `init_on_alloc=1` nullt Speicher vor der Vergabe (uninitialisierte Heap-Leaks); `vsyscall=none` entfernt die vsyscall-Seite als ROP-Trampolin. Meltdown wird über Kernel Page-Table Isolation (`pti=on`) abgefangen, Spectre v2 über `spectre_v2=on`. Einzelne oder die Kombination dieser Maßnahmen können Performance-Einbußen nach sich ziehen, insbesondere, wenn sie im Default nicht aktiviert sind.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:
  - kernel_config_randomize_base
  - kernel_config_randomize_memory
  - kernel_config_stackprotector
  - kernel_config_stackprotector_strong
  - kernel_config_strict_kernel_rwx
  - kernel_config_slab_freelist_random
  - sysctl_kernel_randomize_va_space
  - sysctl_kernel_exec_shield
  - sysctl_kernel_kptr_restrict
  - grub2_page_poison_argument
  - grub2_init_on_alloc_argument
  - grub2_vsyscall_argument
<!-- not adding spectre and meltdown mitigations, as current hardware should not be vulnerable anymore. -->
<!-- - grub2_pti_argument -->
<!-- - grub2_spectre_v2_argument -->

### Implementation Status: partial

______________________________________________________________________
