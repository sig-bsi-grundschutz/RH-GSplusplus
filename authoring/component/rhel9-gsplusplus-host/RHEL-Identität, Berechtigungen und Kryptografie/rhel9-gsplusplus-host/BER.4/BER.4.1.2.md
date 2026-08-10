---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.1.2 - \[Berechtigungsmanagement\] JIT‑/JEA‑Berechtigungen

## Control Statement

Berechtigung KANN die Berechtigung zum Zeitpunkt des Zugriffs für {{ insert: param, ber.4.1.2-prm1 }} aktivieren.


## Control guidance

„JIT‑/JEA‑Berechtigungen“ (Just‑In‑Time/Just‑Enough‑Access) ist die zeitlich und inhaltlich begrenzte Vergabe von Rechten zum Zeitpunkt eines Zugriffs auf eine Ressource. Dies kann insbesondere für privilegierte Zugangskonten und Administrationszugänge sinnvoll sein, um erhöhte Rechte nur genau dann zu ermöglichen, wenn sie wirklich erforderlich sind.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Klassisches Just-in-Time-/Just-Enough-Access steuert RHEL auf dem Host nicht allein: dauerhafte lokale Admin-Rechte widersprechen dem Ziel. Stattdessen aktiviert die Institution erhöhte Rechte zum Bedarfszeitpunkt über Automation — typischerweise Red Hat Ansible Automation Platform (AAP) in Verbindung mit Freigabe-Workflows (z. B. ServiceNow): kurzlebige Gruppenmitgliedschaften, befristete sudoers- oder IdM-Rollenänderungen werden nach Freigabe ausgerollt und danach wieder entzogen. Ergänzend begrenzt `sudo` mit kurzem Timestamp-Timeout die Wirkdauer bereits gewährter Escalation auf der Session-Ebene. Der Host bleibt Ausführungsziel; die JIT-Steuerung sitzt in Automation/IAM.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Systemadministration mit RHEL System Roles automatisieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/automating_system_administration_by_using_rhel_system_roles/index).

### Implementation Status: alternative

______________________________________________________________________
