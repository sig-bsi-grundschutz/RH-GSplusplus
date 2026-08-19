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

RHEL kann TPM 2.0  als einen kryptographischen Hardwarespeicher einbinden: Schlüssel und Geheimnisse können im Trusted Platform Module erzeugt, gespeichert und nur unter definierten Bedingungen freigegeben werden (z. B. persistente Schlüsselobjekte, versiegelte Geheimnisse an Platform Configuration Registers). Die Werkzeuge `tpm2-tools` und die Bibliothek `tpm2-tss` sind in RHEL 9 enthalten; mit `tpm2-pkcs11` können Anwendungen Schlüssel über eine PKCS#11-Schnittstelle nutzen, ohne dass private Schlüsselmaterial den TPM-Chip verlässt. TPM-Hardware (Firmware- oder Diskreter-Chip) wird von RHEL nicht erzwungen — die Institution muss sie bereitstellen, aktivieren und die Schlüsselverwaltung selbst konfigurieren.

Weitere Informationen:[Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: planned

______________________________________________________________________
