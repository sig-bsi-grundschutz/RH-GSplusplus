---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.2 - \[Schutz vor Schadcode\] Regelmäßige Scans

## Control Statement

Konfiguration für IT-Systeme SOLLTE einen regelmäßigen Scan von Dateien auf dem System nach potenziellem Schadcode aktivieren.

## Control guidance

Schadcode kann sich sowohl auf lokalen Speichermedien, als auch auf Netzlaufwerken oder Wechseldatenträgern befinden. Für Netzlaufwerke kann die Anforderung auch umgesetzt werden, indem Dateien bei der Speicherung auf dem zentralen System auf Schadcode geprüft werden. Die Anwendung zur Schadcodeprüfung kann z.B. auch als EDR, XDR oder IDS bezeichnet werden. Moderne Systeme zur Erkennung von Schadcode verwenden eine Kombination aus Virensignaturen, Heuristiken, als auch Anomalieerkennung. Falls das System die Installation von Anwendungen nicht unterstützt, so ist dieser Teilschritt entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Regelmäßige Dateiprüfung ermöglicht AIDE (Advanced Intrusion Detection Environment): Eine Baseline-Dateidatenbank wird erstellt und per systemd-Timer oder Cron periodisch verglichen; Abweichungen signalisieren unautorisierte Änderungen (Integrität, nicht Malware-Signaturen). `dnf-automatic` installiert sicherheitsrelevante Updates nach Policy. Malware-Scans à la ClamAV sind in RHEL nicht supported — AIDE deckt Integritätsaspekte, nicht Viren-Erkennung.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
