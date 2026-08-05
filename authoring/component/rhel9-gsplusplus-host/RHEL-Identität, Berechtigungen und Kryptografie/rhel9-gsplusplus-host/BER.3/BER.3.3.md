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

Die Kontodatenbanken `/etc/passwd`, `/etc/shadow`, `/etc/group` und `/etc/gshadow` gehören `root` und sind für andere Nutzende nicht beschreibbar, sodass Erstellung, Änderung von Metadaten/Berechtigungen und Löschung eines Zugangskontos technisch nur über die privilegierten Werkzeuge `useradd`, `usermod`, `userdel` bzw. `groupadd`/`groupdel` möglich sind. Der Zugriff auf diese Werkzeuge erfordert root-Rechte, die über `sudo` gezielt an eine dedizierte Gruppe vergeben werden können; zusätzlich lässt sich mit PAM (`pam_wheel.so`) der Wechsel zu `root` per `su` auf Mitglieder einer bestimmten Gruppe beschränken. In zentral verwalteten Umgebungen verlagert sich das Management zusätzlich in Red Hat IdM oder Active Directory, wo Rollen (z.B. IdM-Berechtigungen/Privilegien) genauer als die binäre root/non-root-Unterscheidung des lokalen Hosts festlegen können, wer Konten anlegen, ändern oder löschen darf. Welche konkreten Personen als "Administrierende" gelten und wie diese Rolle vergeben wird (Vier-Augen-Prinzip, Genehmigungsprozess), bleibt eine organisatorische Festlegung der Institution.

### Implementation Status: alternative

______________________________________________________________________
