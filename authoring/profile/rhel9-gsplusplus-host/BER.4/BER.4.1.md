---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# BER.4.1 - \[Berechtigungsmanagement\] Prinzip der geringsten Berechtigungen

## Control Statement

Berechtigung SOLLTE die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen einschränken.

## Control guidance

Das Prinzip der geringsten Berechtigungen, im Englischen als Principle of Least Privilege (PoLP) bekannt, besagt, dass Nutzende, Prozesse oder Systeme nur die minimal notwendigen Zugriffsrechte erhalten dürfen, um die ihnen jeweils zugewiesenen Aufgaben zu erfüllen. Dies dient primär der Minimierung der Angriffsfläche und der Begrenzung potenzieller Schäden. Sollte beispielsweise ein Zugangskonto durch Phishing kompromittiert werden, könnte ein Angreifer ohne dieses Prinzip weitreichenden Zugriff auf kritische Daten oder Systeme erlangen und diese manipulieren, exfiltrieren oder verschlüsseln. Die konsequente Anwendung dieses Grundsatzes kann die Ausbreitung von Schadsoftware nach einem ersten Eindringen erheblich erschweren und sicherstellen, dass Mitarbeitende nur jene Informationen einsehen, die für ihre Tätigkeit unmittelbar relevant sind. Hierdurch wird auch das Risiko von Datendiebstahl durch Innentäter reduziert. Es empfiehlt sich als Ergänzung hier auch das "Need to know"-Prinzip zu betrachten, da sich beide Prinzipien ergänzen. Während das "Least Privilege"-Prinzip auf Systremrechte, Rollen und Berechtigungen fokussiert, liegt der Fokus des "Need to know"-Prinzips mehr auf Informationen und Datenzugriff. Zur sinnvollen Umsetzung kann die Institution ein rollenbasiertes Berechtigungskonzept (Role-Based Access Control, RBAC) etablieren, bei dem Berechtigungen nicht an einzelne Personen, sondern an vordefinierte Rollen (z.B. "Finanzbuchhaltung" oder "Netzwerkadministrator") gebunden werden. Für die Einführung in eine bestehende Umgebung kann ein gestuftes Vorgehen gewählt werden: (1) Zunächst wird ein Überwachungsmodus ("Audit-Only") aktiviert, der protokolliert, welche Zugriffe durch eine strengere Richtlinie verweigert würden, ohne sie tatsächlich zu blockieren. (2) Anschließend werden diese Protokolle analysiert, um legitime, für den Geschäftsbetrieb notwendige Zugriffe zu identifizieren und diese gezielt in die jeweiligen Rollen und Berechtigungsgruppen aufzunehmen. (3) Erst wenn keine legitimen Zugriffe mehr in den Protokollen als "verweigert" auftauchen, wird die Richtlinie scharf geschaltet und blockiert aktiv alle nicht explizit erlaubten Zugriffe. Alle relevanten Anforderungen zur Vergabe von Berechtigungen können mit den Handlungsworten "authentifizieren", "autorisieren" und "einschränken" gefunden werden.

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
