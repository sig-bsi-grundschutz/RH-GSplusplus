---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.3 - \[Zugangskonten\] Einschränkung des Managements

## Control Statement

Berechtigung SOLLTE das Management von Zugangskonten auf Administrierende einschränken.

## Control guidance

Management meint hier Aktionen wie z.B. das Erstellen oder Ändern von Metadaten oder Berechtigungen oder die Löschung des Zugangskontos.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Kontodatendateien `/etc/passwd`, `/etc/shadow`, `/etc/group` und `/etc/gshadow` sind unter RHEL standardmäßig ausschließlich `root` als Eigentümer zugeordnet und nur für `root` beschreibbar; jede administrative Aktion an einem Zugangskonto — Anlegen, Ändern von Metadaten oder Berechtigungen, Löschen — erfordert damit root- bzw. sudo-Rechte. Zusätzlich verhindert eine restriktive `sudoers`-Konfiguration, dass pauschale `ALL ALL=(ALL) ALL`-Einträge Nicht-Administrierenden ebenfalls uneingeschränkten Zugriff verschaffen. In zentral verwalteten Umgebungen (SSSD-Anbindung an IdM/AD/LDAP) verschiebt sich die eigentliche Rechteprüfung für Kontenverwaltung auf den Verzeichnisdienst; dessen ACIs/Rollenkonzept liegen außerhalb der Kontrolle dieses Hosts.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules

  - file_owner_etc_passwd
  - file_permissions_etc_passwd
  - file_owner_etc_shadow
  - file_permissions_etc_shadow
  - file_owner_etc_gshadow
  - file_permissions_etc_gshadow
  - sudo_restrict_privilege_elevation_to_authorized

### Implementation Status: implemented

______________________________________________________________________
