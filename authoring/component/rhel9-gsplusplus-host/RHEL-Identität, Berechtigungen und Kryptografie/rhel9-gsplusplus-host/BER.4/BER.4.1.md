---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  "RHEL-Identität, Berechtigungen und Kryptografie":
    - name: var_sudo_timestamp_timeout
      values:
        - "5"
      component-values:
        - "5"
    - name: var_pam_wheel_group_for_su
      values:
        - sugroup
      component-values:
        - sugroup

---

# BER.4.1 - \[Berechtigungsmanagement\] Prinzip der geringsten Berechtigungen

## Control Statement

Berechtigung SOLLTE die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen einschränken.


## Control guidance

Das Prinzip der geringsten Berechtigungen, im Englischen als Principle of Least Privilege (PoLP) bekannt, besagt, dass Nutzende, Prozesse oder Systeme nur die minimal notwendigen Zugriffsrechte erhalten dürfen, um die ihnen jeweils zugewiesenen Aufgaben zu erfüllen. Dies dient primär der Minimierung der Angriffsfläche und der Begrenzung potenzieller Schäden. Sollte beispielsweise ein Zugangskonto durch Phishing kompromittiert werden, könnte ein Angreifer ohne dieses Prinzip weitreichenden Zugriff auf kritische Daten oder Systeme erlangen und diese manipulieren, exfiltrieren oder verschlüsseln. Die konsequente Anwendung dieses Grundsatzes kann die Ausbreitung von Schadsoftware nach einem ersten Eindringen erheblich erschweren und sicherstellen, dass Mitarbeitende nur jene Informationen einsehen, die für ihre Tätigkeit unmittelbar relevant sind. Hierdurch wird auch das Risiko von Datendiebstahl durch Innentäter reduziert. Es empfiehlt sich als Ergänzung hier auch das "Need to know"-Prinzip zu betrachten, da sich beide Prinzipien ergänzen. Während das "Least Privilege"-Prinzip auf Systremrechte, Rollen und Berechtigungen fokussiert, liegt der Fokus des "Need to know"-Prinzips mehr auf Informationen und Datenzugriff. Zur sinnvollen Umsetzung kann die Institution ein rollenbasiertes Berechtigungskonzept (Role-Based Access Control, RBAC) etablieren, bei dem Berechtigungen nicht an einzelne Personen, sondern an vordefinierte Rollen (z.B. "Finanzbuchhaltung" oder "Netzwerkadministrator") gebunden werden. Für die Einführung in eine bestehende Umgebung kann ein gestuftes Vorgehen gewählt werden: (1) Zunächst wird ein Überwachungsmodus ("Audit-Only") aktiviert, der protokolliert, welche Zugriffe durch eine strengere Richtlinie verweigert würden, ohne sie tatsächlich zu blockieren. (2) Anschließend werden diese Protokolle analysiert, um legitime, für den Geschäftsbetrieb notwendige Zugriffe zu identifizieren und diese gezielt in die jeweiligen Rollen und Berechtigungsgruppen aufzunehmen. (3) Erst wenn keine legitimen Zugriffe mehr in den Protokollen als "verweigert" auftauchen, wird die Richtlinie scharf geschaltet und blockiert aktiv alle nicht explizit erlaubten Zugriffe. Alle relevanten Anforderungen zur Vergabe von Berechtigungen können mit den Handlungsworten "authentifizieren", "autorisieren" und "einschränken" gefunden werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Das Prinzip der geringsten Berechtigungen setzt RHEL auf Host-Ebene über getrennte Administrationspfade und enge lokale Rechte um: privilegierte Eingriffe laufen über `sudo` mit gezielten Regeln in `/etc/sudoers` bzw. `/etc/sudoers.d/` statt dauerhafter Root-Shells; `su` lässt sich mit `pam_wheel` auf eine leere oder eng geführte Gruppe beschränken, und nur UID 0 bleibt dem Systemkonto `root` vorbehalten. Ergänzend verhindert `PermitRootLogin no` in OpenSSH direkte Root-Anmeldungen über das Netz. Gruppenmitgliedschaften, IdM-Rollen/HBAC sowie SELinux (Mandatory Access Control) schränken weiter ein, welche Identitäten welche Ressourcen erreichen. Die fachliche Rollenmodellierung (Need-to-know, Audit-Only-Einführung, Abgleich mit Geschäftsprozessen) bleibt institutionell und liegt außerhalb der reinen Host-Konfiguration.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - sudo_remove_nopasswd
  - sudo_require_authentication
  - sudo_require_reauthentication
  - use_pam_wheel_for_su
  - ensure_pam_wheel_group_empty
  - accounts_no_uid_except_zero

### Implementation Status: partial

______________________________________________________________________
