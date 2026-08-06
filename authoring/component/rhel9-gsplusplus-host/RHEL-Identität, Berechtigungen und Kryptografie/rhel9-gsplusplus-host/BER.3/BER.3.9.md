---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.3.9 - \[Zugangskonten\] Ereignisgesteuerte Deaktivierung

## Control Statement

Berechtigung SOLLTE Zugangskonten ereignisgesteuert deaktivieren.

## Control guidance

Ungenutzte Zugangskonten stellen ein unnötiges Risiko für unberechtigte Zugriffe dar. Werden sie z.B. bei längerer Inaktivität, bei Personalweggang oder bei Verletzung von Richtlinien unverzüglich deaktiviert, so vermindert sich das Risiko eines Missbrauchs erheblich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Sofern zentrale Verzeichnisdienste, wie in anderen BER Anforderungen gefordert, eingesetzt werden, muss auf den RHEL-Host keine zusätzliche Maßnahme ergriffen werden.

RHEL kann lokale Zugangskonten anhand mehrerer Ereignisse automatisiert deaktivieren, ohne dass ein Administrator jeden Fall einzeln bearbeiten muss. Bei längerer Inaktivität sorgt der `INACTIVE`-Wert in `/etc/default/useradd` (bzw. je Konto über `chage -I`) dafür, dass ein Konto eine festgelegte Anzahl Tage nach Ablauf des Passworts automatisch gesperrt wird. Der dritte im Grundschutz++-Katalog genannte Auslöser, der Personalweggang, hat auf dem Host selbst keinen technischen Anknüpfungspunkt: Ohne Anbindung an eine zentrale Identitätsverwaltung (z. B. Red Hat IdM/SSSD) oder einen HR-Prozess bleibt die Deaktivierung bei Personalweggang eine organisatorische Aufgabe der Institution. Lokale Accounts über mehrere Systeme hinweg können mittels eines Konfigurations-Management-Tools (z.B. Ansible) automatisiert entfernt werden.

Weitere Informationen: [Authentifizierung und Autorisierung – Konfiguration mit authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect_configuring-authentication-and-authorization-in-rhel), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index)

### Rules:

  - account_disable_post_pw_expiration

### Implementation Status: partial

______________________________________________________________________
