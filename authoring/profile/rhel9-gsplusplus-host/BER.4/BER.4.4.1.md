---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.4.4.1 - \[Berechtigungsmanagement\] Überprüfung tatsächlicher Berechtigungen

## Control Statement

Berechtigung SOLLTE dokumentierte und tatsächlich vergebene Berechtigungen {{ insert: param, ber.4.4.1-prm1 }} auf Übereinstimmung überprüfen.

## Control guidance

Der Sinn und Zweck der Vorgabe liegt darin, eine unbemerkte Abweichung zwischen Dokumentation und Realität frühzeitig zu erkennen. Ohne diesen Abgleich könnte es vorkommen, dass ehemalige Mitarbeitende weiterhin Zugriff auf interne Systeme behalten oder dass sich im Laufe der Zeit unautorisierte Rechteanhäufungen einschleichen. Durch eine wirksame Überprüfung kann hingegen sichergestellt werden, dass nur aktuelle, geprüfte und erforderliche Zugriffsrechte bestehen bleiben und so die Angriffsfläche der Institution reduziert werden kann. Zur Umsetzung kann die Institution Berechtigungsübersichten automatisiert aus IT-Systemen exportieren und diese mit den in Verzeichnissen oder Rollenmodellen hinterlegten Daten vergleichen, z.B. anhand eines automatisierten Abgleiches mit Personalstammdaten einmal pro Quartal. Diese Anforderung ist auch dann erfüllt, wenn Dokumentation der Berechtigungen und tatsächliche Berechtigung (z.B. ein Verzeichnisdienst) dasselbe sind. Bitte beachten Sie dabei, dass die generelle Anforderung zur Überprüfung vergebener Berechtigungen weiter gefasst ist und z.B. auch den Abgleich zwischen tatsächlich vergebenen Berechtigungen und nicht dokumentieren Erfordernissen (beispielsweise durch die Vorlage bei Vorgesetzten) umfassen kann.

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
