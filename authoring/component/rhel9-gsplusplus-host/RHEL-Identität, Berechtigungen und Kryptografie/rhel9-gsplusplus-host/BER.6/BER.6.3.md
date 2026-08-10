---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
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

Trivial- und Wörterbuchpasswörter blockiert RHEL mit `pam_pwquality`: über `/etc/security/pwquality.conf` bzw. authselect-gesteuerte PAM-Zeilen greifen `dictcheck`, Mindestlänge und Zeichenklassen; Passwortänderungen scheitern, wenn das neue Geheimnis Wörterbuchworten oder zu einfachen Mustern entspricht. ComplianceAsCode-Regeln prüfen Aktivierung und Parameter (u. a. `dictcheck`, `minlen`). Abgleich mit öffentlichen Leak-Datenbanken ist kein PAM-Feature und muss ggf. extern (IdM/IAM-Hook) ergänzt werden.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: implemented

______________________________________________________________________
