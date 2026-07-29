---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.4.1 - \[Konfiguration von Systemen\] Nicht benötigte Zertifikate

## Control Statement

Konfiguration für IT-Systeme SOLLTE nicht benötigte Zertifikate deaktivieren.

## Control guidance

Hierbei ist insbesondere an die vom Betriebssystem als vertrauenswürdig eingestuften Zertifizierungsstellen zu denken, wenn sie nicht länger benötigt werden. Verfügt das IT-System über keine Zertifikate, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL verwaltet als vertrauenswürdig eingestufte Zertifizierungsstellen zentral über `update-ca-trust`/p11-kit: Der systemweite Vertrauensspeicher wird aus `/etc/pki/ca-trust/source/anchors/` (institutseigene CAs) sowie den mitgelieferten Systemankern zusammengeführt (`update-ca-trust extract`), und einzelne CAs lassen sich gezielt als "nicht vertrauenswürdig" markieren (`trust anchor --store` bzw. Ablage in `/etc/pki/ca-trust/source/blacklist/`), ohne das gesamte Zertifikatsbündel zu ersetzen. Dadurch kann eine Institution nicht mehr benötigte CA-Zertifikate aus dem aktiven Vertrauenspfad entfernen, statt sie unverändert im System-Trust-Store zu belassen. Welche Zertifizierungsstellen tatsächlich benötigt werden und wann eine Deaktivierung angemessen ist, muss die Institution anhand ihrer Anwendungslandschaft festlegen; RHEL erzwingt keine automatische Bereinigung.

### Implementation Status: partial

______________________________________________________________________
