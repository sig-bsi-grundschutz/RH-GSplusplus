---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

---
x-trestle-set-params:
  konf.2.5-prm1:
    values:
---

# KONF.2.5 - \[Konfiguration von Systemen\] Überprüfung der Konfiguration

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Übereinstimmung der tatsächlichen Konfiguration mit dem Referenzzustand {{ insert: param, konf.2.5-prm1 }} überprüfen.

## Control guidance

Referenzzustand („baseline configuration“) bezeichnet hier die dokumentierte und freigegebene Konfiguration eines IT-Systems, also die gewünschte und autorisierte Einstellung von Parametern, Diensten und Komponenten. Die tatsächliche Konfiguration ist die aktuelle technische Umsetzung dieser Einstellungen auf dem System selbst. Der Abgleich beider Zustände dient vor allem der Vermeidung von Configuration Drift – d.h. dass Systeme schleichend von der definierten Soll-Konfiguration abweichen. Dies könnte auftreten, wenn Änderungen nicht zentral dokumentiert oder automatisierte Installationen nicht einheitlich umgesetzt werden. Ohne diese Kontrolle könnte es zu unbemerkten Fehlkonfigurationen kommen, die Sicherheitslücken öffnen oder Betriebsstörungen verursachen. Durch regelmäßige Vergleiche kann eine Institution sicherstellen, dass Systeme konsistent, vertrauenswürdig und wartbar bleiben. Eine praktische Umsetzung kann auf verschiedenen Ebenen erfolgen. Technisch kann eine Institution (1) Konfigurations-Management-Werkzeuge einsetzen, die Referenzzustand-Definitionen mit Systemzuständen automatisch abgleichen, (2) Skripte oder Policies nutzen, die regelmäßig Konfigurationsdateien oder Systemeinstellungen auslesen und protokollieren, oder (3) Hash- oder Signaturverfahren anwenden, um Veränderungen an Konfigurationsdateien nachzuweisen. Prozessual kann es hilfreich sein, Änderungen zentral zu dokumentieren und automatische Reports über Abweichungen an Verantwortliche weiterzuleiten, damit diese reagieren können. Zusätzlich kann eine Institution Pilotprüfungen an Stichproben-Systemen durchführen, um die Wirksamkeit automatischer Abgleiche zu validieren. Durch diese Maßnahmen kann eine Institution eine belastbare Routine etablieren, die Configuration Drift reduziert und nicht nur technische Abweichungen sichtbar macht, sondern auch menschliche Fehler oder unautorisierte Eingriffe frühzeitig erkennen kann.

______________________________________________________________________

## What is the solution and how is it implemented?

Abgleich der Ist-Konfiguration mit Referenzvorgaben ist über OpenSCAP (scap-security-guide), AIDE und RHEL Insights möglich; Referenzdefinition, Intervalle und Remediation-Prozesse legt die Institution fest.

### Rules:

  - package_aide_installed
  - aide_periodic_cron_checking

### Implementation Status: partial

______________________________________________________________________
