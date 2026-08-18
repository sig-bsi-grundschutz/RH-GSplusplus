---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.5.1 - \[Authentifizierung\] Authentifizierung am System

## Control Statement

Konfiguration für IT-Systeme SOLLTE den Zugriff auf das System im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement authentifizieren.

## Control guidance

Betrifft sowohl die lokale Anmeldung über eine Benutzeroberfläche als auch den Zugriff über Fernwartungsprotokolle oder -anwendungen wie RDP, SNMP, wenn diese vorhanden sind. Die Umsetzung erfolgt im einfachsten Fall durch einen Login, bzw. eine Bildschirmsperre für das IT-System. Biometrische Daten wie Fingerabdrücke können gefälscht werden und sind nicht so leicht zu ändern wie Passwörter. Setzen Sie Biometrie daher nicht als einzigen Authentifizierungsfaktor ein, sondern wenn, dann nur zur Ergänzung (Mehr-Faktor-Authentifizierung). Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Authentifizierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Kryptographie zu finden ist. Die Anforderung ist entbehrlich, wenn das System keinen Zugriff auf schützenswerte Daten erlaubt, z.B. bei Nutzung als Kiosk.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL erzwingt Systemzugang über den PAM-Stack, den `authselect` mit getesteten Profilen (z. B. `sssd` oder `local`) konsistent in `/etc/pam.d/system-auth` und `password-auth` konfiguriert; Anmeldungen an Konsole, GDM, `su`/`sudo` und — mit `UsePAM yes` in `sshd_config` — SSH laufen damit durch dieselbe Authentifizierungskette. PAM-Module ohne `nullok` verhindern Logins ohne gesetztes Passwort; der Notfall-Rescue-Modus erfordert zusätzliche Authentifizierung. Für grafische Arbeitsplätze kann GNOME per dconf Bildschirmsperre nach Leerlauf und automatische Sperre bei Aktivierung aktivieren. An zentrale Identitätsquellen (IdM, Active Directory) bindet SSSD Identitäten und Berechtigungen per NSS/PAM an — die konkrete IAM-Richtlinie (Passwortqualität, MFA, Kryptografie gemäß BER) legt die Institution fest; Biometrie allein als Faktor oder Kiosk-Ausnahmen sind organisatorisch zu steuern. Nicht-PAM-Dienste (z. B. SNMP, RDP falls installiert) sowie reine Server ohne GUI deckt RHEL nicht flächendeckend ab.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Benutzerauthentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect_configuring-authentication-and-authorization-in-rhel)

### Implementation Status: partial

______________________________________________________________________
