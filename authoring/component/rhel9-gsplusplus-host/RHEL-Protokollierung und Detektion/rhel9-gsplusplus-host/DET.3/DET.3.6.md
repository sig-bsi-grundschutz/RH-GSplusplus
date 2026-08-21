---
x-trestle-param-values:
  det.3.6-prm1:
  det.3.6-prm2:
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.3.6 - \[Protokollierung\] Unbestreitbarkeit

## Control Statement

Detektion für Daten KANN Nachweise für den Zusammenhang {{ insert: param, det.3.6-prm1 }} mit {{ insert: param, det.3.6-prm2 }} dokumentieren.

## Control guidance

Für Handlungen, die eine besondere Bedeutung für die rechtliche Compliance oder die korrekte Verarbeitung von Daten in kritischen Geschäftsprozessen haben, kann es sinnvoll sein, eine zweifelsfreie Zuordnung des Ereignisses zu einer Person zu gewährleisten. Beispiele können das Senden von Nachrichten als Geschäftsleitung, die Überweisung hoher Beträge auf Konten im Ausland oder der Zugang einer Nachricht mit großer rechtlicher Bedeutung sein. Für einen zweifelsfreien Nachweis reicht die einfache Zuordnung zu einem Zugangskonto oft nicht aus, da das Konto auch von anderen missbraucht worden sein könnte. Zum Nachweis können verschiedene Maßnahmen eingesetzt werden: Digitale Signaturen auf Basis asymmetrischer Kryptographie können die Urheberschaft von Dokumenten verifizieren, während Zeitstempel von vertrauenswürdigen Zeitservern die chronologische Integrität sicherstellen. Eine dezentrale Speicherung der Logs auf verschiedenen Systemen erschwert Manipulationsversuche; ergänzend erhöht die Implementierung einer Blockchain-Technologie mit verketteten Hashwerten die Fälschungssicherheit erheblich. Hardwarebasierte Sicherheitsmodule (HSMs) können kryptografische Schlüssel vor unbefugtem Zugriff schützen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Unbestreitbarkeit auf dem Host stützt sich auf eindeutige UIDs (kein zweites UID 0), vertrauenswürdige Zeit (`chronyd`) und revisionssichere Audit-Records (Immutable-Modus, Remote-Kopie). Das verknüpft ein Ereignis mit einem Zugangskonto und einem Zeitstempel, nicht rechtssicher mit einer natürlichen Person. Digitale Signaturen, HSM-Schlüssel oder Blockchain-Hashketten sind nicht Teil der RHEL-Basisprotokollierung.

Weitere Informationen: [Audit-Aufzeichnungen konfigurieren](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/assembly_configuring-audit-records_security-hardening), [Grundlegende Systemeinstellungen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/index).

### Implementation Status: partial

______________________________________________________________________
