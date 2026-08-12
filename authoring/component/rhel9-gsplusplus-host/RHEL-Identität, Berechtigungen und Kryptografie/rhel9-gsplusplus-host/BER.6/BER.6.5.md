---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.6.5 - \[Passwortgebrauch\] Anlassbezogene Passwortwechsel

## Control Statement

Berechtigung SOLLTE einen Passwortwechsel ausschließlich anlassbezogen ausführen.


## Control guidance

Ein ausschließlich anlassbezogener Passwortwechsel bedeutet, dass Passwörter nur genau dann geändert werden, wenn ein begründeter Sicherheitsanlass vorliegt – beispielsweise ein Verdacht auf Kompromittierung des Endgerätes oder Zugangs, neue einschlägige Einträge in öffentlichen Leak-Datenbanken, die Weitergabe an Unbefugte durch einen Phishing-Vorfall, oder technische Indikatoren für einen möglichen Missbrauch des Zugangs zu Systemen oder Anwendungen. Dieser Ansatz unterscheidet sich vom früher häufig praktizierten, periodischen Passwortwechsel, der ohne konkreten Anlass in festen Intervallen erzwungen wurde. Ein solcher erzwungener Rhythmus könnte die Passwortsicherheit sogar verringern, weil Nutzende dann dazu neigen, schwächere, nur leicht veränderte Passwörter („sommer5“) zu wählen oder Zugangsdaten in verschiedenen Zugängen wiederzuverwenden. Zweck dieser Regelung ist es, die tatsächliche Sicherheit von Zugangskonten zu erhöhen und unnötige Belastungen der Nutzenden zu vermeiden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Grundsätzlich sollte ein RHEL-Host an zentrale Identity-Provider/Verzeichnisdienste angebunden sein und an dieser Stelle die Einstellungen zum Passwort-Alter durchgesetzt sein. Für lokale Konten auf RHEL-Hosts bedeutet dies, dass `PASS_MAX_DAYS` in `/etc/login.defs` nicht oder auf einen unrealistisch hohen Wert gesetzt sind.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Implementation Status: not-applicable

______________________________________________________________________
