---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.1.2 - \[Minimal erforderliche Berechtigungen für Anwendungen\] Isolierung von Anwendungen

## Control Statement

Konfiguration für IT-Systeme KANN die Isolierung von {{ insert: param, konf.6.1.2-prm1 }} aktivieren.

## Control guidance

Die Isolation von Anwendungen (auch Kapselung oder Application Sandboxing genannt) dient dazu, die Angriffsfläche eines Systems zu reduzieren und die Vertraulichkeit, Integrität sowie Verfügbarkeit kritischer Komponenten besser zu schützen. Durch eine klare Trennung der Anwendungs- und Systemprozesse und von deren Ressourcenzugriffen (Netzwerk, Datei‑ oder Geräte‑I/O) kann eine kompromittierte Applikation nicht unbegrenzt auf weitere Systemressourcen zugreifen, sondern ist auf genau definierte Schnittstellen beschränkt. Bestimmte Anwendungen meint hier, dass konkret festgelegt wird, welche Anwendungen konkret isoliert ausgeführt werden. Dies ermöglicht es, Fehlfunktionen oder Angriffe einzudämmen, Schadsoftware leichter zu erkennen und Verantwortlichkeiten einzelner Module transparent zu halten. Dies kann z.B. durch Containerisierung oder eine Microservice-Architektur, in der jede Komponente nur über REST- oder Message-Queue-Schnittstellen kommuniziert umgesetzt werden. Auch klassische Virtualisierung (Gastsysteme mit Hypervisor) oder Betriebssystemfunktionen wie SELinux/AppArmor‑Profile und chroot‑Jails zählen dazu, weil sie Applikationen auf genau festgelegte Ressourcen beschränken. Im Kontext der Containerisierung empfiehlt es sich ebenfalls eine feste Zuordnung von Containern zu Container-Hosts vorzunehmen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL trennt Anwendungen technisch über Linux-Namespaces (PID, Mount, UTS, Netzwerk, User) und cgroups, die systemd-Slices und die Container-Runtime Podman nutzen. SELinux weist Prozessen unterschiedliche Security Domains zu und unterbindet querschnittliche Zugriffe. Systemd-Unit-Optionen (`PrivateDevices`, `RestrictNamespaces`) können weitere Grenzen setzen. Welche Isolationsstufe (Prozess, Container, VM) pro Workload gilt, definiert die Institution.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index).

### Implementation Status: partial

______________________________________________________________________
