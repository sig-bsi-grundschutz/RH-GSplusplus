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

Für mit den Internet verbundene Systeme wird Red Hat Lightspeed kontinuierlich durch Red Hat mit neuen Signaturen aktualisiert. Da in disconnected/air-gapped Systemen RHEL aktuell (Aug 2026) kein Malware-Scanning bereitstellt, obliegt hier die Implementation der entsprechenden 3rd Party Software.

### Implementation Status: planned

______________________________________________________________________
