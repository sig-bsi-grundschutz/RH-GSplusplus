---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.2.2 - \[Identitätsmanagement\] Einschränkung

## Control Statement

Berechtigung SOLLTE die Einrichtung, Änderung oder Löschung einer Identität einschränken.

## Control guidance

Das Identitäts- und Berechtigungsmanagement ist entscheidend für die sichere Authentifizierung vor Zugang zu Informationen. Identitäten sind die Grundlage hierfür. Je nach Organisationsstruktur benötigen z.B. das Personalmanagement oder Administrierende schreibenden Zugang zu Identitäten.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL beschränkt technisch, wer Identitäten anlegen, ändern oder löschen kann: Die Konten- und Berechtigungsdatenbanken `/etc/passwd`, `/etc/shadow`, `/etc/group` und `/etc/gshadow` sind ausschließlich für `root` beschreibbar, sodass reguläre Nutzende sie nicht direkt manipulieren können. Werkzeuge wie `useradd`, `usermod` und `userdel` erfordern root-Rechte bzw. eine explizite `sudo`-Freigabe, wodurch die Einrichtung, Änderung und Löschung von Identitäten auf privilegierte Administrationswege begrenzt bleibt. Die organisatorische Ausgestaltung, wer diese privilegierten Rechte erhält (z.B. Vier-Augen-Prinzip, Genehmigungsworkflow zwischen Personalmanagement und Administration), bleibt Aufgabe der Institution. Ebenfalls ist es empfehlenswert in großen Umgebungen einen zentralen Identity-Provider (Red Hat IdM, Active Directory oder ander LDAP-Server) zu verwenden, und diese lediglich an die RHEL Server anzubinden. Dies ermöglicht zusätzlich die Anwendung zentraler Prozesse über verschiedene Systeme (Netzwerk-Devices, Linux, Windows, ...) hinweg.

### Rules:

  - file_permissions_etc_passwd
  - file_permissions_etc_shadow
  - file_permissions_etc_group
  - file_permissions_etc_gshadow
  - file_owner_etc_passwd
  - file_owner_etc_shadow
  - file_owner_etc_group
  - file_owner_etc_gshadow
  - file_groupowner_etc_passwd
  - file_groupowner_etc_shadow
  - file_groupowner_etc_group
  - file_groupowner_etc_gshadow

### Implementation Status: implemented

______________________________________________________________________
