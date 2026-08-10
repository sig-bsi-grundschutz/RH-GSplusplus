---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.3 - \[Berechtigungsmanagement\] Begründung von Berechtigungen

## Control Statement

Berechtigung SOLLTE die Vergabe von Berechtigungen und Änderungen an Berechtigungen mit einer Begründung dokumentieren.


## Control guidance

Zweck ist die Nachvollziehbarkeit der Vergabe von Berechtigungen. Die Dokumentation kann z.B. mit einem Identity-Access-Management oder Personalmanagementsystem automatisiert werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Begründungen für Berechtigungsvergaben speichert RHEL lokal nicht als Pflichtfeld: `useradd`/`usermod`/`visudo` verlangen keinen Begründungstext. Nachvollziehbarkeit entsteht, wenn die Institution Zuweisungen über IdM, ein IAM- oder Personalmanagement-System mit Ticket-/Begründungsfeld führt und der Host nur den technisch wirksamen Zustand übernimmt. Ergänzend dokumentieren auditd-Ereignisse Zeitpunkt und Akteur von Änderungen an Konten, Gruppen und sudoers — jedoch ohne fachliche Begründung. Die Anforderung ist damit hostseitig nur teilweise, prozessual über IAM erfüllbar.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
