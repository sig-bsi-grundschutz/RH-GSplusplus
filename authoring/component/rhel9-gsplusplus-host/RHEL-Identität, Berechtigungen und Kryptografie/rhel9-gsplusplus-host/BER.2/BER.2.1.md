---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.2.1 - \[Identitätsmanagement\] Person-Identität

## Control Statement

Berechtigung SOLLTE eine eindeutige Identität zu genau einer natürlichen Person oder einem IT-System zuweisen.

## Control guidance

Hier wird eine Identität ("muellera") genau einer natürlichen Person ("Andrea Müller") zugewiesen, oder einem IT-System ("pc02348" zu "pc02348.our.domain").

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt technisch sicher, dass jede lokale Benutzer-ID (UID) genau einmal vergeben ist, sodass keine zwei Identitäten unbemerkt dasselbe Konto teilen. In zentral verwalteten Umgebungen bindet SSSD den Host an Red Hat IdM, Active Directory oder LDAP an; die Identität stammt dann direkt aus dem Verzeichnisdatensatz der Person bzw. des IT-Systems, statt lokal frei vergeben zu werden. Die eigentliche Zuordnung eines Kontonamens zu einer bestimmten natürlichen Person (Namenskonvention, Personalprozess) bleibt jedoch ein organisatorischer Vorgang außerhalb der technischen Prüfmöglichkeiten des Hosts.

### Rules:

  - account_unique_id

### Implementation Status: partial

______________________________________________________________________
