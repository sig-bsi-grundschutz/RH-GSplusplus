---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.4 - \[Konfiguration von Systemen\] Deaktivierung nicht benötigter Systemfunktionen

## Control Statement

Konfiguration für IT-Systeme SOLLTE nicht benötigte Systemfunktionen deaktivieren.

## Control guidance

Die Deaktivierung von Funktionen, die für Betrieb oder aus Sicherheitssicht nicht benötigt werden, hilft, die Angriffsfläche und Fehlerkomplexität zu verringern, z.B. unnötige Identitäten, ggf. nicht benötigte Schnittstellen wie Bluetooth, nicht verwendete Netzprotokolle wie NTLMv1 Authentifizierung, schwache Verschlüsselungsalgorithmen wie TLS1.1, die Anzeige von Nachrichteninhalten auf dem Sperrbildschirm oder nicht benötigte System- oder Telemetriedienste. Relevant sind dabei sowohl Betriebssystem- als auch Firmwarefunktionen.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL erlaubt das gezielte Deaktivieren nicht benötigter Systemfunktionen auf mehreren Ebenen: Netzwerkdienste werden über systemd dauerhaft gestoppt und maskiert (`systemctl mask --now <dienst>.service`, ggf. inklusive zugehöriger `.socket`-Unit), sodass sie weder manuell noch als Abhängigkeit eines anderen Dienstes erneut starten können. Nicht benötigte Kernel-Module (Dateisysteme, veraltete Netzprotokolle) werden über modprobe-Blacklist-/`install /bin/false`-Konfiguration in `/etc/modprobe.d/` am Laden gehindert. Für eine systematische, wiederholbare Reduzierung stellt scap-security-guide gebündelte Profile (z. B. OSPP, ANSSI) bereit, die eine Vielzahl solcher Dienst- und Modul-Deaktivierungen sowie Firmware-/BIOS-nahe Einstellungen zusammenfassen und per OpenSCAP-Remediation ausrollen lassen. Welche konkreten Dienste, Schnittstellen (z. B. Bluetooth) und Protokolle als "nicht benötigt" gelten, hängt vom Einsatzzweck des Systems ab und ist eine Entscheidung der Institution.

### Rules:

  - service_avahi-daemon_disabled
  - kernel_module_cramfs_disabled

### Implementation Status: partial

______________________________________________________________________
