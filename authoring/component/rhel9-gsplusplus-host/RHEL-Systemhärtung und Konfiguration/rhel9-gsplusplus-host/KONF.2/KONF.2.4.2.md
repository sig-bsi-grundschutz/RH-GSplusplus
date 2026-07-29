---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.4.2 - \[Konfiguration von Systemen\] Externe Cloud-Anbindungen

## Control Statement

Konfiguration für IT-Systeme SOLLTE nicht benötigte Cloud-Anbindungen deaktivieren.

## Control guidance

Eine Cloud-Anbindung ist eine technische Schnittstelle, über die ein IT-System Daten oder Dienste mit einer externen Cloud-Plattform austauscht. Dazu können sowohl direkte API-Integrationen wie die Anmeldung an Cloud-Verzeichnisdienste, aber auch automatische Synchronisationsmechanismen, Hintergrund-Updates über Cloud-Server oder agentenbasierte Remote-Management-Funktionen zählen. Nicht benötigte Anbindungen können dadurch identifiziert werden, dass sie weder für den produktiven Betrieb noch für Wartung, Support oder Sicherheitsfunktionen erforderlich sind. Der Sinn und Zweck dieser Regelung liegt darin, die Angriffsfläche zu reduzieren und unkontrollierte Datenflüsse zu vermeiden. Ein nicht genutzter, aber weiterhin aktiver Cloud-Connector könnte etwa unbemerkt sensible Metadaten an Drittdienste übertragen oder als Einfallstor für Schadsoftware missbraucht werden; die gezielte Deaktivierung kann dagegen unnötige Risiken eliminieren und die Übersichtlichkeit der Systemarchitektur erhöhen.

______________________________________________________________________

## What is the solution and how is it implemented?

Die Cloud-Anbindung auf RHEL ist der insights-client, der als Standardpaket vorinstalliert ist und Systeme über den systemd-Timer `insights-client.timer` periodisch mit Red Hat Lightspeed (vormals Red Hat Insights) auf der Red Hat Hybrid Cloud Console verbindet, sofern die Institution eine entsprechende Registrierung durchführt. In verbundenen Umgebungen deckt Lightspeed dabei sicherheits-, wartungs- und supportrelevante Funktionen ab: kontinuierliches CVE-Scanning mit priorisierter Schwachstellenbewertung und Remediation-Playbooks (Sicherheit), Advisor-Empfehlungen zu Konfigurationsfehlern sowie zentral gesteuertes Patch- und Errata-Management (Wartung), und SCAP-basiertes Compliance-Tracking zusammen mit Systemtelemetrie, die dem Red-Hat-Support eine schnellere Diagnose ermöglicht (Support). Institutionen, die keine direkte Anbindung einzelner Hosts an die externe Hybrid Cloud Console wünschen, können Red Hat Satellite als optionalen Ersatz betreiben: Bei Registrierung an Satellite konfiguriert sich insights-client anhand der lokalen RHSM-Registrierung automatisch auf den Satellite-Hostnamen um und leitet Daten an den selbst betriebenen Satellite-Server statt an Red Hat; ab Satellite 6.18 lässt sich die Advisor-/Schwachstellenanalyse (iop-advisor-engine) zusätzlich vollständig air-gapped ohne jede Internetanbindung betreiben, wobei einzelne Cloud-only-Funktionen wie zentrales Subscription-Tracking entfallen. Wird weder die direkte Lightspeed-Anbindung noch ein Satellite-Betrieb benötigt, lässt sich insights-client über `systemctl mask --now insights-client.timer` bzw. `dnf remove insights-client` deaktivieren oder vollständig entfernen. Die Institution muss dabei abwägen, ob der Verlust der beschriebenen Sicherheits-, Wartungs- und Support-Funktionen durch die gewonnene Reduktion der Angriffsfläche aufgewogen wird.

### Implementation Status: partial

______________________________________________________________________
