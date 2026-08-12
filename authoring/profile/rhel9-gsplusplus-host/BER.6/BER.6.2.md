---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.6.2 - \[Passwortgebrauch\] Blockieren von Passwort Recycling

## Control Statement

Berechtigung für Nutzende SOLLTE die Wiederverwendung von Passwörtern blockieren.

## Control guidance

Die Wiederverwendung von Passwörtern („password reuse“) ist die Nutzung identischer oder bereits früher verwendeter Passwörter für verschiedene Konten, Systeme oder aufeinanderfolgende Authentifizierungsvorgänge. Die Blockierung der Passwortwiederverwendung bedeutet hier, dass das Berechtigungsmanagementsystem („access management system“) technisch verhindert, dass ein neues Passwort mit einem zuvor verwendeten identisch ist oder einer vordefinierten Anzahl früherer Passwörter entspricht. Dies könnte nicht nur bei Wiederverwendung einer Person problematisch sein, sondern auch bei einer systemübergreifenden Fehlkonfiguration: Ein typisches Szenario wäre, dass in einer Institution mehrere Arbeitsplatzrechner mit identischen lokalen Administratorpasswörtern konfiguriert sind („local admin password reuse“). Wird ein einzelner Rechner durch Schadsoftware oder physischen Zugriff kompromittiert, könnte ein Angreifer dieses Passwort anschließend nutzen, um sich mit denselben Anmeldeinformationen lateral auf weitere Systeme auszubreiten. Die Wiederverwendung des lokalen Administratorpassworts könnte somit eine vollständige Kompromittierung der internen IT-Infrastruktur ermöglichen. Diese Anforderung adressiert den Schutz vor solchen Angriffen, die sich aus der Wiederverwendung kompromittierter Anmeldeinformationen ergeben könnten, etwa durch Credential-Stuffing oder Brute-Force-Angriffe auf bekannte Passwortmuster. Blockieren kann das Risiko verringern, dass ein Angreifer durch bekannte Passwörter unbefugten Zugang zu Konten erhält. Hierzu können zum einen eine lokale Passworthistorie oder zum anderen elektronische Passwortmanager genutzt werden, die unabhängige sichere Passwörter generieren, wo die Wahrscheinlichkeit einer Passwortwiederholung ausgeschlossen werden kann.

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
