---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.5.2 - \[Authentifizierung\] Keine Mehrfachanmeldung

## Control Statement

Konfiguration für IT-Systeme SOLLTE die gleichzeitige Anmeldung mehrerer Zugangskonten deaktivieren.

## Control guidance

Wenn Nutzende mit verschiedenen Identitäten simultan im System angemeldet sind, erhöht sich das Risiko von versehentlichen Datenvermischungen oder Falscheingaben deutlich. Dies kann besonders in sensiblen Bereichen wie im Finanzwesen oder Gesundheitswesen schwerwiegende Folgen haben, wo vertrauliche Kundendaten oder Patienteninformationen unbeabsichtigt zwischen verschiedenen Kontexten übertragen werden könnten. Bei Vorfällen wird so auch erschwert herauszufinden, von welchem Zugangskonto bestimmte Ereignisse stammen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL kann über PAM und `pam_limits` in `/etc/security/limits.conf` bzw. `/etc/security/limits.d/` die Zahl gleichzeitiger interaktiver Anmeldungen pro Zugangskonto begrenzen (`maxlogins`); die CaC-Regel `accounts_max_concurrent_login_sessions` prüft und setzt diesen Mechanismus (typisch `* hard maxlogins 10`, per Variable auch `1`). Damit wird pro Konto nur eine oder wenige parallele Sessions erlaubt — die Regel stellt ausdrücklich fest, dass sie nicht den Fall „eine Person mit mehreren Zugangskonten parallel angemeldet“ abdeckt. Für SSH kann zusätzlich `MaxSessions` in `sshd_config` (`sshd_set_max_sessions`) parallele Kanäle pro Verbindung drosseln, ohne verschiedene Identitäten zu verknüpfen. Die Verhinderung simultaner Mehrfachkonten-Anmeldung (eine Identität pro Nutzer, Trennung von Admin- und Arbeitskonten) erfordert institutionelle Vorgaben und IAM-Prozesse; RHEL bietet keinen Standardmechanismus, der mehrere verschiedene UID-Accounts derselben Person technisch ausschließt.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: partial

______________________________________________________________________
