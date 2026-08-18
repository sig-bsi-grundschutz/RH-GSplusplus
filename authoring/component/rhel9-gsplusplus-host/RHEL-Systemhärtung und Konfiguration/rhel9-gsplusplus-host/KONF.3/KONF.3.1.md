---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.3.1 - \[Physischer Schutz\] Kryptographischer Hardwarespeicher

## Control Statement

Konfiguration für IT-Systeme SOLLTE einen kryptographischen Hardwarespeicher aktivieren.

## Control guidance

Ein kryptographischer Hardwarespeicher bezeichnet in diesem Kontext eine gesicherte, hardwarebasierte Komponente, die kryptographische Schlüssel oder andere besonders sensible Geheimnisse in einer isolierten und manipulationsgeschützten Umgebung verwahrt. Der Einsatz solcher Speicher kann das Risiko deutlich reduzieren, dass kryptographische Schlüssel bei einem Softwareangriff kompromittiert werden, und kann gleichzeitig die Integrität sicherheitskritischer Prozesse wie Verschlüsselung, Signatur oder Authentifizierung erhöhen. Als Standards können hierzu etwa eine Trusted Execution Environment (TEE), Secure Elements (SE) or Dedicated Security Components (DSC) infrage kommen. Vgl. ISO/IEC 11889 (TPM 2.0), ISO/IEC 19790 / FIPS 140-3 oder ETSI EN 303 645 (für IoT).

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL stellt hardwaregestützte Schlüsselaufbewahrung über TPM 2.0 und PKCS#11-Geräte bereit: Das Clevis-Framework (Policy-Based Decryption) bindet mit dem tpm2-Pin LUKS-Volumeschlüssel an einen TPM-2.0-Chip, sodass der Master-Key manipulationsgeschützt im Hardwaremodul verbleibt; der pkcs11-Pin sowie Pakete wie opensc und tpm2-pkcs11 ermöglichen dieselbe Funktion über Smartcards oder HSM. Die erforderlichen Komponenten (tpm2-tools, tpm2-tss, clevis-pin-tpm2) sind in RHEL 9 verfügbar, werden aber nicht standardmäßig aktiviert — die Institution muss TPM-Hardware bzw. PKCS#11-Geräte bereitstellen und die Bindung (z. B. `clevis luks bind -d <device> tpm2 …`) selbst konfigurieren. Trusted Execution Environments oder dedizierte Security Components außerhalb von TPM/PKCS#11 erzwingt RHEL nicht; ohne vorhandene TPM- oder Token-Hardware bleibt nur softwarebasierte Schlüsselverwaltung.

Weitere Informationen: [Policy-Based Decryption (Clevis/TPM2)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening), [Blockgeräte mit LUKS verschlüsseln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/encrypting-block-devices-using-luks_security-hardening).

### Implementation Status: partial

______________________________________________________________________
