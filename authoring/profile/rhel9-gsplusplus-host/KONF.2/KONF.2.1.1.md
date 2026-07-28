---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
---

# KONF.2.1.1 - \[Konfiguration von Systemen\] Versionierung der Systemkonfiguration

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine Versionierung vorheriger Konfigurationen verankern.

## Control guidance

Die Versionierung bezeichnet hier die strukturierte Nachvollziehbarkeit von Änderungen an Konfigurationen, also das Speichern, Dokumentieren und bei Bedarf Wiederherstellen älterer Zustände eines IT-Systems. Sie unterscheidet sich von einem einfachen Backup dadurch, dass nicht nur eine Kopie vorliegt, sondern explizit eine fortlaufende Historie mit Vergleichen, Rücksetzpunkten (rollback points) und optional Kommentaren geführt wird. Der Zweck liegt darin, dass eine ungewollte oder fehlerhafte Anpassung an einer Konfiguration im Betrieb schnell erkannt und – wenn erforderlich – präzise auf einen definierten, funktionsfähigen Zustand zurückgesetzt werden kann. Ohne eine solche Versionierung könnte eine fehlerhafte Änderung unbemerkt bleiben oder nur schwer rückgängig gemacht werden. Praktisch umgesetzt kann dies z. B. durch den Einsatz von Konfigurationsmanagement-Tools erfolgen, die automatisch Änderungen versionieren und mit Prüfsummen sichern. Alternativ kann eine Institution auch Konfigurationsdateien regelmäßig in ein Versionsverwaltungssystem wie Git einspielen. Zusätzlich kann es hilfreich sein, Konfigurationsänderungen über standardisierte Änderungsprozesse einzupflegen, sodass jede Anpassung nachvollziehbar protokolliert wird. Eine weitere Möglichkeit kann die Einrichtung von Skripten sein, die Konfigurationsstände automatisch aus Geräten exportieren und revisionssicher ablegen. Zur Umsetzung können Anwendungen zur Geheimnisverwaltung, oft als Secrets-Manager oder Vault bezeichnet, eingesetzt werden. Solche Anwendungen speichern alle Geheimnisse zentral und hochverschlüsselt und stellen sie erst bei Bedarf zur Laufzeit über eine authentifizierte und gesicherte Schnittstelle (API) zur Verfügung. Eine weitere, weit verbreitete Praxis ist die Auslagerung von Secrets aus den Konfigurationsdateien in Umgebungsvariablen (Environment Variables) des ausführenden Systems, wodurch eine strikte Trennung von Code und Konfiguration erreicht wird. Alternativ kann auch die Konfigurationsdatei selbst oder zumindest die Abschnitte, die Geheimnisse enthalten, verschlüsselt werden, wobei dies erfordert, dass der zur Entschlüsselung notwendige Schlüssel seinerseits sicher an die Applikation übergeben wird.

# Editable Content

<!-- Make additions and edits below -->
<!-- See docs/CURATION.md and https://oscal-compass.github.io/compliance-trestle/tutorials/ssp_profile_catalog_authoring/ssp_profile_catalog_authoring -->
