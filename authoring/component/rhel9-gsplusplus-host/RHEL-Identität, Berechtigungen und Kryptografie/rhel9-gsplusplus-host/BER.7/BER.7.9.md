---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.9 - \[Schlüsselmanagement\] Zweckbindung

## Control Statement

Berechtigung SOLLTE Verstöße gegen die Zweckbindung bei der Schlüsselnutzung untersagen.


## Control guidance

Zweckbindung bedeutet, dass der Schlüssel ausschließlich zu dem im Verzeichnis öffentlicher Schlüssel festgelegten Nutzungszweck verwendet werden darf. Die Zweckbindung gilt insbesondere auch für den privaten Schlüssel.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Für X.509-Zertifikate erzwingen OpenSSL, NSS und GnuTLS bei der Nutzung die im Zertifikat hinterlegte Zweckbindung (Key Usage, Extended Key Usage): Ein nur für Signatur ausgestelltes Zertifikat wird für TLS-Verschlüsselung abgelehnt. SSH-Host- und Benutzerschlüssel kennen keine vergleichbare X.509-Erweiterung — Zweckbindung wird hier über Organisationsprozess (getrennte Schlüsselpaare, `authorized_keys`-Einschränkungen) abgebildet. Ein zentrales „Verzeichnis öffentlicher Schlüssel" (BER.7.3) ist auf RHEL-Host-Ebene nicht existent.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
