---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.3.2 - \[Physischer Schutz\] Speicherverschlüsselung

## Control Statement

Konfiguration für IT-Systeme SOLLTE integrierte Festspeichermedien verschlüsseln.

## Control guidance

Die Verschlüsselung von Datenträgern erschwert es Angreifern, Daten von verlorenen oder gestohlenen Geräten auszulesen. Die Verschlüsselung kann in Hard- oder Software (z.B. Windows BitLocker®, Apple FileVault®, Linux® dm-crypt) erfolgen. Für anerkannte kryptographische Algorithmen siehe BSI TR 02102.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL kann integrierte Festspeichermedien über LUKS (`cryptsetup`) verschlüsseln: Bei der Installation kann Anaconda oder Kickstart (`--encrypted`) Partitionen als `crypto_LUKS` anlegen. Bestehende Blockgeräte lassen sich nachträglich mit LUKS2 verschlüsseln (`cryptsetup`). RHEL erzwingt keine Vollverschlüsselung — die Entscheidung, Schlüsselverwaltung (Passphrase, optional Network Bound Device Encryption/Clevis) und ggf. Hardware-Self-Encrypting-Drives liegen bei der Institution.

Weitere Informationen: [Blockgeräte mit LUKS verschlüsseln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/encrypting-block-devices-using-luks_security-hardening)

### Rules:

  - encrypt_partitions
  - package_cryptsetup-luks_installed

### Implementation Status: implemented

______________________________________________________________________
