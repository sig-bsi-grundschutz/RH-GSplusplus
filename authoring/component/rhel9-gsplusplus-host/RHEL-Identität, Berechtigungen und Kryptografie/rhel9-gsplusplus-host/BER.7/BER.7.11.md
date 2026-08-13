---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.11 - \[Schlüsselmanagement\] Integrität

## Control Statement

Berechtigung SOLLTE die Verifikation der Integrität geheimer Schlüssel vor jeder Nutzung verankern.


## Control guidance

Wird die Integrität von Schlüsseln vor der Verwendung nicht geprüft, so könnte er unbemerkt durch einen Angreifer ausgetauscht werden, wodurch der Angreifer den vermeintlich verschlüsselten Austausch mitlesen. Daher ist ein Integritätsschutz (z.B. eine bekannte Checksumme oder Fingerabdruck) von abgelegten Schlüsseln sinnvoll. Dies kann z.B. durch den Abgleich von Prüfsummen geschehen, welche auf einem anderen IT-System gespeichert sind. Für die Implementierung genügt es, wenn die eingesetzten IT-Produkte bereits so entwickelt oder beschafft worden sind, dass sie die Prüfung automatisiert durchführen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Schlüssel in Hardware (TPM 2.0, PKCS#11-HSM, Smartcards) bleiben nicht exportierbar; Integrität und Manipulationsschutz werden vom Secure Element geprüft, bevor kryptografische Operationen ausgeführt werden. Dateibasierte geheime Schlüssel des Hosts (z. B. `/etc/ssh/*_key`) schützt RHEL über restriktive Dateirechte und Gruppenzugehörigkeit. Weiterhin wird beim erstmaligen Verbindungsaufbau eines Hosts der Fingerabdruck des Schlüssels angezeigt und kann von Hand oder via DNS-Speicherung verifiziert werden (`known_hosts`). Bei subsequenten Verbindungen wird der präsentierte Fingerabdruck des Servers gegen den gespeicherten Fingerabdruck auf dem initiierenden Client geprüft. Für persönliche, private Schlüssel ist keine Integritätsprüfung vorgesehen. Indirekt kann eine Integritätsprüfung von Dateien über AIDE (Advanced Intrusion Detection Environment) durchgeführt werden, wodurch regelmäßig Hash-Summen der Schlüsselmaterialien gebildet werden und entsprechende Alarme erzeugt werden.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Rules:

  - file_groupownership_sshd_private_key
  - file_ownership_sshd_private_key
  - file_permissions_sshd_private_key
  - aide_build_database
  - package_aide_installed
  - aide_periodic_cron_checking
  - aide_scan_notification

### Implementation Status: alternative

______________________________________________________________________
