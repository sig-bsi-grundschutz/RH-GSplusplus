---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.4.1 - \[Privilegierte Systemfunktionen\] Rollenbasierte Privilegierung

## Control Statement

Konfiguration für IT-Systeme KANN rollenbasiertes Berechtigungsmanagement aktivieren.

## Control guidance

Rollenbasierte Administration schränkt die Berechtigungen administrativer Zugangskonten anhand von Rollen so ein, dass nur die jeweils erforderlichen Funktionen freigeschaltet sind. Dies kann z.B. mit Windows PowerShell Just Enough Administration (JEA) oder SELinux, AppArmor oder Sudoers umgesetzt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->


Auf RHEL können Rollen als Berechtigungsgruppe abgebildet werden. Für die jeweiligen Gruppen (`/etc/groups`) können sowohl SELinux Profile als auch entsprechende Berechtigungen auf Dateien, Verzeichnisse oder in `sudo` vergeben werden. Eine zentralisierte Verwaltung auch über mehrere Hosts hinweg bietet hierbei Red Hat IdM. Die Lokalen Gruppen können auch via `sssd` auf Berechtigungsgruppen im zentralen Verzeichnisdienst (IdM, Active Directory, LDAP) verweisen.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

<!-- automatisierte Prüfregeln ergeben hier keinen Sinn. Großteil der Mechanismen in anderen Controls abgedeckt. -->
<!-- Inhalt hier wichtiger, als die Mechanismen -->

### Implementation Status: not-applicable

______________________________________________________________________
