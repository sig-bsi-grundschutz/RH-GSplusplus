---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.7 - \[Schutz vor Schadcode\] Regelmäßiger Funktionstest

## Control Statement

Konfiguration für IT-Systeme KANN die Funktionsfähigkeit des Schadcodeschutzes {{ insert: param, konf.7.7-prm1 }} überprüfen.

## Control guidance

Die Funktionsfähigkeit des Schadcodeschutzes beschreibt den operativen Zustand der eingesetzten Schutzmechanismen (engl. Malware Protection, oft auch Antivirus oder Endpoint Detection and Response, kurz EDR), der über die reine Installation der Software hinausgeht. Sie umfasst die korrekte Ausführung der Schutzdienste, die Aktualität der Erkennungssignaturen und Verhaltensregeln sowie die Fähigkeit, auf Bedrohungen aktiv zu reagieren und diese zu protokollieren. Eine regelmäßige Überprüfung dieser Funktionsfähigkeit kann die Institution vor unbemerkten Sicherheitslücken schützen. Ein deaktivierter oder fehlerhafter Schutzmechanismus könnte beispielsweise dazu führen, dass Ransomware unbemerkt Daten verschlüsselt oder ein Trojaner Anmeldeinformationen abgreift, obwohl eine Schutzsoftware installiert ist. Durch die proaktive Verifikation kann hingegen sichergestellt werden, dass diese wesentliche Verteidigungslinie durchgehend intakt ist und auf Angriffsversuche reagieren kann. Zur konkreten Umsetzung kann die Institution auf verschiedene, sich ergänzende Maßnahmen zurückgreifen. Eine zentrale Verwaltungskonsole der eingesetzten Schutzlösung kann genutzt werden, um den Status aller angebundenen Systeme automatisiert zu überwachen und Alarme auszulösen, wenn Systeme sich nicht mehr melden, veraltete Signaturen aufweisen oder Dienste beendet wurden. Ergänzend kann die tatsächliche Erkennungsleistung proaktiv durch den Einsatz einer standardisierten Testdatei wie dem EICAR-Teststring verifiziert werden; dieser kann automatisiert auf den Systemen platziert werden, um zu prüfen, ob der Schadcodeschutz wie erwartet anschlägt und eine Meldung generiert. Auf Systemen ohne zentrale Anbindung kann die Funktionsfähigkeit mittels Skripten überprüft werden, die lokal den Dienststatus und das Alter der Signaturdateien auslesen und in einer überwachten Logdatei dokumentieren.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Funktionsfähigkeit des Schadcodeschutzes kann institutionell durch periodische AIDE-Läufe, Testinstallation signierter Pakete oder Monitoring auf fehlgeschlagene `dnf`-Verifikationen geprüft werden. ClamAV-Tests erfordern Drittanbieter — RHEL bietet keinen eingebauten Self-Test für Malware-Engines. Integritäts- und Paketprüf-Workflows sind die technische Basis für Funktionstests.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
