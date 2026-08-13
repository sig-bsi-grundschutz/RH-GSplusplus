---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.6 - \[Schlüsselmanagement\] Etablierte Algorithmen beim Transport

## Control Statement

Berechtigung SOLLTE die ausschließliche Verwendung etablierter kryptografischer Algorithmen beim Transport geheimer Schlüssel verankern.


## Control guidance

Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Der Transport kann mit Public Key Cryptography Standards (PKCS), z.B. PKCS#12 Dateiformat erfolgen. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Beim Transport geheimer Schlüssel über das Netz (TLS, SSH, IPsec) erzwingt RHEL etablierte Algorithmen über die systemweite Crypto Policy: TLS-Versionen, Cipher Suites, KEX- und MAC-Algorithmen für OpenSSL/GnuTLS/NSS sowie OpenSSH werden zentral gesteuert und schwache Verfahren deaktiviert. PKCS#12-Exporte und verschlüsselte Übertragungen profitieren von denselben OpenSSL-Policy-Backends. Abweichungen in Dienstkonfigurationen (`/etc/ssh/sshd_config.d/`, Apache/Nginx TLS) werden durch dedizierte CaC-Regeln erkannt.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
