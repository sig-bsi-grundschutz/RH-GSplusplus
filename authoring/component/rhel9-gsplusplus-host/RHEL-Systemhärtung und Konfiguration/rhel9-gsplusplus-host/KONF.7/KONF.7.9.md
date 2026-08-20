---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.9 - \[Schutz vor Schadcode\] Einschränkung der Installation

## Control Statement

Konfiguration für IT-Systeme SOLLTE die Installation von Anwendungen einschränken.

## Control guidance

Es empfiehlt sich z.B. die zu installierende Software nicht unkontrolliert in das Wurzeldateisystem des Betriebssystems zu installieren. Wenn die zu installierende Software aus dem Quellcode kompiliert werden soll, dann empfiehlt es sich diese nur unter einem unprivilegierten Konto zu entpacken, zu konfigurieren und zu übersetzen.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Die Installation von Paketen via `dnf` ist an `sudo` gebunden. Rootless-Nutzer können Binaries in `$HOME/.local` ablegen. `fapolicyd` kann mit deny-by-default die Ad-hoc-Installation und Nutzung von Software einschränken. Eine Alternative ist der Einsatz von Image-Mode. Hier sind auf einem System ohne Build-Prozess Softwareinstallationen stark eingeschränkt.

Weitere Informationen: [Image Mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index), [fapolicyd](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_blocking-and-allowing-applications-using-fapolicyd_security-hardening)

### Rules:

  - fapolicy_default_deny
  - package_fapolicyd_installed
  - service_fapolicyd_enabled

<!-- implemented, da wir technisch hier nichts prüfen können. Es ist default-verhalten -->
### Implementation Status: implemented

______________________________________________________________________
