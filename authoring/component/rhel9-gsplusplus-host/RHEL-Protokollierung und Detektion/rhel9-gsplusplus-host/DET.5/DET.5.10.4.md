---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.10.4 - \[Management von Schwachstellen\] Integritätsprüfung von Patches

## Control Statement

Detektion SOLLTE Patches vor der Installation auf Integrität testen.

## Control guidance

Wenn Patches durch Fehler bei der Übertragung oder sogar bewusst von Angreifern verändert wurden, kann dies nach der Installation zu nicht behebbaren Fehlerzuständen oder zur Verbreitung von Schadcode führen. Kann durch einen Abgleich von Prüfsummen umgesetzt werden, z.B. durch automatisierte Installationsroutinen oder einen manuellen Abgleich mit der Herstellerwebseite.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

`dnf`/`rpm` prüfen vor der Installation die GPG-Signatur der Pakete, sofern `gpgcheck` global und je Repository aktiv ist und auch lokale RPMs nicht ohne Signatur durchgehen. Das ist der automatisierte Integritätsabgleich gegen den Hersteller-Schlüssel, kein manueller SHA-Vergleich mit einer Webseite. Abschalten von `gpgcheck` oder ungeprüfte `rpm -i`-Installationen umgehen den Schutz.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
