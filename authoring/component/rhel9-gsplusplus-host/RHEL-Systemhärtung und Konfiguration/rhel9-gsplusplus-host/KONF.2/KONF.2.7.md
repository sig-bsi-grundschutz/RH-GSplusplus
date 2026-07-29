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

RHEL selbst ist quelloffen (Upstream in Fedora/CentOS Stream) und bringt bereits eine Reihe lokal betreibbarer, herstellerunabhängiger Werkzeuge mit, die keine externe Cloud-Anbindung benötigen: Ansible für Konfigurationsmanagement, OpenSCAP/scap-security-guide für Compliance-Scans, `dnf`/Reposync und Satellite/Pulp für selbstgehostete Paket-Repositories, sowie Podman für containerisierten Betrieb einzelner Werkzeuge ohne zentralen Daemon. Dadurch lässt sich eine Werkzeugkette für Build, Patch-Management und Monitoring vollständig innerhalb der eigenen Infrastruktur betreiben, ohne dass ein Ausfall oder eine Lizenzänderung eines externen Cloud-Anbieters die Handlungsfähigkeit einschränkt. Welche konkreten Werkzeuge als "souverän" im Sinne der Anforderung eingestuft, freigegeben und in einem internen, geprüften Repository bereitgestellt werden, entscheidet die Institution.

### Implementation Status: partial

______________________________________________________________________
