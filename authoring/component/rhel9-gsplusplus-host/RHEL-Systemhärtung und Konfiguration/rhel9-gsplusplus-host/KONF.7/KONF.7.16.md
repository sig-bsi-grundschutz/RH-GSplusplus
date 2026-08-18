---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
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

RHEL aktiviert mehrere Kernel- und Laufzeitschutzmechanismen gegen Exploit-Ausnutzung: NX/DEP über die CPU, SMEP/SMAP auf unterstützter Hardware (sofern nicht per Kernel-Parameter deaktiviert), Stack-Canaries und weitere Compiler-Härtung in Distribution-Binaries sowie SELinux als obligatorische MAC-Schicht. Zusätzliche Einschränkungen (sysctl, seccomp-Profile, `kernel.yama.ptrace_scope`) sind konfigurierbar, decken aber nicht automatisch alle bekannten Angriffsklassen ab — betriebsspezifische Bewertung bleibt nötig.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
