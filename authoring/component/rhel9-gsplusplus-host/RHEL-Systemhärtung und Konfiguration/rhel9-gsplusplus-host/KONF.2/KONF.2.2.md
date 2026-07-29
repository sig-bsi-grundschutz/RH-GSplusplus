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

RHEL setzt kryptographische Verfahren zentral über die System-wide Crypto Policies durch (`update-crypto-policies --set <Policy>`): Alle policy-fähigen Bibliotheken und Dienste (OpenSSL, GnuTLS, NSS, OpenSSH, libkrb5 u. a.) übernehmen automatisch dasselbe Regelwerk für TLS-Versionen, Schlüssellängen und Hash-Algorithmen, statt individuell konfiguriert zu werden. Im DEFAULT-Profil sind in RHEL 9 bereits TLS < 1.2, DH/RSA-Schlüssel < 2048 Bit, SHA-1 für Signaturen sowie veraltete Chiffren wie 3DES und RC4 deaktiviert; für Umgebungen mit erhöhten Anforderungen stehen FIPS- und FIPS:OSPP-Subpolicies zur Verfügung, die insbesondere im Zusammenspiel mit Identitäts- und Berechtigungsmanagement (SSH, Kerberos, TLS-Client-Auth) verwendet werden. Die Regel `crypto_policy_not_overridden` stellt zusätzlich sicher, dass keine Anwendung die zentrale Policy durch eigene Konfigurationsdateien in `/etc/crypto-policies/back-ends` unterläuft. Welches konkrete Profil (DEFAULT, FIPS, FIPS:OSPP, LEGACY) angemessen ist, hängt von den Anforderungen aus Berechtigung (BER) ab und ist eine Entscheidung der Institution.

### Rules:

  - configure_crypto_policy
  - crypto_policy_not_overridden

### Implementation Status: partial

______________________________________________________________________
