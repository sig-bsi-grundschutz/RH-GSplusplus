---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.12 - \[Schutz vor Schadcode\] Einschränkung von Skripten

## Control Statement

Konfiguration für IT-Systeme KANN die Ausführung nicht autorisierter Skripte einschränken.

## Control guidance

Skripte könnten Schadcode enthalten oder zu Fehlerzuständen auf dem System führen. Die Auswirkungen schädlicher Skripte können eingeschränkt werden, indem nur bestimmte Systemfunktionen für Skripte erlaubt werden. Die Umsetzung ist mit Funktionen wie dem Windows PowerShell Constrained Language Mode oder Linux Secure Computing Mode möglich. Verfügt das System über keine Möglichkeit zur Ausführung von Skripten, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Skript-Ausführung kann fapolicyd nach Pfad, Hash oder MIME-Typ einschränken; SELinux-Booleans wie `selinuxuser_execstack` härten Speicher-Execution. `noexec`-Mounts blockieren Skripte auf eingebundenen Medien. Interpretierte Sprachen (Python, Shell) erfordern explizite Allow-Regeln in der fapolicyd-Policy.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
