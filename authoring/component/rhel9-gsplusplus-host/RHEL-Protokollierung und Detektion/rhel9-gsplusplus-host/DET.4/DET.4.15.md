---
x-trestle-param-values:
  det.4.15-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.15 - \[Überwachung von Aktivitäten\] Ressourcenauslastung von Hostsystemen

## Control Statement

Detektion für Hostsysteme SOLLTE die Ressourcenauslastung anhand von {{ insert: param, det.4.15-prm1 }} überwachen.

## Control guidance

Hierzu zählt z.B. die Auslastung der CPU, des Arbeitsspeichers, des Festspeichers. Dazu ist es sinnvoll vorab Schwellwerte zu ermitteln (KPI Baselining). Mögliche Reaktionsmaßnahmen bei zu hoher Auslastung sind z.B. die Lastverteilung auf mehrere Host-Rechner oder die Beschränkung der Ressourcennutzung pro Client.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL erfasst CPU-, Speicher- und I/O-Auslastung über PCP (`pmcd`/`pmlogger`), `systemd-cgtop` und optional Red Hat Insights; Schwellwerte und KPI-Baselining setzt das Monitoring (Grafana, Satellite, Insights). Lastverteilung und Client-Quoten sind Architektur, nicht eine einzelne Host-Härtungsregel. CaC enthält keine Enable-Regel für sysstat/PCP (sysstat wird in Baselines eher deaktiviert).

Weitere Informationen: [Systemstatus und Leistung überwachen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index).

### Implementation Status: partial

______________________________________________________________________
