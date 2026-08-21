---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  RHEL-Systemhärtung und Konfiguration:
    - name: var_accounts_max_concurrent_login_sessions
      values:
        - "1"
      component-values:
        - "1"
    - name: var_sshd_max_sessions
      values:
        - "10"
      component-values:
        - "10"
    - name: var_accounts_tmout
      values:
        - "600"
      component-values:
        - "600"
    - name: sshd_idle_timeout_value
      values:
        - "300"
      component-values:
        - "300"
    - name: var_sshd_set_keepalive
      values:
        - "0"
      component-values:
        - "0"

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

RHEL kann über PAM und `pam_limits` in `/etc/security/limits.conf` bzw. `/etc/security/limits.d/` die Zahl gleichzeitiger interaktiver Anmeldungen **pro Zugangskonto** begrenzen (`maxlogins`); typisch sind Einträge wie `* hard maxlogins 10`, bei strenger Policy auch `1`. Damit wird pro Konto nur eine oder wenige parallele Sessions erlaubt. Für SSH kann zusätzlich `MaxSessions` in `sshd_config` parallele Kanäle pro Netzwerk-Verbindung drosseln, ohne verschiedene Identitäten zu verknüpfen. Um die gleichzeitige Anmeldung von verschiedenen Nutzerkonten zu verbieten, also effektiv nur eine gleichzeitige Anmeldung am System zu erlauben, muss `* maxsyslogins 1` in `/etc/security/limits.d/` gesetzt werden. `maxsyslogin` wirkt nicht auf den user `root` diesem kann aber explizit der Zugang via SSH untersagt werden. Es ist empfehlenswert bei einer solch strengen Konfiguration (`* maxsyslogins 1`) einen Notfall-Plan zu implementieren, wie man in dem Falle umgeht, dass eine Session dauerhaft offen ist und nicht geschlossen wird. Ebenfalls ist die Auswirkung auf potentielle Automatisierung zu berücksichtigen, die auf die Systeme zugreift. Session-Timeouts oder alternative Administrationswege (z.B. via Console) können hierbei unterstützend wirken.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - accounts_max_concurrent_login_sessions
  - sshd_set_max_sessions
  - sshd_disable_root_login
  - accounts_tmout
  - sshd_set_idle_timeout
  - sshd_set_keepalive

<!-- insbesondere die maxsyslogins 1 sind nicht gecovert in den Rules -->

### Implementation Status: partial

______________________________________________________________________
