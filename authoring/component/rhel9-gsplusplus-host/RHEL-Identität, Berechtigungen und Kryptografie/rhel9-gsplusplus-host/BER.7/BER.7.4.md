---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.4 - \[Schlüsselmanagement\] Erzeugung auf sicheren IT-Systemen

## Control Statement

Berechtigung SOLLTE die Verwendung eines IT-Systems, welches mindestens dasselbe Schutzniveau bietet, für das der Schlüssel eingesetzt werden soll, bei der Schlüsselerzeugung verankern.


## Control guidance

Wird ein Schlüssel auf einem System erzeugt, dass einen geringeren Schutz bietet als auf dem späteren Einsatzsystem, dann könnte der Schlüssel bereits kompromittiert sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Schlüssel sollten auf dem Zielsystem (RHEL-Host) erzeugt werden, sofern die lokale verwendbaren Entropie-Quellen ausreichend sind; dedizierte Offline-Erzeugung auf Hardware Security Modules/TPM oder isolierten Administrationshosts ist organisatorisch festzulegen. RHEL erzwingt die Gleichwertigkeit des Erzeugungssystems nicht automatisch — die Institution wählt Erzeugungsort und Schutzniveau.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: alternative

______________________________________________________________________
