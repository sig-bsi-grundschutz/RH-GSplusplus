---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.10.1 - \[Management von Schwachstellen\] Autorisierte Bezugsquellen

## Control Statement

Detektion SOLLTE zuverlässige Bezugsquellen für Patches autorisieren.

## Control guidance

Eine Quelle ist unzuverlässig, wenn zukünftig mit Verstößen gegen die Schutzziele Vertraulichkeit, Verfügbarkeit oder Integrität durch die Entität zu rechnen ist (d.h. eine Prognose der Vertrauenswürdigkeit). Dies ist insbesondere der Fall, wenn erhebliche Verstöße gegen die Schutzziele durch die Entität begangen worden sind oder Anzeichen dafür vorliegen, dass bei einer Verwendung mit solchen Verstößen zu rechnen ist.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Autorisierte Bezugsquellen auf dem Host sind die konfigurierten `dnf`-Repositories mit erzwungener GPG-Prüfung (`gpgcheck` global und je Repo, Red-Hat-Release-Key installiert, `gpgcheck` nirgends aus). Satellite kann die Repos intern spiegeln. Ob eine Entität als Bezugsquelle vertrauenswürdig **ist**, entscheidet die Institution; der Host setzt nur die technische Bindung an signierte RH-Inhalte durch.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
