---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.17 - \[Zugangskonten\] Gruppenkonten - MFA

## Control Statement

Berechtigung SOLLTE für Gruppenkonten die Mehr-Faktor-Authentisierung aktivieren.

## Control guidance

Werden trotz des damit verbundenen Risikos Gruppenkonten genutzt, so kann mit Mehr-Faktor-Authentifizierung der Mißbrauch von Zugangsdaten erschwert werden. Kann zum Beispiel durch mehrere dem Zugangskonto zugewiesene Hardwaretoken oder durch OTP-Apps umgesetzt werden. Falls keine Gruppenkonten verwendet werden, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Mehr-Faktor-Authentisierung für Zugangskonten – einschließlich unvermeidbarer Gruppenkonten – lässt sich unter RHEL auf zwei Wegen umsetzen. Zum einen kann SSSD (ab RHEL 9.1 über `sssd-idp` und den OAuth-2.0-Device-Authorization-Flow, typischerweise an IdM gekoppelt) die Authentisierung an einen externen OIDC-/OAuth-Identity-Provider delegieren, der MFA – etwa OTP-Apps oder weitere Faktoren – zentral erzwingt; der Host schließt die Anmeldung erst nach erfolgreicher IdP-Prüfung ab. Welche Faktoren und Richtlinien greifen, bestimmt der IdP bzw. die IAM-Konfiguration, nicht das Betriebssystem selbst; ein natives OTP-PAM-Modul ohne IdP-Anbindung stellt RHEL nicht bereit. Zum anderen über SSSD und `authselect select sssd with-smartcard`: PAM verlangt dann zusätzlich zum Passwort eine Smartcard bzw. ein PKI-Zertifikat, wahlweise mit `with-smartcard-required` erzwungen; über Identity Management können einem Konto mehrere Zertifikate bzw. Hardwaretoken zugeordnet werden.

Weitere Informationen: [Smartcard-Authentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_smart_card_authentication/configuring-smart-cards-using-authselect_managing-smart-card-authentication), [Externe Identity Provider zur Authentisierung an IdM nutzen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_external_red_hat_utilities_with_identity_management/assembly_using-external-identity-providers-to-authenticate-to-idm_using-external-red-hat-utilities-with-idm)

<!-- while we could add some CaC Rules, which cover Smartcard authentication, I do not want to drive Users to do this -->
<!-- because using OIDC / IdP enforced authentication is the better manageable apporach. -->

<!--
### Rules:

  - sssd_enable_smartcards
  - install_smartcard_packages
  - package_opensc_installed
  - package_pcsc-lite_installed
  - service_pcscd_enabled
  - sssd_enable_certmap
-->

### Implementation Status: partial

______________________________________________________________________
