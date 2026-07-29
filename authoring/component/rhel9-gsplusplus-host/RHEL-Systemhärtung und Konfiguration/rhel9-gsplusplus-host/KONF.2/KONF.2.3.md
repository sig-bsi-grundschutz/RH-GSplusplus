---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.2.3 - \[Konfiguration von Systemen\] Änderung von Default-Zugangsdaten

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Änderung von Default-Zugangsdaten ausführen.

## Control guidance

"Default-Zugangsdaten" sind werkseitig voreingestellte Benutzername-Passwort-Kombinationen wie "root" oder "administrator", sowie vergleichbare Authentifizierungsmerkmale, die bei der Erstinbetriebnahme von IT-Systemen unverändert vorhanden sind. Diese Daten sind in der Regel öffentlich dokumentiert oder leicht im Internet auffindbar. Ihr Fortbestehen im Produktivbetrieb könnte ein erhebliches Risiko darstellen, da ein Angreifer mit minimalem Aufwand Zugriff auf Systeme erlangen könnte. Ein klassischer Vorfall könnte sein, dass ein öffentlich erreichbarer Router mit unveränderten Standardzugängen übernommen wird. Die Änderung kann demgegenüber sicherstellen, dass nur berechtigte Personen Zugriff erlangen, und kann damit unbefugte Manipulationen oder Datendiebstahl wirksam erschweren. Eine Institution kann die Anforderung umsetzen, indem bei der Inbetriebnahme jedes Systems ein Prozess etabliert wird, der die Standardzugangsdaten unmittelbar ersetzt. Dies kann beispielsweise (1) durch verpflichtende Initial-Setup-Routinen erfolgen, die eine Passwortänderung erzwingen, oder (2) durch zentrale Checklisten oder automatisierte Inventarisierung, die offene Standardzugänge identifizieren und schließen. Die Anforderung ist auch dann erfüllt, wenn diese Zugänge deaktiviert oder durch Zugänge mit von der Institution verwalteten Zugangsdaten ersetzt werden.

______________________________________________________________________

## What is the solution and how is it implemented?

RHEL liefert selbst keine vorab gesetzten Standard-Zugangsdaten aus: Bei der Installation über Anaconda/Kickstart muss für das root-Konto entweder ein Passwort oder ein SSH-Schlüssel explizit gesetzt werden, es existiert kein werkseitig bekanntes "root/root"-Login. Ergänzend erzwingt die PAM-Konfiguration in `/etc/pam.d/system-auth` und `/etc/pam.d/password-auth` standardmäßig, dass keine Konten mit leerem Passwort angemeldet werden können (kein `nullok`); Für Dienstkonten und Abbild-/Cloud-Images bleibt es Aufgabe der Institution, mitgelieferte oder aus Vorlagen übernommene Zugangsdaten (z. B. in vorkonfigurierten VM-Images) unmittelbar nach Inbetriebnahme zu ersetzen oder das Konto zu deaktivieren. Zusätzlich gibt es die Möglichkeit den Login des root-Users in der SSHD Konfiguration zu unterbinden.

### Rules:

  - sshd_disable_root_password_login
  - ensure_root_password_configured

### Implementation Status: implemented

______________________________________________________________________
