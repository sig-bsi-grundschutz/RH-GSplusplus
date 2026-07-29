---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.1 - \[Konfiguration von Systemen\] Grundkonfiguration für Systeme

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine Grundkonfiguration dokumentieren.

## Control guidance

Eine Grundkonfiguration (engl. baseline configuration) bezeichnet hier einen dokumentierten Ausgangszustand, der alle sicherheitsrelevanten Einstellungen, Dienste und Komponenten umfasst und als verbindlicher Referenzpunkt für den Betrieb und die Härtung dient. Sie stellt damit eine Art „Zielzustand“ dar, anhand dessen spätere Änderungen überprüft oder Abweichungen erkannt werden können. Ohne eine solche Referenz könnte es bei Installationen, Updates oder Wiederherstellungen zu unsicheren Abweichungen kommen, etwa wenn unnötige Dienste aktiv bleiben, Standardkonten nicht deaktiviert sind oder Kommunikationsschnittstellen unkontrolliert offenstehen; umgekehrt kann eine saubere Grundkonfiguration sicherstellen, dass Systeme konsistent, nachvollziehbar und auf Basis etablierter Sicherheitsanforderungen betrieben werden. Hierzu gehört z.B. die Konfiguration der Uhrensychronisation, von DNS und Verzeichnisdiensten, die Änderung von Default-Zugangsdaten oder der automatische Abruf benötigter Lizenzen. Die Umsetzung einer Grundkonfiguration kann durch verschiedene Maßnahmen unterstützt werden: (1) Es ist sinnvoll, Herstellerdokumentationen zu sichten und empfohlene Härtungseinstellungen (z. B. Deaktivierung unsicherer Protokolle) als Ausgangspunkt zu übernehmen. (2) Ergänzend können Empfehlungen des BSI oder Benchmarks wie die CIS Benchmarks herangezogen werden, um systematisch sicherheitskritische Parameter zu prüfen und einzupflegen. (3) Für komplexe Umgebungen kann ein Konfigurationsskript oder ein Automatisierungs-Tool (z. B. Ansible, Puppet, Chef) genutzt werden, um eine reproduzierbare Baseline einzuspielen und Abhängigkeiten der Komponenten konsistent zu berücksichtigen. Auf diese Weise kann die Institution sicherstellen, dass jede Installation oder Wiederherstellung eines Systems auf einer überprüfbaren und einheitlichen Basis erfolgt.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL liefert die technischen Bausteine, aus denen eine Institution eine Grundkonfiguration ableiten und reproduzierbar ausrollen kann: Anaconda/Kickstart und Image Builder-Blueprints erzeugen definierte Installationszustände, chronyd steuert Zeitsynchronisation, NetworkManager/SSSD/realmd binden DNS- und Verzeichnisdienste ein, und scap-security-guide stellt vorgefertigte Härtungsprofile (z. B. OSPP, CIS) bereit, die per OpenSCAP oder Ansible-Remediation auf ein System angewendet werden. Red Hat Insights vergleicht laufende Systeme gegen bekannte Best-Practice- und Compliance-Regelsätze und meldet Abweichungen. Welche Einstellungen konkret als verbindliche Referenz gelten, welches Benchmark (BSI, CIS) zugrunde gelegt wird und wie die Freigabe der Grundkonfiguration organisatorisch erfolgt, legt die Institution jedoch selbst fest; RHEL erzwingt keine bestimmte Baseline.

### Implementation Status: partial

______________________________________________________________________
