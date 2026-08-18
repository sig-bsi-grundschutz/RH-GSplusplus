---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.6.5 - \[Rollen und Berechtigungen\] Dynamische Zugriffskontrolle im System

## Control Statement

Konfiguration für IT-Systeme KANN dynamische Zugriffskontrolle im System aktivieren.

## Control guidance

Eine dynamische Zugriffskontrolle (engl. Dynamic Access Control, DAC) bezeichnet ein Verfahren, bei dem Zugriffsentscheidungen nicht ausschließlich auf statischen Berechtigungen (z. B. Benutzerrollen oder ACLs) beruhen, sondern zusätzlich kontextabhängige Bedingungen wie Gerätezustand, Sensitivität der Daten, Standort, Zeitfenster oder Sicherheitsklassifikation auswerten. Dabei bleibt die Policy, also die zugrundeliegende Regelmenge zur Zugriffsbewertung, fest definiert und nachvollziehbar dokumentiert – lediglich die Entscheidung über den konkreten Zugriff erfolgt dynamisch anhand dieser Bedingungen. Ziel ist eine feinere Steuerung des Datenzugriffs auf Basis aktueller Risikosituationen, ohne dass Administratoren Berechtigungen manuell anpassen müssen. Solche Mechanismen können etwa verhindern, dass ein Benutzer sensible Daten von einem nicht verwalteten Endgerät ausliest, während er im internen Netz regulär Zugriff hätte. Da DAC komplex sein kann ist es zweckmäßig, auch auf Funktionen zur Auditierung und Protokollierung der DAC zu achten.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL implementiert dynamische Zugriffskontrolle als Mandatory Access Control über SELinux: Labels an Dateien, Prozessen und Ports werden beim Zugriff geprüft; Domain-Übergänge folgen Policy-Regeln. `setroubleshoot` und Audit-Logs dokumentieren Verletzungen. Die Policy ist distribution-seitig vorgegeben und kann lokal erweitert werden; feingranulare Anwendungsprofile erfordern Custom-Module oder Booleans — nicht automatische Echtzeit-Umgebungsanalyse wie ABAC.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
