---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.1.1 - \[Konfiguration von Systemen\] Versionierung der Systemkonfiguration

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine Versionierung vorheriger Konfigurationen verankern.

## Control guidance

Die Versionierung bezeichnet hier die strukturierte Nachvollziehbarkeit von Änderungen an Konfigurationen, also das Speichern, Dokumentieren und bei Bedarf Wiederherstellen älterer Zustände eines IT-Systems. Sie unterscheidet sich von einem einfachen Backup dadurch, dass nicht nur eine Kopie vorliegt, sondern explizit eine fortlaufende Historie mit Vergleichen, Rücksetzpunkten (rollback points) und optional Kommentaren geführt wird. Der Zweck liegt darin, dass eine ungewollte oder fehlerhafte Anpassung an einer Konfiguration im Betrieb schnell erkannt und – wenn erforderlich – präzise auf einen definierten, funktionsfähigen Zustand zurückgesetzt werden kann. Ohne eine solche Versionierung könnte eine fehlerhafte Änderung unbemerkt bleiben oder nur schwer rückgängig gemacht werden. Praktisch umgesetzt kann dies z. B. durch den Einsatz von Konfigurationsmanagement-Tools erfolgen, die automatisch Änderungen versionieren und mit Prüfsummen sichern. Alternativ kann eine Institution auch Konfigurationsdateien regelmäßig in ein Versionsverwaltungssystem wie Git einspielen. Zusätzlich kann es hilfreich sein, Konfigurationsänderungen über standardisierte Änderungsprozesse einzupflegen, sodass jede Anpassung nachvollziehbar protokolliert wird. Eine weitere Möglichkeit kann die Einrichtung von Skripten sein, die Konfigurationsstände automatisch aus Geräten exportieren und revisionssicher ablegen. Zur Umsetzung können Anwendungen zur Geheimnisverwaltung, oft als Secrets-Manager oder Vault bezeichnet, eingesetzt werden. Solche Anwendungen speichern alle Geheimnisse zentral und hochverschlüsselt und stellen sie erst bei Bedarf zur Laufzeit über eine authentifizierte und gesicherte Schnittstelle (API) zur Verfügung. Eine weitere, weit verbreitete Praxis ist die Auslagerung von Secrets aus den Konfigurationsdateien in Umgebungsvariablen (Environment Variables) des ausführenden Systems, wodurch eine strikte Trennung von Code und Konfiguration erreicht wird. Alternativ kann auch die Konfigurationsdatei selbst oder zumindest die Abschnitte, die Geheimnisse enthalten, verschlüsselt werden, wobei dies erfordert, dass der zur Entschlüsselung notwendige Schlüssel seinerseits sicher an die Applikation übergeben wird.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL selbst führt keine automatische Versionierung von /etc, doch die dortigen Konfigurationsartefakte sind textbasiert und lassen sich in ein Versionsverwaltungssystem wie Git integrieren, etwa über etckeeper-artige Ansätze oder als Teil eines Ansible-Playbook-Repositories, dessen Rollen und Inventar den Systemzustand deklarativ beschreiben. Kickstart-Dateien und Image Builder-Blueprints selbst sind versionierbare Artefakte, aus denen reproduzierbare Installationen abgeleitet werden können; RPM-Paketverwaltung (dnf history, RPM-Transaktionshistorie) protokolliert zusätzlich Paketänderungen mit Rollback-Möglichkeit. Für Geheimnisse, die nicht im Klartext versioniert werden sollen, kann Ansible Vault oder eine externe Geheimnisverwaltung (z. B. HashiCorp Vault) eingesetzt werden. Die Einrichtung eines fortlaufenden, mit Rücksetzpunkten versehenen Versionsprozesses samt Änderungsfreigabe ist jedoch ein organisatorischer Schritt, den die Institution etablieren und betreiben muss.

### Implementation Status: partial

______________________________________________________________________
