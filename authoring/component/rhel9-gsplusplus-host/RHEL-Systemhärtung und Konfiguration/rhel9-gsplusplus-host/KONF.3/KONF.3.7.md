---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.3.7 - \[Physischer Schutz\] Einschränkung angeschlossener Peripherie

## Control Statement

Konfiguration für IT-Systeme SOLLTE angeschlossene Peripherie einschränken.

## Control guidance

Peripherie bezeichnet angeschlossene Geräte, die über Schnittstellen wie USB, Bluetooth oder andere Ports mit dem IT-System kommunizieren. Gemeint sind sowohl physische Peripheriegeräte wie Drucker, USB-Sticks oder Netzanbindungen, als auch die Installation virtueller Peripherie z.B. virtuelle Druckertreiber. Einschränkung bedeutet hierbei, dass die Nutzung von Peripheriegeräten verhindert wird, die nicht von der Institution autorisiert wurden, abhängig vom Einsatzzweck des Systems. Der Sinn und Zweck dieser Regelung liegt darin, Angriffsflächen zu verringern und das Einschleusen oder Abfließen von Daten zu erschweren. So könnte ein unkontrollierter Anschluss externer USB-Sticks Schadsoftware einschleusen oder sensible Daten unbemerkt kopieren, während eine restriktive Konfiguration unautorisierte Datenabflüsse wirksam verhindern kann.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Unautorisierte USB- und andere Peripheriegeräte kann RHEL über USBGuard einschränken: Der `usbguard`-Dienst wertet eine Policy in `/etc/usbguard/rules.conf` aus und blockiert Geräte, die nicht explizit erlaubt sind; Tastatur und Maus lassen sich über eigene Allow-Regeln freischalten. Alternativ oder ergänzend kann der Kernel-Treiber `usb-storage` per modprobe-Blacklist deaktiviert werden, sodass USB-Massenspeicher nicht angebunden werden. Bluetooth-Geräte können über `rfkill` oder Dienstkonfiguration eingeschränkt werden. Welche Geräteklassen für einen Einsatzzweck zugelassen sind und wie Policy-Änderungen freigegeben werden, legt die Institution fest — RHEL liefert Mechanismen, keine Allowlist.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
