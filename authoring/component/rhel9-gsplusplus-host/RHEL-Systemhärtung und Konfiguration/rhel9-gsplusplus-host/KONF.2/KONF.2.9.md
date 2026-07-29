---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.9 - \[Konfiguration von Systemen\] Abgesicherter und authentisierter Bootprozess

## Control Statement

Konfiguration für IT-Systeme KANN einen abgesicherten und authentisierten Bootprozess aktivieren.

## Control guidance

Dies empfiehlt sich für eingebettete Systeme (Embedded Systems), indem z.B. der Bootloader die Integrität des Betriebssystems überprüft und es nur dann lädt, wenn es als korrekt eingestuft wurde. Ebenso empfiehlt es sich ein mehrstufiges Boot-Konzept mit kryptographisch sicherer Überprüfung der Einzelschritte zu realisieren, sichere Hardware-Vertrauensanker zu verwenden, bei ARM & UEFI-basierten Systemem jeweils (ARM) Secure Boot zu nutzen.

______________________________________________________________________

## What is the solution and how is it implemented?

Auf UEFI-Systemen unterstützt RHEL einen mehrstufig authentisierten Bootprozess: Der Bootloader `shim` sowie GRUB2 und der Kernel sind mit Red-Hat-Schlüsseln signiert und werden von der UEFI-Firmware anhand der Microsoft-UEFI-CA- bzw. Red-Hat-Schlüssel in der `db`-Zertifikatsdatenbank verifiziert, bevor sie ausgeführt werden. Für zusätzliche, selbst signierte Kernel oder Fremd-Kernelmodule (z. B. DKMS-Treiber) steht die Machine-Owner-Key-Infrastruktur (`mokutil`) bereit, mit der ein eigenes Schlüsselpaar in die Firmware-Vertrauensliste eingebracht wird, ohne die UEFI-`db` direkt zu verändern. Der aktuelle Status lässt sich mit `mokutil --sb-state` prüfen.

### Rules:

  - secure_boot_enabled

### Implementation Status: planned

______________________________________________________________________
