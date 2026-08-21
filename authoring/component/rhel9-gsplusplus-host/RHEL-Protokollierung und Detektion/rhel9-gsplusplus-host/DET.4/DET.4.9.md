---
x-trestle-param-values:
  det.4.9-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.9 - \[Überwachung von Aktivitäten\] Manipulations-Checkup

## Control Statement

Detektion für IT-Systeme KANN das System auf Manipulationsversuche {{ insert: param, det.4.9-prm1 }} überprüfen.

## Control guidance

Falls Systeme einem erhöhten Manipulationsrisiko ausgesetzt sind (z.B. wegen öffentlicher Aufstellung), die Vertraulichkeit oder Integrität des Systems oder damit verbundener Daten oder Netze jedoch nicht vernachlässigenswert ist, so ist eine regelmäßige Überprüfung auf Manipulationen empfehlenswert. Hierfür können Gerätesiegel verwendet werden. Maßnahmen bei Feststellung einer Manipulation können z.B. das Zurücksetzen auf den Werkszustand oder die Aussonderung sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL prüft Software- und Konfigurationsintegrität mit AIDE (Baseline, periodischer `--check`, optional Benachrichtigung) und mit RPM-Hashvergleich (`rpm --verify`). IMA/EVM kann Dateimesswerte in erweiterten Attributen ergänzen. Physische Gerätesiegel, Werksreset und Aussonderung nach Manipulation sind organisatorisch bzw. Hardware, nicht Teil der OS-Konfiguration.

Weitere Informationen: [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
