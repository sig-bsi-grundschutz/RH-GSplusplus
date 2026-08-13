---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.12 - \[Schlüsselmanagement\] Authentizität

## Control Statement

Berechtigung SOLLTE die Verifikation der Authentizität öffentlicher Schlüssel vor jeder Nutzung verankern.


## Control guidance

Für die Implementierung genügt es, wenn die eingesetzten IT-Produkte bereits so entwickelt oder beschafft worden sind, dass sie die Prüfung automatisiert durchführen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Vor jeder TLS-Nutzung validiert RHEL die Authentizität öffentlicher Schlüssel über Zertifikatskettenprüfung gegen den System-Trust-Store (`/etc/pki/ca-trust/`); unbekannte oder nicht signierte Zertifikate werden abgelehnt, sofern nicht explizit konfiguriert. SSH prüft Hostschlüssel über `known_hosts` bzw. erstmalige Fingerprint-Bestätigung. Für Anwendungen außerhalb TLS/SSH liegt die Authentizitätsprüfung beim Anwender oder der Institution.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: implemented

______________________________________________________________________
