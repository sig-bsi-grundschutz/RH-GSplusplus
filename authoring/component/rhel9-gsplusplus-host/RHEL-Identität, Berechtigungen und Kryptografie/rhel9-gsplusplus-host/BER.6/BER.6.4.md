---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.6.4 - \[Passwortgebrauch\] Kriterien für die Qualität von Passwörtern

## Control Statement

Berechtigung SOLLTE Kriterien für die Qualität von Passwörtern anhand von Lebensdauer und Angriffsmöglichkeiten verankern.


## Control guidance

Kriterien für die Qualität von Passwörtern können z.B. eine minimale Entropie, Passwortlänge oder Verwendung verschiedener Symbole sein. Die Lebensdauer meint die erwartete Nutzungsdauer des Passwortes. Die erforderliche Qualität hängt von den Angriffsmöglichkeiten ab, z.B. Anzahl der Zugangskonten, verwendetes kryptografisches Verfahren (vgl. BSI TR-02102) und begleitenden Sicherheitsmaßnahmen wie maximale Passwortversuche oder Mehr-Faktor-Authentifizierung. Für Zugänge ohne begleitende Maßnahmen ist eine Passwortlänge nicht unter 14 Zeichen empfehlenswert. Die Kriterien können einmalig festgelegt werden oder zwischen Zugängen oder Anwendungen differenzieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Passwortqualität und Lebensdauer konfiguriert RHEL kombiniert: `pam_pwquality` setzt Länge, Komplexität und Wiederholungsversuche; `LOGIN_DEFS`/`chage` (`PASS_MAX_DAYS`, `PASS_MIN_DAYS`, Warnfristen) steuern die maximale und minimale Nutzungsdauer neuer und bestehender Konten. Die konkreten Schwellen (z. B. ≥14 Zeichen ohne MFA laut Guidance) sind per Policy/Variablen zu wählen und an Angriffsfläche sowie begleitende MFA anzupassen. CaC liefert prüfbare Regeln für beide Dimensionen.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
