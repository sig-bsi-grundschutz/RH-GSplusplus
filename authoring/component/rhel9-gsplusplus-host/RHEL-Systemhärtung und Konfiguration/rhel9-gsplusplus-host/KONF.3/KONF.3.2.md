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

RHEL verschlüsselt integrierte Festspeichermedien über LUKS/dm-crypt (`cryptsetup`): Bei der Installation kann Anaconda oder Kickstart (`--encrypted`) Partitionen als `crypto_LUKS` anlegen; bestehende Blockgeräte lassen sich nachträglich mit LUKS2 verschlüsseln (`cryptsetup reencrypt`). Standardalgorithmus ist `aes-xts-plain64` mit 512-Bit-Schlüssel. ComplianceAsCode-Regeln prüfen den LUKS-Typ persistenter Partitionen (`encrypt_partitions`) und die Installation von `cryptsetup` (`package_cryptsetup-luks_installed`). RHEL erzwingt keine Vollverschlüsselung — die Entscheidung, Schlüsselverwaltung (Passphrase, optional NBDE/Clevis) und ggf. Hardware-Self-Encrypting-Drives liegen bei der Institution; ein reiner Software-Ansatz über LUKS deckt die in der Anleitung genannte dm-crypt-Variante ab.

Weitere Informationen: [Blockgeräte mit LUKS verschlüsseln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/encrypting-block-devices-using-luks_security-hardening)

### Implementation Status: partial

______________________________________________________________________
