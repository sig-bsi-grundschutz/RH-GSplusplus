---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.1 - \[Schutz vor Schadcode\] Echtzeitscanner

## Control Statement

Konfiguration für IT-Systeme SOLLTE eine automatische Prüfung auf Schadcode bei Installation oder Öffnung von Dateien aktivieren.

## Control guidance

Schadcode kann sich sowohl auf lokalen Speichermedien, als auch auf Netzlaufwerken oder Wechseldatenträgern befinden. Für Netzlaufwerke kann die Anforderung auch umgesetzt werden, indem Dateien bei der Speicherung auf dem zentralen System auf Schadcode geprüft werden. Die Anwendung zur Schadcodeprüfung kann z.B. auch als EDR, XDR oder IDS bezeichnet werden. Moderne Systeme zur Erkennung von Schadcode verwenden eine Kombination aus Virensignaturen, Heuristiken, als auch Anomalieerkennung. Falls das System die Installation von Anwendungen nicht unterstützt, so ist dieser Teilschritt entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Echtzeit-Prüfung beim Öffnen oder Installieren wie klassische AV-Scanner liefert RHEL nicht als unterstützten Teil des Produkts. Stattdessen sind mehrere mitigierende Maßnahmen im Einsatz, die darauf abzielen einer Schadcode-Infizierung entgegenzuwirken. Der Image-Mode in Red Hat verhindert das klassische Installieren von Software und erfordert einen Build-Prozess des Betriebssystems vorab. Hierdurch ist das aktive Betriebssystem immutable und zu großen Teilen Read-Only. Hierdurch würde die Anforderung erfüllt (keine Software installierbar). Für klassische RHEL Installationen stellt Red Hat installierbare Software als RPM bereit. `dnf` verifiziert bei Paketinstallation die GPG-Signaturen aus den konfigurierten Repositories (`gpgcheck=1`, Red-Hat-GPG-Schlüssel). Red Hat selbst baut entsprechende Softwarepakete gemäß [SLSA](https://slsa.dev/) Level 3 (Supply-Chain Levels for Software Artifacts) um eine entsprechende Kompromitierung zu verhindern. Real-time-Malware-Scans werden von durch Red Hat nicht supportete Drittanbieter (z. B. [ClamAV](https://access.redhat.com/solutions/22007) via EPEL [Extra Packages for Enterprise Linux](https://access.redhat.com/solutions/3358)) bereitgestellt und können entsprechend der [Third Party Support Guidelines](https://access.redhat.com/articles/third-party-software-support) genutzt werden.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [SLSA](https://slsa.dev/), [ClamAV](https://access.redhat.com/solutions/22007), [Extra Packages for Enterprise Linux](https://access.redhat.com/solutions/3358), [Image Mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index)

### Rules:

  - install_endpoint_security_software,
  - ensure_gpgcheck_globally_activated
  - ensure_gpgcheck_never_disabled
  - ensure_gpgcheck_local_packages

### Implementation Status: alternative

______________________________________________________________________
