---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.6.4 - \[Passwortgebrauch\] Kriterien für die Qualität von Passwörtern

## Control Statement

Berechtigung SOLLTE Kriterien für die Qualität von Passwörtern anhand von Lebensdauer und Angriffsmöglichkeiten verankern.


## Control guidance

Kriterien für die Qualität von Passwörtern können z.B. eine minimale Entropie, Passwortlänge oder Verwendung verschiedener Symbole sein. Die Lebensdauer meint die erwartete Nutzungsdauer des Passwortes. Die erforderliche Qualität hängt von den Angriffsmöglichkeiten ab, z.B. Anzahl der Zugangskonten, verwendetes kryptografisches Verfahren (vgl. BSI TR-02102) und begleitenden Sicherheitsmaßnahmen wie maximale Passwortversuche oder Mehr-Faktor-Authentifizierung. Für Zugänge ohne begleitende Maßnahmen ist eine Passwortlänge nicht unter 14 Zeichen empfehlenswert. Die Kriterien können einmalig festgelegt werden oder zwischen Zugängen oder Anwendungen differenzieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Grundsätzlich sollte ein RHEL-Host an zentrale Identity-Provider/Verzeichnisdienste angebunden sein und an dieser Stelle die Passwort-Qualität durchgesetzt sein. Für lokale Accounts blockiert RHEL mit `pam_pwquality` die Trivial- und Wörterbuchpasswörter: über authselect-gesteuerte PAM-Zeilen oder alternativ  über `/etc/security/pwquality.conf` greifen `dictcheck`, Mindestlänge und Zeichenklassen; Passwortänderungen scheitern, wenn das neue Geheimnis Wörterbuchworten oder zu einfachen Mustern entspricht.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - accounts_password_pam_dictcheck
  - accounts_password_pam_minlen
  - accounts_password_pam_minclass
  - accounts_password_pam_dcredit
  - accounts_password_pam_ucredit
  - accounts_password_pam_lcredit
  - accounts_password_pam_ocredit
  - accounts_password_pam_pwquality_password_auth
  - accounts_password_pam_pwquality_system_auth
<!-- excluded these because of BER.6.5 -->
<!--  - accounts_maximum_age_login_defs -->
<!--  - accounts_password_set_max_life_existing -->

### Implementation Status: implemented

______________________________________________________________________
