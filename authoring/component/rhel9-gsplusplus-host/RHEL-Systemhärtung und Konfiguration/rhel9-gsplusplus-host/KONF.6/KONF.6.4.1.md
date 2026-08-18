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

Rollenbasierte Verwaltung auf RHEL bindet SSSD an sudo-Regeln und Host-Based Access Control (HBAC) in Red Hat IdM oder LDAP-Schema; sudoers kann aus zentralen Maps bezogen werden. Polkit-Rollen steuern lokale privilegierte GUI-Aktionen. Active-Directory-Umgebungen nutzen oft sudo-Gruppen oder den SSSD-sudo-Provider. RBAC-Modell und Rollendefinitionen sind institutionelle IAM-Vorgaben.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: partial

______________________________________________________________________
