---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.4 - \[Vertrauenswürdige Basisdienste\] Einschränkung von Fernwartungsfunktionen

## Control Statement

Konfiguration für IT-Systeme SOLLTE Fernwartungsfunktionen im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement einschränken.

## Control guidance

Fernwartungszugänge, etwa über RDP, SNMP oder Anwendungen zur Fernsteuerung des Systems erlauben typischerweise eine Vielzahl von Eingriffen in Systemkonfiguration und Datenverarbeitungen. Beispiele sind die Remote-Zwischenablage und die automatische Einbindung von Peripheriegeräten, Wechseldatenträgern und Netzlaufwerken. Unautorisierte Fernwartungszugänge könnten für Angriffe missbraucht werden. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Authentifizierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Kryptographie zu finden ist.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Auf RHEL ist SSH der zentrale Fernwartungsweg; die Institution schränkt ihn über `/etc/ssh/sshd_config` und Drop-ins in `sshd_config.d/` ein: Nur autorisierte Konten oder Gruppen (`AllowUsers`/`AllowGroups`/`DenyUsers`/`DenyGroups`), kein direkter Root-Login, keine leeren Passwörter und PAM-gestützte Authentifizierung (inkl. zentraler Verzeichnisdienste über SSSD) binden den Zugang an die IAM-Vorgaben aus BER. Zusätzlich lassen sich Weiterleitungsfunktionen (X11, TCP, ssh-agent) per `DisableForwarding`, `X11Forwarding` und `AllowTcpForwarding` deaktivieren, um Tunnel- und Clipboard-Risiken zu reduzieren; die systemweite Crypto Policy bindet OpenSSH über `50-redhat.conf` an aktuelle Verschlüsselungsalgorithmen. Nicht benötigte Fernwartungsdienste wie SNMP können wie andere Netzwerkdienste per systemd deaktiviert werden. Welche Konten, Schlüssel und Ausnahmen gelten, definiert die Institution; RHEL erzwingt keine konkrete AllowList ohne explizite Konfiguration.

Weitere Informationen: [Sichere Kommunikation mit OpenSSH](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/assembly_using-secure-communications-between-two-systems-with-openssh_securing-networks), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Systemweite kryptographische Policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening).

### Implementation Status: partial

______________________________________________________________________
