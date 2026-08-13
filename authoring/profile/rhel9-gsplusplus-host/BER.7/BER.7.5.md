---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.7.5 - \[Schlüsselmanagement\] Kriterien für die Qualität von Zufallszahlen

## Control Statement

Berechtigung SOLLTE {{ insert: param, ber.7.5-prm1 }} für die Qualität von Zufallszahlen bei der Schlüsselerzeugung verankern.

## Control guidance

Wenn bei der Schlüsselerzeugung ein ungeeigneter Zufallszahlengenerator verwendet wird, könnte ein Angreifer Schlüssel errechnen. Daher sind Kriterien für Zufallszahlengeneratoren zu wählen, z.B. Verwendung etablierter, durch unabängige Dritte geprüfter Zufallszahlengeneratoren. Für Details siehe BSI TR-02102-1. Wichtig ist dabei auch, dass die verwendete Zufallsquelle tatsächlich eine nicht vorhersagbare Zahlenerzeugung erreicht. Inbesondere virtualisierte Systeme könnten ungeeignet sein zur Schlüsselerzeugung, da ihre Zufallszahlenquellen nicht direkt auf Hardwarefunktionen zurückgreifen.
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
