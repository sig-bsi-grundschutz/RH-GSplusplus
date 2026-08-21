---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  "RHEL-Identität, Berechtigungen und Kryptografie":
      - name: var_password_pam_dictcheck
        values:
          - "1"
        component-values:
          - "1"
      - name: var_password_pam_maxsequence
        values:
          - "3"
        component-values:
          - "3"
      - name: var_password_pam_maxrepeat
        values:
          - "3"
        component-values:
          - "3"
---

# BER.6.3 - \[Passwortgebrauch\] Trivialpasswörter

## Control Statement

Berechtigung für Nutzende SOLLTE die Verwendung von Trivialpassworten blockieren.


## Control guidance

Trivialpasswörter sind leicht zu erratende oder zu diesem Zugangskonto bereits öffentlich bekannte Passwörter (erkennbar durch Nutzung sog. Leak Check Datenbanken). Leicht zu erraten sind Passwörter, wenn sie mit gängigen Wörterbuchangriffen (dictionary attacks) bzw. systematischem Ausprobieren (brute force) in kurzer Zeit zu kompromittieren sind. Dazu zählen etwa einfache Folgen wie „123456“, „Passwort“ oder „qwerty“ sowie häufig vorkommende, in Leaks dokumentierte Standardkombinationen. Der Zweck der Anforderung liegt darin, das Risiko unautorisierter Zugriffe zu reduzieren: Ein Angreifer könnte mit automatisierten Tools in Sekunden oder Minuten triviale Passwörter durchprobieren, was zu einem unbefugten Zugriff auf Benutzerkonten, Systemressourcen oder sensible Daten führen könnte. Die Blockierung solcher Passwörter kann dagegen sicherstellen, dass nur schwer vorhersehbare Kennwörter verwendet werden, wodurch ein entscheidender Schutz gegen automatisierte Angriffsverfahren erreicht werden kann. Zudem können Passwortmanager beim Generieren nicht-trivialer Passwörter unterstützen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Grundsätzlich sollte ein RHEL-Host an zentrale Identity-Provider/Verzeichnisdienste angebunden sein und an dieser Stelle die Passwort-Qualität durchgesetzt sein. Für lokale Accounts blockiert RHEL mit `pam_pwquality` die Trivial- und Wörterbuchpasswörter: über authselect-gesteuerte PAM-Zeilen oder alternativ  über `/etc/security/pwquality.conf` greifen `dictcheck`, Mindestlänge und Zeichenklassen; Passwortänderungen scheitern, wenn das neue Geheimnis Wörterbuchworten oder zu einfachen Mustern entspricht. Ein Abgleich mit öffentlichen Leak-Datenbanken ist kein PAM-Feature.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - package_pam_pwquality_installed
  - accounts_password_pam_pwquality_system_auth
  - accounts_password_pam_pwquality_password_auth
  - accounts_password_pam_dictcheck
  - accounts_password_pam_maxsequence
  - accounts_password_pam_maxrepeat

### Implementation Status: partial

______________________________________________________________________
