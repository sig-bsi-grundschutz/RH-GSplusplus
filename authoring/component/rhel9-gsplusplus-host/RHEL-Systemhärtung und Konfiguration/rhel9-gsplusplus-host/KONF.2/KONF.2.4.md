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

Nicht benötigte Dienste, Kernel-Module und Schnittstellen können über systemd, modprobe-Konfiguration und scap-security-guide-Baselines reduziert werden; die Auswahl obliegt der Institution.

### Rules:

  - service_avahi-daemon_disabled
  - kernel_module_cramfs_disabled

### Implementation Status: partial

______________________________________________________________________
