---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# KONF.4.2.1 - \[Vertrauenswürdige Basisdienste\] DNS-Verschlüsselung

## Control Statement

Konfiguration für IT-Systeme SOLLTE DNS-Verbindungen durch {{ insert: param, konf.4.2.1-prm1 }} verschlüsseln.

## Control guidance

DNS-Verschlüsselung, im Englischen oft als DNS over TLS (DoT) oder DNS over HTTPS (DoH) bezeichnet, ist ein Verfahren, bei dem Anfragen zur Namensauflösung im Internet kryptographisch geschützt werden, um deren Vertraulichkeit und Integrität sicherzustellen. Erfolgen diese Anfragen unverschlüsselt, könnte ein Angreifer im Netz die aufgerufenen Webseiten und Dienste eines Nutzers mitlesen und protokollieren. Schlimmer noch, ein Angreifer könnte die Antworten manipulieren, um den Nutzer unbemerkt auf gefälschte Webseiten umzuleiten, beispielsweise für Phishing-Angriffe. Die Aktivierung der DNS-Verschlüsselung kann einem solchen Ausspähen und Manipulieren der Namensauflösung effektiv entgegenwirken und stellt sicher, dass die Kommunikation zwischen dem Client und dem DNS-Server authentisch und nicht einsehbar ist. Nutzt das System kein DNS, so ist die Anforderung entbehrlich.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Ab RHEL 9.6 ist verschlüsseltes DNS (eDNS) als Technology Preview verfügbar: NetworkManager kann über das DNS-Plugin `dnsconfd` einen lokalen Unbound-Resolver betreiben, der Upstream-Anfragen per DNS-over-TLS (DoT) mit TLS kryptographisch schützt; alternativ kann in IdM-Umgebungen DoT zwischen Clients und integriertem DNS per `ipa-client-encrypted-dns` und `--dns-over-tls` aktiviert werden. Standardinstallationen nutzen jedoch unverschlüsselte Resolver-Konfiguration über NetworkManager; DoT muss explizit konfiguriert werden (z. B. `dns=dnsconfd`, globale `dns+tls://`-Server, optional Kernel-Argumente für frühen Boot). DNS-over-HTTPS wird in der RHEL-9-Dokumentation nicht als gleichwertige Systemoption beschrieben. Ob DNS genutzt wird und welche DoT-Server vertrauenswürdig sind, legt die Institution fest.

Weitere Informationen: [Technology Previews in RHEL 9.6](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/9.6_release_notes/technology-previews)

### Implementation Status: partial

______________________________________________________________________
