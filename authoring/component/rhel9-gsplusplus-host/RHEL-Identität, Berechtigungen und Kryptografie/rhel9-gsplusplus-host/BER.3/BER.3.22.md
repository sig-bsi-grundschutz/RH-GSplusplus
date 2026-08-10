---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.22 - \[Zugangskonten\] Notfallzugang

## Control Statement

Berechtigung KANN Notfallzugangskonten installieren.

## Control guidance

Ein Notfallzugangskonto (sog. Break Glass Account) ist ein Zugang mit privilegierten Berechtigungen, der bei Notfällen als letztes Mittel zum Zugang zu wichtigen Systemen verwendet werden kann, z.B. Verzeichnisdienste, Cloud-Infrastrukturen. Es empfiehlt sich für diese Konten die Verwendung langer Passwörter und die Aufbewahrung dieser z.B. in einem Safe oder aufgeteilt auf mehrere Administrierende.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL trennt die Authentifizierung technisch in lokale Konten (`/etc/passwd`/`/etc/shadow`) und zentral über SSSD angebundene Verzeichnisdienste (IdM, Active Directory, LDAP); über `authselect` konfiguriertes PAM/NSS greift bei Ausfall von SSSD automatisch auf die lokale `files`-Quelle zurück, sodass ein lokal angelegtes Notfallkonto (z. B. `root` oder ein dediziertes Break-Glass-Konto, angelegt mit `useradd`/`passwd`) auch dann nutzbar bleibt, wenn die zentrale Authentifizierung nicht erreichbar ist. Mit `chage -E never` bzw. `chage -l` lässt sich sicherstellen, dass ein solches Konto — anders als reguläre temporäre Zugänge — nicht automatisch abläuft. Die sichere Aufbewahrung des Passworts (z. B. Safe, Aufteilung auf mehrere Administrierende) sowie die organisatorische Festlegung, welche Konten als Notfallzugang gelten, bleiben Prozessaufgaben der Organisation. Alternativ kann ein SSH-Key zur Authentifizierung via SSH verwendet werden. Für den Fall, dass der Host netzwerkseitig nicht mehr erreichbar ist und über die Konsole administriert werden muss, ist zwingend ein Passwort erforderlich (technisch ist es möglich, im SingleUser-Mode kein Passwort abzufragen, dies ist jedoch eine unsichere Konfiguration).

Weitere Informationen: [Authentifizierung und Autorisierung konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index)

### Implementation Status: partial

______________________________________________________________________
