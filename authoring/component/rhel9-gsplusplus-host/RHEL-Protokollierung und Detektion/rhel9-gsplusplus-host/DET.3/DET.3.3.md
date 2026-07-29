---
x-trestle-param-values:
  det.3.3-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.3 - \[Protokollierung\] Filterung nicht benötigter Inhalte

## Control Statement

Detektion KANN die Protokollierung nicht benötigter Inhalte anhand von {{ insert: param, det.3.3-prm1 }} einschränken.

## Control guidance

Je nach Anwendung und Konfigurationeinstellungen könnten Protokolle auch Daten enthalten, die dort nicht benötigt werden, z.B. um die Vertraulichkeit der Daten zu wahren oder aufgrund von Compliance-Anforderungen. Dem kommt eine noch höhere Bedeutung zu, wenn die Protokolle zwischen Institutionen ausgetauscht, oder bei Cloud-Dienstleistern gespeichert oder analysiert werden. Maßnahmen können z.B. Anonymisierung von IP-Adressen oder anderen personenbezogenen Daten oder Geschäftsgeheimnissen, sowie enge Löschfristen sein. Für Verkehrsdaten kann der BfDI Leitfaden Speicherung Verkehrsdaten als Grundlage genutzt werden. Soweit möglich, ist es sinnvoll, die Filterung minimalinvasiv zu gestalten, d.h. nur diejenigen Daten auszufiltern, deren Speicherung nicht rechtlich oder tatsächlich möglich ist, die restlichen Angaben zum Ergebnis jedoch zu protokollieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

auditd unterstützt Aktionen bei vollem Datenträger und Schwellwerte für freien Speicherplatz, wie in der RHEL-Dokumentation beschrieben; Partitionierung und Archivierung verbleiben bei der Institution.

### Rules:

  - auditd_data_retention_space_left

### Implementation Status: partial

______________________________________________________________________
