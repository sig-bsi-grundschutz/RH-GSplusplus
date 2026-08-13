---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.15 - \[Schlüsselmanagement\] Vorgehensweise nach Nutzung

## Control Statement

Berechtigung SOLLTE eine Vorgehensweise zur Außerbetriebnahme geheimer Schlüssel , sobald sie nicht mehr benötigt werden, verankern.


## Control guidance

Werden Schlüssen nicht mehr benötigt, so ist es sinnvoll diese im Einklang mit den Anforderungen zur Löschung von Informationen außer Betrieb zu nehmen. Hierbei ist zu beachten, dass bei einem Schlüsselwechsel verschlüsselte Daten entschlüsselt und erneut verschlüsselt werden. Flüchtige Schlüssel sind nach der Sitzung umgehend zu löschen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Außerbetriebnahme geheimer Schlüssel ist primär organisatorischer Prozess; technisch unterstützt RHEL sichere Löschung und Rotation: Schlüsseldateien können entfernt, `authorized_keys`-Einträge widerrufen und Dienste neu gestartet werden; flüchtige Schlüssel in Prozessspeicher enden mit der Sitzung. Skalierbare Umsetzung ist per Ansible/AAP automatisierbar (Entfernen von Dateien, Neukonfiguration von Diensten). Verfahren und Nachweis obliegen der Institution.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: not-applicable

______________________________________________________________________
