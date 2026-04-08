#!/usr/bin/env python3
"""Build component-definition.json from mappings/rhel9_gsplusplus_slice.json."""
from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

NS_URL = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
TRESTLE_RULE_NS = "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd"


def _now_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def _req_uuid(control_id: str) -> str:
    return str(uuid.uuid5(NS_URL, f"rhel9-gsplusplus:{control_id}"))


def build_component_definition(mapping: dict, *, cd_uuid: str, component_uuid: str, ci_uuid: str) -> dict:
    profile_href = mapping["profile_relative_path"]
    docs = mapping["docs"]
    prod = mapping["product"]
    last_mod = (mapping.get("artifact_metadata") or {}).get("component_definition_last_modified") or _now_z()

    implemented = []
    for row in mapping["controls"]:
        cid = row["control_id"]
        doc_keys = row.get("doc_keys") or []
        doc_links = []
        for k in doc_keys:
            href = docs.get(k)
            if href:
                doc_links.append({"href": href, "rel": "reference", "text": k.replace("_", " ")})

        props = [
            {
                "name": "implementation-status",
                "ns": TRESTLE_RULE_NS,
                "value": row["implementation_status"],
            }
        ]
        for rid in row.get("rule_ids") or []:
            props.append(
                {
                    "name": "Rule_Id",
                    "ns": TRESTLE_RULE_NS,
                    "value": rid,
                }
            )

        entry: dict = {
            "uuid": _req_uuid(cid),
            "control-id": cid,
            "description": row["statement"],
            "props": props,
        }
        if doc_links:
            entry["links"] = doc_links
        implemented.append(entry)

    return {
        "component-definition": {
            "uuid": cd_uuid,
            "metadata": {
                "title": f'{prod["title"]} — Grundschutz++ implementation (pilot slice)',
                "last-modified": last_mod,
                "version": "0.1.0",
                "oscal-version": "1.1.3",
                "remarks": (
                    "Implementation statements describe how Red Hat Enterprise Linux 9 can contribute to "
                    "selected Grundschutz++ controls when deployed and operated by the customer. "
                    "This is not a certification or legal interpretation of BSI requirements."
                ),
            },
            "components": [
                {
                    "uuid": component_uuid,
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
                            "uuid": ci_uuid,
                            "source": f"trestle://{profile_href}",
                            "description": (
                                "Control implementations mapped from the pilot Grundschutz++ profile slice; "
                                "see mappings/rhel9_gsplusplus_slice.json and ComplianceAsCode rule identifiers where present."
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
        "--mapping",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "mappings" / "rhel9_gsplusplus_slice.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "component-definitions"
        / "rhel9-gsplusplus-slice"
        / "component-definition.json",
    )
    parser.add_argument(
        "--cd-uuid",
        default="8376b619-3755-4be7-afa7-5f58c014779b",
        help="Root component-definition UUID (change when document meaningfully changes).",
    )
    parser.add_argument(
        "--component-uuid",
        default="e5f5e589-d6a7-4530-b40b-25c50dfe97ad",
    )
    parser.add_argument(
        "--ci-uuid",
        default="ac121dff-877d-4be2-8aa1-a6961bf05242",
    )
    args = parser.parse_args()

    mapping = json.loads(args.mapping.read_text(encoding="utf-8"))
    doc = build_component_definition(
        mapping,
        cd_uuid=args.cd_uuid,
        component_uuid=args.component_uuid,
        ci_uuid=args.ci_uuid,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
