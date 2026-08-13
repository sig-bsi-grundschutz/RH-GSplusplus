---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# BER.7.1 - \[Schlüsselmanagement\] Etablierte Algorithmen bei der Schlüsselerzeugung

## Control Statement

Berechtigung SOLLTE die ausschließliche Verwendung etablierter kryptografischer Algorithmen bei der Schlüsselerzeugung nach {{ insert: param, ber.7.1-prm1 }} verankern.


## Control guidance

Etablierte kryptografische Algorithmen sind mathematisch fundierte Verschlüsselungsverfahren und Protokolle, die in der aktuellen Praxis nicht mit vertretbarem Aufwand gebrochen werden können. Sie basieren auf mathematisch schwer lösbaren Problemen, bieten Resistenz gegen bekannte kryptanalytische Angriffe, unterstützen ausreichend große Schlüssellängen und wurden von Experten gründlich geprüft und analysiert. Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Bei der Schlüsselerzeugung binden RHEL-Anwendungen und -Werkzeuge (OpenSSL, OpenSSH `ssh-keygen`, GnuPG) an die systemweite Crypto Policy (`update-crypto-policies`): Profile wie `DEFAULT`, `FUTURE` oder `FIPS` schließen schwache oder veraltete Algorithmen aus und erlauben nur etablierte Verfahren mit ausreichenden Schlüssellängen. Die Policy wirkt über Backend-Konfigurationen in `/etc/crypto-policies/back-ends/` auf alle angebundenen Bibliotheken; lokale Abweichungen in Dienstkonfigurationen werden durch CaC-Regeln wie `crypto_policy_not_overridden` verhindert. Institutionelle Festlegung des anerkannten Standards (z. B. BSI TR-02102) erfolgt über die Policy-Wahl bzw. angepasste Policy-Module — nicht durch Einzelkonfiguration jedes Tools.

Weitere Informationen: [Systemweite kryptografische Richtlinien](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_using-the-system-wide-cryptographic-policies_security-hardening), [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: implemented

______________________________________________________________________
