---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.4.1 - \[Vertrauenswürdige Basisdienste\] Anbindung an Verzeichnisdienst

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Anbindung an einen Verzeichnisdienst aktivieren.

## Control guidance

Anbindung meint hier die Authentifizierung und Autorisierungsprüfung von Zugangskonten über einen Verzeichnisdient (häufig auch als Directory Service bezeichnet). Dies ermöglicht die zentrale Verwaltung von Identitäten und deren Berechtigungen. Dies bedeutet, dass Zugriffsrechte für alle angebundenen Systeme zentral verwaltet und bei Bedarf umgehend angepasst werden können, was die Einhaltung des Prinzips der geringsten Rechte (Principle of Least Privilege) unterstützt. Ein häufiger Ansatz zur technischen Umsetzung ist die Verwendung von Protokollen wie LDAP (Lightweight Directory Access Protocol) oder der Einsatz von Single Sign-On (SSO) Lösungen, die eine einmalige Authentifizierung des Nutzers für mehrere Systeme ermöglichen. Institutionen können dabei die Anbindung neuer Systeme durch Automatisierung im Rahmen des Provisioning-Prozesses sicherstellen, um menschliche Fehler zu reduzieren. Beispielsweise könnte ein Standard-Skript bei der Installation eines neuen Servers dessen automatische Anbindung an den Verzeichnisdient veranlassen. In Windows Betriebssystemen erfolgt die Konfiguration des Betriebssystem über entsprechende Gruppenrichtlinien (Group Policy Object) aus dem Active Directory.

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
