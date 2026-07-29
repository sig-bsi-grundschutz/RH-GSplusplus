---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.4.5 - \[Vertrauenswürdige Basisdienste\] Zeitquellen

## Control Statement

Konfiguration für IT-Systeme SOLLTE Zeitquellen autorisieren.

## Control guidance

Eine einheitliche Zeitquelle für die Systemuhr (meist über NTP oder PTP) ist essenziell für die einheitliche Auswertung von Logdateien, sowie für moderne kryptographische Verfahren. Es empfiehlt sich zu definieren, welche NTP-Server von welchen NTP-Clients genutzt werden sollen und ob NTP-Server im Broadcast-Modus oder im Client-Server-Modus arbeiten. Letzteres (Client-Server) ist hierbei Best Practice. In bestimmten Fällen empfiehlt es sich außerdem, dass sich NTP-Server bei der Kommunikation gegenüber Clients authentisieren und demnach NTP-Clients nur authentifizierte NTP-Daten akzeptieren.

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
