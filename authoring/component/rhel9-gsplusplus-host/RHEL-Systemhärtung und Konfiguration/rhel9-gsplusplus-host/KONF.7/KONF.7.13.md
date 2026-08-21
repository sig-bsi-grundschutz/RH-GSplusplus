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

Für klassische Services erlaubt `systemd` die Filterung erlaubter Kernelcalls (Systemaufrufe) über die Spezifizierung von `SystemCallFilter` in der System-Unit können entweder über allow- oder über deny-listing entsprechende Kernelcalls eingeschränkt werden. Für containerisierte Anwendungen erlaubt `podman` das Aufzeichnen von Systemaufrufen (`sudo podman run --annotation io.containers.trace-syscall=of:/tmp/ls.json fedora:30 ls / > /dev/null`) und Speichern selbiger in einer Datei. Diese kann dann bei nachfolgenden Aufrufen des Containers als Allow-List mitgegeben werden (`sudo podman run --security-opt seccomp=/tmp/ls.json fedora ls -l / > /dev/null`). Für die Definition der SecComp-Profile ist zu berücksichtigen, dass sie den vollständigen Anwendungsfunktionsumfang abbilden müssen und daher während der automatisierten Tests der Anwendung erzeugt werden sollten. Nicht aufgezeichnete - und damit fehlende - Systemcalls können zu Fehlfunktionen der Anwendung um Produktivbetrieb führen. Weiterhin ist das Seccomp-Profil mit der Anwendung über Umgebungen zu transportieren (bspw. als RPM).

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index), [SystemCallFilter](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html), [Podman Seccomp](https://www.redhat.com/en/blog/container-security-seccomp)

<!-- This cannot be checked automatically by rules, as the institution needs to take care of specifying this profiles -->
### Implementation Status: not-applicable

______________________________________________________________________
