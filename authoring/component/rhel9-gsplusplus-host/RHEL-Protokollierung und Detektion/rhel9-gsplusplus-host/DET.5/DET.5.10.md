---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.10 - \[Management von Schwachstellen\] Zeitnahes Patchmanagement

## Control Statement

Detektion SOLLTE ein zeitnahes Patchmanagement verankern.

## Control guidance

Patches (Updates oder Sicherheitsaktualisierungen) sind neue Versionen, die Sicherheitslücken schließen. Je nach Aufbau der betroffenen Assets kann es bei der Aktualisierung auch erforderlich sein, Abhängigkeiten (Bibliotheken, Upstream Software) ebenfalls zu aktualisieren. Dies kann durch automatisierte Installation oder nach einem Test umgesetzt werden. Die Umsetzung kann auch den schrittweisen Rollout von Patches vorsehen, sodass bei Fehlern im Patch nicht alle Systeme gleichzeitig betroffen sind und auch komplexe Fehlerbilder durch Rückmeldungen frühzeitig erkannt werden können. Dies kann zum Beispiel nach dem One-Many-All-Prinzip oder Blue-Green-Deployment erfolgen. Zur Beurteilung der Kritikalität von Patches kann die Krititikalität der mit dem Patch verbundenen Schwachstellen, das Risikoprofil der zu patchenden Assets oder eine Korrelation komplexer Angriffswege herangezogen werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL bezieht Sicherheitserrata über `dnf` aus autorisierten Red-Hat-Repos; `dnf-automatic` (Timer plus `apply_updates` / `upgrade_type=security` in `/etc/dnf/automatic.conf`) kann Patches zeitnah automatisch einspielen. `security_patches_up_to_date` beschreibt den Sollzustand „Errata angewendet“. Staged Rollout (One-Many-All, Blue-Green) und Test vor der Fläche sind Satellite/Automation- bzw. Change-Prozesse, nicht die Host-Paketkonfiguration allein.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
