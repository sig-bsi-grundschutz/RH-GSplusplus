---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.1.1 - \[Vertrauenswürdige Basisdienste\] Weiterleitung von Anmeldeinformationen

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Weiterleitung mehrfach verwendbarer Anmeldeinformationen deaktivieren.

## Control guidance

„Weiterleitung mehrfach verwendbarer Anmeldeinformationen“ (auch als Credential Forwarding oder Credential Delegation bekannt) meint technische Mechanismen, bei denen die Anmeldeinformationen eines Zugangskontos (z.B. Kennworthashes oder Kerberos-Tickets) an ein zweites System weitergereicht werden, um sich dort ebenfalls zu authentifizieren, ohne die Daten erneut eingeben zu müssen. Ziel der Deaktivierung ist hier die Unterbrechung von Angriffsketten, die auf dem Diebstahl von Zugangsdaten basieren. Ein Angreifer könnte sonst nach der Kompromittierung eines weniger kritischen Systems, wie einem Webserver, die dorthin weitergeleiteten Anmeldeinformationen eines Administrators aus dem Arbeitsspeicher auslesen und sich mit diesen Rechten unbemerkt im gesamten Netzwerk weiter ausbreiten (Laterale Bewegung). Das gezielte Deaktivieren des Credential Forwarding kann die Angriffsfläche erheblich reduzieren und solche „Pass-the-Hash“- oder „Pass-the-Ticket“-Angriffe effektiv eindämmen, da Anmeldeinformationen mit hohen Privilegien gar nicht erst auf unsichere Systeme gelangen. Stattdessen kann die Authentifizierung ausschließlich temporäre, eingeschränkte Tickets oder Tokens verwenden. Hierzu gehören z.B. Windows Remote Credential Guard oder RestrictedAdmin, sowie unter Linux SSH-Agent Forwarding oder GSSAPI. Eine Token-basierte Authentifizierung ist eine Strategie zur Verbesserung der Informationssicherheit. Nachdem Benutzende ihre Anmeldedaten eingegeben haben, werden diese überprüft und ein einmaliges verschlüsseltes Token generiert, mit dem sie anschließend auf Online-Ressourcen zugreifen können, ohne bei jeder Anfrage ihren Benutzernamen und ihr Passwort eingeben zu müssen. Bei SSH-Verbindungen kann die unsichere „Agent Forwarding“-Funktion serverseitig in der Konfigurationsdatei deaktiviert werden.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Auf RHEL wird die Weiterleitung wiederverwendbarer Anmeldeinformationen über OpenSSH primär serverseitig in `/etc/ssh/sshd_config` bzw. Drop-in-Dateien unter `/etc/ssh/sshd_config.d/` unterbunden: `DisableForwarding yes` deaktiviert alle Forwarding-Funktionen einschließlich SSH-Agent-Forwarding, TCP- und X11-Weiterleitung; alternativ lassen sich `AllowAgentForwarding no` und `AllowTcpForwarding no` gezielt setzen. Für Kerberos/GSSAPI-Delegation kann ergänzend `GSSAPIDelegateCredentials no` gesetzt werden. Scap-Security-Guide deckt die SSH-Forwarding-Pfade mit `sshd_disable_forwarding` ab; GSSAPI-Ticket-Weiterleitung außerhalb von SSH, Pass-the-Hash aus dem Speicher kompromittierter Dienste oder clientseitig erzwungenes Agent-Forwarding auf Servern mit lockerer sshd-Policy bleiben organisatorisch bzw. im Gesamtdesign zu adressieren.

Weitere Informationen: [Netzwerke absichern](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/htmlsingle/securing_networks/index), [Sichere Kommunikation mit OpenSSH](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_using-secure-communications-between-two-systems-with-openssh_configuring-basic-system-settings).

### Implementation Status: partial

______________________________________________________________________
