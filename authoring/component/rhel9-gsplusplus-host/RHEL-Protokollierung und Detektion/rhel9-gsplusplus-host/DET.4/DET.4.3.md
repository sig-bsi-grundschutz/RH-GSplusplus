---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.3 - \[Überwachung von Aktivitäten\] Überwachung der Angriffserkennung

## Control Statement

Detektion SOLLTE die Funktionsfähigkeit der automatisierten Angriffserkennung überwachen.

## Control guidance

Hierzu gehört insbesondere die Aktivierung oder Deaktivierung der Angriffserkennung, oder das Stoppen zugehöriger Dienste.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Funktionsfähigkeit der Host-Detektion hängt daran, dass die zugehörigen systemd-Units nicht still gestoppt werden: `auditd`, `aide`-Timer/`cron`, `fapolicyd`, USBGuard. CaC prüft den Enabled-Zustand dieser Dienste; ein bewusstes Maskieren oder Stoppen fällt in Journal und optional im Remote-Log auf. Eine eigene Überwachung „HIDS-Prozess lebt und liefert Daten“ (Heartbeat der Erkennung) ist Sache von Monitoring/SIEM.

Weitere Informationen: [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening).

### Implementation Status: partial

______________________________________________________________________
