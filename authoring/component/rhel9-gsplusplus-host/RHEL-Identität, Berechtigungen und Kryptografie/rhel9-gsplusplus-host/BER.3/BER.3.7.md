---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.7 - \[Zugangskonten\] Single-Sign-On

## Control Statement

Berechtigung für Anwendungen SOLLTE die Anmeldung über einen zentralen Identitätsprovider aktivieren.

## Control guidance

Bei Single Sign-on authentifizieren sich Nutzende bei einem zentralen Identity Provider, der auch die Berechtigungen zur Nutzung der Anwendung prüft. Bei erfolgreicher Authentifizierung und passenden Berechtigungen wird für die Sitzung ein Token ausgestellt, das den Zugang zur Anwendung ermöglicht. Da Nutzende durch Single-Sign-On weniger Anmeldeinformationen benötigen, wird es leichter, sich komplexe Passwörter zu merken oder zentrale gepflegte Schutzmaßnahmen, wie eine Mehr-Faktor-Authentifizierung oder Überwachung von Anmeldeinformationen, auch auf die Anwendung anzuwenden. Zudem erschwert Single-Sign-On auch Phishing-Angriffe, da Anmeldeinformationen nur noch an zentraler Stelle und nicht mehr verstreut in einzelne Anwendungen oder Webseiten abgefragt werden. Andererseits ist bei der Kompromittierung des Single-Sign-On-Logins auch die Authentifizierung an der Anwendung kompromittiert und die Verfügbarkeit der Anwendung hängt auch von der Verfügbarkeit des zentralen Logins ab. Dies kann unter Windows durch Nutzung eines Windows Server Domain Controllers und unter Linux durch Samba mit aktiviertem Heimdal Kerberos Key Distribution Center (KDC) umgesetzt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL bindet Anwendungen über den Security System Services Daemon (SSSD) an einen zentralen Identitätsprovider wie Red Hat Identity Management, Active Directory oder einen LDAP-Verzeichnisdienst an; SSSD stellt die dort verwalteten Identitäten und Berechtigungen über NSS und PAM lokal bereit und cached Anmeldeinformationen für Offline-Zugriff. Nach erfolgreicher Kerberos-Authentifizierung erhält die Sitzung ein Ticket-Granting-Ticket, das für nachfolgende PAM- oder GSSAPI-fähige Dienste (z. B. SSH, sudo, per Kerberos abgesicherte Webanwendungen) automatisch wiederverwendet wird, sodass keine erneute Passworteingabe nötig ist. Das Werkzeug `authselect` konfiguriert den PAM-/NSS-Stack konsistent für das gewählte Profil statt die Authentifizierungskette manuell zusammenzusetzen, und `realmd` kann den Host automatisiert einer IdM-Domäne beitreten lassen. Diese Anbindung deckt lokale sowie PAM- oder Kerberos-fähige Anwendungen ab; eigenständige webbasierte SSO-Protokolle einzelner Anwendungen (z. B. SAML, OIDC) sowie Aufbau und Betrieb des zentralen Identitätsproviders selbst — etwa eines Windows Server Domain Controllers oder eines Samba-AD mit Heimdal-KDC — liegen außerhalb der Hostkonfiguration und bleiben organisatorische bzw. anwendungsseitige Aufgaben.

Weitere Informationen: [Einführung in die Systemauthentifizierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/introduction-to-system-authentication_configuring-authentication-and-authorization-in-rhel)

### Implementation Status: partial

______________________________________________________________________
