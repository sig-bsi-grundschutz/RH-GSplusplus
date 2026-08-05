---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.1 - \[Zugangskonten\] Zentrales Management

## Control Statement

Berechtigung SOLLTE ein zentrales Managementsystem für Zugangskonten installieren.

## Control guidance

Wenn Zugangskonten lokal auf jedem Gerät einzeln verwaltet werden, könnte es zu inkonsistenten und veralteten Zugängen und Berechtigungen kommen. Ein zentrales System steuert Benutzeridentitäten und Zugriffsrechte übergreifend – oft als Identity and Access Management (IAM) oder bei sensiblen Konten als Privileged Access Management (PAM) bezeichnet. Es kann die Nachvollziehbarkeit erhöhen, Audits erleichtern und gerade in komplexen IT-Umgebungen Transparenz schaffen. Umsetzbar ist dies etwa über Verzeichnisdienste wie LDAP oder Active Directory, ergänzt durch rollenbasierte Zugriffsmodelle (RBAC). Praktische Maßnahmen zum Management können Self-Service-Portale, automatische Genehmigungsworkflows und regelmäßige Rechteüberprüfungen umfassen. Für den Einstieg kann eine Institution kritische Systeme priorisieren und Prozesse schrittweise zentralisieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL verwaltet Zugangskonten standardmäßig lokal über `/etc/passwd`, `/etc/shadow` und `/etc/group`; für ein zentrales Managementsystem bindet der System Security Services Daemon (SSSD) den Host stattdessen an Red Hat Identity Management (IdM), Active Directory oder einen LDAP-Verzeichnisdienst an. Die Werkzeuge `realm join` bzw. `ipa-client-install` übernehmen die Domänenanbindung, wonach Identitäten, Gruppenmitgliedschaften und – über IdM zusätzlich HBAC- und sudo-Regeln – zentral im Verzeichnis gepflegt und über `authselect` in PAM/NSS eingebunden werden. Damit entfällt die inkonsistente Pflege einzelner lokaler Konten je Host, und Änderungen im Verzeichnis wirken sich sofort auf alle angebundenen Systeme aus. Der Aufbau und Betrieb des zentralen IdM-/AD-Verzeichnisses selbst (Hochverfügbarkeit, Rollenmodell, Genehmigungsworkflows) bleibt eine organisatorische bzw. infrastrukturelle Aufgabe außerhalb des einzelnen RHEL-Hosts.

### Implementation Status: alternative

______________________________________________________________________
