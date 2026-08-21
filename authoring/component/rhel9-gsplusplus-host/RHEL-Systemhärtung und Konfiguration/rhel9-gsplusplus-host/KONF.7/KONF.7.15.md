---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.15 - \[Schutz vor Schadcode\] Lokale Firewall

## Control Statement

Konfiguration für IT-Systeme SOLLTE ein- und ausgehende Netzverbindungen einschränken.

## Control guidance

Eine lokale Firewall ist eine Anwendung, welche nur die zum Betrieb und zur Wartung des IT-Systems notwendigen ein- und ausgehenden Verbindungen zulässt. Bringt das Betriebssystem diese Funktionalität bereits vom Werkszustand her mit, so ist die Anforderung ebenfalls erfüllt, wenn sie entsprechend konfiguriert ist. Zweckmäßig ist hierbei ein Allowlist-Ansatz, der die gewünschte Verbindung möglichst genau beschreibt (z.B. anhand Server-IP und Port).

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt mit `firewalld` (nftables-Backend) eine hostbasierte Paketfilterung bereit. Zonen definieren Allowlist-Regeln für eingehenden und ausgehenden Verkehr und die Drop-Zone lehnt eingehende Pakete ab, sofern sie nicht explizit freigegeben sind. Per `firewall-cmd` können Zonen, Services und Ports festgelegt werden. Diese sollten wie folgt konfiguriert sein: Default-Zone: Drop (damit default-deny gilt), für jede notwendige eingehende Verbindung sollte via `firewall-cmd` explizit der Port freigegeben werden.

Weitere Informationen: [Firewalls und Paketfilter konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_firewalls_and_packet_filters/index).

### Rules:

  - configured_firewalld_default_deny
  - set_firewalld_default_zone
  - package_firewalld_installed
  - service_firewalld_enabled

### Implementation Status: implemented

______________________________________________________________________
