---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.5 - \[Protokollierung\] Störungen der Netzerreichbarkeit

## Control Statement

Detektion für IT-Systeme KANN Störungen der Netzerreichbarkeit protokollieren.

## Control guidance

Eine Störung der Netzerreichbarkeit kann ein Indiz für Überlastungen, Fehler oder Angriffe im Netz sein. Wann eine Störung vorliegt, kann anhand von Schwellwerten, z.B. durch das Ausbleiben eines regelmäßigen Heartbeat-Paketes, getestet werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Red Hat Enterprise Linux enthält Performance Co-Pilot (`pcp`). Diese Werkzeug kann verschiedene Performance-Metriken sammeln und mittles `pmlogger` weiterleiten, zentralisieren und beispielsweise mittels Grafana visualisieren. Das Paket `pcp-pmda-netcheck` stellt hierfür Netzwerk-Prüfungen bereit. Diese können als Indikatoren für eine Störung der Netzerreichbarkeit oder Überlastung genutzt werden. Alternative Lösungen sind mittels Monitoring-Lösungen von 3rd-Parties marktverfügbar.

Weitere Informationen: [Edge Network Monitoring](https://www.redhat.com/en/blog/lets-monitor-edge-computing-networks-rhel), [Performace Co-Pilot](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#installing-and-enabling-pcp)


### Implementation Status: planned

______________________________________________________________________
