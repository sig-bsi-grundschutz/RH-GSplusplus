---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.1.8 - \[Protokollierung\] Privilegierte Ereignisse

## Control Statement

Detektion für Anwendungen SOLLTE privilegierte Ereignisse einschließlich der Aktivierung, Deaktivierung oder Blockierung privilegierter Funktionen protokollieren.

## Control guidance

Privilegierte Ereignisse sind Vorgänge, bei denen besonders weitreichende Rechte genutzt werden – beispielsweise die Vergabe oder Entziehung von Administratorrechten, das Deaktivieren von Virenscannern oder Änderungen an Firewallregeln. Gerade solche Eingriffe könnten einen erheblichen Einfluss auf die Verfügbarkeit und Integrität von Daten haben. Ohne eine gezielte Aufzeichnung könnten sicherheitsrelevante Änderungen unentdeckt bleiben – etwa, wenn ein Angreifer unbefugt einen privilegierten Account übernimmt und Spuren verwischt, oder wenn ein interner Benutzer kritische Funktionen deaktiviert, wodurch Schutzmaßnahmen umgangen werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL protokolliert privilegierte Host-Vorgänge über `auditd`: Ausführung von SUID-/Admin-Werkzeugen (`sudo`, `su`, `passwd`, Modulwerkzeuge), Änderungen an `/etc/sudoers` und `/etc/sudoers.d/` sowie SELinux-Policy-Dateien. Das Journal nimmt zusätzlich Dienstestarts und SELinux-Denials auf. Aktivierung oder Deaktivierung anwendungsinterner privilegierter Funktionen (z. B. AV-Ausnahmen in Drittanbieter-Software) liegt außerhalb des generischen Host-Audits.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
