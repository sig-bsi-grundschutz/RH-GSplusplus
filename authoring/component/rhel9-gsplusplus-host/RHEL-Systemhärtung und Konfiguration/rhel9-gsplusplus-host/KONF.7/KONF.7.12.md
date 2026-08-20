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

Skript-Ausführung kann über `fapolicyd` eingeschränkt werden. Mitgeliefert wird ein Regelwerk, welches über `/usr/share/fapolicyd/sample-rules/72-shell.rules` Shell-Skripte explizit freigibt. Sofern dies nicht implementiert wird, sind Shell-Skripte verboten, da interpretierte Sprachen (Python, Shell)  explizite Allow-Regeln in der fapolicyd-Policy erfordern.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - fapolicy_default_deny
  - package_fapolicyd_installed
  - service_fapolicyd_enabled

### Implementation Status: partial

______________________________________________________________________
