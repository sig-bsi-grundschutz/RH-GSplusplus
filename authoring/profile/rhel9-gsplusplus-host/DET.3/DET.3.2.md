---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.3.2 - \[Protokollierung\] Integration von Cloud-Diensten

## Control Statement

Detektion für Cloud-Dienste KANN Ereignisse in der Cloud im Audit Log der Institution protokollieren.

## Control guidance

Daten in Cloud-Diensten könnten von Angreifern über das Internet angegriffen werden, ohne dass Ereignisse im internen Netz hierauf Rückschlüsse geben. Dies könnte zum Beispiel durch Phishing geschehen, wodurch ein OAuth Token für den Cloud-Zugang missbraucht wird. Die Integration der Logs des Cloud-Dienstleisters in die institutionseigene Protokollierung kann hier helfen, z.B. bei Authentifizierung oder Berechtigungsänderungen, sowie bei Zugriff oder Veränderung von Daten. Insbesondere die Integration des Loggings mit einer bedingten Zugriffsrichtlinie kann hier helfen, z.B. indem Zugriffe von ungewöhnlichen IP-Adressen oder Browser Agents auf Angriffe hinweisen können. Die Integration von Cloud-Protokollen in ein internes Logging birgt oft erhebliche Herausforderungen, darunter die Bewältigung des enormen Volumens und der Vielfalt an Datenformaten, was durch selektive Protokollierung, Datennormalisierung und -anreicherung angegangen werden kann. Die Absicherung der Datenpipeline gegen Man-in-the-Middle-Angriffe kann durch die Einhaltung der technischen Anforderungen an die beteiligten IT-Systeme und Anwendungen bewältigt werden, z.B. Verschlüsselung und Authentifizierung. Da Cloud-Anbieter oftzusätzliche Gebühren für den Datentransfer (Egress-Kosten) verlangen bietet es sich an, die Protokolle vor der Übertragung zu filtern, um die Kosten für die Verbesserung der Sicherheit gering zu halten.

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
