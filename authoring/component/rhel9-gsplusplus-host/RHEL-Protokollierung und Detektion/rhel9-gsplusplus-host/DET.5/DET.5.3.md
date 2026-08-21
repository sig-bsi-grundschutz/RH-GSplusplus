---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.5.3 - \[Management von Schwachstellen\] Schwachstellenscans

## Control Statement

Detektion SOLLTE eine Vorgehensweise zum Scan nach Schwachstellen einschließlich deren Auswertung und Behandlung verankern.

## Control guidance

Über das Netz erreichbare Schwachstellen bergen das Risiko, dass hierüber Angriffe in IT-Systeme und Anwendungen eindringen, Daten auslesen oder sich über das Netz verbreiten. Schwachstellenscans finden solche Lücken, indem sie Anfragen zu bekannten Schwachstellen im Netz stellen und die Antworten auswerten. Regelmäßige Scans tragen dazu bei, dass Sicherheitslücken entdeckt werden, bevor sie ausgenutzt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Auf dem Host liefert OpenSCAP (`openscap-scanner`) Konfigurations- und (historisch) CVE-Scans gegen SCAP-Inhalte; Red Hat Insights bzw. Satellite orchestrieren wiederkehrende Schwachstellenscans und die Auswertung. OVAL-CVE-Feeds in OpenSCAP sind abgekündigt — Insights ist der unterstützte Weg für aktuelle CVEs. Verfahren, Freigabe kritischer Scans und Behandlung der Findings bleiben organisatorisch.

Weitere Informationen: [OpenSCAP-Compliance-Scan](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/scanning-the-system-for-configuration-compliance-and-vulnerabilities_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
