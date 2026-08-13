---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.13 - \[Schlüsselmanagement\] Gültigkeit

## Control Statement

Berechtigung SOLLTE die Verifikation der Gültigkeit des Schlüssels vor jeder Nutzung verankern.


## Control guidance

Die Gültigkeit ergibt sich aus Nutzungszeit und Revocation-Status. Für die Implementierung genügt es, wenn die eingesetzten IT-Produkte bereits so entwickelt oder beschafft worden sind, dass sie die Prüfung automatisiert durchführen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Gültigkeitsprüfung (Nutzungszeit und Widerrufsstatus) erfolgt bei X.509-Zertifikaten automatisch durch den TLS-Stack. Abgelaufene oder widerrufene Zertifikate werden vor Nutzung abgewiesen; CRL-Caches können lokal hinterlegt werden. SSH-Rohschlüssel ohne eingebettete Gültigkeits- oder Widerrufsinformation erfordern organisatorisches Lifecycle-Management; RHEL bietet hier keinen generischen Widerrufsmechanismus.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: partial

______________________________________________________________________
