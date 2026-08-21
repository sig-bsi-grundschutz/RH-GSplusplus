---
x-trestle-param-values:
  det.5.10.2-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.10.2 - \[Management von Schwachstellen\] Automatisierte Überwachung von Systemupdates

## Control Statement

Detektion für IT-Systeme SOLLTE den Patchstatus durch {{ insert: param, det.5.10.2-prm1 }} überwachen.

## Control guidance

Der Patchsstatus des Informationsverbundes kann dabei durch Kennzahlen bestimmt werden, z.B. durchschnittliche Zeit bis zum Patch (Mean Time To Patch), Prozentsatz aktuell gepatchter Assets, Anzahl offener/geschlossener Ausnahmen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Den Patchstatus des **Systems** (RPM) überwacht `dnf`/`dnf-automatic` und der Abgleich gegen verfügbare Security-Errata (`security_patches_up_to_date`); Red Hat Insights und Satellite liefern Flotten-Kennzahlen (Anteil gepatcht, offene Advisories). Mean Time To Patch und Ausnahmequoten sind Berichtswesen, kein einzelnes Host-File. Der Param verlangt einen automatisierten Mechanismus — dnf-automatic plus Insights erfüllen das für RPM-Inhalte.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
