---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  "RHEL-Identität, Berechtigungen und Kryptografie":
    - name: var_system_crypto_policy
      values:
        - DEFAULT
      component-values:
        - DEFAULT

---

# BER.7.1 - \[Schlüsselmanagement\] Etablierte Algorithmen bei der Schlüsselerzeugung

## Control Statement

Berechtigung SOLLTE die ausschließliche Verwendung etablierter kryptografischer Algorithmen bei der Schlüsselerzeugung nach {{ insert: param, ber.7.1-prm1 }} verankern.


## Control guidance

Etablierte kryptografische Algorithmen sind mathematisch fundierte Verschlüsselungsverfahren und Protokolle, die in der aktuellen Praxis nicht mit vertretbarem Aufwand gebrochen werden können. Sie basieren auf mathematisch schwer lösbaren Problemen, bieten Resistenz gegen bekannte kryptanalytische Angriffe, unterstützen ausreichend große Schlüssellängen und wurden von Experten gründlich geprüft und analysiert. Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Etablierte kryptografische Algorithmen für Authentisierungspfad und Protokolle erzwingt RHEL über systemweite Crypto Policies (`update-crypto-policies`): Stufen wie `DEFAULT`, `FUTURE` oder `FIPS` vereinheitlichen TLS, SSH, Kerberos, OpenSSL und weitere Backends und entfernen schwache Verfahren. Dienste, die die Policy einbinden (u. a. OpenSSH über Crypto-Policy-Drop-ins), erben dieselbe Algorithmuswahl. Es ist möglich eine eigene Konfiguration zu erstellen, die die BSI TR-02102 implementiert. Änderungen sind jedoch strikt zu testen. Es sollte das entsprechende Fachwissen für diese Anpassungen vorhanden sein, um fehlerhafte und schwächende Konfigurationen zu vermeiden.

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
