---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.4.8 - \[Überwachung von Aktivitäten\] Ausstellung neuer HTTPS-Zertifikate

## Control Statement

Detektion für Webserver KANN die rechtzeitige Ausstellung neuer HTTPS-Zertifikate für Hostsysteme, die im Internet erreichbar sind, überwachen.

## Control guidance

„Rechtzeitige Ausstellung neuer HTTPS-Zertifikate“ meint hier, dass überwacht wird, ob vor Ablauf eines bestehenden TLS-/HTTPS-Zertifikats ein neues, gültiges und zur jeweiligen Webserver-Identität passendes Zertifikat aktiviert wird (certificate expiry monitoring, certificate renewal). „HTTPS-Zertifikate“ sind hier X.509-Zertifikate für TLS-gesicherte Webverbindungen, die insbesondere Servernamen, Gültigkeitszeitraum, ausstellende Zertifizierungsstelle und kryptografische Bindung an einen Schlüssel enthalten. „Server, die im Internet erreichbar sind“ bezeichnet Webserver mit öffentlich erreichbarer Adresse oder öffentlich auflösbarem Namen, etwa Webportale, APIs, Kundenportale oder Administrationsoberflächen, sofern sie aus dem Internet angesprochen werden können. Die Vorschrift zielt darauf ab, ablaufende oder nicht rechtzeitig erneuerte Zertifikate frühzeitig sichtbar zu machen: Ein versäumter Austausch könnte zu Browserwarnungen, Dienstunterbrechungen, fehlgeschlagenen API-Verbindungen, Vertrauensverlust bei Nutzenden oder improvisierten Notfallmaßnahmen führen. Eine entsprechende Detektion kann die Verfügbarkeit und Vertrauenswürdigkeit öffentlich erreichbarer Webdienste unterstützen und kann zugleich Hinweise auf Fehlkonfigurationen, unvollständige Automatisierung oder unerwartete Änderungen im Zertifikatsbestand liefern. Hierbei ist es sinnvoll nicht nur die Restlaufzeit mit Schwellwerten zu überwachen, sondern auch die tatsächliche Bereitstellung des neuen Zertifikates. Dazu können ein Monitoring der Zertifikatsdaten direkt am Webendpunkt, sowie Auswertungen aus Load-Balancern oder Reverse-Proxys gehören.

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
