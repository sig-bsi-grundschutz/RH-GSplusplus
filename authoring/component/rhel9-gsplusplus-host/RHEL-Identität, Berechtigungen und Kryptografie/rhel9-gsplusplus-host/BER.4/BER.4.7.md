---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.7 - \[Berechtigungsmanagement\] IT-System-Zugangskonto

## Control Statement

Berechtigung für IT-Systeme KANN diese genau einem Zugangskonto zuweisen.


## Control guidance

Wenn ein besonders schützenswertes IT-System nur von einer Person oder Identität genutzt wird, empfiehlt es sich dieses mit genau einem zugehörigen Zugangskonto zu verknüpfen. Dadurch wird ausgeschlossen, dass weitere Konten unnötig Zugriff erhalten. Bei Revisionen ist auf diese Weise eindeutig nachvollziehbar, welche Identität Zugriff auf das System hatte. Das Vorgehen ist auch auf virtualisierte IT-Systeme übertragbar. Ein Beispiel ist eine spezielle Administrationskonsole, die ausschließlich einem dedizierten Admin-Konto zugeordnet ist.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL unterstützt das Muster, indem für Administrationskonsolen oder dedizierte Hosts ein einziges funktionales Konto (lokal oder in IdM) berechtigt wird, direkte Root-Netzlogins unterbleiben (`PermitRootLogin no`) und weitere interaktive Konten fehlen bzw. gesperrt sind.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - sshd_disable_root_login

### Implementation Status: partial

______________________________________________________________________
