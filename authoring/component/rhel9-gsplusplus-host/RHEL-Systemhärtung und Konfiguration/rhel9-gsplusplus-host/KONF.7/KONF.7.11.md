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

Bibliotheken-Ladung steuert fapolicyd über Regeln für dynamische Linker und Bibliothekspfade; SELinux verhindert unerlaubte cross-domain Library-Nutzung. Der Dynamic Linker und Distribution-Härtung in glibc reduzieren Angriffsflächen. Whitelist-Pflege für erlaubte Bibliotheken liegt bei der Institution.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
