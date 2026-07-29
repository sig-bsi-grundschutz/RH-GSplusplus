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

RHEL erlaubt das gezielte Deaktivieren nicht benötigter Systemfunktionen auf mehreren Ebenen: Netzwerkdienste werden über systemd dauerhaft gestoppt und maskiert (`systemctl mask --now <dienst>.service`, ggf. inklusive zugehöriger `.socket`-Unit), sodass sie weder manuell noch als Abhängigkeit eines anderen Dienstes erneut starten können. Nicht benötigte Kernel-Module (Dateisysteme, veraltete Netzprotokolle) werden über modprobe-Blacklist-/`install /bin/false`-Konfiguration in `/etc/modprobe.d/` am Laden gehindert. Welche konkreten Dienste, Schnittstellen (z. B. Bluetooth) und Protokolle als "nicht benötigt" gelten, hängt vom Einsatzzweck des Systems ab und ist eine Entscheidung der Institution.

### Rules:
      - service_avahi-daemon_disabled
      - service_abrtd_disabled
      - service_kdump_disabled
      - service_ntpdate_disabled
      - service_oddjobd_disabled
      - service_qpidd_disabled
      - service_rdisc_disabled
      - service_rhnsd_disabled
      - service_atd_disabled
      - service_dhcpd_disabled
      - service_named_disabled
      - service_dnsmasq_disabled
      - service_vsftpd_disabled
      - service_httpd_disabled
      - service_dovecot_disabled
      - service_slapd_disabled
      - service_rpcbind_disabled
      - service_nfs_disabled
      - service_xinetd_disabled
      - service_ypserv_disabled
      - service_rexec_disabled
      - service_rlogin_disabled
      - service_rsyncd_disabled
      - service_telnet_disabled
      - service_cups_disabled
      - service_squid_disabled
      - service_smb_disabled
      - service_snmpd_disabled
      - service_debug-shell_disabled
      - service_bluetooth_disabled
      - service_autofs_disabled
      - mask_nonessential_services

### Implementation Status: partial

______________________________________________________________________
