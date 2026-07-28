#!/usr/bin/env python3
"""Generate scoped OSCAL profile and component-definition for a Red Hat GS++ product artifact."""
from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path

NS_URL = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
TRESTLE_RULE_NS = "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd"
KERNEL_CLASS = "BSI-Stand-der-Technik-Kernel"


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


def normalize_docs(raw_docs: dict) -> dict[str, dict[str, str]]:
    """Accept {key: href} or {key: {href, text}}."""
    out: dict[str, dict[str, str]] = {}
    for key, value in raw_docs.items():
        if isinstance(value, str):
            out[key] = {"href": value, "text": key.replace("_", " ")}
        elif isinstance(value, dict):
            href = value.get("href")
            if not href:
                raise ValueError(f"docs[{key}] missing href")
            out[key] = {
                "href": href,
                "text": value.get("text") or key.replace("_", " "),
            }
        else:
            raise ValueError(f"Invalid docs entry for {key!r}")
    return out


def _text(config: dict, key: str, **kwargs: str) -> str:
    template = (config.get("texts") or {}).get(key, "")
    return template.format(**kwargs) if template else ""


def validate_kernel_controls(scope_ids: list[str], catalog_by_id: dict[str, dict]) -> None:
    for cid in scope_ids:
        ctrl = catalog_by_id[cid]
        cls = ctrl.get("class")
        if cls != KERNEL_CLASS:
            title = (ctrl.get("title") or "").strip()
            raise SystemExit(
                f"Control {cid} ({title!r}) has class {cls!r}, expected {KERNEL_CLASS!r}. "
                "Host slices must reference Stand-der-Technik Kernel controls only."
            )


def build_profile_json(config: dict, control_ids: list[str]) -> dict:
    prof = config["profile"]
    artifact_id = config["artifact_id"]
    last_mod = (config.get("artifact_metadata") or {}).get(
        "profile_last_modified", "2026-01-01T00:00:00.000Z"
    )
    remarks = _text(config, "profile_remarks", slice_id=config.get("slice_id", ""))
    return {
        "profile": {
            "uuid": prof.get("uuid") or _uuid(artifact_id, "profile"),
            "metadata": {
                "title": prof["metadata_title"],
                "last-modified": last_mod,
                "version": prof["metadata_version"],
                "oscal-version": "1.1.3",
                "remarks": remarks,
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
    docs: dict[str, dict[str, str]],
) -> dict:
    defaults = config["defaults"]
    tier = mapping.get("tier", 2)

    statement = mapping.get("statement")
    if not statement:
        statement = _default_statement(defaults["statement_template"], control_id, title)

    impl_status = mapping.get("implementation_status", defaults["implementation_status"])
    doc_keys = mapping.get("doc_keys", defaults["doc_keys"])

    doc_links = []
    for key in doc_keys:
        entry = docs.get(key)
        if entry:
            doc_links.append({"href": entry["href"], "rel": "reference", "text": entry["text"]})

    props: list[dict] = [
        {"name": "implementation-status", "ns": TRESTLE_RULE_NS, "value": impl_status},
    ]
    for rid in mapping.get("rule_ids") or []:
        props.append({"name": "Rule_Id", "ns": TRESTLE_RULE_NS, "value": rid})

    req: dict = {
        "uuid": _uuid(config["artifact_id"], f"req:{control_id}"),
        "control-id": control_id,
        "description": statement,
        "props": props,
    }
    if doc_links:
        req["links"] = doc_links
    return req


def build_component_definition_json(
    config: dict,
    components_cfg: dict,
    controls_by_id: dict[str, dict],
    catalog_by_id: dict[str, dict],
    scope_ids: list[str],
    docs: dict[str, dict[str, str]],
) -> dict:
    cd_cfg = config["component_definition"]
    artifact_id = config["artifact_id"]
    product = config["product"]
    last_mod = (config.get("artifact_metadata") or {}).get(
        "component_definition_last_modified", "2026-01-01T00:00:00.000Z"
    )
    source = config.get("profile_source_href") or f"trestle://profiles/{artifact_id}/profile.json"
    bsi_link_text = _text(config, "bsi_link_text") or "BSI Stand der Technik Bibliothek (Grundschutz++)"

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
        comp_links = []
        for key in comp.get("doc_keys") or []:
            entry = docs.get(key)
            if entry:
                comp_links.append(
                    {"href": entry["href"], "rel": "reference", "text": entry["text"]}
                )
        comp_links.append(
            {
                "href": "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek",
                "rel": "reference",
                "text": bsi_link_text,
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
                        "description": _text(
                            config,
                            "control_implementation_description",
                            component_title=comp["title"],
                            artifact_id=artifact_id,
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
                "remarks": _text(config, "component_definition_remarks"),
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
    config["slice_id"] = load_json(root, config["slice_relative_path"]).get("id")

    catalog = load_json(root, config["catalog_relative_path"])
    catalog_by_id = {c["id"]: c for c in load_catalog_controls(catalog)}

    slice_doc = load_json(root, config["slice_relative_path"])
    scope_ids = slice_doc["control_ids"]
    for cid in scope_ids:
        if cid not in catalog_by_id:
            raise SystemExit(f"Control {cid} not found in vendored catalog")

    validate_kernel_controls(scope_ids, catalog_by_id)

    controls_doc = load_json(root, config["controls_relative_path"])
    controls_by_id = controls_doc.get("controls") or {}
    for cid in scope_ids:
        if cid not in controls_by_id:
            raise SystemExit(f"Control {cid} missing from {config['controls_relative_path']}")

    components_cfg = load_json(root, config["components_relative_path"])
    docs = normalize_docs(load_json(root, config["docs_relative_path"]))

    profile_out = root / config["profile_output_path"]
    profile_out.parent.mkdir(parents=True, exist_ok=True)
    profile_out.write_text(
        json.dumps(build_profile_json(config, scope_ids), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
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
    print(
        f"Wrote {cd_out} ({total_reqs} implemented-requirements across "
        f"{len(cd_doc['component-definition']['components'])} components)"
    )


if __name__ == "__main__":
    main()
