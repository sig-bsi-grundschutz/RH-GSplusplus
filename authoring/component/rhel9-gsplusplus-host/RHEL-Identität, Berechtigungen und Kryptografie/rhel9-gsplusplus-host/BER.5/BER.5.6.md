---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.6 - \[Umgang mit Authentisierungsmitteln\] Vorkonfigurierte Authentisierungsmittel von IT-Systemen

## Control Statement

Berechtigung für IT-Systeme SOLLTE vorkonfigurierte Authentisierungsmittel deaktivieren.


## Control guidance

Herstellerseitige Standardkonten und Default-Passwörter stellen ein beliebtes Eingangstor für Angreifer dar. Achten Sie hierbei nicht nur auf Passwörter, sondern auch auf andere Zugangsmittel wie Hardware-Zugangstoken, Zertifikate oder physische Zugangskontrollsysteme.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Vorkonfigurierte bzw. leere Authentisierungsmittel existieren in RHEL im Auslieferungszustand nicht. Der einzige Account, der immer vorhanden ist ist `root`. Die Authentisierungsmittel für diesen müssen durch die Organisation definiert werden. Zur weiteren Absicherung entsprechender organisatorischen Maßnahmen zur Verhinderung leerer Passwörter, können entsprechende Optionen für sshd und Prüfungen der `/etc/shadow` auf leere Passwörter eingesetzt werden.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - no_empty_passwords
  - no_empty_passwords_etc_shadow
  - sshd_disable_empty_passwords

### Implementation Status: implemented

______________________________________________________________________
