---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.21 - \[Zugangskonten\] Dienstekonten

## Control Statement

Berechtigung für Hostsysteme SOLLTE eine automatische Verwaltung der Zugangsdaten von Dienste-Konten aktivieren.

## Control guidance

Eine automatische Verwaltung der Zugangsdaten von Dienste-Konten bezeichnet in diesem Kontext die technische Fähigkeit, Passwörter, Schlüssel oder Tokens solcher Konten – im Englischen häufig als service accounts oder machine identities bezeichnet – durch spezialisierte Systeme ohne manuelles Eingreifen zu erzeugen, zu speichern, regelmäßig zu erneuern und kontrolliert zu verteilen. Zugangsdaten sind hierbei sämtliche Authentifizierungsinformationen, die einem Dienst ermöglichen, auf Ressourcen anderer Systeme zuzugreifen, beispielsweise API-Schlüssel, SSH-Keys oder Anmeldedaten für Datenbanken. Dienste-Konten werden meist von Applikationen, Hintergrunddiensten oder Automatisierungsprozessen genutzt und unterscheiden sich von personenbezogenen Benutzerkonten dadurch, dass sie keinem Individuum zugeordnet sind, sondern einem technischen Zweck dienen. Erfolgt bei Zugangskonten für automatisierte Dienste eine automatische Rotation von Passwörtern oder Anmeldezertifikaten, so werden statische Passwörter, die Ablage von Zugangsdaten auf Netzlaufwerken oder plötzliche Fehlfunktionen durch Zertifikatsablauf vermieden. Ihre automatische Verwaltung kann durch zentrale Passworttresore (password vaults), Identitätsmanagementsysteme (Identity and Access Management, IAM) oder Secret-Management-Lösungen realisiert werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

 Für Kerberos-basierte Dienste verwaltet SSSD im Zusammenspiel mit IdM die zugehörigen Keytabs zentral im Verzeichnis; eine Rotation des Dienstprinzipal-Schlüssels (z.B. via `ipa-getkeytab`) erfolgt IdM-seitig, sodass keine dauerhaften Klartext-Anmeldedaten lokal auf dem Host vorgehalten werden müssen. Für generische Zugangsdaten wie API-Schlüssel oder Datenbank-Anmeldedaten stellt RHEL selbst jedoch keinen Passworttresor bereit. Hilfsweise kann über Red Hat Ansible Automation Platform mittles `ansible-vault` eine entsprechend verschlüsselte Speicherung von Passwörtern, sowie die automatisierte Verteilung und Rotation erfolgen. Die Integration mit vollwertigen Secret-Management-Lösungen wie HashiCorp Vault ist technisch möglich und empfehlenswert.


### Implementation Status: alternative

______________________________________________________________________
