---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.5 - \[Zugangskonten\] Identität-Zugangskonto

## Control Statement

Berechtigung SOLLTE ein Zugangskonto zu genau einer Identität zuweisen.

## Control guidance

Wenn ein Zugangskonto genau einer Identität zugewiesen ist erleichtert dies die Vergabe von Berechtigungen nach dem Need-to-know-Prinzip. Außerdem kann so bei einem Vorfall nachvollzogen werden, welche Person welche Befehle ausgeführt hat, z.B. mittels des Audit Logs. Anders herum können einer Identität auch mehrere Zugangskonten zugewiesen sein, z.B. ein normalen Nutzungskonto und ein Zugangskonto für die Systemadministration.

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
