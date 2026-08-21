---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.6.2 - \[Vorfallserkennung\] Beurteilung von Eingängen

## Control Statement

Detektion SOLLTE ein Verfahren zur Beurteilung von Datei-Eingängen verankern.

## Control guidance

Kann beispielsweise ein Virenscanner eine Datei nicht überprüfen, weil sie mit einem Passwort geschützt ist, erhalten Nutzende die Datei erst, wenn sie durch das für Detektion zuständige Personal freigegeben wurde. Dazu muss die Datei aus einer vertrauenswürdigen Quelle stammen und keine Anzeichen für einen Angriff vorliegen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL liefert keinen nativen Virenscanner für Datei-Eingänge; `fapolicyd` kann Ausführung unbekannter Dateien verhindern (Allowlist), prüft aber nicht den Inhalt passwortgeschützter Archive. ClamAV o. ä. wäre Zusatzsoftware (EPEL/Drittanbieter), Freigabe durch Detektionspersonal ein Prozess. Mail-/Proxy-Sandboxen liegen außerhalb des generischen Hosts.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
