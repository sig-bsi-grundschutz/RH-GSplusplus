---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.5 - \[Umgang mit Authentisierungsmitteln\] Deaktivierung einfacher Biometrie auf IT-Systemen

## Control Statement

Berechtigung für IT-Systeme SOLLTE die Authentifizierung nur anhand von Biometrie deaktivieren.


## Control guidance

Wenn die Authentifizierung nur biometrisch vorgenommen wird (z.B. anhand von Fingerabdrücken oder Abbildern des Gesichtes), dann könnten Angreifer Fälschungen oder gestohlene Fingerabdrücke missbrauchen, um sich Zugang zu verschaffen. Werden biometrische Verfahren dagegen mit weiteren Authentisierungsmittel (z.B. einer PIN) kombiniert, können sie den Zugriffsschutz verbessern. Ein häufig vorkommendes Beispiel sind Mobilgeräte wie Smartphones, die durch Fingerabdruck den Zugriff auf Daten oder Funktionen wie das mobile Bezahlen gestatten - obwohl auf dem Gerät selbst häufig noch Fingerabdrücke erkennbar sind.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Rein biometrische Anmeldung ist auf typischen RHEL-Servern selten; falls `fprintd`/Fingerprint-PAM genutzt wird, steuert `authselect` die Faktoren: Fingerprint kann weggelassen oder nur kombiniert mit Passwort/PIN betrieben werden, statt als alleiniger Faktor. Ohne installierte Biometrie-Stack greift die Anforderung faktisch nicht. Für Host-Umfang „RHEL Server“ ist Biometrie meist irrelevant; wo Client-Images Biometrie erlauben, muss MFA (z. B. Smartcard oder Passwort+Biometrie) erzwungen werden.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index) (authselect-Profile und Faktoren).

### Implementation Status: partial

______________________________________________________________________
