---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.4 - \[Überwachung von Aktivitäten\] Änderungen an Sicherheitsrichtlinien

## Control Statement

Detektion SOLLTE Änderungen an Sicherheitsrichtlinien einschließlich deren Aktivierung oder Deaktivierung überwachen.

## Control guidance

Wird die Aktivität von automatisierten Sicherheitswerkzeugen nicht überwacht, so könnten Angreifer diese Schutzmechanismen unbemerkt deaktivieren und die Person so in falscher Sicherheit wiegen. Zudem installieren Angreifer gerne permanente Hintertüren über neue Konten oder Gruppenwechsel. Automatisierte Sicherheitsrichtlinien sind z.B. Ausnahmelisten von Antivirus- oder EDR, über den Verzeichnisdienst hinzugefügte Gruppenzugehörigkeiten zu sicherheitsrelevanten Gruppen (z.B. Admin), NAC oder Firewallregeln.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

`auditd`-Watches und AIDE beobachten Änderungen an sicherheitsrelevanten Host-Richtlinien: SELinux-Policy, `/etc/sudoers` und `sudoers.d`, PAM, Firewalld-Zonen unter `/etc/firewalld/`. Das erkennt lokale Deaktivierung oder Aufweichen dieser Mechanismen. Ausnahmelisten von Drittanbieter-EDR/AV, NAC-Regeln und Gruppenmitgliedschaften im zentralen Verzeichnisdienst liegen außerhalb des Host-Dateisystems.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening).

### Implementation Status: partial

______________________________________________________________________
