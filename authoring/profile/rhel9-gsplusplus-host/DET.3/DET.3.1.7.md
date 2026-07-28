---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.3.1.7 - \[Protokollierung\] Was, Wann, Wo

## Control Statement

Detektion für Anwendungen SOLLTE zu jedem sicherheitsrelevanten Ereignis mindestens Zeitpunkt, die Quelle und das Zielobjekt protokollieren.

## Control guidance

Für die Definition eines Sicherheitsrelevanten Ereignisses, siehe Glossar (Namensräume des Grundschutz++). Damit einem Ereignis zuverlässig ein bestimmter Zeitpunkt zugewiesen werden kann, ist eine einheitliche Zeitquelle für die Systemuhr (meist über NTP oder PTP) als Voraussetzung erforderlich. Bei der Protokollierung der Herkunft oder Quelle (z.B. Gerätenamen, IP-Adresse) besteht ein enger Zusammenhang zu Compliance-Anforderungen, etwa zum Datenschutz.

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
