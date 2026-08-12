---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.6.6 - \[Passwortgebrauch\] Monitoring von Zugangsdaten

## Control Statement

Berechtigung SOLLTE Zugangsdaten auf Kompromittierung durch {{ insert: param, ber.6.6-prm1 }} überwachen.


## Control guidance

Eine Kompromittierung meint hier, dass Zugangsdaten wie Benutzername und Passwort (englisch: credentials) von Unbefugten eingesehen, abgefangen oder manipuliert wurden, sodass ein Missbrauch für unautorisierte Zugriffe möglich wird. Dies könnte etwa durch Leaks in Datenbanken, durch Phishing-Angriffe oder durch das Abfangen unverschlüsselter Übertragungen entstehen. Ein automatisierter Mechanismus bezeichnet hierbei eine technische Lösung, die ohne manuelles Zutun kontinuierlich prüft, ob bekannte Indikatoren einer Kompromittierung vorliegen (englisch: credential monitoring system). Geeignete Mechanismen können etwa Credential-Leak-Monitoring-Dienste, Data Breach Checker oder Darknet-Scanning-Tools sein. Der Zweck dieser Vorgabe liegt darin, dass ein frühzeitiges Erkennen von kompromittierten Zugangsdaten helfen kann, unautorisierte Logins und den Missbrauch sensibler Systeme zu verhindern; ohne eine solche Überwachung könnte ein Angreifer über lange Zeit unentdeckt mit gestohlenen Daten arbeiten und kritische Schäden verursachen. Ergeben sich hierbei Anzeichen auf eine Kompromittierung oder einen Leak der Zugangsdaten, so kann als Reaktion ein Wechsel der Zugangsdaten über einen nicht kompromittierten Kommunikationskanal veranlasst oder schlicht das betroffene Zugangskonto gesperrt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Automatisiertes Credential-Leak-Monitoring (Darknet/Breach-Checker) ist kein Bestandteil von RHEL. Der Host liefert stattdessen die Voraussetzung für Missbrauchs- und Anmeldeüberwachung: auditd und Journal protokollieren Authentisierungsereignisse, sudo-Nutzung und Änderungen an Kontodaten; Logs können an ein zentrales SIEM weitergeleitet werden. Kompromittierungsindikatoren aus externen Leak-Diensten müssen IAM/SOC anbinden und dann Sperrung oder Reset (vgl. BER.5.14) auslösen. Damit wird die Anforderung auf dem Host entsprechend unterstützt.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - audit_rules_login_events_tallylog
  - audit_rules_login_events_faillock
  - audit_rules_login_events_lastlog
  - audit_rules_usergroup_modification_shadow

### Implementation Status: partial

______________________________________________________________________
