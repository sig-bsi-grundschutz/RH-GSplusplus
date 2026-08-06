---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.14 - \[Zugangskonten\] Kein Recycling von Zugängen

## Control Statement

Berechtigung SOLLTE die Wiederverwendung von Zugangskonten für {{ insert: param, ber.3.14-prm1 }} blockieren.

## Control guidance

Wiederverwendung von Zugangskonten meint hier die erneute Vergabe oder Reaktivierung zuvor bereits verwendeter Zugangskonten für Einzelpersonen, Gruppen, Rollen, Dienste oder Geräte zu anderen Einzelpersonen, Gruppen, Rollen, Diensten oder Geräten (engl. account reuse, account recycling). Der Parameter „einen bestimmten Zeitraum“ beschreibt eine durch die Institution festgelegte Sperr- oder Karenzfrist, innerhalb derer ein deaktiviertes, entzogenes oder nicht mehr zugeordnetes Konto nicht erneut verwendet werden kann; sinnvolle Werte können je nach Schutzbedarf etwa 90 Tage, 180 Tage, ein Jahr oder bei besonders kritischen bzw. privilegierten Konten eine dauerhafte Nichtwiederverwendung sein. Ohne eine solche Sperrfrist könnte eine neue nutzende Person fälschlich Zugriff auf alte Berechtigungen, Protokollzuordnungen, Postfächer, Schlüssel, Tokens oder Anwendungskontexte erhalten, und ein Sicherheitsvorfall könnte später nicht mehr eindeutig einer handelnden Person oder einem technischen Vorgang zugeordnet werden.

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
