---
x-trestle-global:
  profile:
    title: Red Hat Enterprise Linux 9 — Grundschutz++ (Host-Umfang, kuratiert)
    href: trestle://profiles/rhel9-gsplusplus-host/profile.json
---

# DET.4.8 - \[Überwachung von Aktivitäten\] Ausstellung neuer HTTPS-Zertifikate

## Control Statement

Detektion für Webserver KANN die rechtzeitige Ausstellung neuer HTTPS-Zertifikate für Hostsysteme, die im Internet erreichbar sind, überwachen.

## Control guidance

„Rechtzeitige Ausstellung neuer HTTPS-Zertifikate“ meint hier, dass überwacht wird, ob vor Ablauf eines bestehenden TLS-/HTTPS-Zertifikats ein neues, gültiges und zur jeweiligen Webserver-Identität passendes Zertifikat aktiviert wird (certificate expiry monitoring, certificate renewal). „HTTPS-Zertifikate“ sind hier X.509-Zertifikate für TLS-gesicherte Webverbindungen, die insbesondere Servernamen, Gültigkeitszeitraum, ausstellende Zertifizierungsstelle und kryptografische Bindung an einen Schlüssel enthalten. „Server, die im Internet erreichbar sind“ bezeichnet Webserver mit öffentlich erreichbarer Adresse oder öffentlich auflösbarem Namen, etwa Webportale, APIs, Kundenportale oder Administrationsoberflächen, sofern sie aus dem Internet angesprochen werden können. Die Vorschrift zielt darauf ab, ablaufende oder nicht rechtzeitig erneuerte Zertifikate frühzeitig sichtbar zu machen: Ein versäumter Austausch könnte zu Browserwarnungen, Dienstunterbrechungen, fehlgeschlagenen API-Verbindungen, Vertrauensverlust bei Nutzenden oder improvisierten Notfallmaßnahmen führen. Eine entsprechende Detektion kann die Verfügbarkeit und Vertrauenswürdigkeit öffentlich erreichbarer Webdienste unterstützen und kann zugleich Hinweise auf Fehlkonfigurationen, unvollständige Automatisierung oder unerwartete Änderungen im Zertifikatsbestand liefern. Hierbei ist es sinnvoll nicht nur die Restlaufzeit mit Schwellwerten zu überwachen, sondern auch die tatsächliche Bereitstellung des neuen Zertifikates. Dazu können ein Monitoring der Zertifikatsdaten direkt am Webendpunkt, sowie Auswertungen aus Load-Balancern oder Reverse-Proxys gehören.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Für öffentlich erreichbare TLS-Endpunkte auf RHEL überwacht `certmonger` (typisch mit IdM/IPA) Ablauf und erneuert Zertifikate rechtzeitig; alternativ prüft die Institution das am Load-Balancer oder per externem Certificate-Monitoring. CaC enthält keine Regel, die Zertifikatsablauf oder erfolgreiche Bereitstellung prüft (im Gegenteil existiert `service_certmonger_disabled` für Minimalinstallationen). Ob das neue Zertifikat tatsächlich am Webendpunkt aktiv ist, bleibt Monitoring außerhalb der Basis-Härtung.

Weitere Informationen: [Sicherheitshärtung](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/index).

### Implementation Status: partial

______________________________________________________________________
