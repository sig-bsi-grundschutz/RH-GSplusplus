---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.14 - \[Umgang mit Authentisierungsmitteln\] Kompromittierte Authentifizierungsmittel

## Control Statement

Berechtigung SOLLTE die Sperrung kompromittierter Authentifizierungsmittel verankern.


## Control guidance

Ein Authentifizierungsmittel gilt als kompromittiert, wenn Anzeichen bestehen, dass Unbefugte es nutzen oder Zugriff darauf gehabt haben könnten. Beispiele sind Passwörter, die durch Datenlecks öffentlich geworden sind, oder biometrische Merkmale (z. B. Fingerabdrücke), die Unbefugten vorliegen. In solchen Fällen ist das Authentifizierungsmittel zu sperren oder zu entziehen, etwa durch den Einsatz von Sperrlisten. Bei biometrischen Merkmalen besteht zusätzlich ein enger Bezug zu datenschutzrechtlichen Anforderungen, da diese Daten nicht einfach ausgetauscht werden können.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Kompromittierte Authentisierungsmittel lassen sich auf RHEL technisch sperren oder ersetzen: lokale Konten mit `usermod -L`, Passwortreset, Entfernen von Einträgen in `authorized_keys`, Widerruf von Zertifikaten/Smartcards in IdM bzw. CRL/OCSP, sowie Deaktivieren des IdM-/AD-Kontos über SSSD. Automation (AAP) kann diese Schritte standardisieren. Erkennung (Leak-Meldung, Phishing, Anomalie) und die Entscheidung zur Sperrung sind Prozessaufgaben; das OS liefert die Durchsetzungsmittel, kein eingebautes Leak-Monitoring.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Smart-Card-Authentifizierung verwalten](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_smart_card_authentication/index).

### Implementation Status: partial

______________________________________________________________________
