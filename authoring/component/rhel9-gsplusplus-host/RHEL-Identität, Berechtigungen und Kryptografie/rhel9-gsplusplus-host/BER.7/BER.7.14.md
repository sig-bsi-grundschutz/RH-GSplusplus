---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.14 - \[Schlüsselmanagement\] Schlüssel vor Ablauf prüfen

## Control Statement

Berechtigung SOLLTE Schlüssel auf das baldige Auslaufen der Nutzungszeit {{ insert: param, ber.7.14-prm1 }} überprüfen.


## Control guidance

Wird die Gültigkeit von Schlüsseln vor dem Auslaufen nicht überwacht, so könnten Schlüssel ungültig werden, wodurch Schnittstellen oder Anwendungen plötzlich nicht mehr verfügbar sein könnten. Läuft ein Schlüssel bald ab, obwohl der Zweck weiterhin bestehen bleibt, so ist es sinnvoll den Schlüssel rechtzeitig durch einen neuen zu ersetzen. Hierbei ist zu beachten, dass bei Schlüsselwechsel verschlüsselte Daten entschlüsselt und erneut verschlüsselt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

RHEL stellt Werkzeuge zur proaktiven Ablaufüberwachung bereit: `certmonger` kann Zertifikate überwachen und vor Ablauf erneuern; `openssl x509 -checkend` oder Skripte in `cron`/`systemd`-Timern eignen sich für regelmäßige Prüfungen. Automatisierte CaC-Regeln für „regelmäßige Ablaufprüfung" existieren nicht — Schwellwert, Intervall und Eskalation sind institutionell festzulegen und operativ umzusetzen (z. B. Monitoring-Alert bei Restlaufzeit < 30 Tage).

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
