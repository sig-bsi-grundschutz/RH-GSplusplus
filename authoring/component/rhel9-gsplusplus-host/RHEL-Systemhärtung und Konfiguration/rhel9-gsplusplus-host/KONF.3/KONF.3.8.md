---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.3.8 - \[Physischer Schutz\] Einschränkung von Wechselmedien

## Control Statement

Konfiguration für IT-Systeme SOLLTE das automatische Einbinden von Wechselmedien einschränken.

## Control guidance

Funktionen, die Wechselmedien automatisch einbinden und Inhalte darauf öffnen oder ausführen könnten zur unkontrollierter Verbreitung von Schadcode beitragen. Betrifft z.B. CD/DVD-Laufwerke, Bandlaufwerke oder USB-Sticks. Dies Kann umgesetzt werden, indem die Einbindung in das Betriebssystem durch spezielle Managementanwendungen blockiert wird oder auch durch systemeigene Sicherheitsfunktionen, z.B. indem alle Dateien auf Wechselmedien als nicht ausführbar markiert sind (Mount-Option „noexec“). Verfügt das IT-System über keine Anschlussmöglichkeit für Wechsellaufwerke, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Das automatische Einbinden von Wechselmedien unterbindet RHEL auf mehreren Ebenen: In GNOME-Arbeitsplätzen deaktiviert dconf (`automount` und `automount-open` auf `false`) das automatische Mounten und Öffnen eingesteckter Medien. Server ohne GUI nutzen keine Desktop-Automount-Funktion; Wechselmedien können in `/etc/fstab` mit `noauto` belassen oder global über den `usb-storage`-Treiber blockiert werden. Für eingebundene removable Partitionen empfehlen sich Mount-Optionen wie `noexec`, `nosuid` und `nodev`, damit Inhalte nicht ausgeführt werden. Institutionelle Freigabe einzelner Medientypen und Ausnahmen für Backup-Geräte bleiben organisatorisch.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
