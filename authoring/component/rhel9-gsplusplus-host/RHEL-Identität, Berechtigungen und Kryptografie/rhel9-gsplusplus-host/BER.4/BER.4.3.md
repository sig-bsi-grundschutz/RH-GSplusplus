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

Begründungen für Berechtigungsvergaben werden nicht lokal in RHEL gespeichert: `useradd`/`usermod`/`visudo` erfordern keinen Begründungstext. Die Berechtigungsänderung sollte daher durch einen automatisierten Prozess mit Genehmigungsaufgabe außerhalb von RHEL erfolgen, beispielsweise mittels Red Hat Ansible Automation Platform. Weiterhin sollte die Berechtigung primär in einem zentralen, an den RHEL-Host angebundenen, IAM erfolgen.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index)

### Implementation Status: alternative

______________________________________________________________________
