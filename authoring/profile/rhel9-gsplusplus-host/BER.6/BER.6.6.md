---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.6.6 - \[Passwortgebrauch\] Monitoring von Zugangsdaten

## Control Statement

Berechtigung SOLLTE Zugangsdaten auf Kompromittierung durch {{ insert: param, ber.6.6-prm1 }} überwachen.

## Control guidance

Eine Kompromittierung meint hier, dass Zugangsdaten wie Benutzername und Passwort (englisch: credentials) von Unbefugten eingesehen, abgefangen oder manipuliert wurden, sodass ein Missbrauch für unautorisierte Zugriffe möglich wird. Dies könnte etwa durch Leaks in Datenbanken, durch Phishing-Angriffe oder durch das Abfangen unverschlüsselter Übertragungen entstehen. Ein automatisierter Mechanismus bezeichnet hierbei eine technische Lösung, die ohne manuelles Zutun kontinuierlich prüft, ob bekannte Indikatoren einer Kompromittierung vorliegen (englisch: credential monitoring system). Geeignete Mechanismen können etwa Credential-Leak-Monitoring-Dienste, Data Breach Checker oder Darknet-Scanning-Tools sein. Der Zweck dieser Vorgabe liegt darin, dass ein frühzeitiges Erkennen von kompromittierten Zugangsdaten helfen kann, unautorisierte Logins und den Missbrauch sensibler Systeme zu verhindern; ohne eine solche Überwachung könnte ein Angreifer über lange Zeit unentdeckt mit gestohlenen Daten arbeiten und kritische Schäden verursachen. Ergeben sich hierbei Anzeichen auf eine Kompromittierung oder einen Leak der Zugangsdaten, so kann als Reaktion ein Wechsel der Zugangsdaten über einen nicht kompromittierten Kommunikationskanal veranlasst oder schlicht das betroffene Zugangskonto gesperrt werden.

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
