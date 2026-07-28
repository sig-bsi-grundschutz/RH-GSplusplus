---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

---
x-trestle-set-params:
  konf.2.2-prm1:
    values:
---

# KONF.2.2 - \[Konfiguration von Systemen\] Kryptographische Verfahren in IT-Systemen

## Control Statement

Konfiguration für IT-Systeme SOLLTE kryptographische Verfahren nach {{ insert: param, konf.2.2-prm1 }} im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement aktivieren.

## Control guidance

Kryptographie wird für die Authentifizierung, Verschlüsselung und Integritätprüfung in Systemen verwendet, z.B. bei der Verschlüsselung von Speichermedien, bei der Anmeldung am System, Transportverschlüsselung von Systemupdates oder Integritätsprüfung von Systemfunktionen. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Funktionen so zu konfigurieren sind, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Kryptographie zu finden ist.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL System-wide Crypto Policies (/etc/crypto-policies) steuern zulässige kryptographische Verfahren für Dienste; die Institution wählt das passende Profil (z. B. DEFAULT, FIPS:OSPP).

### Rules:

  - configure_crypto_policy
  - crypto_policy_not_overridden

### Implementation Status: partial

______________________________________________________________________
