---
x-trestle-param-values:
  det.3.1.6-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.6 - \[Protokollierung\] Systemspezifische Ereignisse

## Control Statement

Detektion für IT-Systeme KANN {{ insert: param, det.3.1.6-prm1 }} protokollieren.

## Control guidance

Bestimmte systemspezifische Ereignisse meint hier, dass von der Instiution konkret festgehalten wurde, welche für das System relevanten Ereignisse im Einzelnen protokolliert werden. Beispiele sind Aktionen mit spezifisch konfigurierten privilegierten Berechtigungen, Prozessaktivitäten des Betriebssystems, wie das Starten eines Systemprozesses, Dateierzeugung oder das Laden eines Treibers, die Modifikation von Systemkonfigurationsdateien oder die Installation oder Deinstallation von Systemdiensten und Anwendungen, sowie das Herunterfahren oder Neustarten des Systems. Die Festlegung, welche dieser oder weiterer systemspezifischer Ereignisse protokolliert werden, obliegt der Institution und hängt von der jeweiligen Systemumgebung und dem Schutzbedarf ab.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Welche systemspezifischen Ereignisse aufgezeichnet werden, bestimmt die Institution über Audit-Regeln (`/etc/audit/rules.d/`) und Journal-Einheiten: privilegierte Kommandos, Kernel-Modul-Laden, Dateiänderungen, sudoers-Watches sowie Start/Stopp von systemd-Units im Journal. Der Param nennt die Ereignismenge — RHEL liefert die Mechanismen, nicht die fachliche Auswahl. Prozessstarts (`execve`) und Reboots sind abbildbar, anwendungsspezifische Semantik nicht generisch.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
