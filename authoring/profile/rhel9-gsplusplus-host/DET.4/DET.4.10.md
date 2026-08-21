---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.4.10 - \[Überwachung von Aktivitäten\] Host-basierte Köder

## Control Statement

Detektion für IT-Systeme KANN Host-basierte Köder installieren.

## Control guidance

Köder sind Anwendungen, Dateien oder Datensätze auf dem IT-System, welche die Aufmerksamkeit von Angreifern auf sich ziehen, um diese zu entdecken, nachzuverfolgen oder von echten Zielen abzulenken. Sie werden auch als Canaries oder Tripwire bezeichnet. Beispielsweise kann das Sicherheitsteam eine gefälschte, aber verlockende Datei (z. B. „IBAN-Kontodaten.xlsx“) im System platzieren und eine Überwachung einrichten, die sie benachrichtigt, wenn die Datei berührt wird - da legitime Benutzer nicht darauf zugreifen können, signalisiert jede Interaktion potenziell unbefugte Aktivitäten. Ein weiteres Beispiel ist eine Datei „unattended.xml“, da sie für Angreifer nützliche Anmeldedaten für automatische Installationen enthalten könnte. Indem Sie eine gefälschte Version mit harmlosen Daten erstellen und den Zugriff auf die Datei oder Anmeldeversuche mit diesen Zugangsdaten überwachen, erhalten Sie eine frühzeitige Warnung, wenn jemand Ihr System auf der Suche nach einfachen Möglichkeiten zur Erlangung von Administratorrechten durchforstet, so dass Sie reagieren können, bevor es zu einem schwerwiegenderen Verstoß kommt. Allerdings kann es hierbei zu falsch-positiv Vorfallsmeldungen kommen, insbesondere wenn die Köder dort platziert werden wo sie für legitime Nutzende leicht zugänglich sind.

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
