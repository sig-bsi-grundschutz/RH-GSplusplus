---
x-trestle-set-params:
    # This section contains the parameters that are part of this control.
  # Each parameter has properties. Only the profile-values and display-name properties are editable.
  # The other properties are informational.
  #
  # The values property for a parameter represents values inherited from the OSCAL catalog.
  # To override the catalog settings, use bullets under profile-values as shown below:
  #
  #   profile-values:
  #     - value 1
  #     - value 2
  #
  # If the "- <REPLACE_ME>" placeholder appears under profile-values, it is the same as if
  # the profile-values property were left empty.
  #
  # Some parameters may show an aggregates property which lists other parameters. This means
  # the parameter value is made up of the values from the other parameters. For parameters
  # that aggregate, profile-values is not applicable.
  #
  # Property param-value-origin is meant for putting the origin from where that parameter comes from.
  # In order to be changed in the current profile, profile-param-value-origin property will be displayed with
  # the placeholder "<REPLACE_ME>" for you to be replaced. If a parameter already has a param-value-origin
  # coming from an inherited profile, do no change this value, instead use profile-param-value-origin as follows:
  #
  #    param-value-origin: DO NOT REPLACE - this is the original value
  #    profile-param-value-origin: <REPLACE_ME> - replace the new value required HERE
  #
  det.4.11.1-prm1:
    alt-identifier: 1fc84b56-0931-439d-9b5a-4642926e0d04
    profile-values:
      - <REPLACE_ME>
    profile-param-value-origin: <REPLACE_ME>
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# DET.4.11.1 - \[Überwachung von Aktivitäten\] Authentifizierungsversuche an externen Schnittstellen

## Control Statement

Detektion für Externe Netzanschlüsse KANN Authentifizierungsversuche auf unauthorisierte Verbindungen {{ insert: param, det.4.11.1-prm1 }} überprüfen.

## Control guidance

Ohne solche Überprüfungen könnte ein Angreifer unbemerkt wiederholt Zugangsdaten erraten (Brute-Force- oder Wörterbuchangriffe) oder unautorisierte Geräte an Schnittstellen wie VPN-Gateways, Firewalls oder externen Modems anbinden. Auch ein unbemerktes Einschleusen von Schadsoftware über offene Remote-Desktop- oder SSH-Verbindungen könnte langfristig unentdeckt bleiben. Eine kontinuierliche Auswertung von Anmeldeversuchen kann dagegen Auffälligkeiten wie ungewöhnlich viele Fehlversuche, Anmeldungen aus geografisch atypischen Regionen oder Verbindungsaufbau außerhalb üblicher Betriebszeiten aufzeigen und so eine wirksame Schutzwirkung entfalten. Als Frist können Intervalle wie "täglich", "wöchentlich" oder "in Echtzeit" je nach Kritikalität des Anschlusses angemessen sein. Verbindungen sind hier unautorisiert, wenn Anzeichen vorliegen, dass sie von unautorisierten Personen oder von unautorisierten Systemen stammen. Die Überprüfung kann manuell oder durch automatische Analyse von Logdateien erfolgen. Empfehlenswert ist eine kontinuierliche Überwachung. Dabei kann z.B. nach ungewöhnlichen vielen fehlgeschlagenen Anmeldungen, veralteten Berechtigungen, Einwahlen von Adminaccounts, ungewöhnlichen Einwahlorten/IP-Adressbereichen/User Agents oder Uhrzeiten gesucht werden. Als Reaktion kommen z.B. Sperren betroffener Adressbereiche, die Abschaltung angegriffener Schnittstellen oder stärkere Authentifizierungsmechanismen wie Mehr-Faktor-Authentifizierung in Betracht.

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
