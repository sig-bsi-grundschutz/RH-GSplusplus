#!/usr/bin/env python3
"""Generate scoped OSCAL profile and component-definition for a Red Hat GS++ product artifact."""
from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path

NS_URL = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
TRESTLE_RULE_NS = "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd"


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _uuid(artifact_id: str, suffix: str) -> str:
    return str(uuid.uuid5(NS_URL, f"{artifact_id}:{suffix}"))


def _walk_controls(controls: list[dict], out: list[dict]) -> None:
    for ctrl in controls:
        out.append(ctrl)
        nested = ctrl.get("controls") or []
        if nested:
            _walk_controls(nested, out)


def _walk_groups(group: dict, out: list[dict]) -> None:
    _walk_controls(group.get("controls") or [], out)
    for sub in group.get("groups") or []:
        _walk_groups(sub, out)


def load_catalog_controls(catalog: dict) -> list[dict]:
    cat = catalog.get("catalog", catalog)
    controls: list[dict] = []
    for g in cat.get("groups") or []:
        _walk_groups(g, controls)
    return controls


def _default_statement(template: str, control_id: str, title: str) -> str:
    return template.replace("{control_id}", control_id).replace("{title}", title or control_id)


def load_json(root: Path, rel: str) -> dict:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def build_profile_json(config: dict, control_ids: list[str]) -> dict:
    prof = config["profile"]
    artifact_id = config["artifact_id"]
    last_mod = (config.get("artifact_metadata") or {}).get(
        "profile_last_modified", "2026-01-01T00:00:00.000Z"
    )
    return {
        "profile": {
            "uuid": prof.get("uuid") or _uuid(artifact_id, "profile"),
            "metadata": {
                "title": prof["metadata_title"],
                "last-modified": last_mod,
                "version": prof["metadata_version"],
                "oscal-version": "1.1.3",
                "remarks": (
                    "Scoped host-applicability profile for Red Hat Enterprise Linux. "
                    "Organizational Grundschutz++ controls remain in the BSI catalog; "
                    "this profile lists only controls addressed by the companion component definition. "
                    f"Current vertical slice: {config.get('slice_id', 'see mappings/shared/slices/')}."
                ),
            },
            "imports": [
                {
                    "href": "trestle://catalogs/bsi-grundschutz-plus-plus/catalog.json",
                    "include-controls": [{"with-ids": sorted(control_ids)}],
                }
            ],
            "merge": {"combine": {"method": "merge"}, "as-is": True},
        }
    }


def build_implemented_requirement(
    control_id: str,
    title: str,
    mapping: dict,
    config: dict,
    docs: dict[str, str],
) -> dict:
    defaults = config["defaults"]
    tier = mapping.get("tier", 2)

    statement = mapping.get("statement")
    if not statement and tier == 2:
        statement = _default_statement(defaults["statement_template"], control_id, title)
    elif not statement:
        statement = _default_statement(defaults["statement_template"], control_id, title)

    impl_status = mapping.get("implementation_status", defaults["implementation_status"])
    doc_keys = mapping.get("doc_keys", defaults["doc_keys"])

    doc_links = []
    for key in doc_keys:
        href = docs.get(key)
        if href:
            doc_links.append({"href": href, "rel": "reference", "text": key.replace("_", " ")})

    props: list[dict] = [
        {"name": "implementation-status", "ns": TRESTLE_RULE_NS, "value": impl_status},
    ]
    for rid in mapping.get("rule_ids") or []:
        props.append({"name": "Rule_Id", "ns": TRESTLE_RULE_NS, "value": rid})

    entry: dict = {
        "uuid": _uuid(config["artifact_id"], f"req:{control_id}"),
        "control-id": control_id,
        "description": statement,
        "props": props,
    }
    if doc_links:
        entry["links"] = doc_links
    return entry


def build_component_definition_json(
    config: dict,
    components_cfg: dict,
    controls_by_id: dict[str, dict],
    catalog_by_id: dict[str, dict],
    scope_ids: list[str],
    docs: dict[str, str],
) -> dict:
    cd_cfg = config["component_definition"]
    artifact_id = config["artifact_id"]
    product = config["product"]
    last_mod = (config.get("artifact_metadata") or {}).get(
        "component_definition_last_modified", "2026-01-01T00:00:00.000Z"
    )
    source = config.get("profile_source_href") or f"trestle://profiles/{artifact_id}/profile.json"

    by_component: dict[str, list[dict]] = {}
    for cid in scope_ids:
        mapping = controls_by_id.get(cid, {})
        comp_id = mapping.get("component")
        if not comp_id:
            raise ValueError(f"Control {cid} has no component mapping")
        ctrl = catalog_by_id.get(cid, {})
        title = (ctrl.get("title") or "").strip()
        by_component.setdefault(comp_id, []).append(
            build_implemented_requirement(cid, title, mapping, config, docs)
        )

    component_defs = {c["id"]: c for c in components_cfg.get("components") or []}
    components_out = []
    for comp_id, implemented in sorted(by_component.items()):
        comp = component_defs.get(comp_id)
        if not comp:
            raise ValueError(f"Unknown component id {comp_id!r}")
        comp_doc_keys = comp.get("doc_keys") or []
        comp_links = []
        for key in comp_doc_keys:
            href = docs.get(key)
            if href:
                comp_links.append(
                    {"href": href, "rel": "reference", "text": key.replace("_", " ")}
                )
        comp_links.append(
            {
                "href": "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek",
                "rel": "reference",
                "text": "BSI Stand der Technik Bibliothek (Grundschutz++)",
            }
        )
        implemented.sort(key=lambda r: r["control-id"])
        components_out.append(
            {
                "uuid": _uuid(artifact_id, f"component:{comp_id}"),
                "type": comp.get("type", product.get("type", "software")),
                "title": comp["title"],
                "description": comp.get("description", ""),
                "links": comp_links,
                "control-implementations": [
                    {
                        "uuid": _uuid(artifact_id, f"control-implementation:{comp_id}"),
                        "source": source,
                        "description": (
                            f"Grundschutz++ controls implemented by {comp['title']} "
                            f"(artifact {artifact_id})."
                        ),
                        "implemented-requirements": implemented,
                    }
                ],
            }
        )

    return {
        "component-definition": {
            "uuid": cd_cfg.get("uuid") or _uuid(artifact_id, "component-definition"),
            "metadata": {
                "title": cd_cfg["metadata_title"],
                "last-modified": last_mod,
                "version": cd_cfg["metadata_version"],
                "oscal-version": "1.1.3",
                "remarks": (
                    "Product-scoped implementation statements for Grundschutz++ controls applicable "
                    "to Red Hat Enterprise Linux. Tier-1 entries are curated; Tier-2 entries use an "
                    "honest documentation template. ComplianceAsCode Rule_Id values appear only where "
                    "listed in mappings/shared/controls/. Not a certification or legal interpretation."
                ),
            },
            "components": components_out,
        }
    }


def resolve_product_config(root: Path, product_key: str) -> Path:
    path = root / "mappings" / product_key / "artifact.json"
    if not path.is_file():
        raise SystemExit(f"Missing product config: {path}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--product",
        default="rhel9",
        help="Product key under mappings/ (default: rhel9)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Override path to artifact.json",
    )
    args = parser.parse_args()
    root = _repo_root()
    config_path = args.config or resolve_product_config(root, args.product)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    artifact_id = config["artifact_id"]
    config["slice_id"] = load_json(root, config["slice_relative_path"]).get("id")

    catalog = load_json(root, config["catalog_relative_path"])
    catalog_controls = load_catalog_controls(catalog)
    catalog_by_id = {c["id"]: c for c in catalog_controls}

    slice_doc = load_json(root, config["slice_relative_path"])
    scope_ids = slice_doc["control_ids"]
    for cid in scope_ids:
        if cid not in catalog_by_id:
            raise SystemExit(f"Control {cid} not found in vendored catalog")

    controls_doc = load_json(root, config["controls_relative_path"])
    controls_by_id = controls_doc.get("controls") or {}
    for cid in scope_ids:
        if cid not in controls_by_id:
            raise SystemExit(f"Control {cid} missing from {config['controls_relative_path']}")

    components_cfg = load_json(root, config["components_relative_path"])
    docs = load_json(root, config["docs_relative_path"])

    profile_doc = build_profile_json(config, scope_ids)
    profile_out = root / config["profile_output_path"]
    profile_out.parent.mkdir(parents=True, exist_ok=True)
    profile_out.write_text(json.dumps(profile_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {profile_out} ({len(scope_ids)} controls)")

    cd_doc = build_component_definition_json(
        config, components_cfg, controls_by_id, catalog_by_id, scope_ids, docs
    )
    cd_out = root / config["component_definition_output_path"]
    cd_out.parent.mkdir(parents=True, exist_ok=True)
    cd_out.write_text(json.dumps(cd_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    total_reqs = sum(
        len(ci["implemented-requirements"])
        for comp in cd_doc["component-definition"]["components"]
        for ci in comp["control-implementations"]
    )
    print(f"Wrote {cd_out} ({total_reqs} implemented-requirements across "
          f"{len(cd_doc['component-definition']['components'])} components)")


if __name__ == "__main__":
    main()
