#!/usr/bin/env python3
"""
Regenerate mappings/rhel9_gsplusplus_overrides.json from the BSI catalog.

Preserves hand-curated entries for selected controls; generates doc.redhat.com-oriented
overrides (doc_keys + English statements) for every catalog control using:
  - top-level Grundschutz++ practice area (GC, KONF, …)
  - German keyword hints in the control title

Run from repo root:
  python3 scripts/build_gsplusplus_overrides.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalogs/bsi-grundschutz-plus-plus/catalog.json"
OUT = ROOT / "mappings/rhel9_gsplusplus_overrides.json"

# Curated controls (authoritative — do not overwrite)
CURATED: dict[str, dict] = {
    "GC.1.1": {
        "implementation_status": "partial",
        "statement": "RHEL 9 is a controlled platform for building an ISMS scope; organizational scoping, asset inventory, and governance remain customer responsibilities. Product documentation supports security-relevant deployment and lifecycle practices.",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "GC.2.1": {
        "implementation_status": "partial",
        "statement": "Regulatory and contractual requirements are interpreted and applied by the customer; RHEL provides configurable technical controls (audit, crypto, identity, MAC) to help meet common obligations when properly deployed.",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "GC.3.1": {
        "implementation_status": "partial",
        "statement": "Policies and procedures are owned by the institution; RHEL supplies security hardening guides, crypto frameworks, and automation-friendly interfaces (e.g. OpenSCAP, system roles).",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "GC.4.1": {
        "implementation_status": "partial",
        "statement": "Management commitment and roles are organizational; RHEL supports delegated administration (sudo, RBAC integrations via SSSD) consistent with customer-defined roles.",
        "rule_ids": [],
        "doc_keys": ["sssd"],
    },
    "GC.5.1": {
        "implementation_status": "partial",
        "statement": "Risk treatment plans are customer-owned; RHEL offers documented hardening paths and compliance-oriented profiles in scap-security-guide to reduce technical risk when selected and applied.",
        "rule_ids": ["installed_OS_is_vendor_supported"],
        "doc_keys": ["security_hardening", "updates"],
    },
    "GC.6.1": {
        "implementation_status": "partial",
        "statement": "Third-party and supply-chain governance is shared: Red Hat signs content and publishes errata; customers verify signatures and subscribe to update channels appropriate to their assurance needs.",
        "rule_ids": ["ensure_redhat_gpgkey_installed", "ensure_gpgcheck_globally_activated"],
        "doc_keys": ["updates"],
    },
    "GC.7.1": {
        "implementation_status": "partial",
        "statement": "Incident handling processes are organizational; RHEL provides auditd, journaling, and integrations for centralized logging when configured by the customer.",
        "rule_ids": ["service_auditd_enabled"],
        "doc_keys": ["audit"],
    },
    "GC.8.1": {
        "implementation_status": "partial",
        "statement": "Business continuity is customer-designed; RHEL supports backup-friendly storage, high-availability patterns, and reproducible configuration via automation.",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "GC.9.1": {
        "implementation_status": "partial",
        "statement": "Data protection impact and privacy engineering are contextual; RHEL provides disk encryption (LUKS), TLS stacks, and MAC (SELinux) as technical building blocks.",
        "rule_ids": ["enable_dracut_fips_module"],
        "doc_keys": ["managing_encryption", "selinux"],
    },
    "GC.10.1": {
        "implementation_status": "partial",
        "statement": "Awareness and training are organizational; Red Hat documents security features so administrators can operate RHEL consistently with institutional standards.",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "STM.1.1": {
        "implementation_status": "partial",
        "statement": "Network segmentation and zoning are implemented with customer topology; RHEL provides firewalld, nftables, and routing features to enforce host-level network policy.",
        "rule_ids": ["service_firewalld_enabled"],
        "doc_keys": ["firewalld"],
    },
    "STM.1.2": {
        "implementation_status": "partial",
        "statement": "Remote access controls depend on customer services; RHEL ships OpenSSH and PAM, configurable to disallow root login, enforce key-based auth, and integrate with enterprise identity.",
        "rule_ids": ["sshd_disable_root_login"],
        "doc_keys": ["security_hardening"],
    },
    "STM.2.1": {
        "implementation_status": "implemented",
        "statement": "RHEL 9 includes SELinux (MAC) and documented policies; enforcing mode is supported and recommended for many deployments when compatible with workloads.",
        "rule_ids": ["selinux_state"],
        "doc_keys": ["selinux"],
    },
    "STM.3.1": {
        "implementation_status": "partial",
        "statement": "Malware mitigation combines customer process with technical controls: package signing, minimal installation, and Security-Enhanced Linux reduce exposure; additional AV/EDR is customer-chosen.",
        "rule_ids": ["package_aide_installed"],
        "doc_keys": ["security_hardening"],
    },
    "STM.4.1": {
        "implementation_status": "partial",
        "statement": "Patch and vulnerability management uses customer processes; RHEL provides dnf, Red Hat Errata, and tools to evaluate system security posture (OpenSCAP) when installed.",
        "rule_ids": ["security_patches_up_to_date"],
        "doc_keys": ["updates"],
    },
    "STM.4.2": {
        "implementation_status": "partial",
        "statement": "Secure configuration baselines can be applied using scap-security-guide profiles, system roles, or image builders; the exact baseline is customer-selected.",
        "rule_ids": [],
        "doc_keys": ["security_hardening"],
    },
    "STM.5.1": {
        "implementation_status": "partial",
        "statement": "Logging and monitoring use auditd, systemd journal, and rsyslog; forwarding to SIEM is customer-configured.",
        "rule_ids": ["service_auditd_enabled"],
        "doc_keys": ["audit"],
    },
    "STM.5.2": {
        "implementation_status": "partial",
        "statement": "Time synchronization for audit correlation is typically provided by chrony; customers point strata to trusted time sources.",
        "rule_ids": [],
        "doc_keys": ["systemd"],
    },
}

# (keywords in title, doc_keys to add, capability clause for statement)
KEYWORD_RULES: list[tuple[tuple[str, ...], list[str], str]] = [
    (
        (
            "netzwerk",
            "netz",
            "firewall",
            "vpn",
            "fernzugriff",
            "remote",
            "zugriff extern",
            "wlan",
            "dns",
            "routing",
        ),
        ["firewalld", "networking"],
        "Host networking policy (firewalld, nftables, SSH, and IP configuration) is described for RHEL.",
    ),
    (
        (
            "verschlüssel",
            "krypt",
            "tls",
            "zertifikat",
            "cipher",
            "schlüssel",
            "fips",
            "crypto",
        ),
        ["managing_encryption"],
        "Disk, transport, and application crypto (OpenSSL/NSS, LUKS, certificate handling) are covered in RHEL security guides.",
    ),
    (
        (
            "authentifiz",
            "identität",
            "anmeldung",
            "passwort",
            "konto",
            "berechtigung",
            "rolle",
            "sudo",
            "privileg",
            "ldap",
            "kerberos",
            "sso",
        ),
        ["sssd"],
        "Authentication and authorization integration (PAM, SSSD, identity stores) is documented for RHEL.",
    ),
    (
        (
            "protokoll",
            "logging",
            "audit",
            "protokollierung",
            "nachvollzieh",
            "überwachung technisch",
            "ereignis",
        ),
        ["audit"],
        "Audit records and system journaling (auditd, systemd journal, forwarding) are described for RHEL.",
    ),
    (
        ("patch", "update", "schwachstelle", "schwachstell", "errata", "cve"),
        ["updates"],
        "Patching and software maintenance use DNF, subscription tooling, and Red Hat Errata as documented.",
    ),
    (
        ("container", "podman", "oci", "image"),
        ["podman"],
        "Container workloads on RHEL use Podman and related tooling as documented.",
    ),
    (
        ("backup", "sicherung", "wiederherstellung", "restore"),
        ["storage"],
        "Storage layout, snapshots, and backup-oriented workflows are supported as described in RHEL storage guides.",
    ),
    (
        ("kernel", "sysctl", "modul", "treiber"),
        ["kernel"],
        "Kernel tuning, module controls, and driver behavior are covered in RHEL kernel administration guides.",
    ),
    (
        ("scan", "compliance", "schwachstellenanalyse", "bewertung sicherheit"),
        ["openscap"],
        "OpenSCAP-based compliance and vulnerability scanning is documented for RHEL.",
    ),
    (
        ("software", "entwicklung", "code", "deployment", "pipeline", "build"),
        ["openscap", "security_hardening"],
        "Secure engineering on RHEL can leverage hardening guidance and automated compliance checks.",
    ),
    (
        ("speicher", "festplatte", "luks", "datenträger"),
        ["storage", "managing_encryption"],
        "Disk encryption and block storage management use LUKS and related RHEL storage documentation.",
    ),
    (
        ("recht", "datenschutz", "personenbezogen", "ds-gvo", "dsgvo"),
        ["security_hardening"],
        "Legal and privacy interpretation is organizational; RHEL supplies configurable technical controls as building blocks.",
    ),
    (
        ("physikalisch", "gebäude", "zutritt", "raum"),
        ["security_hardening"],
        "Physical and facility controls are outside the OS; RHEL documentation still supports secure operation of in-room systems.",
    ),
    (
        ("dienstleister", "lieferant", "cloud", "outsourcing"),
        ["security_hardening", "updates"],
        "Supplier and service-provider governance is primarily procedural; RHEL supports verifiable patching and hardening of vendor-managed stacks when you operate the OS.",
    ),
    (
        ("notfall", "kontinuität", "wiederanlauf"),
        ["storage", "security_hardening"],
        "Business continuity design is customer-owned; RHEL supports resilient configuration and recovery-oriented tooling.",
    ),
    (
        ("leistung", "performance", "kapazität", "verfügbarkeit"),
        ["monitoring"],
        "Performance and availability monitoring uses standard RHEL observability tooling as documented.",
    ),
    (
        ("systemd", "dienst", "service", "daemon"),
        ["systemd"],
        "Service management with systemd and boot configuration is covered in basic system settings documentation.",
    ),
    (
        ("malware", "viren", "schadsoftware", "anti"),
        ["selinux", "security_hardening"],
        "Malware risk reduction uses MAC, package integrity, and minimal attack surface patterns documented for RHEL.",
    ),
]

GROUP_META: dict[str, tuple[str, str, list[str]]] = {
    "GC": (
        "Governance and compliance",
        "Institutions define ISMS scope, policy, and accountability; the OS is one technical layer.",
        ["security_hardening"],
    ),
    "STM": (
        "Structure modeling",
        "Requirements are structured into packages and target objects; RHEL features help where measures apply to hosts.",
        ["security_hardening", "audit"],
    ),
    "UMS": (
        "Implementation",
        "Measures are applied to systems and services; RHEL provides configurable security and lifecycle tooling.",
        ["security_hardening", "updates"],
    ),
    "VRB": (
        "Improvement",
        "Continuous improvement uses measurement and feedback; RHEL supports audits and scans of configured systems.",
        ["security_hardening", "openscap"],
    ),
    "PERF": (
        "Monitoring and evaluation",
        "Monitoring and review of effectiveness can use host telemetry, audit trails, and performance tooling.",
        ["monitoring", "audit"],
    ),
    "RISK": (
        "Risk management",
        "Risk treatment selects controls; RHEL reduces technical exposure when hardened and patched per documentation.",
        ["security_hardening", "updates"],
    ),
    "ASST": (
        "Information and assets",
        "Asset and information handling may rely on labeling, encryption, and access control features of the platform.",
        ["security_hardening", "managing_encryption"],
    ),
    "PERS": (
        "Personnel",
        "Personnel security is organizational; RHEL documentation supports administrators in applying least privilege and identity integration.",
        ["security_hardening", "sssd"],
    ),
    "BES": (
        "Procurement",
        "Procurement and sourcing are organizational; RHEL content integrity and supportability are described for installed systems.",
        ["security_hardening", "updates"],
    ),
    "DLS": (
        "Service provider control",
        "Managing providers is procedural; for RHEL instances you operate, hardening and patch practices remain applicable.",
        ["security_hardening", "updates"],
    ),
    "TEST": (
        "Changes and tests",
        "Testing changes before production can include OpenSCAP evaluation and staged configuration on RHEL systems.",
        ["openscap", "security_hardening"],
    ),
    "GEB": (
        "Facility management",
        "Facility and physical security are outside the OS; RHEL still documents secure operation of servers located on premises.",
        ["security_hardening"],
    ),
    "SENS": (
        "Awareness",
        "Awareness is organizational; Red Hat product docs explain security features administrators must configure.",
        ["security_hardening"],
    ),
    "ARCH": (
        "Architecture",
        "Architecture choices may include network segmentation, containers, and crypto; RHEL documentation covers these building blocks.",
        ["networking", "security_hardening", "podman"],
    ),
    "BER": (
        "Authorization",
        "Authorization and entitlement enforcement maps to identity integration, SELinux, and privilege management on RHEL.",
        ["sssd", "selinux", "security_hardening"],
    ),
    "NOT": (
        "Contingency planning",
        "Contingency and recovery planning is customer-owned; RHEL supports backups, storage, and reproducible configuration.",
        ["storage", "security_hardening"],
    ),
    "DET": (
        "Detection",
        "Detection may leverage host audit, logging, and monitoring integrations described for RHEL.",
        ["audit", "monitoring", "security_hardening"],
    ),
    "REA": (
        "Security incident handling",
        "Incident handling processes are organizational; RHEL supplies logs, audit trails, and forensic-friendly interfaces when enabled.",
        ["audit", "security_hardening"],
    ),
    "KONF": (
        "Configuration",
        "Secure configuration spans services, MAC, crypto, updates, and network hardening on RHEL hosts.",
        ["updates", "selinux", "audit", "firewalld", "security_hardening"],
    ),
    "DEV": (
        "Development",
        "Secure development and deployment on RHEL can use hardening guides, compliance scanning, and container tooling.",
        ["openscap", "security_hardening", "podman"],
    ),
}


def _walk_groups(group: dict, top_id: str, out: list[tuple[str, dict]]) -> None:
    for ctrl in group.get("controls") or []:
        out.append((top_id, ctrl))
    for sg in group.get("groups") or []:
        _walk_groups(sg, top_id, out)


def _load_controls_by_top() -> list[tuple[str, dict]]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    cat = data["catalog"]
    rows: list[tuple[str, dict]] = []
    for g in cat.get("groups") or []:
        top = g.get("id", "")
        _walk_groups(g, top, rows)
    return rows


def _dedupe_keys(keys: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for k in keys:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out


def _match_keywords(title: str) -> tuple[list[str], list[str]]:
    t = title.lower()
    extra_keys: list[str] = []
    clauses: list[str] = []
    for keywords, keys, clause in KEYWORD_RULES:
        if any(kw in t for kw in keywords):
            extra_keys.extend(keys)
            if clause not in clauses:
                clauses.append(clause)
    return extra_keys, clauses


def _generate_entry(top: str, ctrl: dict) -> dict:
    cid = ctrl["id"]
    title = (ctrl.get("title") or "").strip()
    meta = GROUP_META.get(
        top,
        (
            "General practice",
            "This practice may touch systems running RHEL; apply product documentation where technical measures apply.",
            ["security_hardening"],
        ),
    )
    group_name, group_blurb, base_keys = meta
    kw_keys, clauses = _match_keywords(title)
    doc_keys = _dedupe_keys(base_keys + kw_keys)
    if not clauses:
        cap = (
            "general security hardening, identity, logging, updates, and network controls as documented for RHEL 9."
        )
    else:
        cap = " ".join(clauses)
    statement = (
        f"**{cid}** — *{title}* ({group_name}, BSI Grundschutz++). {group_blurb} "
        f"On **Red Hat Enterprise Linux 9** hosts, relevant product documentation addresses: {cap} "
        "Broader ISMS, organizational, physical, or supplier context beyond the OS remains the customer's responsibility. "
        "This statement is not a legal interpretation of the German catalog text."
    )
    return {
        "implementation_status": "partial",
        "statement": statement,
        "rule_ids": [],
        "doc_keys": doc_keys,
    }


def main() -> None:
    rows = _load_controls_by_top()
    by_id: dict[str, dict] = {}
    for top, ctrl in rows:
        cid = ctrl["id"]
        if cid in CURATED:
            by_id[cid] = json.loads(json.dumps(CURATED[cid]))
        else:
            by_id[cid] = _generate_entry(top, ctrl)

    if len(by_id) != len(rows):
        raise SystemExit(f"internal error: expected {len(rows)} controls, got {len(by_id)}")

    OUT.write_text(
        json.dumps(
            {
                "_generated_by": "scripts/build_gsplusplus_overrides.py",
                "_note": "Curated controls preserved; others generated from catalog group + German title keywords.",
                "controls": dict(sorted(by_id.items())),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(by_id)} control overrides to {OUT}")


if __name__ == "__main__":
    main()
