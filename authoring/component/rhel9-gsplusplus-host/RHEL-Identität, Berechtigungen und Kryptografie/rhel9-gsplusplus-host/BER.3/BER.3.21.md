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

RHEL bietet native Bausteine für Teile der automatischen Zugangsdatenverwaltung von Dienste-Konten, jedoch keine eigenständige Gesamtlösung: Ist der Host in Red Hat IdM eingebunden, überwacht der `certmonger`-Dienst die Gültigkeit von Dienstzertifikaten und stößt bei einer integrierten IdM-CA automatisch — üblicherweise 28 Tage vor Ablauf — die Erneuerung an, ohne dass ein manueller Eingriff nötig ist. Für Kerberos-basierte Dienste verwaltet SSSD im Zusammenspiel mit IdM die zugehörigen Keytabs zentral im Verzeichnis; eine Rotation des Dienstprinzipal-Schlüssels (z.B. via `ipa-getkeytab`) erfolgt serverseitig, sodass keine dauerhaften Klartext-Anmeldedaten lokal vorgehalten werden müssen. Für generische Zugangsdaten wie API-Schlüssel oder Datenbank-Anmeldedaten stellt RHEL selbst jedoch keinen Passworttresor bereit; hierfür ist die Anbindung an ein externes Secret-Management-System (z.B. HashiCorp Vault, CyberArk) oder ein zentrales IAM nötig, das der Host lediglich konsumiert. Diese externe Integration ist aktuell durch keine CaC-Regel abgedeckt, da sie keine lokal prüfbare Baseline-Einstellung, sondern eine Architekturentscheidung auf Verzeichnis-/IAM-Ebene darstellt.

Weitere Informationen: [Zertifikate in IdM verwalten – Erhalten eines IdM-Zertifikats für einen Dienst mit certmonger](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_certificates_in_idm/using-certmonger_recovering-from-expired-system-certificates)

### Implementation Status: partial

______________________________________________________________________
