---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.8 - \[Schlüsselmanagement\] Etablierte Algorithmen bei der Schlüsselnutzung

## Control Statement

Berechtigung SOLLTE die ausschließliche Verwendung etablierter Algorithmen bei der Schlüsselnutzung verankern.


## Control guidance

Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Bei der operativen Schlüsselnutzung (TLS-Handshakes, SSH-Sitzungen, Kerberos, IPsec) wendet RHEL die systemweite Crypto Policy an: Alle policy-fähigen Bibliotheken und Dienste verwenden dieselben erlaubten Algorithmen und Schlüssellängen, sodass bei Verschlüsselung, Signatur und Authentisierung nur etablierte Verfahren zum Einsatz kommen. OpenSSH bindet die Policy über Crypto-Policy-Drop-ins ein; TLS-Dienste nutzen OpenSSL/GnuTLS-Backends.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

Rules:

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
