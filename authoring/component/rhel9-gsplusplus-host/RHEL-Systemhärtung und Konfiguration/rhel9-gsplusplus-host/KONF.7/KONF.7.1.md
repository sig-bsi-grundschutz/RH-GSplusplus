---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.1 - \[Schutz vor Schadcode\] Echtzeitscanner

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine automatische Prüfung auf Schadcode bei Installation oder Öffnung von Dateien aktivieren.

## Control guidance

Schadcode kann sich sowohl auf lokalen Speichermedien, als auch auf Netzlaufwerken oder Wechseldatenträgern befinden. Für Netzlaufwerke kann die Anforderung auch umgesetzt werden, indem Dateien bei der Speicherung auf dem zentralen System auf Schadcode geprüft werden. Die Anwendung zur Schadcodeprüfung kann z.B. auch als EDR, XDR oder IDS bezeichnet werden. Moderne Systeme zur Erkennung von Schadcode verwenden eine Kombination aus Virensignaturen, Heuristiken, als auch Anomalieerkennung. Falls das System die Installation von Anwendungen nicht unterstützt, so ist dieser Teilschritt entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Echtzeit-Prüfung beim Öffnen oder Installieren wie klassische AV-Scanner liefert RHEL nicht als supported Product. Stattdessen verifiziert `dnf`/`rpm` bei Paketinstallation GPG-Signaturen aus konfigurierten Repositories (`gpgcheck=1`, Red-Hat-GPG-Schlüssel). Build-Pipelines (Image Builder, Kickstart) können nur signierte oder vorab geprüfte Artefakte einbringen. Real-time-Malware-Scan erfordert unsupported Drittanbieter (z. B. EPEL ClamAV) — die institutionelle Alternative ist Paketsignatur und gehärtete Softwarequellen.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: alternative

______________________________________________________________________
