---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.4.1 - \[Berechtigungsmanagement\] Überprüfung tatsächlicher Berechtigungen

## Control Statement

Berechtigung SOLLTE dokumentierte und tatsächlich vergebene Berechtigungen {{ insert: param, ber.4.4.1-prm1 }} auf Übereinstimmung überprüfen.


## Control guidance

Der Sinn und Zweck der Vorgabe liegt darin, eine unbemerkte Abweichung zwischen Dokumentation und Realität frühzeitig zu erkennen. Ohne diesen Abgleich könnte es vorkommen, dass ehemalige Mitarbeitende weiterhin Zugriff auf interne Systeme behalten oder dass sich im Laufe der Zeit unautorisierte Rechteanhäufungen einschleichen. Durch eine wirksame Überprüfung kann hingegen sichergestellt werden, dass nur aktuelle, geprüfte und erforderliche Zugriffsrechte bestehen bleiben und so die Angriffsfläche der Institution reduziert werden kann. Zur Umsetzung kann die Institution Berechtigungsübersichten automatisiert aus IT-Systemen exportieren und diese mit den in Verzeichnissen oder Rollenmodellen hinterlegten Daten vergleichen, z.B. anhand eines automatisierten Abgleiches mit Personalstammdaten einmal pro Quartal. Diese Anforderung ist auch dann erfüllt, wenn Dokumentation der Berechtigungen und tatsächliche Berechtigung (z.B. ein Verzeichnisdienst) dasselbe sind. Bitte beachten Sie dabei, dass die generelle Anforderung zur Überprüfung vergebener Berechtigungen weiter gefasst ist und z.B. auch den Abgleich zwischen tatsächlich vergebenen Berechtigungen und nicht dokumentieren Erfordernissen (beispielsweise durch die Vorlage bei Vorgesetzten) umfassen kann.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Im Kontext von RHEL-Hosts sollte die Berechtigung primär zentral im Verzeichnisdienst vorgenommen werden, der über sssd angebunden wird. Bei IdM-Anbindung ist das Verzeichnis oft zugleich Dokumentation und Wirkbetrieb — dann entfällt ein separater Abgleich laut Guidance.

Weitere Informationen: [IdM-Benutzer, Gruppen, Hosts und Zugriffskontrollregeln](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_idm_users_groups_hosts_and_access_control_rules/index)

### Implementation Status: alternative

______________________________________________________________________
