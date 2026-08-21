---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.5 - \[Protokollierung\] Revisionssicherheit

## Control Statement

Detektion SOLLTE Änderungen am Audit Log revisionssicher dokumentieren.

## Control guidance

Wenn die Protokollaufzeichnung unzureichend vor Veränderung geschützt ist, könnten Innentäter diese manipulieren oder löschen, um nicht erkannt oder belangt zu werden. Hierzu gehört auch, dass Administrierende die Protokolldaten zu ihren eigenen Tätigkeiten manipulieren oder löschen könnten. Die Integrität kann durch die Erstellung und getrennte Aufbewahrung von kryptografischen Hashes oder ein Versionskontrollsystem sichergestellt werden. Um sicherzustellen, dass nur autorisierte Personen die Protokolle verändern können, können z.B. Verschlüsselung und getrennte Aufbewahrung des Schlüssels, einmalig beschreibare Datenträger, oder ein Protokollierungsserver/SIEM mit stark eingeschränkten Zugriffsrechten eingesetzt werden. Auch die Aufzeichnung in einer öffentlichen Transparenzdatei ist möglich, wenn die Protokolle keine vertraulichen Daten enthalten.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL schützt das Audit-Log durch restriktive Dateirechte unter `/var/log/audit/`, den Immutable-Modus von `auditd` (`-e 2`, danach nur noch per Reboot änderbar) und optionale Weiterleitung an einen getrennten Log-Host. AIDE kann die Audit-Werkzeuge selbst auf unerwartete Änderungen prüfen. Kryptographische Hash-Ketten, WORM-Medien, getrennte Schlüssel oder ein SIEM mit hart eingeschränkten Rechten stellt der Host nicht von selbst bereit.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening).

### Implementation Status: partial

______________________________________________________________________
