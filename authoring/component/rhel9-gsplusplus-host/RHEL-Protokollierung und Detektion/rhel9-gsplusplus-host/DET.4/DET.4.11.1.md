---
x-trestle-param-values:
  det.4.11.1-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.11.1 - \[Überwachung von Aktivitäten\] Authentifizierungsversuche an externen Schnittstellen

## Control Statement

Detektion für Externe Netzanschlüsse KANN Authentifizierungsversuche auf unauthorisierte Verbindungen {{ insert: param, det.4.11.1-prm1 }} überprüfen.

## Control guidance

Ohne solche Überprüfungen könnte ein Angreifer unbemerkt wiederholt Zugangsdaten erraten (Brute-Force- oder Wörterbuchangriffe) oder unautorisierte Geräte an Schnittstellen wie VPN-Gateways, Firewalls oder externen Modems anbinden. Auch ein unbemerktes Einschleusen von Schadsoftware über offene Remote-Desktop- oder SSH-Verbindungen könnte langfristig unentdeckt bleiben. Eine kontinuierliche Auswertung von Anmeldeversuchen kann dagegen Auffälligkeiten wie ungewöhnlich viele Fehlversuche, Anmeldungen aus geografisch atypischen Regionen oder Verbindungsaufbau außerhalb üblicher Betriebszeiten aufzeigen und so eine wirksame Schutzwirkung entfalten. Als Frist können Intervalle wie "täglich", "wöchentlich" oder "in Echtzeit" je nach Kritikalität des Anschlusses angemessen sein. Verbindungen sind hier unautorisiert, wenn Anzeichen vorliegen, dass sie von unautorisierten Personen oder von unautorisierten Systemen stammen. Die Überprüfung kann manuell oder durch automatische Analyse von Logdateien erfolgen. Empfehlenswert ist eine kontinuierliche Überwachung. Dabei kann z.B. nach ungewöhnlichen vielen fehlgeschlagenen Anmeldungen, veralteten Berechtigungen, Einwahlen von Adminaccounts, ungewöhnlichen Einwahlorten/IP-Adressbereichen/User Agents oder Uhrzeiten gesucht werden. Als Reaktion kommen z.B. Sperren betroffener Adressbereiche, die Abschaltung angegriffener Schnittstellen oder stärkere Authentifizierungsmechanismen wie Mehr-Faktor-Authentifizierung in Betracht.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

SSH- und lokale Anmeldeversuche landen in Audit (`audit_rules_login_events*`) und in `/var/log/secure` bzw. dem Journal; `pam_faillock` sperrt nach Fehlversuchen. Auswertung auf ungewöhnliche Quellen, Zeiten oder Admin-Logins ist Loganalyse (SIEM), nicht eine Host-Regel. fail2ban/sshguard sind nicht Teil der RHEL-Basisprofile. VPN-Gateways und externe Modems liegen außerhalb dieses Host-Scopes.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
