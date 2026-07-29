---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

---
x-trestle-set-params:
  konf.2.5.1-prm1:
    values:
---

# KONF.2.5.1 - \[Konfiguration von Systemen\] Automatische Konfigurationsverwaltung

## Control Statement

Konfiguration für IT-Systeme KANN die Überprüfung der Konfiguration durch {{ insert: param, konf.2.5.1-prm1 }} aktivieren.

## Control guidance

Eine automatische Konfigurationsverwaltung ermöglicht eine einheitliche Konfiguration, z.B. für Passwortvorgaben, Verschlüsselung oder automatische Updates. Insbesondere bei der Verwaltung zahlreicher Endgeräte oder einer Bring Your Own Device Strategie (BYOD) bietet eine solche Verwaltung den einzig praktikablen Ansatz die Sicherheitsparameter der Geräte zu kontrollieren. Dies kann über selbst betriebenes zentrales Managementsystem (UEM oder MDM), Cloud-Dienste wie Intune oder Konfigurationsmanagement-Werkzeuge wie Ansible umgesetzt werden. Bei Abweichungen kann entweder ein automatisierter Mechanismus die erforderliche Konfiguration vornehmen, oder eine manuelle Entscheidung über die passende Behandlung erfolgen.

______________________________________________________________________

## What is the solution and how is it implemented?

Für automatisierte Konfigurationsverwaltung stellt RHEL mehrere zusammenspielende Werkzeuge bereit: Ansible führt deklarativ beschriebene Playbooks/Rollen aus und kann bei Abweichungen selbstständig den Soll-Zustand wiederherstellen; OpenSCAP kann mit `oscap xccdf eval --remediate` erkannte Abweichungen von einem scap-security-guide-Profil automatisiert korrigieren, statt sie nur zu melden; Red Hat Ansible Automation Platform, Red Hat Satellite bzw. Red Hat Lightspeed-Remediation-Pläne erlauben eine zentrale, flottenweite Anwendung solcher Korrekturen über viele Hosts hinweg, und Image Builder sorgt dafür, dass neu ausgerollte Systeme bereits im Soll-Zustand starten. Diese Werkzeuge automatisieren die technische Durchsetzung, ersetzen aber nicht die Entscheidung der Institution, welches Werkzeug in welchem Umfang zum Einsatz kommt, wie automatische Korrekturen freigegeben werden und wie mit Abweichungen umgegangen wird, die keine automatische Behebung erlauben.

### Implementation Status: partial

______________________________________________________________________
