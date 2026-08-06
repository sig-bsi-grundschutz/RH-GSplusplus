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

Mehr-Faktor-Authentisierung für Zugangskonten – einschließlich unvermeidbarer Gruppenkonten – lässt sich unter RHEL über SSSD und `authselect select sssd with-smartcard` aktivieren: PAM verlangt dann zusätzlich zum Passwort eine Smartcard bzw. ein PKI-Zertifikat, wahlweise mit `with-smartcard-required` erzwungen. Über Identity Management können einem Konto mehrere Zertifikate bzw. Hardwaretoken zugeordnet werden, wie es die Anforderung für Gruppenkonten vorsieht. Eine native Unterstützung für OTP-Apps ist im Betriebssystem selbst nicht vorgesehen, und ob MFA tatsächlich für die (wenigen unvermeidbaren) Gruppenkonten verpflichtend gemacht wird, bleibt eine organisatorische Entscheidung der Institution.

Weitere Informationen: [Smartcard-Authentifizierung mit authselect konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_smart_card_authentication/configuring-smart-cards-using-authselect_managing-smart-card-authentication)

### Implementation Status: partial

______________________________________________________________________
