---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.5 - \[Zugangskonten\] Identität-Zugangskonto

## Control Statement

Berechtigung SOLLTE ein Zugangskonto zu genau einer Identität zuweisen.

## Control guidance

Wenn ein Zugangskonto genau einer Identität zugewiesen ist erleichtert dies die Vergabe von Berechtigungen nach dem Need-to-know-Prinzip. Außerdem kann so bei einem Vorfall nachvollzogen werden, welche Person welche Befehle ausgeführt hat, z.B. mittels des Audit Logs. Anders herum können einer Identität auch mehrere Zugangskonten zugewiesen sein, z.B. ein normalen Nutzungskonto und ein Zugangskonto für die Systemadministration.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL erzwingt technisch keine 1:1-Zuordnung von Zugangskonto zu Identität; ob ein Konto tatsächlich nur einer Person zugewiesen wird, ist ein Provisionierungs- und Namensprozess der Institution (personalisierte Benutzernamen statt geteilter/generischer Konten). Mit aktiviertem `auditd`-Dienst protokolliert das System jedoch UID/`auid` zu jeder erfassten Aktion, sodass sich im Nachhinein nachvollziehen lässt, welches Konto welche Befehle ausgeführt hat — die von der Leitlinie genannte Rückverfolgbarkeit im Vorfall ist damit technisch unterstützt. Zusätzlich stellt die Beschränkung auf autorisierte, dokumentierte lokale Konten sicher, dass keine verwaisten oder unklar zugeordneten Konten bestehen bleiben. Ob mehrere Personen sich ein Konto teilen (z.B. bei generischen Servicekonten), entscheidet die Institution bei der Kontovergabe — dies liegt außerhalb der technischen Kontrolle des Hosts.

### Implementation Status: partial

______________________________________________________________________
