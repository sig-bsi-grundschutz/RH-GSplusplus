---
x-trestle-param-values:
  det.6.1.1-prm1:
  det.6.1.1-prm2:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.6.1.1 - \[Vorfallserkennung\] Automatisierte Feststellung

## Control Statement

Detektion SOLLTE kritische Vorfälle anhand von {{ insert: param, det.6.1.1-prm1 }} durch {{ insert: param, det.6.1.1-prm2 }} protokollieren.

## Control guidance

Zur Erfüllung der Anforderung ist es nicht erforderlich, dass alle denkbaren Sicherheitsvorfälle automatisch erkannt werden, sondern nur, dass diejenigen Vorfälle, die in der vorhandenen Infrastruktur automatisch feststellbar sind und mit einem hohen Risiko verbunden sind, automatisch festgestellt werden. Beispiele sind hier ein Virenbefall des zentralen Verzeichnisdienstes, unautorisierte Datenabflüsse oder das Aufbrechen eines Fensters im Sicherheitsbereich. Ressourcen meint hier z.B. Systeme, Zugangskonten, Datenkategorien.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Automatisch feststellbare, risikoreiche Host-Ereignisse kann `auditd` (Syscall-/Watch-Regeln) plus SELinux-Denials und AIDE-Abweichungen in das Journal/Audit schreiben; audispd reicht sie an syslog/SIEM weiter. Welche Kriterien und Ressourcen (Konten, Pfade, Datenkategorien) als „kritischer Vorfall“ gelten, setzt die Institution in Regeln und SIEM-Korrelation. Virenbefall des zentralen Verzeichnisdienstes oder physische Alarme sind nicht die Aufgabe dieses Hosts.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening).

### Implementation Status: partial

______________________________________________________________________
