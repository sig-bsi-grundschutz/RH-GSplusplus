---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.9 - \[Umgang mit Authentisierungsmitteln\] Mehr-Faktor-Authentisierung für weitreichende Berechtigungen

## Control Statement

Berechtigung SOLLTE Mehr-Faktor-Authentisierung für weitreichende Berechtigungen aktivieren.


## Control guidance

Eine Mehr-Faktor-Authentifizierung bei Zugängen mit weitreichenden Berechtigungen, z.B. Administrationskonten, die Zugriff auf wichtige Server wie den Verzeichnisdienst, das MDM, EDR oder DNS haben, erschwert den unberechtigten Zugang zu diesen Zugängen. Auch der Zugriff auch besonders sensible Daten kann eine weitreichende Berechtigung sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

 Ab RHEL 9.1 kann `sssd-idp` MFA an einen externen OIDC-/OAuth-IdP delegieren. Dies sollte die präferierte Konfiguration sein. Ein generisches OTP-PAM ohne IdP liefert RHEL nicht mit. Mehr-Faktor-Authentisierung für weitreichende Rechte (root/sudo, kritische Hosts) lässt sich unter RHEL analog zu anderen MFA-Kontrollen umsetzen: SSSD mit `authselect select sssd with-smartcard` (optional `with-smartcard-required`) verlangt Zertifikat/Smartcard zusätzlich zum oder statt des Passworts;

Weitere Informationen: [Smartcard-Authentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_smart_card_authentication/configuring-smart-cards-using-authselect_managing-smart-card-authentication), [Externe Identity Provider zur Authentisierung an IdM nutzen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_external_red_hat_utilities_with_identity_management/assembly_using-external-identity-providers-to-authenticate-to-idm_using-external-red-hat-utilities-with-idm).

<!-- even though we could implement some smartcard related technical controls, we chose to not do this, as this would lead people in implementing this over IdP delegation -->


### Implementation Status: alternative

______________________________________________________________________
