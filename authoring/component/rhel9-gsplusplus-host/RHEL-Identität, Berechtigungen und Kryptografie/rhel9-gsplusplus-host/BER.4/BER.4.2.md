---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.4.2 - \[Berechtigungsmanagement\] Autorisierung von Berechtigungen

## Control Statement

Berechtigung SOLLTE die Zuweisung von Berechtigungen durch {{ insert: param, ber.4.2-prm1 }} autorisieren.


## Control guidance

Mit „bestimmte Personen oder Rollen“ sind hier vorab festgelegte, nachvollziehbar benannte Autorisierungsinstanzen gemeint, also etwa disziplinarische Führungskräfte, fachliche Daten- oder Prozessverantwortliche, Systemverantwortliche, Rollen wie Application Owner, Data Owner, Service Owner oder Genehmiger in einem Identity-and-Access-Management-Prozess. Gemeint ist nicht eine beliebige informelle Zustimmung, sondern eine fachlich oder organisatorisch legitimierte Entscheidung darüber, ob eine konkrete Berechtigung zu einer Person, Funktion, Aufgabe oder einem Schutzbedarf passt. Die Vorschrift zielt darauf ab, unkontrollierte, fachlich nicht begründete oder zu weitreichende Berechtigungsvergaben zu vermeiden; ohne eine festgelegte Autorisierungsinstanz könnte ein Zugangskonto Zugriff auf vertrauliche Daten erhalten, eine nicht mehr passende Gruppenmitgliedschaft könnte bestehen bleiben oder ein privilegierter Zugang könnte ohne ausreichende fachliche Prüfung vergeben werden. Eine geregelte Autorisierung kann die Nachvollziehbarkeit von Zugriffsentscheidungen erhöhen, Interessenkonflikte reduzieren und sicherstellen, dass Berechtigungen an Aufgaben, Verantwortlichkeiten und Schutzbedarf ausgerichtet bleiben.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Autorisierung von Berechtigungszuweisungen ist primär ein IAM-/Organisationsprozess (Führungskraft, Data Owner, Application Owner). Auf dem RHEL-Host stützen technische Kontrollen die Nachvollziehbarkeit: Änderungen an lokalen Konten, Gruppen und `sudoers` lassen sich mit auditd-Watch-Regeln protokollieren; zentral über IdM laufen Zuweisungen über Rollen und HBAC, deren Änderungen im Verzeichnis auditierbar sind. Der Host erzwingt jedoch nicht, dass vor einer technischen Zuweisung eine bestimmte Person oder Rolle zugestimmt hat — Freigabe-Workflows gehören in IdM, ITSM oder AAP.

Weitere Informationen: [Authentifizierung und Autorisierung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/index), [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening).

### Implementation Status: partial

______________________________________________________________________
