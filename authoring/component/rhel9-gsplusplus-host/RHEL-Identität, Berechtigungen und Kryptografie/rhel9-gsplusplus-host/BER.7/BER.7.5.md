---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.5 - \[Schlüsselmanagement\] Kriterien für die Qualität von Zufallszahlen

## Control Statement

Berechtigung SOLLTE {{ insert: param, ber.7.5-prm1 }} für die Qualität von Zufallszahlen bei der Schlüsselerzeugung verankern.


## Control guidance

Wenn bei der Schlüsselerzeugung ein ungeeigneter Zufallszahlengenerator verwendet wird, könnte ein Angreifer Schlüssel errechnen. Daher sind Kriterien für Zufallszahlengeneratoren zu wählen, z.B. Verwendung etablierter, durch unabängige Dritte geprüfter Zufallszahlengeneratoren. Für Details siehe BSI TR-02102-1. Wichtig ist dabei auch, dass die verwendete Zufallsquelle tatsächlich eine nicht vorhersagbare Zahlenerzeugung erreicht. Inbesondere virtualisierte Systeme könnten ungeeignet sein zur Schlüsselerzeugung, da ihre Zufallszahlenquellen nicht direkt auf Hardwarefunktionen zurückgreifen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Für kryptografische Schlüsselerzeugung nutzt RHEL den Kernel-CSPRNG über `/dev/urandom` bzw. im FIPS-Modus den zertifizierten DRBG des Kernels (`grubby --update-kernel=ALL --args fips=1`, `/proc/sys/crypto/fips_enabled`). Optional ergänzt `rngd` (Hardware-RNG) die Entropiequelle auf Systemen mit TRNG. OpenSSH kann über `SSH_USE_STRONG_RNG` zusätzliche Entropiebytes anfordern. Die Auswahl und Dokumentation der Qualitätskriterien (z. B. nach BSI TR-02102-1) sowie die Bewertung virtualisierter Entropiequellen obliegen der Institution; RHEL liefert die technische Basis, nicht die policy-seitige Kriterienfestlegung.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
