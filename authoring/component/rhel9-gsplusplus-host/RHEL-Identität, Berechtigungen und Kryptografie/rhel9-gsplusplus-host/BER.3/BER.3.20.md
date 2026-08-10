---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.20 - \[Zugangskonten\] Zwischenspeicherung von Zugangsdaten

## Control Statement

Berechtigung für IT-Systeme SOLLTE die Zwischenspeicherung der Zugangsdaten von Nutzern deaktivieren.

## Control guidance

Wird die Zwischenspeicherung von Zugangsdaten auf IT-Systemen deaktiviert, so wird Angreifern deren Diebstahl erschwert. Kann unter Windows ab Server 2012 R2 durch Zuweisung aller Zugangskonten zur Gruppe "Geschützte Benutzer" (Protected Users) umgesetzt werden. Konten für Dienste und Computer brauchen nicht Mitglied von „Geschützte Nutzer“ sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Per Voreinstellung speichert SSSD keine Zugangsdaten (Passwörter, ersten Authentisierungsfaktor) zwischen; erst durch explizites Setzen von `cache_credentials = true` in der jeweiligen Domain-Sektion von `/etc/sssd/sssd.conf` wird eine Offline-Zwischenspeicherung überhaupt aktiviert. Ist diese aus betrieblichen Gründen (Anmeldung ohne Verbindung zum Identity-Provider) erforderlich, begrenzt `offline_credentials_expiration = 1` im Abschnitt `[pam]` die Gültigkeitsdauer der zwischengespeicherten Zugangsdaten auf einen Tag, sodass veraltete Anmeldeinformationen nicht unbegrenzt nutzbar bleiben. Für die temporäre Zwischenspeicherung von Zugangsdaten bei Rechteerhöhung erzwingt `Defaults timestamp_timeout=0` in `/etc/sudoers`, dass `sudo` bei jedem Aufruf erneut nach dem Passwort fragt, wodurch dieser Cache faktisch deaktiviert wird. Andere Zwischenspeicher wie der Kernel-Keyring, `ssh-agent` oder grafische Schlüsselbunde bleiben von diesen Kontrollen unberührt.

Weitere Informationen: [Offline-Authentifizierung aktivieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/assembly_additional-configuration-for-identity-and-authentication-providers_configuring-authentication-and-authorization-in-rhel), [sudo erfordert keine erneute Passwortauthentifizierung](https://access.redhat.com/solutions/6978911)

### Rules:

  - sssd_offline_cred_expiration
  - sudo_require_reauthentication

### Implementation Status: implemented

______________________________________________________________________
