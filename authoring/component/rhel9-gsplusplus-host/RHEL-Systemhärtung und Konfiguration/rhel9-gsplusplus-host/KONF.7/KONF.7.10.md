---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.10 - \[Schutz vor Schadcode\] Einschränkung der Ausführung

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Ausführung nicht autorisierter Anwendungen einschränken.

## Control guidance

Wenn Anwendungen an beliebigen Speicherorten installiert und ausgeführt werden, z.B. im Wurzeldateisystem des Betriebssystems oder an Speicherorten zusammen mit Daten der Nutzerumgebung, dann könnte dies zahlreiche Sicherheitsrisiken mit sich bringen. Unbefugte oder schadhafte Anwendungen könnten unbemerkt an unautorisierte Orte platziert werden, wo sie außerhalb etablierter Sicherheitskontrollen agieren und beispielsweise Privilege-Escalation-Angriffe durchführen können. Zudem wird das Risiko der Manipulation von Anwendungsdateien erhöht, da Angreifer gezielt nach nicht-geschützten Speicherorten suchen, um dort eigenen Code zu hinterlegen oder legitime Anwendungen zu modifizieren. Eine solche Situation kann zu "Living-off-the-Land"-Angriffen führen, bei denen Angreifer vorhandene legitime Programme missbrauchen, um Schadaktionen auszuführen, was die Erkennung erheblich erschwert. Die Beschränkung von Ausführungsspeicherorten (Execution Control) zielt darauf ab, die Angriffsfläche zu reduzieren und eine bessere Kontrolle über ausführbare Programme zu ermöglichen. Zur technischen Umsetzung dieser Anforderung kann eine Institution verschiedene Maßnahmen implementieren. Application Allowlisting kann eingesetzt werden, um nur vertrauenswürdige Anwendungen aus definierten Verzeichnissen auszuführen, beispielsweise mittels AppLocker unter Windows oder SELinux unter Linux-Systemen. Zusätzlich können Software Restriction Policies (SRPs) konfiguriert werden, um Ausführungsrechte auf bestimmte Verzeichnispfade zu begrenzen, wobei eine Trennung zwischen Systemverzeichnissen und Nutzerverzeichnissen empfehlenswert ist. Weitere wirksame Techniken umfassen die Implementierung von Code Signing, wodurch nur digital signierte Anwendungen ausgeführt werden können, sowie die Nutzung von Container-Technologien wie Docker, die eine isolierte Ausführungsumgebung bieten. Dabei kann auf das Inventar der Anwendungen als Grundlage zurückgegriffen werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Ausführung nicht autorisierter Programme begrenzt fapolicyd mit deny-all/permit-by-exception-Policy auf lokale Dateisysteme; zusätzlich `noexec` auf Datenpartitionen und SELinux-Domains. Die Institution pflegt Whitelists in `/etc/fapolicyd/rules.d/`. Ausführung aus User-Home ohne Policy bleibt ein Risiko, das organisatorisch adressiert werden muss.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
