---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.1 - \[Zugangskonten\] Zentrales Management

## Control Statement

Berechtigung SOLLTE ein zentrales Managementsystem für Zugangskonten installieren.

## Control guidance

Wenn Zugangskonten lokal auf jedem Gerät einzeln verwaltet werden, könnte es zu inkonsistenten und veralteten Zugängen und Berechtigungen kommen. Ein zentrales System steuert Benutzeridentitäten und Zugriffsrechte übergreifend – oft als Identity and Access Management (IAM) oder bei sensiblen Konten als Privileged Access Management (PAM) bezeichnet. Es kann die Nachvollziehbarkeit erhöhen, Audits erleichtern und gerade in komplexen IT-Umgebungen Transparenz schaffen. Umsetzbar ist dies etwa über Verzeichnisdienste wie LDAP oder Active Directory, ergänzt durch rollenbasierte Zugriffsmodelle (RBAC). Praktische Maßnahmen zum Management können Self-Service-Portale, automatische Genehmigungsworkflows und regelmäßige Rechteüberprüfungen umfassen. Für den Einstieg kann eine Institution kritische Systeme priorisieren und Prozesse schrittweise zentralisieren.

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
