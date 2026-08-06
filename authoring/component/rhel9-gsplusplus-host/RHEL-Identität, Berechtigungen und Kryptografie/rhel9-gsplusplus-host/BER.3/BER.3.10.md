---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.10 - \[Zugangskonten\] Anmeldeversuchsgrenze am System

## Control Statement

Berechtigung für IT-Systeme SOLLTE weitere Anmeldeversuche nach Erreichen von {{ insert: param, ber.3.10-prm1 }} fehlgeschlagenen Versuchen vorübergehend blockieren.

## Control guidance

Betrifft sowohl die lokale Anmeldung über eine Benutzeroberfläche als auch den Zugriff über Fernwartungsprotokolle oder -anwendungen wie RDP, SNMP, wenn diese vorhanden sind. Die Umsetzung erfolgt im einfachsten Fall durch ein Login, bzw. eine Bildschirmsperre für das IT-System. Biometrische Daten wie Fingerabdrücke können gefälscht werden und sind nicht so leicht zu ändern wie Passwörter. Setzen Sie Biometrie daher nicht als einzigen Authentifizierungsfaktor ein, sondern wenn, dann nur zur Ergänzung (Mehr-Faktor-Authentifizierung). Die Anforderung ist entbehrlich, wenn das System keinen Zugriff auf schützenswerte Daten erlaubt, z.B. bei Nutzung als Kiosk.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Red Hat Enterprise Linux implementiert die lokalen und via "Fernwartung" (=SSH)" Anmeldeversuchsgrenze über das PAM-Modul `pam_faillock`, das nach `authselect enable-feature with-faillock` in die PAM-Stacks `system-auth` und `password-auth` eingebunden wird und damit lokale Anmeldungen, `su`/`sudo` sowie SSH-Zugänge gleichermaßen erfasst. Die Parameter `deny` und `fail_interval` in `/etc/security/faillock.conf` legen den maximalen Schwellwert fehlgeschlagener Versuche und das Zeitfenster für deren Zählung fest, während `unlock_time` die vorübergehende Sperrdauer definiert; für das root-Konto lässt sich dies über `deny_root`/`root_unlock_time` gesondert steuern.

Weitere Informationen: [Benutzerauthentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect_configuring-authentication-and-authorization-in-rhel)

### Rules:

  - accounts_passwords_pam_faillock_enabled
  - accounts_passwords_pam_faillock_deny
  - accounts_passwords_pam_faillock_unlock_time
  - accounts_passwords_pam_faillock_interval
  - account_password_pam_faillock_system_auth
  - account_password_pam_faillock_password_auth
  - accounts_passwords_pam_faillock_deny_root
  - accounts_passwords_pam_faillock_even_deny_root_or_root_unlock_time

### Implementation Status: implemented

______________________________________________________________________
