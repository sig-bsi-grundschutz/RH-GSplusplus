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

Beim Transport geheimer Schlüssel über das Netz (TLS, SSH, IPsec) erzwingt RHEL etablierte Algorithmen über die systemweite Crypto Policy: TLS-Versionen, Cipher Suites, KEX- und MAC-Algorithmen für OpenSSL/GnuTLS/NSS sowie OpenSSH werden zentral gesteuert und schwache Verfahren deaktiviert. PKCS#12-Exporte und verschlüsselte Übertragungen profitieren von denselben OpenSSL-Policy-Backends.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - configure_crypto_policy
  - configure_gnutls_tls_crypto_policy
  - configure_kerberos_crypto_policy
  - configure_libreswan_crypto_policy
  - configure_openssl_crypto_policy
  - configure_openssl_tls_crypto_policy
  - configure_ssh_crypto_policy
  - crypto_policy_not_legacy
  - crypto_policy_not_overridden
  - package_crypto_policies_installed

### Implementation Status: implemented

______________________________________________________________________
