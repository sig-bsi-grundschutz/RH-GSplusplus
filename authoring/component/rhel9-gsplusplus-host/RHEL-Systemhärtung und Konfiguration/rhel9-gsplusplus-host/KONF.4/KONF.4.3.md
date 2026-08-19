---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.3 - \[Vertrauenswürdige Basisdienste\] Authentifizierung von Fernwartungsfunktionen

## Control Statement

Konfiguration für IT-Systeme SOLLTE Fernwartungsfunktionen im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement authentifizieren.

## Control guidance

Unter Fernwartungsfunktionen versteht man technische Zugänge, die es ermöglichen, IT-Systeme aus der Ferne zu administrieren oder Fehler zu beheben, etwa über Protokolle wie RDP, SSH oder proprietäre Remote-Support-Lösungen. Fernwartungsfunktionen könnten für eine Institution erhebliche Risiken bergen, wenn ihre Nutzung nicht eindeutig authentifiziert wird. Ohne verlässliche Identitäts- und Berechtigungsprüfung könnte ein Unbefugter über eine Remote-Schnittstelle auf Systeme zugreifen, Konfigurationen manipulieren oder Schadsoftware einschleusen. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Authentifizierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Kryptographie zu finden ist.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die primäre Fernwartung auf RHEL erfolgt über OpenSSH (`sshd`). Der Dienst bindet Anmeldeversuche an PAM (`UsePAM yes`), sodass dieselben Identitätsquellen wie bei lokalen Sitzungen greifen. Ebenfalls kann `sshd` so konfiguriert werden, dass keine Host-basierte Authentifizierung erfolgt (`HostbasedAuthentication no` und `IgnoreRhosts yes`). Die systemweite Crypto Policy wird über das OpenSSH-Drop-in eingebunden, sodass Transport- und Authentisierungsverfahren den kryptographischen Anforderungen entsprechen.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - sshd_enable_pam
  - sshd_disable_empty_passwords
  - disable_host_auth
  - sshd_disable_rhosts
  - sshd_include_crypto_policy

### Implementation Status: implemented

______________________________________________________________________
