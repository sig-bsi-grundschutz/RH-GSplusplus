---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.1 - \[Rollen und Berechtigungen\] Minimal erforderliche Berechtigungen für Anwendungen

## Control Statement

Konfiguration für IT-Systeme SOLLTE erforderliche Berechtigungen für Anwendungen einschränken.

## Control guidance

Ziel ist es, Angriffsflächen zu minimieren und unerwünschte Seiteneffekte zu vermeiden. Durch restriktive Rechtevergabe pro App lässt sich das Risiko für Zugriffe auf sensible Bereiche stark senken. Gleichzeitig trägt dieses Prinzip dazu bei, eine klare Trennung zwischen den einzelnen Systemkomponenten zu bewahren und unkontrollierte Wechselwirkungen zu verhindern. Beispiele sind Lese- und Schreibrechte für Verzeichnisse, insbesondere für Systemverzeichnisse, Berechtigungen zum Zugriff auf Sensoren oder Peripheriegeräte, sowie der Netzzugriff. Um die Umsetzung zu erleichtern können Berechtigungsprofile erstellt werden, die je nach Anwendungsklasse (z. B. Office, Multimedia, Tools) eine Basislinie an Privilegien definieren. Diese Profile können in einer zentralen Verwaltungssoftware (z. B. über Gruppenrichtlinien oder ein Mobile‑Device‑Management) hinterlegt und automatisch auf neue Installationen angewendet werden. Vor der Freigabe einer Softwareinstallation kann ein Reviewprozess etabliert werden, bei dem anhand von Funktionsdokumentationen geprüft wird, welche minimalen Rechte erforderlich sind. Darüber hinaus kann der Einsatz von Sandboxing- oder Virtualisierungstechnologien unterstützen, indem Anwendungen in einer isolierten Umgebung mit genau festgelegten Schnittstellen betrieben werden können. Tools zur Rechteanalyse (etwa zur Ermittlung der tatsächlich genutzten APIs und Dateizugriffe) können helfen, überflüssige Freigaben im Nachgang weiter einzuschränken.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Anwendungsberechtigungen beschränkt RHEL primär über SELinux im enforcing-Modus, der im Standard aktiviert ist und bereits ab Boot aktiv ist: Prozesse laufen in getrennten Domains mit minimalen Rechten auf Dateien, Capabilities und Netzwerk-Ports. Datei-POSIX-Rechte, Capability-Binding und systemd-Unit-Hardening (`ProtectSystem`, `PrivateTmp`) reduzieren zusätzlich unnötige Privilegien. Die notwendigen Berechtigungen/Anwendungsprofile werden bei Software, die aus Red Hat Repositories stammt typischerweise mitgeliefert und installiert. Zusätzlich ist es möglich Anwendungen auf RHEL containerisiert mittels `podman` auszuführen und sie so zusätzlich zu kapseln.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - selinux_state
  - selinux_policytype
  - selinux_not_disabled
  - grub2_enable_selinux
  - selinux_confinement_of_daemons

### Implementation Status: implemented

______________________________________________________________________
