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

RHEL schützt den Arbeitsspeicher standardmäßig durch ASLR (`kernel.randomize_va_space`), das NX-Bit (Execute Disable) der CPU und Stack-Canaries in mit `-fstack-protector` gebauten Binaries. DEP verhindert Ausführung von Code in Datenbereichen; ASLR erschwert vorhersagbare Speicherlayouts für ROP- und Overflow-Angriffe. Side-Channel-Angriffe (Spectre/Meltdown) und hardwarebasierte TEE erfordern Firmware/Microcode und ggf. zusätzliche Kernel-Mitigationen — nicht vollständig durch Host-Konfiguration allein abgedeckt.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
