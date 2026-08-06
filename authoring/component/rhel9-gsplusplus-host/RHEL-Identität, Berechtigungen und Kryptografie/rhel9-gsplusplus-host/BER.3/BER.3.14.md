---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.14 - \[Zugangskonten\] Kein Recycling von Zugängen

## Control Statement

Berechtigung SOLLTE die Wiederverwendung von Zugangskonten für {{ insert: param, ber.3.14-prm1 }} blockieren.

## Control guidance

Wiederverwendung von Zugangskonten meint hier die erneute Vergabe oder Reaktivierung zuvor bereits verwendeter Zugangskonten für Einzelpersonen, Gruppen, Rollen, Dienste oder Geräte zu anderen Einzelpersonen, Gruppen, Rollen, Diensten oder Geräten (engl. account reuse, account recycling). Der Parameter „einen bestimmten Zeitraum“ beschreibt eine durch die Institution festgelegte Sperr- oder Karenzfrist, innerhalb derer ein deaktiviertes, entzogenes oder nicht mehr zugeordnetes Konto nicht erneut verwendet werden kann; sinnvolle Werte können je nach Schutzbedarf etwa 90 Tage, 180 Tage, ein Jahr oder bei besonders kritischen bzw. privilegierten Konten eine dauerhafte Nichtwiederverwendung sein. Ohne eine solche Sperrfrist könnte eine neue nutzende Person fälschlich Zugriff auf alte Berechtigungen, Protokollzuordnungen, Postfächer, Schlüssel, Tokens oder Anwendungskontexte erhalten, und ein Sicherheitsvorfall könnte später nicht mehr eindeutig einer handelnden Person oder einem technischen Vorgang zugeordnet werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL erzwingt keine automatische Sperr- oder Karenzfrist für die Wiederverwendung von Zugangskontennamen oder UIDs; nach dem Löschen eines Kontos mit `userdel` kann derselbe Benutzername oder dieselbe UID sofort neu vergeben werden, ohne dass das Betriebssystem dies verhindert. In zentral verwalteten Umgebungen bindet SSSD den Host an Red Hat IdM, Active Directory oder LDAP an; dort erfolgt die Kontovergabe über das Verzeichnis, sodass eine organisatorisch festgelegte Sperrfrist vor Neuvergabe eines Namens dort durchsetzbar ist, statt lokal frei entschieden zu werden. Als Übergangsmaßnahme kann ein Konto statt sofortiger Löschung mit `usermod -L` gesperrt oder über `chage -E` mit einem Ablaufdatum versehen werden, um es für die Dauer der Karenzfrist inaktiv, aber unter demselben Namen bzw. derselben UID reserviert zu halten. Die eigentliche Durchsetzung der Sperr- oder Karenzfrist — also das Verbot, einen Namen oder eine UID vor Ablauf des festgelegten Zeitraums neu zu vergeben — bleibt jedoch ein organisatorischer Prozess außerhalb der technischen Prüfmöglichkeiten des einzelnen RHEL-Hosts.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index)

### Implementation Status: partial

______________________________________________________________________
