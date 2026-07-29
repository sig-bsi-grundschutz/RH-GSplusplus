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

Automatisierte Konfigurationsprüfung und -anpassung kann über Ansible, OpenSCAP-Remediation, Image Builder oder Satellite erfolgen; Freigabe und Betrieb automatisierter Werkzeuge obliegen der Institution.

### Implementation Status: partial

______________________________________________________________________
