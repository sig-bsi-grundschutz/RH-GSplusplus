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

RHEL deckt den Abgleich zwischen Referenz- und Ist-Konfiguration auf den in der Control Guidance beschriebenen Ebenen ab: (1) Als Konfigurationsmanagement-Werkzeug beschreibt Ansible (bspw. auch über die mitgelieferten RHEL System Roles) den Referenzzustand deklarativ in Playbooks und Rollen; ein Lauf im Check-Modus (`--check --diff`) gleicht die tatsächliche Systemkonfiguration automatisch gegen diese Definition ab und meldet Abweichungen. Alternativ können diese aber auch direkt überschrieben werden. (2) Als Referenz-Baseline-Kontrolle liest OpenSCAP (`oscap xccdf eval`) anhand eines scap-security-guide-Profils periodisch die im Profil definierte Baseline - Dienste, Paketstände, Kernel- und Anwendungseinstellungen – und prüft das System gegen diese. Abweichungen werden in einem Report (ARF/HTML) protokolliert und kann an zentraler Stelle (Red Hat Lightspeed oder Red Hat Satellite) gesammelt werden. Dies stellt eine wiederholbare, versionierte Baseline-Prüfung bereit; Red Hat Lightspeed ergänzt dies um eine kontinuierliche Überwachung laufender Systeme gegen bekannte Best-Practice-Regelsätze mit zentraler Meldung. (3) Für die dateibezogene Integritätsebene setzt AIDE Hash- und Signaturverfahren ein: Nach dem Anlegen einer initialen Datenbank (`aide --init`) aus Hash-Werten, Berechtigungen und weiteren Attributen der in `/etc/aide.conf` definierten Pfade vergleicht `aide --check` den aktuellen Dateizustand fortlaufend gegen diese Referenz und meldet Änderungen, neue oder gelöschte Dateien; die mitgelieferten CaC-Regeln stellen zusätzlich sicher, dass das Paket installiert ist und die Prüfung mindestens wöchentlich per Cronjob automatisiert läuft, statt nur manuell ausgeführt zu werden. Was konkret als Referenzzustand gilt, wie eng die Prüfintervalle sind und wie auf gemeldete Abweichungen reagiert wird (Remediation-Prozess, Eskalation), muss die Institution jedoch selbst festlegen und betreiben.

### Rules:

  - package_aide_installed
  - aide_build_database
  - aide_periodic_cron_checking
  - aide_scan_notification
  - rpm_verify_hashes
  - rpm_verify_ownership
  - rpm_verify_permissions

### Implementation Status: partial

______________________________________________________________________
