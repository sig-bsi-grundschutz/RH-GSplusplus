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

Einschränkung der Softwareinstallation: `dnf`/`yum` beziehen Pakete nur aus konfigurierten, gpggeprüften Repositories; Subscription Manager kanalisiert Red-Hat-Content. Privilegierte Installation bleibt an sudo/Polkit gebunden. Rootless-Nutzer können Binaries in `$HOME/.local` ablegen — fapolicyd mit deny-by-default oder organisatorische Software-Freigabe schränken Ad-hoc-Installation ein. Image-Mode- und Bootable-Container-Deployments reduzieren unkontrollierte Paketinstallation.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
