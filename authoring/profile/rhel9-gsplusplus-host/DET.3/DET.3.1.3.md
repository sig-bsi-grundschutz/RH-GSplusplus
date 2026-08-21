---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.3.1.3 - \[Protokollierung\] Anbindung von Peripheriegeräten

## Control Statement

Detektion für IT-Systeme SOLLTE das Anschließen von Peripheriegeräten protokollieren.

## Control guidance

Das Protokollieren der Anbindung von Peripheriegeräten kann helfen, Manipulationsversuche an IT-Systemen frühzeitig zu erkennen und nachzuvollziehen. Ohne ein solches Protokoll könnte beispielsweise ein unbefugtes Speichermedium angeschlossen und vertrauliche Daten unbemerkt entwendet werden, oder es könnte Schadsoftware über ein USB-Gerät eingeschleust werden. Auch manipulierte Eingabegeräte könnten genutzt werden, um Tastatureingaben auszulesen oder unbemerkt Befehle einzuschleusen. Unter Peripheriegeräten sind in diesem Kontext externe Komponenten (aus Hardware oder virtuell) zu verstehen, die ein IT-System erweitern oder mit diesem verbunden werden – etwa USB-Sticks, externe Festplatten, Smartphones im Lade- oder Datenmodus, Drucker oder auch spezialisierte Geräte wie Diagnose- oder Messinstrumente. Zur praktischen Umsetzung kann eine Institution beispielsweise auf Betriebssystemfunktionen zurückgreifen, die Geräteanschlüsse im System-Log erfassen, oder ergänzende Endpoint-Management-Lösungen einsetzen, die eine zentralisierte Protokollierung erlauben.

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
