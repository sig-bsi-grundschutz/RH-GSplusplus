---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.8 - \[Berechtigungsmanagement\] Entzug von Berechtigungen

## Control Statement

Berechtigung SOLLTE eine Vorgehensweise zum Entzug von Berechtigungen verankern.


## Control guidance

Innerhalb der Institution ist ein Prozess etabliert, mit dem Berechtigungen system- und anwendungsübergreifend entzogen sowie Zugänge deaktiviert oder gelöscht werden, sobald diese nicht mehr benötigt werden. Dadurch wird sichergestellt, dass bei Personalwechseln oder Aufgabenänderungen keine Berechtigungen für einzelne Systeme oder Anwendungen bestehen bleiben. Der Entzug von Berechtigungen bei Kündigungen, Versetzungen oder Änderungen von Zuständigkeiten ist, soweit möglich, als automatisierter Ablauf umgesetzt.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Den Entzug von Berechtigungen setzt RHEL technisch über Sperren und Mitgliedschaftsänderungen um: lokale Konten mit `usermod -L` / `chage`, Entfernen aus Gruppen und sudoers, Löschen oder Ersetzen von SSH-Autorized-Keys sowie — bei SSSD/IdM — Deaktivieren des Verzeichniskontos, HBAC-Entzug und Gruppenaustritt, worauf der Host bei Ticket-/Cache-Ablauf den Zugang verweigert. Automation (AAP, System Roles) kann diese Schritte bei Austritt oder Rollenwechsel standardisieren. Der institutionelle Prozess (Trigger aus HR/ITSM, systemübergreifende Vollständigkeit) bleibt außerhalb des einzelnen Hosts; ohne zentralen IdP drohen lokale Restrechte.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [IdM-Benutzer, Gruppen, Hosts und Zugriffskontrollregeln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_idm_users_groups_hosts_and_access_control_rules/index).

### Implementation Status: partial

______________________________________________________________________
