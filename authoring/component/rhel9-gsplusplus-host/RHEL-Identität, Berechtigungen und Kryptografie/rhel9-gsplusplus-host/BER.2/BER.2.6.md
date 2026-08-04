---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.2.6 - \[Identitätsmanagement\] Löschen nach Fristablauf

## Control Statement

Berechtigung SOLLTE nicht mehr benötigte Identitäten nach Ablauf der Löschfristen löschen.

## Control guidance

Gesetzliche Aufbewahrungs- und Löschfristen ergeben sich aus dem Compliance-Management, z.B. aus Regelungen der DSGVO oder dem Handels- und Steuerrecht. Sicheres Löschen bedeutet, Daten so zu entfernen, dass sie mit vertretbarem Aufwand (auch forensisch) nicht mehr rekonstruierbar sind. Je nach Medium geschieht das z. B. durch verifizierbares Überschreiben, kryptografisches Löschen (Schlüsselvernichtung) oder physische Zerstörung (inklusive zugehöriger Metadaten, Caches und Datensicherungen).

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Auf einzelnen RHEL-Hosts entfernt `userdel` (bei Bedarf mit `-r` für das Heimatverzeichnis) eine nicht mehr benötigte Identität vollständig aus `/etc/passwd`, `/etc/shadow`, `/etc/group` und `/etc/gshadow`; Für zentral verwaltete Umgebungen empfiehlt sich, die Identität einmalig in Red Hat IdM oder einem anderen Verzeichnisdienst (Active Directory, LDAP) zu deprovisionieren und die Löschung über die Red Hat Ansible Automation Platform (AAP) mit einer entsprechenden Rolle/Playbook automatisiert und auditierbar auf alle angebundenen RHEL-Hosts der Flotte auszurollen, statt jeden Host manuell per `userdel` zu bearbeiten. Die Bestimmung der gesetzlichen Löschfrist selbst sowie ein forensisch belastbares Löschen der zugehörigen Daten (verifizierbares Überschreiben, kryptografisches Löschen von Datenträgern, Bereinigung von Datensicherungen) sind organisatorische bzw. Storage-/Backup-Ebene und liegen außerhalb der Kontenverwaltung des Hosts.

### Rules:

  - accounts_authorized_local_users

### Implementation Status: partial

______________________________________________________________________
