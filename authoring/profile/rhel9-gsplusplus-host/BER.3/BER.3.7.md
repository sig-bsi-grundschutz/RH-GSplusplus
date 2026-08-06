---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.3.7 - \[Zugangskonten\] Single-Sign-On

## Control Statement

Berechtigung für Anwendungen SOLLTE die Anmeldung über einen zentralen Identitätsprovider aktivieren.

## Control guidance

Bei Single Sign-on authentifizieren sich Nutzende bei einem zentralen Identity Provider, der auch die Berechtigungen zur Nutzung der Anwendung prüft. Bei erfolgreicher Authentifizierung und passenden Berechtigungen wird für die Sitzung ein Token ausgestellt, das den Zugang zur Anwendung ermöglicht. Da Nutzende durch Single-Sign-On weniger Anmeldeinformationen benötigen, wird es leichter, sich komplexe Passwörter zu merken oder zentrale gepflegte Schutzmaßnahmen, wie eine Mehr-Faktor-Authentifizierung oder Überwachung von Anmeldeinformationen, auch auf die Anwendung anzuwenden. Zudem erschwert Single-Sign-On auch Phishing-Angriffe, da Anmeldeinformationen nur noch an zentraler Stelle und nicht mehr verstreut in einzelne Anwendungen oder Webseiten abgefragt werden. Andererseits ist bei der Kompromittierung des Single-Sign-On-Logins auch die Authentifizierung an der Anwendung kompromittiert und die Verfügbarkeit der Anwendung hängt auch von der Verfügbarkeit des zentralen Logins ab. Dies kann unter Windows durch Nutzung eines Windows Server Domain Controllers und unter Linux durch Samba mit aktiviertem Heimdal Kerberos Key Distribution Center (KDC) umgesetzt werden.

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
