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

RHEL bindet Zugangskonten über den System Security Services Daemon (SSSD) an ein zentrales Verzeichnis wie Red Hat IdM, Active Directory oder LDAP an; `authselect` und `sssctl` konfigurieren dabei PAM und NSS entsprechend. Mit installiertem und aktiviertem `sssd`-Dienst entsteht die technische Voraussetzung für ein zentrales Managementsystem auf Hostebene, sodass Identitäten und Zugriffsrechte nicht mehr lokal je Gerät gepflegt werden müssen. Rollenbasierte Zugriffsmodelle (RBAC), Self-Service-Portale, automatisierte Genehmigungsworkflows und regelmäßige Rechteüberprüfungen sind hingegen Funktionen des zentralen Verzeichnisdienstes bzw. IAM-Systems selbst und liegen außerhalb dessen, was der RHEL-Host bereitstellen oder erzwingen kann.

### Implementation Status: partial

______________________________________________________________________
