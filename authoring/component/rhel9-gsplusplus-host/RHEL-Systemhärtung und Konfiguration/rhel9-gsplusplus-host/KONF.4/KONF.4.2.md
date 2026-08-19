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

RHEL konfiguriert die vom System verwendeten DNS-Resolver im Standard via NetworkManager. In Verbindungsprofilen (`nmcli`) trägt die Institution autorisierte Resolver — eigene oder externe Anbieter — als `ipv4.dns`/`ipv6.dns` ein. Diese Informationen werden im Optimalfall automatisiert via DHCP-Server verteilt. NetworkManager schreibt diese Einträge standardmäßig in `resolv.conf`. Eine manuelle Konfiguration der DNS-Server in `resolv.conf` ist ebenfalls möglich. Für kontinuierliche Auflösung auch beim Ausfall eines DNS-Servers sollten mindestens zwei Nameserver eingetragen sein. Welche IP-Adressen als autorisiert gelten und ob nur institutionelle Resolver erlaubt sind, definiert die Institution in Baseline und Provisioning — eine automatische Allowlist-Prüfung gibt es in RHEL nicht.

Weitere Informationen: [Netzwerkkonfiguration und -verwaltung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index), [Manuelle Konfiguration von /etc/resolv.conf](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/manually-configuring-the-etc-resolv-conf-file_configuring-and-managing-networking)

### Rules:

  - network_configure_name_resolution
  - networkmanager_dns_mode

### Implementation Status: implemented

______________________________________________________________________
