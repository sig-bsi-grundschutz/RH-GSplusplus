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

Host-basierte Angriffserkennung kombiniert RHEL über auditd (syscall- und dateibasierte Ereignisprotokollierung mit Regelwerk) und optional AIDE für Integritätsvergleiche. Kein nativer Exploit- oder Anomalie-Detector — Ereignisse werden an SIEM oder Monitoring weitergeleitet. Netzwerk-IDS ist ein separates Thema. Die Institution muss Regeln, Korrelation und Alarmierung definieren.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
