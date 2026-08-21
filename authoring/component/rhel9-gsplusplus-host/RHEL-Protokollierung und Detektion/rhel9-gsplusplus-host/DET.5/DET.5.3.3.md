---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.3.3 - \[Management von Schwachstellen\] Historische Analyse

## Control Statement

Detektion KANN Schwachstellen in öffentlich erreichbaren Systemen oder Anwendungen anhand bekannter Anzeichen im Audit Log testen.

## Control guidance

Die historische Analyse von Logdateien ermöglicht es, vergangene Systemaktivitäten systematisch zu untersuchen, um potenzielle Sicherheitsvorfälle zu identifizieren, die zum Zeitpunkt ihres Auftretens unbemerkt blieben. Nach der Entdeckung einer Schwachstelle kann so rückwirkend festgestellt werden, ob und wie diese bereits ausgenutzt wurde. Die Umsetzung kann durch Etablierung eines zentralisierten Log-Managements mit langer Aufbewahrungsdauer, Implementierung automatisierter Such- und Korrelationsalgorithmen zur Erkennung bekannter Angriffsmuster und Anomalien in den Logdaten, sowie durch forensische Analyse der Zeitstempel, Quell-IPs, Benutzeraktivitäten und Zugriffsversuche erfolgen. Bei der Feststellung von Schwachstellen in öffentlich zugänglichen Systemen ist es sinnvoll die Audit-Logs gezielt nach Indikatoren zu durchsuchen, die auf entsprechende Angriffsmuster hindeuten - darunter ungewöhnliche Zugriffszeiten, auffällige Authentifizierungsversuche, verdächtige Datenbankabfragen oder charakteristische Command-Injection-Versuche, wodurch potenzielle Kompromittierungen retrospektiv aufgedeckt und in ihrem vollen Umfang bewertet werden können.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Historische Suche nach bekannten Angriffszeichen setzt voraus, dass Audit- und Journal-Daten lange genug und auswertbar vorliegen: persistentes Journal, Audit-Retention, besser Remote-Log/SIEM. `ausearch`/`journalctl` erlauben retrospektive Filter (UID, Syscall, Pfad, Zeit), nicht aber fertige IOC-Korrelation. Die eigentliche historische Analyse nach bekannt gewordenen Schwachstellen ist SIEM-/Forensik-Prozess.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
