---
x-trestle-param-values:
  det.3.4-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.4 - \[Protokollierung\] Speicherkapazität

## Control Statement

Detektion SOLLTE den für die Protokollierung zur Verfügung stehenden Speicherplatz {{ insert: param, det.3.4-prm1 }} überprüfen.

## Control guidance

Diese Vorschrift zielt darauf ab, die Verfügbarkeit der Protokolldaten sicherzustellen. Das ist essenziell, da eine unterbrochene oder lückenhafte Aufzeichnung die Früherkennung von Angriffen unmöglich machen könnte, was dazu führen könnte, dass kritische forensische Beweise für eine Untersuchung fehlen. Die Umsetzung dieser Anforderung kann auf verschiedene Arten erfolgen. Es könnte ein Skript oder ein automatisierter Dienst eingesetzt werden, der den Füllstand des Speicherplatzes in regelmäßigen Abständen, zum Beispiel alle 15 Minuten oder einmal pro Stunde, prüft. Alternativ kann eine Überprüfung bei einem definierten Schwellenwert durchgeführt werden, etwa wenn 80 % oder 90 % des zugewiesenen Speicherplatzes belegt sind. Zur Behebung könnte bei Kapazitätsengpässen eine automatische Archivierung älterer Protokolldaten auf einem separaten, kostengünstigeren Speicher gestartet werden, um den primären Speicher zu entlasten. Es kann aber auch eine Rotationsstrategie für Log-Dateien konfiguriert werden, die bei Erreichen einer bestimmten Größe oder eines Alters die ältesten Dateien löscht oder archiviert.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL dokumentiert restriktive Berechtigungen auf Audit-Protokolldateien und optionale unveränderliche Audit-Regeln zum Schutz vor Manipulation; Weiterleitung an einen separaten Log-Host oder SIEM konfiguriert die Institution.

### Rules:

  - file_permissions_var_log_audit
  - audit_rules_immutable

### Implementation Status: partial

______________________________________________________________________
