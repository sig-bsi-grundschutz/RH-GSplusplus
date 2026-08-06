---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.15 - \[Zugangskonten\] Zugang löschen nach Fristablauf

## Control Statement

Berechtigung SOLLTE nicht mehr benötigte Zugangskonten nach Ablauf der Löschfristen löschen.

## Control guidance

Die Löschfristen ergeben sich aus gesetzlichen Aufbewahrungs- und Löschfristen, die dem Compliance-Management entnommen werden können. Sicheres Löschen bedeutet, Daten so zu entfernen, dass sie mit vertretbarem Aufwand (auch forensisch) nicht mehr rekonstruierbar sind. Je nach Medium geschieht das z. B. durch verifizierbares Überschreiben, kryptografisches Löschen (Schlüsselvernichtung) oder physische Zerstörung (inklusive zugehöriger Metadaten, Caches und Datensicherungen).

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Es sollten wann immer möglich zentral verwaltete Zugangskonten verwendet werden.

RHEL stellt mit `userdel --remove --selinux-user` einen Befehl bereit, der ein nicht mehr benötigtes lokales Zugangskonto inklusive Heimatverzeichnis, Mail-Spool und SELinux-Zuordnung entfernt; Ein terminiertes, an gesetzliche Aufbewahrungsfristen gekoppeltes Löschen (z. B. per Ansible-Playbook oder Scheduler) sowie das Löschen zentral verwalteter Konten in RH IdM/AD über SSSD bleiben organisatorische Aufgaben, da RHEL selbst keine Löschfristen aus dem Compliance-Management kennt. Sicheres Löschen der zugehörigen Daten (Überschreiben, kryptografisches Löschen, physische Zerstörung von Datenträgern und Sicherungen) liegt außerhalb der Kontenverwaltung und ist Teil der Datenträger- und Backup-Entsorgung.

Weitere Informationen: [Entfernen eines Benutzers über die Befehlszeile](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-users-and-groups_configuring-basic-system-settings)

### Rules:

  - account_use_centralized_automated_auth

### Implementation Status: alternative

______________________________________________________________________
