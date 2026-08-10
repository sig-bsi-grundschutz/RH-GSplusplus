---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.5.4 - \[Umgang mit Authentisierungsmitteln\] Nur etablierte Kryptographie

## Control Statement

Berechtigung SOLLTE bei kryptografischen Authentifizierungsmitteln die ausschließliche Verwendung etablierter kryptografischer Algorithmen nach {{ insert: param, ber.5.4-prm1 }} verankern.

## Control guidance

Kryptografische Authentifizierungsmittel sind Authentisierungsnachweise, deren Sicherheit wesentlich auf kryptografischen Verfahren beruht, etwa Passwort-Hashing, Zertifikate, Schlüsselpaare, Smartcards, Hardware-Token, Passkeys/FIDO2-Authentifikatoren, signaturbasierte API-Zugänge oder SSH-Schlüssel (engl. cryptographic authenticators). Etablierte kryptografische Algorithmen sind mathematisch fundierte Verschlüsselungsverfahren und Protokolle, die in der aktuellen Praxis nicht mit vertretbarem Aufwand gebrochen werden können, beispielsweise für Signaturen, Message Authentication Codes, Hashfunktionen, Schlüsselableitung oder authentisierte Verschlüsselung. Sie basieren auf mathematisch schwer lösbaren Problemen, bieten Resistenz gegen bekannte kryptanalytische Angriffe, unterstützen ausreichend große Schlüssellängen und wurden von Experten gründlich geprüft und analysiert. Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

# Editable Content

<!-- Make additions and edits below -->
<!-- The above represents the contents of the control as received by the profile, prior to additions. -->
<!-- If the profile makes additions to the control, they will appear below. -->
<!-- The above markdown may not be edited but you may edit the content below, and/or introduce new additions to be made by the profile. -->
<!-- If there is a yaml header at the top, parameter values may be edited. Use --set-parameters to incorporate the changes during assembly. -->
<!-- The content here will then replace what is in the profile for this control, after running profile-assemble. -->
<!-- The current profile has no added parts for this control, but you may add new ones here. -->
<!-- Each addition must have a heading either of the form ## Control my_addition_name -->
<!-- or ## Part a. (where the a. refers to one of the control statement labels.) -->
<!-- "## Control" parts are new parts added after the statement part. -->
<!-- "## Part" parts are new parts added into the top-level statement part with that label. -->
<!-- Subparts may be added with nested hash levels of the form ### My Subpart Name -->
<!-- underneath the parent ## Control or ## Part being added -->
<!-- See https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring for guidance. -->
