---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.2 - \[Vertrauenswürdige Basisdienste\] DNS-Anbindung

## Control Statement

Konfiguration für IT-Systeme SOLLTE die vom System verwendeten DNS-Server autorisieren.

## Control guidance

Autorisierte DNS-Server sind hier Resolving-Server, die von der Institution autorisiert wurden. Dies können entweder DNS-Server der Institution selbst oder externe DNS-Server zuverlässiger Anbieter sein.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL legt die vom System verwendeten DNS-Resolver über NetworkManager oder direkt in `/etc/resolv.conf` fest: In Verbindungsprofilen (`nmcli`, Cockpit oder Kickstart/Ansible) trägt die Institution autorisierte Resolver — eigene oder externe Anbieter — als `ipv4.dns`/`ipv6.dns` ein; NetworkManager schreibt diese Einträge standardmäßig in `resolv.conf`. Für manuelle Pflege deaktiviert die Institution die DNS-Verarbeitung in NetworkManager (`dns=none` in `NetworkManager.conf`) und setzt autorisierte `nameserver`-Zeilen selbst. Für belastbare Auflösung sollten mindestens zwei Nameserver eingetragen sein; bei manueller `resolv.conf`-Pflege muss NetworkManager DNS nicht überschreiben. Welche IP-Adressen als autorisiert gelten und ob nur institutionelle Resolver erlaubt sind, definiert die Organisation in Baseline und Provisioning — eine automatische Allowlist-Prüfung gibt RHEL nicht.

Weitere Informationen: [Netzwerkkonfiguration und -verwaltung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index), [Manuelle Konfiguration von /etc/resolv.conf](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/manually-configuring-the-etc-resolv-conf-file_configuring-and-managing-networking)

### Implementation Status: partial

______________________________________________________________________
