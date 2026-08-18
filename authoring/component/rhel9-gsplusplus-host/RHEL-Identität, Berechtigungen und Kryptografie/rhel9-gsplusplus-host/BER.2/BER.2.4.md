---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.2.4 - \[Identitätsmanagement\] Protokollierung von Stammdatenänderungen

## Control Statement

Berechtigung SOLLTE Änderungen von Identitäts-Stammdaten protokollieren.

## Control guidance

Zu einem Ereignisprotokoll gehört der Zeitpunkt, das Zugangskonto, sowie welche Änderungen vorgenommen wurden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Änderungen an identitätsrelevanten Dateien können mit auditd-Regeln erfasst werden; Identitätslebenszyklus und IAM-Prozesse verbleiben in der Verantwortung der Institution (PAM, SSSD, Verzeichnisintegration).

### Rules:

  - audit_rules_usergroup_modification_passwd

### Implementation Status: partial

______________________________________________________________________
