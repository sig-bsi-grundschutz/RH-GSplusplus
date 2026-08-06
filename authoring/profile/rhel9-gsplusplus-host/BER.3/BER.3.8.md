---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.8 - \[Zugangskonten\] Hinweise bei Anmeldefehlern

## Control Statement

Berechtigung für Anwendungen SOLLTE Hinweise darauf, ob ein Zugangskonto existiert bei erfolglosen Anmeldeversuchen deaktivieren.

## Control guidance

Den Hinweis, dass bei erfolglosen Anmeldeversuchen das Passwort oder die Kennung falsch ist, könnte ein Angreifer als sogenannte User Enumeration (Benutzerkonten-Aufzählung) oder Account Discovery (Konto-Entdeckung) Schwachstelle ausnutzen. Dadurch wird das Risiko einer Brute-Force-Attacke oder eines Credential Stuffings erhöht, bei der ein Angreifer eine Liste potenzieller Benutzernamen durchprobieren könnte, um gültige Konten zu identifizieren. Der Schutz kann gewährleisten, dass ein Angreifer nicht automatisch weiß, welche Konten er als Nächstes mit Passwörtern attackieren muss oder Rückschlüsse auf registrierte Zugangskonten erhält. Zur Umsetzung kann die Institution alle Rückmeldungen bei fehlgeschlagenen Anmeldeversuchen so vereinheitlichen, dass sie keinen Aufschluss über den Grund des Fehlschlags geben, beispielsweise durch die generische Nachricht „Der eingegebene Benutzername oder das Passwort ist ungültig.“.

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
