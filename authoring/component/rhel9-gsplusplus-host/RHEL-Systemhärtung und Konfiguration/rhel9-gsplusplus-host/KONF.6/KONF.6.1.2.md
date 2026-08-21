---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
x-trestle-comp-def-rules-param-vals:
  RHEL-Systemhärtung und Konfiguration:
    - name: var_selinux_state
      values:
        - enforcing
      component-values:
        - enforcing
    - name: var_selinux_policy_name
      values:
        - targeted
      component-values:
        - targeted

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

Die Isolation von Anwendungen ermöglicht RHEL primär über SELinux im enforcing-Modus, der im Standard aktiviert ist und bereits ab Boot aktiv ist: Prozesse laufen in getrennten Domains mit minimalen Rechten auf Dateien, Capabilities und Netzwerk-Ports. Datei-POSIX-Rechte, Capability-Binding und systemd-Unit-Hardening (`ProtectSystem`, `PrivateTmp`) reduzieren zusätzlich unnötige Privilegien. Die notwendigen Berechtigungen/Anwendungsprofile werden bei Software, die aus Red Hat Repositories stammt typischerweise mitgeliefert und installiert. Zusätzlich ist es möglich Anwendungen auf RHEL containerisiert mittels `podman` auszuführen und sie so zusätzlich zu kapseln. Es ist ebenfalls möglich auf einem RHEL Host mittels `kvm` und `qemu` entsprechende virtuelle Maschinen zu erzeugen und Workloads so zu kapseln. Dies ist jedoch gerade für größere Umgebungen keine Lösung, die auch Hochverfügbarkeitsaspekte berücksichtigt. In solchen Fällen sollte auf Red Hat OpenShift-Virtualization oder 3rd Party Virtualisierungslösungen zurückgegriffen werden. Die feste Zuordnung von Containern sollte maximal zu einer Container-Host-Gruppe erfolgen um Verfügbarkeitsziele zu erreichen.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - selinux_state
  - selinux_policytype
  - selinux_not_disabled
  - grub2_enable_selinux
  - selinux_confinement_of_daemons

### Implementation Status: implemented

______________________________________________________________________
