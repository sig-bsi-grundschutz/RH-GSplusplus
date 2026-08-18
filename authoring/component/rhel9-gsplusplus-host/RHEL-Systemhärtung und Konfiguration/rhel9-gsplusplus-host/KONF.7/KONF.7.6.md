---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.6 - \[Schutz vor Schadcode\] Automatische Updates

## Control Statement

Konfiguration für IT-Systeme SOLLTE Automatische Updates der Mechanismen zur Schadcodeerkennung aktivieren.

## Control guidance

Da Schadprogramme und Angriffsmethoden ständig abgeändert werden um bekannte Erkennungsmuster zu umgehen, sind aktuelle Erkennungsfunktionen entscheidend um laufende Angriffe erkennen zu können, z.B. Signatur-Update oder Aktualisierungen der Lernfunktion zur Anomalieerkennung. Dies kann durch automatische Aktualisierungen der Signaturen und Mechanismen zur Angriffserkennung umgesetzt werden, z.B. als tagesaktueller Download von Viren-Signaturen. Die Anforderung kann auch durch einen schrittweisen Rollout der Erkennungsfunktionen umgesetzt werden, um einen Test in der Institution zu ermöglichen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Automatische Aktualisierung von Schutzmechanismen stellt RHEL über `dnf-automatic` (optional security-only) und Red Hat Subscription für signierte Paket- und Policy-Updates bereit. SELinux-Policy-Pakete und Errata kommen über normale Update-Kanäle. Signatur-Updates für Drittanbieter-AV (z. B. `freshclam`) sind nicht Teil des supported Set und erfordern separate Automatisierung.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
