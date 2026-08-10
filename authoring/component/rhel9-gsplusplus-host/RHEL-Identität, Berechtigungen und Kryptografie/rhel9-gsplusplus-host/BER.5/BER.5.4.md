---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.4 - \[Umgang mit Authentisierungsmitteln\] Nur etablierte Kryptographie

## Control Statement

Berechtigung SOLLTE bei kryptografischen Authentifizierungsmitteln die ausschließliche Verwendung etablierter kryptografischer Algorithmen nach {{ insert: param, ber.5.4-prm1 }} verankern.


## Control guidance

Kryptografische Authentifizierungsmittel sind Authentisierungsnachweise, deren Sicherheit wesentlich auf kryptografischen Verfahren beruht, etwa Passwort-Hashing, Zertifikate, Schlüsselpaare, Smartcards, Hardware-Token, Passkeys/FIDO2-Authentifikatoren, signaturbasierte API-Zugänge oder SSH-Schlüssel (engl. cryptographic authenticators). Etablierte kryptografische Algorithmen sind mathematisch fundierte Verschlüsselungsverfahren und Protokolle, die in der aktuellen Praxis nicht mit vertretbarem Aufwand gebrochen werden können, beispielsweise für Signaturen, Message Authentication Codes, Hashfunktionen, Schlüsselableitung oder authentisierte Verschlüsselung. Sie basieren auf mathematisch schwer lösbaren Problemen, bieten Resistenz gegen bekannte kryptanalytische Angriffe, unterstützen ausreichend große Schlüssellängen und wurden von Experten gründlich geprüft und analysiert. Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Etablierte kryptografische Algorithmen für Authentisierungspfad und Protokolle erzwingt RHEL über systemweite Crypto Policies (`update-crypto-policies`): Stufen wie `DEFAULT`, `FUTURE` oder `FIPS` vereinheitlichen TLS, SSH, Kerberos, OpenSSL und weitere Backends und entfernen schwache Verfahren. Dienste, die die Policy einbinden (u. a. OpenSSH über Crypto-Policy-Drop-ins), erben dieselbe Algorithmuswahl; Abweichungen sind möglich, aber bewusst und dokumentationsseitig abzuraten. Die Policy ist an anerkannte Vorgaben (u. a. FIPS) ausrichtbar; BSI TR-02102 bleibt Maßstab für die institutionelle Stufenwahl.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
