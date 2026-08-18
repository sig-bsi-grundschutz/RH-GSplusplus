---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.4.2.1 - \[Vertrauenswürdige Basisdienste\] DNS-Verschlüsselung

## Control Statement

Konfiguration für IT-Systeme SOLLTE DNS-Verbindungen durch {{ insert: param, konf.4.2.1-prm1 }} verschlüsseln.

## Control guidance

DNS-Verschlüsselung, im Englischen oft als DNS over TLS (DoT) oder DNS over HTTPS (DoH) bezeichnet, ist ein Verfahren, bei dem Anfragen zur Namensauflösung im Internet kryptographisch geschützt werden, um deren Vertraulichkeit und Integrität sicherzustellen. Erfolgen diese Anfragen unverschlüsselt, könnte ein Angreifer im Netz die aufgerufenen Webseiten und Dienste eines Nutzers mitlesen und protokollieren. Schlimmer noch, ein Angreifer könnte die Antworten manipulieren, um den Nutzer unbemerkt auf gefälschte Webseiten umzuleiten, beispielsweise für Phishing-Angriffe. Die Aktivierung der DNS-Verschlüsselung kann einem solchen Ausspähen und Manipulieren der Namensauflösung effektiv entgegenwirken und stellt sicher, dass die Kommunikation zwischen dem Client und dem DNS-Server authentisch und nicht einsehbar ist. Nutzt das System kein DNS, so ist die Anforderung entbehrlich.

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
<!-- "## Control" parts are new parts added into the top-level statement part with that label. -->
<!-- Subparts may be added with nested hash levels of the form ### My Subpart Name -->
<!-- underneath the parent ## Control or ## Part being added -->
<!-- See https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring for guidance. -->
