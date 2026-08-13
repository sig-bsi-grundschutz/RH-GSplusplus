---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.10 - \[Schlüsselmanagement\] Abgelaufene Schlüssel

## Control Statement

Berechtigung SOLLTE die Nutzung des Schlüssels zur Verschlüsselung oder Signierung nach Ablauf der Nutzungszeit untersagen.


## Control guidance

Schlüssel dürfen nach Ablauf der Nutzungszeit nur noch zur Entschlüsselung oder Signaturprüfung alter Daten verwendet werden. Bei automatisierter Schlüsselnutzung ist der Schlüssel zu deaktivieren, bei manueller Schlüsselnutzung ist den Nutzenden weitere Verwendung des Schlüssels zu verbieten.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

X.509-basierte Schlüssel und Zertifikate lehnt der TLS-/PKI-Stack nach Ablauf der Gültigkeitszeit automatisch ab: OpenSSL, NSS und GnuTLS prüfen `notAfter` bei jedem Handshake; abgelaufene Server- oder Clientzertifikate können weder signieren noch verschlüsseln. Für dateibasierte Schlüssel (SSH, GPG) ohne eingebaute Ablaufzeit ist die Deaktivierung nach Nutzungsende organisatorisch und durch Entfernen aus `authorized_keys` beispielsweise automatisiert via Ansible oder einer Secret-Management Lösung, Neugenerierung oder Widerruf umzusetzen — RHEL erzwingt keinen universellen Ablaufmechanismus für Rohschlüsseldateien.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
