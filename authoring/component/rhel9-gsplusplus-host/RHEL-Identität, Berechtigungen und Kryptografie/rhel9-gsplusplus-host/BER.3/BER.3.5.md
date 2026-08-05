---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.5 - \[Zugangskonten\] Identität-Zugangskonto

## Control Statement

Berechtigung SOLLTE ein Zugangskonto zu genau einer Identität zuweisen.

## Control guidance

Wenn ein Zugangskonto genau einer Identität zugewiesen ist erleichtert dies die Vergabe von Berechtigungen nach dem Need-to-know-Prinzip. Außerdem kann so bei einem Vorfall nachvollzogen werden, welche Person welche Befehle ausgeführt hat, z.B. mittels des Audit Logs. Anders herum können einer Identität auch mehrere Zugangskonten zugewiesen sein, z.B. ein normalen Nutzungskonto und ein Zugangskonto für die Systemadministration.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt technisch sicher, dass jedes Zugangskonto einen eindeutigen Eintrag mit eigener UID in `/etc/passwd` besitzt; openSCAP-Prüfungen können zusätzlich per Compliance-Scan erkennen, wenn zwei Konten versehentlich dieselbe UID teilen. Ob hinter einem einzelnen Kontonamen jedoch tatsächlich nur eine einzige natürliche Person steht – also ob ein Konto von mehreren Personen gemeinsam genutzt wird ("Shared Account") – lässt sich rein auf Betriebssystemebene nicht erzwingen, da RHEL Anmeldevorgänge nur anhand des präsentierten Credentials (Passwort, SSH-Schlüssel, Zertifikat) autorisiert und keine Kenntnis über die dahinterstehende reale Person hat. In zentral verwalteten Umgebungen unterstützt die Anbindung an Red Hat IdM oder Active Directory über SSSD dieses Ziel, indem Konten direkt aus individuellen Verzeichniseinträgen stammen statt lokal frei angelegt zu werden; dies reduziert das Risiko generischer, gemeinsam genutzter lokaler Konten, verhindert eine Passwortweitergabe technisch aber ebenfalls nicht. Die verbindliche Durchsetzung von "ein Konto, eine Identität" bleibt daher eine organisatorische Vorgabe (Namenskonvention, Verbot der Zugangsdatenweitergabe, Sensibilisierung), die durch keine der genannten Mechanismen technisch erzwungen wird.

### Implementation Status: planned

______________________________________________________________________
