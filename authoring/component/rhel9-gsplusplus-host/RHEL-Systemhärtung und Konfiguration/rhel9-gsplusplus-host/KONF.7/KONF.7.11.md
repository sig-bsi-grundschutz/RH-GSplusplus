---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.11 - \[Schutz vor Schadcode\] Einschränkung von Softwarebibliotheken

## Control Statement

Konfiguration für IT-Systeme KANN die Ausführung nicht autorisierter Softwarebibliotheken einschränken.

## Control guidance

Softwarebibliotheken sind wiederverwendbare Codesammlungen, die Entwicklern fertige Funktionalitäten bieten, ohne diese selbst programmieren zu müssen. Unautorisierte Bibliotheken stellen Sicherheitsrisiken dar, weil sie absichtlich eingeschleusten Schadcode enthalten könnten, der Daten ausspioniert oder Systeme kompromittiert. Sie durchlaufen seltener reguläre Sicherheitsüberprüfungen und könnten für Supply-Chain-Angriffe genutzt werden, bei denen harmlos erscheinender Code mit versteckten Schadfunktionen in Paketmanager eingeschleust wird. Zudem erhalten unautorisierte Bibliotheken häufig keine regelmäßigen Sicherheitsupdates, sodass bekannte Schwachstellen unbehoben bleiben. Mangelnde Dokumentation und unklare Abhängigkeiten von anderen ungeprüften Quellen erhöhen das Risiko zusätzlich. Beispiele sind Dateien der Typen .dll, .ocx, und .so. Die Umsetzung kann durch Sicherheitsfunktionen erfolgen, die nur das Laden autorisierter Bibliotheken in Systemprozessen erlaubt. Verfügt das IT-System über keine Möglichkeit zur Installation von Anwendungen, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Verschiedene Bibliotheken stellt Red Hat bereits mit RHEL bereit. Diese können über `dnf` installiert werden. Da diese Bibliotheken durch Red Hat nach SLSA Level3 gebaut werden, kann hier den Bibliotheken ein höheres Vertrauen entgegen gebracht werden. Zusätzlich stellt Red Hat für Entwickler im Rahmen von *Red Hat Advanced Developer Subscription* eine Trusted Library für weitere Softwarepakete bereit, die nach den gleichen Standards gebaut werden. Um die Anforderung konsequent umzusetzen, empfiehlt sich, die RHEL Systeme air-gapped zu betreiben und ausschließlich erlaubte Software in Repositories für die Systeme bereitzustellen. Dies kann mittels *Red Hat Satellite* und/oder ergänzende Artefakt-Stores erfolgen. Durch eine Netzwerkseitige Zugriffsunterbindung der RHEL-Systeme an das Internet, bleibt lediglich der Artefakt-Speicher als Quelle für vertrauenswürdige Software-Bibliotheken. Ein Prozess muss hierbei sicherstellen, dass die benötigte Software auch zur Verfügung steht und entsprechende Kontrollen der Institution (Zulieferer, Qualitätsmerkmale, Support, etc) eingehalten werden.

Weitere Informationen: [Red Hat Trusted Libraries](https://docs.redhat.com/en/documentation/red_hat_trusted_libraries/1.0), [Red Hat Satellite - Custom File Type Repositories](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html/managing_content/managing-custom-file-type-content)

### Implementation Status: planned

______________________________________________________________________
