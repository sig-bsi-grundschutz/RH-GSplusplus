---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.1 - \[Vertrauenswürdige Basisdienste\] Anbindung an Verzeichnisdienst

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Anbindung an einen Verzeichnisdienst aktivieren.

## Control guidance

Anbindung meint hier die Authentifizierung und Autorisierungsprüfung von Zugangskonten über einen Verzeichnisdient (häufig auch als Directory Service bezeichnet). Dies ermöglicht die zentrale Verwaltung von Identitäten und deren Berechtigungen. Dies bedeutet, dass Zugriffsrechte für alle angebundenen Systeme zentral verwaltet und bei Bedarf umgehend angepasst werden können, was die Einhaltung des Prinzips der geringsten Rechte (Principle of Least Privilege) unterstützt. Ein häufiger Ansatz zur technischen Umsetzung ist die Verwendung von Protokollen wie LDAP (Lightweight Directory Access Protocol) oder der Einsatz von Single Sign-On (SSO) Lösungen, die eine einmalige Authentifizierung des Nutzers für mehrere Systeme ermöglichen. Institutionen können dabei die Anbindung neuer Systeme durch Automatisierung im Rahmen des Provisioning-Prozesses sicherstellen, um menschliche Fehler zu reduzieren. Beispielsweise könnte ein Standard-Skript bei der Installation eines neuen Servers dessen automatische Anbindung an den Verzeichnisdient veranlassen. In Windows Betriebssystemen erfolgt die Konfiguration des Betriebssystem über entsprechende Gruppenrichtlinien (Group Policy Object) aus dem Active Directory.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL bindet Verzeichnisdienste (Red Hat IdM, Active Directory oder generisches LDAP) über SSSD, `authselect` und optional `realmd` bzw. `ipa-client-install` an: NSS/PAM liefern zentrale Identitäten und Autorisierung statt ausschließlich lokaler `/etc/passwd`-Konten. ComplianceAsCode-Regeln prüfen Installation und Aktivierung von SSSD sowie die PAM-Integration; die konkrete Domain-Anbindung, SSO-Föderation und automatisiertes Provisioning (z. B. Kickstart oder Ansible während der Systeminstallation) legt die Institution fest. Zentrale Berechtigungsverwaltung, Least-Privilege-Umsetzung und der in der Anleitung genannte Windows-GPO-Ansatz liegen außerhalb des einzelnen Hosts.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index)

### Implementation Status: partial

______________________________________________________________________
