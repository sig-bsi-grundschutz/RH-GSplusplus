---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.6.5 - \[Passwortgebrauch\] Anlassbezogene Passwortwechsel

## Control Statement

Berechtigung SOLLTE einen Passwortwechsel ausschließlich anlassbezogen ausführen.

## Control guidance

Ein ausschließlich anlassbezogener Passwortwechsel bedeutet, dass Passwörter nur genau dann geändert werden, wenn ein begründeter Sicherheitsanlass vorliegt – beispielsweise ein Verdacht auf Kompromittierung des Endgerätes oder Zugangs, neue einschlägige Einträge in öffentlichen Leak-Datenbanken, die Weitergabe an Unbefugte durch einen Phishing-Vorfall, oder technische Indikatoren für einen möglichen Missbrauch des Zugangs zu Systemen oder Anwendungen. Dieser Ansatz unterscheidet sich vom früher häufig praktizierten, periodischen Passwortwechsel, der ohne konkreten Anlass in festen Intervallen erzwungen wurde. Ein solcher erzwungener Rhythmus könnte die Passwortsicherheit sogar verringern, weil Nutzende dann dazu neigen, schwächere, nur leicht veränderte Passwörter („sommer5“) zu wählen oder Zugangsdaten in verschiedenen Zugängen wiederzuverwenden. Zweck dieser Regelung ist es, die tatsächliche Sicherheit von Zugangskonten zu erhöhen und unnötige Belastungen der Nutzenden zu vermeiden.

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
