---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.7.13 - \[Schutz vor Schadcode\] Einschränkung von Systemaufrufen

## Control Statement

Konfiguration für IT-Systeme KANN Systemaufrufe pro Anwendung einschränken.

## Control guidance

Ein Systemaufruf (engl. system call) ist dabei die Methode, mit der eine Anwendung Zugriff auf die Ressourcen des Betriebssystems anfordert, z.B. um eine Datei zu öffnen, in das Netzwerk zu kommunizieren oder einen neuen Prozess zu starten. Diese feingranulare Einschränkung wird in der Branche auch als Capability-based Security oder Seccomp (Secure Computing Mode) bezeichnet. Der Zweck dieser Vorschrift ist die gezielte Reduzierung der Angriffsfläche, indem selbst eine vertrauenswürdige, aber kompromittierte Anwendung daran gehindert wird, schädliche Aktionen auszuführen. Ein Angreifer könnte beispielsweise die Prozess-ID (PID) einer Anwendung kapern und versuchen, über deren Kontext privilegierte Systemaufrufe durchzuführen, um sich im Netzwerk auszubreiten oder sensible Daten zu löschen. Die Einschränkung dieser Aufrufe kann die Folgen eines erfolgreichen Angriffs erheblich mildern und so die Ausbreitung von Malware oder die Manipulation von Systemprozessen verhindern.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Systemaufrufe pro Anwendung schränken Container und Podman über seccomp-Profile und systemd `SystemCallFilter` ein; libseccomp definiert erlaubte Syscalls. SELinux reduziert syscall-Nutzung indirekt über MAC. Feingranulare per-App-Syscall-Allowlists erfordern Custom seccomp oder LSM-Erweiterungen — nicht Standard-Desktop-Default.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
