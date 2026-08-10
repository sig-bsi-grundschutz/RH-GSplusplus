---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.5.10 - \[Umgang mit Authentisierungsmitteln\] Zugriffsbeschränkung pro IT-System

## Control Statement

Berechtigung für IT-Systeme SOLLTE den lesenden und schreibenden Zugriff auf Authentifizierungsmittel einschränken.

## Control guidance

Lesender Zugriff bezeichnet in diesem Kontext jede Möglichkeit, Authentifizierungsmittel einzusehen, auszulesen, zu exportieren, zu kopieren oder technisch zu verwenden, ohne sie unmittelbar zu verändern; schreibender Zugriff meint jede Möglichkeit, Authentifizierungsmittel anzulegen, zu ändern, zu ersetzen, zu löschen, zu importieren oder deren Vertrauensstatus zu beeinflussen. Authentifizierungsmittel sind hier alle technischen oder organisatorisch verwalteten Mittel, mit denen Identitäten nachgewiesen oder Vertrauensbeziehungen hergestellt werden, etwa Passwörter, private Schlüssel, API-Keys, Token, Zertifikate, Kerberos-Keytabs, SSH-Schlüssel, Recovery-Codes, Hardware-Token-Zuordnungen oder Einträge in Trust Stores. Der Zugriff auf solche Mittel ist besonders sensibel, weil bereits lesender Zugriff in vielen Fällen zur Nachahmung einer Identität oder zur Umgehung vorgesehener Kontrollmechanismen führen könnte, während schreibender Zugriff zusätzlich Manipulationen an Vertrauensketten, Schlüsselmaterial oder Anmeldeverfahren ermöglichen könnte.

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
