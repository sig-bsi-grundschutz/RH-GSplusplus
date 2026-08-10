---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.6.2 - \[Passwortgebrauch\] Blockieren von Passwort Recycling

## Control Statement

Berechtigung für Nutzende SOLLTE die Wiederverwendung von Passwörtern blockieren.


## Control guidance

Die Wiederverwendung von Passwörtern („password reuse“) ist die Nutzung identischer oder bereits früher verwendeter Passwörter für verschiedene Konten, Systeme oder aufeinanderfolgende Authentifizierungsvorgänge. Die Blockierung der Passwortwiederverwendung bedeutet hier, dass das Berechtigungsmanagementsystem („access management system“) technisch verhindert, dass ein neues Passwort mit einem zuvor verwendeten identisch ist oder einer vordefinierten Anzahl früherer Passwörter entspricht. Dies könnte nicht nur bei Wiederverwendung einer Person problematisch sein, sondern auch bei einer systemübergreifenden Fehlkonfiguration: Ein typisches Szenario wäre, dass in einer Institution mehrere Arbeitsplatzrechner mit identischen lokalen Administratorpasswörtern konfiguriert sind („local admin password reuse“). Wird ein einzelner Rechner durch Schadsoftware oder physischen Zugriff kompromittiert, könnte ein Angreifer dieses Passwort anschließend nutzen, um sich mit denselben Anmeldeinformationen lateral auf weitere Systeme auszubreiten. Die Wiederverwendung des lokalen Administratorpassworts könnte somit eine vollständige Kompromittierung der internen IT-Infrastruktur ermöglichen. Diese Anforderung adressiert den Schutz vor solchen Angriffen, die sich aus der Wiederverwendung kompromittierter Anmeldeinformationen ergeben könnten, etwa durch Credential-Stuffing oder Brute-Force-Angriffe auf bekannte Passwortmuster. Blockieren kann das Risiko verringern, dass ein Angreifer durch bekannte Passwörter unbefugten Zugang zu Konten erhält. Hierzu können zum einen eine lokale Passworthistorie oder zum anderen elektronische Passwortmanager genutzt werden, die unabhängige sichere Passwörter generieren, wo die Wahrscheinlichkeit einer Passwortwiederholung ausgeschlossen werden kann.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Passwort-Wiederverwendung blockiert RHEL über PAM: `pam_pwhistory` (bzw. historisch `remember` in `pam_unix`) speichert eine konfigurierbare Historie und lehnt neue Passwörter ab, die jüngst verwendet wurden; `authselect` integriert die Module in `system-auth`/`password-auth`. Die Historientiefe wird per Policy gesetzt und kann auch für root erzwungen werden. Systemübergreifende Wiederverwendung lokaler Admin-Passwörter verhindert PAM allein nicht — dazu dienen unterschiedliche Secrets pro Host (z. B. aus Secret-Management) und zentrale IdM-Konten.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index) (PAM/`pam_pwquality`/`password`-Stack).

### Implementation Status: implemented

______________________________________________________________________
