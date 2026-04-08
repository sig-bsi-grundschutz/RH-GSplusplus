#!/usr/bin/env python3
"""Generate OSCAL profile (full Grundschutz++ catalog) and RHEL 9 component-definition."""
from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path

NS_URL = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
TRESTLE_RULE_NS = "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd"


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _req_uuid(control_id: str) -> str:
    return str(uuid.uuid5(NS_URL, f"rhel9-gsplusplus:{control_id}"))


def _walk_groups(group: dict, out: list[dict]) -> None:
    for ctrl in group.get("controls") or []:
        out.append(ctrl)
    for sub in group.get("groups") or []:
        _walk_groups(sub, out)


def load_catalog_controls(catalog: dict) -> list[dict]:
    cat = catalog.get("catalog", catalog)
    controls: list[dict] = []
    for g in cat.get("groups") or []:
        _walk_groups(g, controls)
    controls.sort(key=lambda c: c["id"])
    return controls


def _default_statement(template: str, control_id: str, title: str) -> str:
    return template.replace("{control_id}", control_id).replace("{title}", title or control_id)


def build_profile_json(config: dict, control_ids: list[str]) -> dict:
    prof = config["profile"]
    last_mod = (config.get("artifact_metadata") or {}).get("profile_last_modified", "2026-01-01T00:00:00.000Z")
    return {
        "profile": {
            "uuid": prof["uuid"],
            "metadata": {
                "title": prof["metadata_title"],
                "last-modified": last_mod,
                "version": prof["metadata_version"],
                "oscal-version": "1.1.3",
                "remarks": (
                    "Includes every control from the vendored BSI Anwenderkatalog Grundschutz++ "
                    "(see catalogs/bsi-grundschutz-plus-plus/catalog.json)."
                ),
            },
            "imports": [
                {
                    "href": "trestle://catalogs/bsi-grundschutz-plus-plus/catalog.json",
                    "include-controls": [{"with-ids": control_ids}],
                }
            ],
            "merge": {"combine": {"method": "merge"}, "as-is": True},
        }
    }


def build_implemented_requirements(
    controls: list[dict],
    config: dict,
    overrides_by_id: dict[str, dict],
) -> list[dict]:
    docs = config["docs"]
    defaults = config["defaults"]
    default_status = defaults["implementation_status"]
    default_doc_keys = defaults["doc_keys"]
    template = defaults["statement_template"]

    implemented: list[dict] = []
    for ctrl in controls:
        cid = ctrl["id"]
        title = (ctrl.get("title") or "").strip()
        ov = overrides_by_id.get(cid, {})

        statement = ov.get("statement") or _default_statement(template, cid, title)
        impl_status = ov.get("implementation_status", default_status)
        doc_keys = ov.get("doc_keys", default_doc_keys)

        doc_links = []
        for k in doc_keys:
            href = docs.get(k)
            if href:
                doc_links.append({"href": href, "rel": "reference", "text": k.replace("_", " ")})

        props: list[dict] = [
            {"name": "implementation-status", "ns": TRESTLE_RULE_NS, "value": impl_status},
        ]
        for rid in ov.get("rule_ids") or []:
            props.append({"name": "Rule_Id", "ns": TRESTLE_RULE_NS, "value": rid})

        entry: dict = {
            "uuid": _req_uuid(cid),
            "control-id": cid,
            "description": statement,
            "props": props,
        }
        if doc_links:
            entry["links"] = doc_links
        implemented.append(entry)

    return implemented


def build_component_definition_json(
    config: dict,
    implemented: list[dict],
) -> dict:
    cd_cfg = config["component_definition"]
    prod = config["product"]
    docs = config["docs"]
    last_mod = (config.get("artifact_metadata") or {}).get(
        "component_definition_last_modified", "2026-01-01T00:00:00.000Z"
    )
    source = config.get("profile_source_href") or "trestle://profiles/rhel9-gsplusplus-full/profile.json"

    return {
        "component-definition": {
            "uuid": cd_cfg["uuid"],
            "metadata": {
                "title": cd_cfg["metadata_title"],
                "last-modified": last_mod,
                "version": cd_cfg["metadata_version"],
                "oscal-version": "1.1.3",
                "remarks": (
                    "Implementation statements cover the full BSI Grundschutz++ Anwenderkatalog control set "
                    "as imported by the companion profile. Defaults are English product-positioning text; "
                    "curated ComplianceAsCode rule IDs appear only where listed in "
                    "mappings/rhel9_gsplusplus_overrides.json. Not a certification or legal interpretation."
                ),
            },
            "components": [
                {
                    "uuid": cd_cfg["component_uuid"],
                    "type": prod["type"],
                    "title": prod["title"],
                    "description": (
                        "Red Hat Enterprise Linux 9 is a general-purpose operating environment. "
                        "Technical effectiveness depends on image selection, configuration, connected services, "
                        "and organizational processes described in Red Hat product documentation."
                    ),
                    "links": [
                        {
                            "href": docs.get("security_hardening", "https://docs.redhat.com/"),
                            "rel": "reference",
                            "text": "RHEL 9 Security hardening (docs.redhat.com)",
                        },
                        {
                            "href": "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek",
                            "rel": "reference",
                            "text": "BSI Stand der Technik Bibliothek (Grundschutz++)",
                        },
                    ],
                    "control-implementations": [
                        {
                            "uuid": cd_cfg["control_implementation_uuid"],
                            "source": source,
                            "description": (
                                "Full-catalog control implementations generated from the BSI Grundschutz++ "
                                "catalog plus mappings/rhel9_gsplusplus.json defaults and "
                                "mappings/rhel9_gsplusplus_overrides.json."
                            ),
                            "implemented-requirements": implemented,
                        }
                    ],
                }
            ],
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=Path,
        default=_repo_root() / "mappings" / "rhel9_gsplusplus.json",
    )
    args = parser.parse_args()
    root = _repo_root()
    config = json.loads((root / args.config).read_text(encoding="utf-8"))

    cat_path = root / config["catalog_relative_path"]
    catalog = json.loads(cat_path.read_text(encoding="utf-8"))
    controls = load_catalog_controls(catalog)
    control_ids = [c["id"] for c in controls]

    ov_path = root / config["overrides_relative_path"]
    overrides_blob = json.loads(ov_path.read_text(encoding="utf-8"))
    overrides_by_id = overrides_blob.get("controls") or {}

    profile_doc = build_profile_json(config, control_ids)
    profile_out = root / config["profile_output_path"]
    profile_out.parent.mkdir(parents=True, exist_ok=True)
    profile_out.write_text(json.dumps(profile_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {profile_out} ({len(control_ids)} controls)")

    implemented = build_implemented_requirements(controls, config, overrides_by_id)
    cd_doc = build_component_definition_json(config, implemented)
    cd_out = root / config["component_definition"]["output_path"]
    cd_out.parent.mkdir(parents=True, exist_ok=True)
    cd_out.write_text(json.dumps(cd_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {cd_out} ({len(implemented)} implemented-requirements)")


if __name__ == "__main__":
    main()
