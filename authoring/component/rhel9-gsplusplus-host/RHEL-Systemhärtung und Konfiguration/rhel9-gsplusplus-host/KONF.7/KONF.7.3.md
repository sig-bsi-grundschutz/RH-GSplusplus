---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.3 - \[Schutz vor Schadcode\] Host-basierte Angriffserkennung

## Control Statement

Konfiguration für IT-Systeme KANN Host-basierte Angriffserkennung aktivieren.

## Control guidance

Host-basierte Angriffserkennung, im Englischen auch als Host-based Intrusion Detection (HID) oder Host-based Intrusion Prevention (HIP) bezeichnet, bezieht sich auf Mechanismen, die auf den einzelnen IT-Systemen, wie Servern oder Workstations, selbst operieren, um böswillige Aktivitäten zu erkennen und zu verhindern. Im Gegensatz zu netzwerkbasierten Systemen, die den Datenverkehr überwachen, fokussiert sich die Host-basierte Erkennung auf interne Systemereignisse, wie die Integrität von Dateisystemen, Änderungen an kritischen Konfigurationsdateien, oder die Erkennung von unbekannten Prozessen. Der Hauptzweck dieser Anforderung besteht darin, eine zusätzliche Sicherheitsebene zu schaffen, die direkt am Endpunkt (Host) agiert, was die Erkennung von Angriffen ermöglicht, die bereits die äußeren Schutzmechanismen überwunden haben könnten, beispielsweise wenn ein Angreifer eine bekannte Schwachstelle ausnutzt, um einen Prozess mit erhöhten Rechten auszuführen. Diese Maßnahmen können dabei helfen, interne Lateralbewegungen eines Angreifers zu erkennen und somit die Ausbreitung eines Vorfalls zu verlangsamen oder zu stoppen, bevor es zu einem größeren Schaden kommt.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

AIDE (Advanced Intrusion Detection Environment) ermöglicht Intrusion Detection: Eine Baseline-Dateidatenbank wird erstellt und per systemd-Timer oder Cron periodisch verglichen; Abweichungen signalisieren unautorisierte Änderungen (Integrität). Ebenfalls bietet IMA (Integrity Measurement Architecture) eine Möglichkeit um zusätzliche Integritätsprüfungen des Kernels und von Dateien durchzuführen. In Kombination mit entsprechenden `auditd` Konfigurationen, können hierdurch an zentralen Stellen (i.e. SIEM) Integritätsereignisse der Hosts gesammelt werden. Zusätzlich kann über `fapolicy` eine Allow-List von Anwendungen implementiert werden, die eine Ausbreitung von Schadcode zusätzlich erschweren und einschränken kann.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Integrity Measurement Architecture](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/enhancing-security-with-the-kernel-integrity-subsystem_assembly_managing-kernel-command-line-parameters-with-uki)

### Rules:

  - package_aide_installed
  - aide_build_database
  - aide_periodic_cron_checking
  - aide_scan_notification
  - package_audit_installed
  - service_auditd_enabled
  - package_fapolicyd_installed
  - service_fapolicyd_enabled
  - fapolicy_default_deny

### Implementation Status: implemented

______________________________________________________________________
