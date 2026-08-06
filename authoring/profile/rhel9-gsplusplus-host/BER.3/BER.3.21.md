---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.21 - \[Zugangskonten\] Dienstekonten

## Control Statement

Berechtigung für Hostsysteme SOLLTE eine automatische Verwaltung der Zugangsdaten von Dienste-Konten aktivieren.

## Control guidance

Eine automatische Verwaltung der Zugangsdaten von Dienste-Konten bezeichnet in diesem Kontext die technische Fähigkeit, Passwörter, Schlüssel oder Tokens solcher Konten – im Englischen häufig als service accounts oder machine identities bezeichnet – durch spezialisierte Systeme ohne manuelles Eingreifen zu erzeugen, zu speichern, regelmäßig zu erneuern und kontrolliert zu verteilen. Zugangsdaten sind hierbei sämtliche Authentifizierungsinformationen, die einem Dienst ermöglichen, auf Ressourcen anderer Systeme zuzugreifen, beispielsweise API-Schlüssel, SSH-Keys oder Anmeldedaten für Datenbanken. Dienste-Konten werden meist von Applikationen, Hintergrunddiensten oder Automatisierungsprozessen genutzt und unterscheiden sich von personenbezogenen Benutzerkonten dadurch, dass sie keinem Individuum zugeordnet sind, sondern einem technischen Zweck dienen. Erfolgt bei Zugangskonten für automatisierte Dienste eine automatische Rotation von Passwörtern oder Anmeldezertifikaten, so werden statische Passwörter, die Ablage von Zugangsdaten auf Netzlaufwerken oder plötzliche Fehlfunktionen durch Zertifikatsablauf vermieden. Ihre automatische Verwaltung kann durch zentrale Passworttresore (password vaults), Identitätsmanagementsysteme (Identity and Access Management, IAM) oder Secret-Management-Lösungen realisiert werden.

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
