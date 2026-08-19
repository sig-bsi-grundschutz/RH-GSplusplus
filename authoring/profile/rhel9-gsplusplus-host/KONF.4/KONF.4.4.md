---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.4.4 - \[Vertrauenswürdige Basisdienste\] Einschränkung von Fernwartungsfunktionen

## Control Statement

Konfiguration für IT-Systeme SOLLTE Fernwartungsfunktionen im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement einschränken.

## Control guidance

Fernwartungszugänge, etwa über RDP, SNMP oder Anwendungen zur Fernsteuerung des Systems erlauben typischerweise eine Vielzahl von Eingriffen in Systemkonfiguration und Datenverarbeitungen. Beispiele sind die Remote-Zwischenablage und die automatische Einbindung von Peripheriegeräten, Wechseldatenträgern und Netzlaufwerken. Unautorisierte Fernwartungszugänge könnten für Angriffe missbraucht werden. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Authentifizierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Kryptographie zu finden ist.

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
