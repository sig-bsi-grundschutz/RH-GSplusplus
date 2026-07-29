---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.7 - \[Konfiguration von Systemen\] Souveräne Werkzeuge

## Control Statement

Konfiguration für IT-Systeme KANN Souveräne Werkzeuge installieren.

## Control guidance

„Souveräne Werkzeuge“ sind Anwendungen, Systeme und physische Werkzeuge, die technisch, rechtlich und organisatorisch unabhängig von externen Herstellern, Cloud-Anbietern oder staatlicher Einflussnahme betrieben werden können. Das umfasst vor allem Lösungen, die lokal kontrollierbar und ohne zwingende Abhängigkeit zu externen Plattformen nutzbar sind. Der Sinn der Vorschrift liegt darin, die Handlungsfähigkeit und Sicherheit der Institution zu stärken: Ein rein cloudbasierter Konfigurationsdienst könnte durch einen plötzlichen Ausfall, eine staatlich erzwungene Sperrung oder durch nachträglich geänderte Lizenzbedingungen die Betriebsfähigkeit gefährden. Die Nutzung souveräner Werkzeuge kann dagegen die Verfügbarkeit kritischer Systeme erhöhen, die Datenhoheit bewahren und Manipulationsmöglichkeiten von Dritten minimieren. Souveräne Konfigurationssysteme machen unabhängig vor Ausfällen, Datenschutzverletzungen oder einseitigen Änderungen der Nutzungsbedingungen durch externe Dienstleister. Eine Institution kann diese Anforderung beispielsweise so umsetzen: (1) Es kann auf quelloffene Konfigurations-Frameworks zurückgegriffen werden, die lokal installiert und betrieben werden. (2) Virtualisierte oder containerisierte Varianten dieser Werkzeuge werden in der eigenen Infrastruktur betrieben, sodass keine unkontrollierten externen Abhängigkeiten entstehen. (3) Ergänzend kann ein internes Repository für Konfigurationsmodule eingerichtet werden, um eine vertrauenswürdige, geprüfte und nachvollziehbare Quellenbasis sicherzustellen.

______________________________________________________________________

## What is the solution and how is it implemented?

Als Open-Source-Basisplattform kann RHEL souveräne Werkzeugketten tragen (Build, Patch, Monitoring). Auswahl, Zulassung und Betrieb solcher Werkzeuge obliegen der Institution.

### Implementation Status: partial

______________________________________________________________________
