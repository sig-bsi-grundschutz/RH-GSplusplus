---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.5.10 - \[Umgang mit Authentisierungsmitteln\] Zugriffsbeschränkung pro IT-System

## Control Statement

Berechtigung für IT-Systeme SOLLTE den lesenden und schreibenden Zugriff auf Authentifizierungsmittel einschränken.


## Control guidance

Lesender Zugriff bezeichnet in diesem Kontext jede Möglichkeit, Authentifizierungsmittel einzusehen, auszulesen, zu exportieren, zu kopieren oder technisch zu verwenden, ohne sie unmittelbar zu verändern; schreibender Zugriff meint jede Möglichkeit, Authentifizierungsmittel anzulegen, zu ändern, zu ersetzen, zu löschen, zu importieren oder deren Vertrauensstatus zu beeinflussen. Authentifizierungsmittel sind hier alle technischen oder organisatorisch verwalteten Mittel, mit denen Identitäten nachgewiesen oder Vertrauensbeziehungen hergestellt werden, etwa Passwörter, private Schlüssel, API-Keys, Token, Zertifikate, Kerberos-Keytabs, SSH-Schlüssel, Recovery-Codes, Hardware-Token-Zuordnungen oder Einträge in Trust Stores. Der Zugriff auf solche Mittel ist besonders sensibel, weil bereits lesender Zugriff in vielen Fällen zur Nachahmung einer Identität oder zur Umgehung vorgesehener Kontrollmechanismen führen könnte, während schreibender Zugriff zusätzlich Manipulationen an Vertrauensketten, Schlüsselmaterial oder Anmeldeverfahren ermöglichen könnte.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Lesenden und schreibenden Zugriff auf Authentisierungsmittel begrenzt RHEL über Dateirechte und Besitz: `/etc/shadow` und `/etc/gshadow` gehören root und sind für andere Benutzer nicht lesbar; Passwort-Hashes liegen nicht in `/etc/passwd`. Private OpenSSH-Host-Schlüssel unter `/etc/ssh/*_key` sind ebenfalls nur für root lesbar. SELinux ergänzt die Discretionary-Rechte. Vergleichbare Vorgaben gelten für weitere Keytabs, TLS-Private-Keys und Token-Dateien, die der Betrieb entsprechend härtet. ComplianceAsCode-Regeln prüfen die kritischen Standardpfade zuverlässig ab. Persönliche Ablagen (Home-Verzeichnis) gehören dem jeweiligen Benutzer und ist für andere Nutzer (außer Server-Administratoren) nicht zugänglich. Hier werden ebenfalls möglicherweise private Schlüssel, Passwörter, Token oder Keytabs abgelegt. Die korrekte Ablage der Daten erfordert auch eine entsprechende Schulung des Personals.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index).

### Rules:

  - file_permissions_etc_passwd
  - file_permissions_etc_shadow
  - file_permissions_etc_group
  - file_permissions_etc_gshadow
  - file_owner_etc_passwd
  - file_owner_etc_shadow
  - file_owner_etc_group
  - file_owner_etc_gshadow
  - file_groupowner_etc_passwd
  - file_groupowner_etc_shadow
  - file_groupowner_etc_group
  - file_groupowner_etc_gshadow
  - accounts_password_all_shadowed
  - file_permissions_sshd_private_key

### Implementation Status: implemented

______________________________________________________________________
