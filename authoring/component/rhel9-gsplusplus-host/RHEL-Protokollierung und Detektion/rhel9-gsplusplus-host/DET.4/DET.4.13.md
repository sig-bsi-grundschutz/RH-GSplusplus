---
x-trestle-param-values:
  det.4.13-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.13 - \[Überwachung von Aktivitäten\] Verfügbarkeit des Hostsystems

## Control Statement

Detektion für Hostsysteme SOLLTE die Netzerreichbarkeit anhand von {{ insert: param, det.4.13-prm1 }} überwachen.

## Control guidance

Schwellwerte (engl. thresholds) sind hier Grenzwerte, die als Maßstab für die normale oder erwartete Netzerreichbarkeit des Hostsystems dienen. Diese Schwellwerte könnten beispielsweise eine bestimmte Anzahl an Fehlversuchen zur Erreichbarkeit in einem definierten Zeitfenster oder eine überdurchschnittlich hohe Anzahl an Verbindungsanfragen sein, die auf ungewöhnliche Netzwerkaktivität hindeuten. Ein Server könnte beispielsweise aufgrund eines Denial-of-Service-Angriffs (DoS) nicht mehr erreichbar sein, wodurch Dienste für Nutzende ausfallen. Ebenso könnte eine unerwartete Nichterreichbarkeit auf einen Hardwaredefekt, einen Konfigurationsfehler oder einen internen Angriff hindeuten, bei dem der Server vom Netz getrennt wurde, um Spuren zu verwischen. Die Überwachung anhand von Schwellwerten kann der Institution dabei helfen, solche Vorfälle frühzeitig zu erkennen und zu reagieren, bevor sie größeren Schaden anrichten. Die Überwachung kann über ein internes Monitoring-System umgesetzt werden, das kontinuierlich die Erreichbarkeit der Server mittels sogenannter Health-Checks oder Probes prüft. Dabei kann beispielsweise ein automatisches Ping-Verfahren eingesetzt werden, das in regelmäßigen Abständen die Antwortzeit des Servers misst. Die festgelegten Schwellwerte könnten zum Beispiel die maximal erlaubte Anzahl an aufeinanderfolgenden fehlgeschlagenen Ping-Antworten oder die durchschnittliche Antwortzeit sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Der Host liefert Gesundheitsdaten für **externe** Erreichbarkeitsprüfung: `systemd` Watchdogs und Unit-Status, optional PCP/Cockpit/Insights, ICMP antwortet wenn nicht gefiltert. Die eigentliche Überwachung anhand von Ping-Schwellwerten und Health-Probes gehört ins Monitoring-System, nicht in eine lokale CaC-Regel. Ein DoS, der den Host vom Netz trennt, sieht der Host selbst oft nicht mehr.

Weitere Informationen: [Systemstatus und Leistung überwachen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index), [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index).

### Implementation Status: partial

______________________________________________________________________
