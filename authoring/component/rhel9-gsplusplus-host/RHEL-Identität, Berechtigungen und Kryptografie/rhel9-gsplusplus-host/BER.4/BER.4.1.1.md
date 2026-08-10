---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.1.1 - \[Berechtigungsmanagement\] Rollenbasierte Berechtigung

## Control Statement

Berechtigung SOLLTE Berechtigungen rollenbasiert zuweisen.


## Control guidance

Aus Gründen der Nachvollziehbarkeit und des administrativen Aufwands wird die direkte Vergabe von Berechtigungen an Einzelkonten vermieden. Berechtigungen werden gemäß dem Least-Privilege-Prinzip in Rollen gebündelt, wobei die Zuweisung und der Entzug ausschließlich über diese Rollen erfolgt. Etwaige Ausnahmen, beispielsweise für temporäre Spezialrechte, werden restriktiv gehandhabt, nachvollziehbar dokumentiert und zeitlich befristet.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Rollenbasierte Berechtigungen bildet RHEL vor allem über Gruppen und zentrale Identity-Dienste ab: lokale Gruppen in `/etc/group`, sudoers-Aliase und gruppenbezogene `sudo`-Regeln bündeln Rechte statt Einzelzuweisungen; mit Red Hat Identity Management (IdM) bzw. SSSD werden Rollen, Host-based Access Control (HBAC) und gruppenbasierte Sudo-Regeln zentral gepflegt und auf den Host angewandt. Ausnahmen (temporäre Spezialrechte) lassen sich über befristete Gruppenmitgliedschaften oder zeitlich begrenzte sudoers-Einträge handhaben, erfordern aber einen geregelten IAM-Prozess. Die reine Betriebssystemkonfiguration erzwingt kein vollständiges Rollenmodell — das muss die Institution in IdM/Verzeichnis und Betriebsprozessen verankern.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [IdM-Benutzer, Gruppen, Hosts und Zugriffskontrollregeln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_idm_users_groups_hosts_and_access_control_rules/index).

### Implementation Status: partial

______________________________________________________________________
