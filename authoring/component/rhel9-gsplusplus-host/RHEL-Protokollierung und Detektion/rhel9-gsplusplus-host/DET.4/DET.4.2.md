---
x-trestle-param-values:
  det.4.2-prm1:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.2 - \[Überwachung von Aktivitäten\] Automatische Angriffserkennung

## Control Statement

Detektion für IT-Systeme SOLLTE diese auf Anzeichen für Angriffe durch {{ insert: param, det.4.2-prm1 }} überwachen.

## Control guidance

Wenn professionelle Tätergruppen Zugriff auf Systeme und Daten erhalten, nutzen sie diese zunehmend schneller für ihre Zwecke aus, z.B. um Daten abfließen zu lassen oder Ransomware zu verteilen. Zur Umsetzung können sowohl netz- als auch hostbasierte Erkennungssysteme (NIDS und HIDS) verwendet werden. Für die Detektion bei IT-Systemen ohne Installationsmöglichkeit wie Appliances, IoT-Geräte oder OT-Systeme kann ein kombinierter Ansatz aus Netzwerk- und Loganalyse sinnvoll sein. Angriffe können signaturbasiert, sowie durch Verhaltensanalyse und Anomalien erkannt werden. Die Anforderung kann auch mit bereits vorhandenen oder im System integrierten Angriffserkennungsmechanismen erfüllt werden. Zweckmäßig ist es Schwellwerte und Kategorien (Info, Warnung, Alarm) so festzulegen, dass Probleme frühzeitig erkannt werden können, aber beim Betriebspersonal keine Alarmmüdigkeit (alert fatigue) aufkommt. Hierzu ist es hilfreich die Ergebnisse regelmäßig auszuwerten und wenn nötig Korrekturmaßnahmen zu ergreifen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Auf dem Host wirken mehrere Erkennungsmechanismen zusammen: SELinux im Enforcing-Modus (Denials im Audit), AIDE für Dateiintegrität, `auditd`-Regeln für privilegierte und ungewöhnliche Aktionen sowie optional `fapolicyd` gegen unerwartete Binärausführung. Das ist hostbasierte Detektion (HIDS-artig), kein NIDS. Signaturen, Anomalie-Schwellwerte und Alarmkategorien muss die Institution justieren, um Alarmmüdigkeit zu vermeiden.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Integrität mit AIDE prüfen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/checking-integrity-with-aide_security-hardening), [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
