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

Vorkonfigurierte bzw. leere Authentisierungsmittel stellt RHEL ab, indem Anmeldungen mit leerem Passwort untersagt werden (`nullok` entfernen / PAM- und SSH-Härting), keine Blank-Hashes in `/etc/shadow` verbleiben und Hersteller-Default-Konten in Härtingsprofilen fehlen bzw. gesperrt werden. OpenSSH lehnt leere Passwörter ab; Passwort-Hashes liegen ausschließlich gehasht in shadow. Weitere Default-Geheimnisse (z. B. SNMP-Communitys) sind gesondert zu entfernen. CaC-Regeln prüfen die zentralen Leer-/Default-Passwortpfade.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
