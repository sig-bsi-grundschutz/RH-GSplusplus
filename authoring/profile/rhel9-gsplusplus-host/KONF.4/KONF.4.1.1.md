---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.4.1.1 - \[Vertrauenswürdige Basisdienste\] Weiterleitung von Anmeldeinformationen

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Weiterleitung mehrfach verwendbarer Anmeldeinformationen deaktivieren.

## Control guidance

„Weiterleitung mehrfach verwendbarer Anmeldeinformationen“ (auch als Credential Forwarding oder Credential Delegation bekannt) meint technische Mechanismen, bei denen die Anmeldeinformationen eines Zugangskontos (z.B. Kennworthashes oder Kerberos-Tickets) an ein zweites System weitergereicht werden, um sich dort ebenfalls zu authentifizieren, ohne die Daten erneut eingeben zu müssen. Ziel der Deaktivierung ist hier die Unterbrechung von Angriffsketten, die auf dem Diebstahl von Zugangsdaten basieren. Ein Angreifer könnte sonst nach der Kompromittierung eines weniger kritischen Systems, wie einem Webserver, die dorthin weitergeleiteten Anmeldeinformationen eines Administrators aus dem Arbeitsspeicher auslesen und sich mit diesen Rechten unbemerkt im gesamten Netzwerk weiter ausbreiten (Laterale Bewegung). Das gezielte Deaktivieren des Credential Forwarding kann die Angriffsfläche erheblich reduzieren und solche „Pass-the-Hash“- oder „Pass-the-Ticket“-Angriffe effektiv eindämmen, da Anmeldeinformationen mit hohen Privilegien gar nicht erst auf unsichere Systeme gelangen. Stattdessen kann die Authentifizierung ausschließlich temporäre, eingeschränkte Tickets oder Tokens verwenden. Hierzu gehören z.B. Windows Remote Credential Guard oder RestrictedAdmin, sowie unter Linux SSH-Agent Forwarding oder GSSAPI. Eine Token-basierte Authentifizierung ist eine Strategie zur Verbesserung der Informationssicherheit. Nachdem Benutzende ihre Anmeldedaten eingegeben haben, werden diese überprüft und ein einmaliges verschlüsseltes Token generiert, mit dem sie anschließend auf Online-Ressourcen zugreifen können, ohne bei jeder Anfrage ihren Benutzernamen und ihr Passwort eingeben zu müssen. Bei SSH-Verbindungen kann die unsichere „Agent Forwarding“-Funktion serverseitig in der Konfigurationsdatei deaktiviert werden.

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
