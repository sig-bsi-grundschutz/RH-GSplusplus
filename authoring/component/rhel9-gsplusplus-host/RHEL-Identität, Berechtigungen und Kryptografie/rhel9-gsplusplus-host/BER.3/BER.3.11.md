---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.11 - \[Zugangskonten\] Anmeldeversuchsgrenze an der Anwendung

## Control Statement

Berechtigung für Anwendungen SOLLTE weitere Anmeldeversuche nach Erreichen von {{ insert: param, ber.3.11-prm1 }} fehlgeschlagenen Versuchen vorübergehend blockieren.

## Control guidance

Häufen sich Anmeldeversuche, so könnte ein Angreifer Zugangsdaten durchprobieren. Durch eine Anmeldeversuchsgrenze wird der Zugriff durch das massenhafte Durchprobieren von Zugangsdaten (Credential Stuffing) verhindert. Dies kann z.B. durch die Begrenzung der Anmeldeversuche pro Client oder pro IP erfolgen. Dies betrifft sowohl die Anmeldung an der Benutzeroberfläche als auch über das Netz. Relevant sind hierbei sowohl primäre als auch ggf. vorhandene sekundäre Zugänge (z.B. Sicherheitsfragen, Passwort zurücksetzen). Für die Wahl des Schwellwertes ist die Anzahl der betroffenen Zugangskonten, die Passwortlänge und der Schutzbedarf der Anwendung von Bedeutung. Je nach Risikoprofil der Anwendung sind verschiedene Lösungen denkbar, z.B. die Verwendung von CAPTCHAS bei Erreichen der Anmeldeversuchsgrenze oder indem der Zeitraum einer Blockierung nach jedem fehlgeschlagenen Anmeldeversuch erhöht wird. Erfordert die Anwendung keine Zugangsdaten, so ist auch diese Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Red Hat Enterprise Linux implementiert eine anwendungsübergreifende Anmeldeversuchsgrenze über das PAM-Modul `pam_faillock`, das mittels `authselect` (`authselect enable-feature with-faillock`) systemweit in die PAM-Stacks `/etc/pam.d/system-auth` und `/etc/pam.d/password-auth` eingebunden wird und damit für alle PAM-integrierten Anwendungen gilt — sowohl für die lokale Anmeldung an Konsole/GUI als auch für Netzwerkzugänge wie SSH, `su` oder `sudo`. Die Parameter `deny`, `fail_interval` und `unlock_time` in `/etc/security/faillock.conf` legen fest, nach wie vielen Fehlversuchen innerhalb welchen Zeitfensters ein Konto für welche Dauer gesperrt wird; bei `unlock_time = 0` ist eine manuelle Entsperrung durch den Administrator (`faillock --reset`) erforderlich. Die Sperre erfolgt pro Benutzerkonto und nicht pro Client oder IP-Adresse, wie es die Anforderung alternativ vorschlägt. Für Individualanwendungen, die nicht über PAM authentifizieren (z. B. eigenständige Webanwendungen), sowie für sekundäre Zugangswege wie Sicherheitsfragen oder Self-Service-Passwort-Reset bietet RHEL keinen technischen Hebel; hier bleibt die Umsetzung Aufgabe der jeweiligen Anwendung.

Weitere Informationen: [Benutzerauthentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect_configuring-authentication-and-authorization-in-rhel)

### Rules:

  - accounts_passwords_pam_faillock_enabled
  - accounts_passwords_pam_faillock_deny
  - accounts_passwords_pam_faillock_interval
  - accounts_passwords_pam_faillock_unlock_time
  - account_password_pam_faillock_system_auth
  - account_password_pam_faillock_password_auth

### Implementation Status: partial

______________________________________________________________________
