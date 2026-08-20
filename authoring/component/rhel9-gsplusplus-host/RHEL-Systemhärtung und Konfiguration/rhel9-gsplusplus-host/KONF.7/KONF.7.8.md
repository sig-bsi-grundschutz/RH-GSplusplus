---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.8 - \[Schutz vor Schadcode\] Dual-Engine-Strategie

## Control Statement

Konfiguration für IT-Systeme KANN für die Erkennung von Schadcode unterschiedliche Scan-Engines aktivieren.

## Control guidance

Hiermit ist gemeint, dass die Angriffserkennung mittels (zwei oder mehr) verschiedenen Scan-Engines durchgeführt wird, um die Erkennungswahrscheinlichkeit zu erhöhen. Hierdurch kann es zu Performanceeinbußen oder einer höheren Fehlerkennungquote kommen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Beim Einsatz von mehreren Scan-Engines auf einem RHEL Host ist eine gegenseitige negative Beeinflussung der Software zu erwarten.

Weitere Informationen: [Is any virus protection software needed for Red Hat Enterprise Linux?](https://access.redhat.com/solutions/9203)

### Implementation Status: not-applicable

______________________________________________________________________
