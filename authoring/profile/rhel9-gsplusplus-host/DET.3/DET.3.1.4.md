---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.3.1.4 - \[Protokollierung\] Systemfehler

## Control Statement

Detektion für IT-Systeme SOLLTE Fehlermeldungen des Systems protokollieren.

## Control guidance

Die Protokollierung von Fehlermeldungen kann eine wesentliche Grundlage für die Früherkennung von Sicherheits- und Stabilitätsproblemen in IT-Systemen bilden. Ohne ein systematisches Logging könnte ein kritischer Hardwaredefekt, eine beschädigte Systemdatei oder ein fehlgeschlagener Sicherheits-Update-Prozess unentdeckt bleiben und dadurch die Integrität oder Verfügbarkeit von IT-Systemen gefährden. Ebenso könnte ein Angreifer, der wiederholt unautorisierte Befehle ausführt oder Dienste fehlerhaft anspricht, unbemerkt bleiben, wenn die resultierenden Fehlermeldungen nicht nachvollzogen werden. Auf technischer Ebene kann es zweckmäßig sein, das native Logging des Betriebssysteme zu aktivieren und so zu konfigurieren, dass Fehlermeldungen konsistent erfasst werden – beispielsweise über Syslog-Dienste oder Windows-Event-Logs. Eine zentrale Log-Sammlung kann helfen, auch bei verteilten Systemen eine einheitliche Auswertung vorzunehmen.

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
