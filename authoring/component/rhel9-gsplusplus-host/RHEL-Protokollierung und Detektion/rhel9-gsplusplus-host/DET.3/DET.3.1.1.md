---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.1 - \[Protokollierung\] Authentifizierungen

## Control Statement

Detektion für IT-Systeme SOLLTE Authentifizierungen bei Erfolg und Fehlschlag protokollieren.

## Control guidance

Relevant sind dabei z.B. die lokale Anmeldung, Anmeldung und Zugriffe auf Schnittstellen des Systems über das Netz, oder auch die physische Authentifizierung an einem Zutrittskontrollsystem.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL auditd kann Erfolg und Fehlschlag von Authentisierungen protokollieren, wenn Audit-Regeln gemäß Produktdokumentation und scap-security-guide-Baselines konfiguriert sind.

### Rules:

  - audit_rules_login_events_faillog

### Implementation Status: partial

______________________________________________________________________
