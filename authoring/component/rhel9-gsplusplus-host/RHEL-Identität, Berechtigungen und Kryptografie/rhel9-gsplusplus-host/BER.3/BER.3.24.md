---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.24 - \[Zugangskonten\] Alternative Authentifizierung am IT-System

## Control Statement

Berechtigung für IT-Systeme KANN ein ebenso vertrauenswürdiges, alternatives Verfahren zur Authentifizierung verankern.

## Control guidance

Wenn Nutzende ihren Primärzugang (z.B. Passwort, Smartphone mit Authentifizierungs-App) verlieren, wird eine alternative Möglichkeit zur Wiederherstellung des Zugangs benötigt. Damit dieser Alternativzugang den Schutz der Primärmethode nicht aushebelt, ist eine vergleichbare Zuverlässigkeit der Authentifizierung erforderlich. Lösungsmöglichkeiten je nach Schutzbedarf sind z.B. (1) die persönliche Vorstellung mit Ausweis, oder (2) die Verifikation über bestehende Sitzungen.oder PUK.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL kann über SSSD und `authselect` ein alternatives, PKI-gestütztes Authentifizierungsverfahren mittels Smartcard oder Zertifikat bereitstellen, das eine mit dem primären Anmeldeverfahren vergleichbare Vertrauenswürdigkeit erreicht: `authselect select sssd with-smartcard` aktiviert die Zertifikatsauthentifizierung zusätzlich zum Passwort, während `pam_cert_auth = True` in `/etc/sssd/sssd.conf` PAM anweist, die Karte zu prüfen. Über eine hinterlegte Vertrauensanker-CA, Sperrlisten-/OCSP-Prüfung (`certificate_verification`) sowie Zertifikatszuordnungsregeln (`sssd_certmap.conf`) wird sichergestellt, dass nur gültige, eindeutig einem Konto zugeordnete Zertifikate zur Anmeldung akzeptiert werden. Damit deckt RHEL die technische Kernanforderung eines gleichwertigen Alternativverfahrens ab; die in der Anleitung beispielhaft genannten Wiederherstellungswege bei Verlust des Primärzugangs — persönliche Vorstellung mit Ausweis, Verifikation über eine bestehende Sitzung oder PUK-Rücksetzung der Smartcard selbst — bleiben organisatorische bzw. kartenverwaltungsseitige Prozesse außerhalb der SSSD/PAM-Konfiguration des Hosts.

Weitere Informationen: [Smartcard-Authentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_smart_card_authentication/configuring-smart-cards-using-authselect_managing-smart-card-authentication)

### Implementation Status: partial

______________________________________________________________________
