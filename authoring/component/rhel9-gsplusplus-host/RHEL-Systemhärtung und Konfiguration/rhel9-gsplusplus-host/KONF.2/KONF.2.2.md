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

RHEL setzt kryptographische Verfahren zentral über die System-wide Crypto Policies durch (`update-crypto-policies --set <Policy>`): Alle policy-fähigen Bibliotheken und Dienste (OpenSSL, GnuTLS, NSS, OpenSSH, libkrb5 u. a.) übernehmen automatisch dasselbe Regelwerk für TLS-Versionen, Schlüssellängen und Hash-Algorithmen, statt individuell konfiguriert zu werden. Im DEFAULT-Profil sind in RHEL 9 bereits TLS < 1.2, DH/RSA-Schlüssel < 2048 Bit, SHA-1 für Signaturen sowie veraltete Chiffren wie 3DES und RC4 deaktiviert;
Zusätzlich zu den Standard-Profilen bietet RHEL 9 das FUTURE-Profil für Umgebungen mit besonders hohen Sicherheitsanforderungen: Es deaktiviert TLS < 1.3, erhöht die minimale Schlüssellänge auf 3072 Bit für RSA/DH und 256 Bit für ECC, verbietet SHA-1 vollständig (auch für HMAC) und aktiviert ausschließlich moderne Cipher Suites. Das FUTURE-Profil ist besonders relevant für kritische Infrastrukturen, kann jedoch Kompatibilitätsprobleme mit älteren Systemen verursachen. Ebenfalls besteht die Möglichkeit entsprechende die Policies zu customizen (siehe `man update-crypto-policies(8)`) um komplett eigene Policies zu schreiben, oder einzelne Algorithmen aus bestehenden Policies zu entfernen. Welches konkrete Profil (DEFAULT, FUTURE, LEGACY) angemessen ist, hängt von den Anforderungen aus Berechtigung (BER) ab und ist eine Entscheidung der Institution.

### Rules:

  - configure_crypto_policy
  - crypto_policy_not_overridden

### Implementation Status: partial

______________________________________________________________________
