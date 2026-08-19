---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.4 - \[Rollen und Berechtigungen\] Privilegierte Systemfunktionen

## Control Statement

Konfiguration für IT-Systeme SOLLTE privilegierte Funktionen einschränken.

## Control guidance

Sind privilegierte Funktionen nicht eingeschränkt, so könnten Innentäter oder Angreifer über das Netz unbefugte Manipulationen vornehmen, Fehlkonfigurationen ausgelöst werden oder sich Schadcode automatisch einnisten. Privilegierte Funktionen können z.B. ein lokales Berechtigungsmanagement, die Installation von Anwendungen, der Schreibzugriff auf Systemverzeichnisse oder die Änderung der Systemkonfiguration sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Privilegierte Operationen steuert RHEL über `sudo` mit granularer sudoers-Konfiguration (`Cmnd_Alias`, Logging, kein pauschales `NOPASSWD`) und Polkit-Regeln für Desktop- und Dienst-Aktionen. Direkter Root-Login per SSH ist üblicherweise deaktiviert (`PermitRootLogin no`). Red Hat IdM kann sudo-Regeln zentral im Verzeichnisdienst verwalten. Es ist empfehlenswert ein zentrales Konfigurationsmanagement (z.B. Ansible) einzusetzen, um einheitliche Vorgehensweisen bei der Nutzung von priveligierten Systemfunktionen zu gewährleisten. Hierdurch kann einem Großteil von Administratoren die notwendigen Berechtigungen entzogen werden, was sowohl die Anzahl an möglichen Innentätern als auch Konfigurationsfehler reduziert.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).


### Rules:

  - sudo_restrict_privilege_elevation_to_authorized
  - sudo_require_authentication
  - sudoers_explicit_command_args
  - sudoers_no_command_negation
  - sshd_disable_root_login
  - use_pam_wheel_for_su
  - accounts_no_uid_except_zero
  - package_sudo_installed

### Implementation Status: implemented

______________________________________________________________________
