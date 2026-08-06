---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.8 - \[Zugangskonten\] Hinweise bei Anmeldefehlern

## Control Statement

Berechtigung für Anwendungen SOLLTE Hinweise darauf, ob ein Zugangskonto existiert bei erfolglosen Anmeldeversuchen deaktivieren.

## Control guidance

Den Hinweis, dass bei erfolglosen Anmeldeversuchen das Passwort oder die Kennung falsch ist, könnte ein Angreifer als sogenannte User Enumeration (Benutzerkonten-Aufzählung) oder Account Discovery (Konto-Entdeckung) Schwachstelle ausnutzen. Dadurch wird das Risiko einer Brute-Force-Attacke oder eines Credential Stuffings erhöht, bei der ein Angreifer eine Liste potenzieller Benutzernamen durchprobieren könnte, um gültige Konten zu identifizieren. Der Schutz kann gewährleisten, dass ein Angreifer nicht automatisch weiß, welche Konten er als Nächstes mit Passwörtern attackieren muss oder Rückschlüsse auf registrierte Zugangskonten erhält. Zur Umsetzung kann die Institution alle Rückmeldungen bei fehlgeschlagenen Anmeldeversuchen so vereinheitlichen, dass sie keinen Aufschluss über den Grund des Fehlschlags geben, beispielsweise durch die generische Nachricht „Der eingegebene Benutzername oder das Passwort ist ungültig.“.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL unterbindet über das PAM-Modul `pam_faillock` mit der Option `silent` in `/etc/security/faillock.conf`, dass bei fehlgeschlagenen Anmeldeversuchen unterschiedliche oder informative Meldungen angezeigt werden, aus denen sich die Existenz oder der Sperrstatus eines Zugangskontos ableiten ließe; alle Anmeldeversuche über den PAM-Stack (Login, SSH, su) erhalten dadurch dieselbe generische Rückmeldung. Aktiviert wird das Modul über `authselect enable-feature with-faillock`, wodurch es in `/etc/pam.d/system-auth` und `password-auth` eingebunden wird. Der Schutz gilt jedoch nur für Anwendungen, die tatsächlich über PAM authentifizieren; Anwendungen mit eigener, PAM-unabhängiger Anmeldelogik (z. B. individuelle Webanwendungen) müssen die Vereinheitlichung ihrer Fehlermeldungen selbst umsetzen, was außerhalb des technischen Wirkungsbereichs des RHEL-Hosts liegt.

Weitere Informationen: [Benutzerauthentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect_configuring-authentication-and-authorization-in-rhel)

### Implementation Status: partial

______________________________________________________________________
