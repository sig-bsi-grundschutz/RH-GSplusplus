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

RHEL stellt update-ca-trust und p11-kit zur Verwaltung von CA-/Zertifikatsvertrauen bereit. Entfernen oder Deaktivieren nicht benötigter Zertifikate obliegt der Institution.

### Implementation Status: partial

______________________________________________________________________
