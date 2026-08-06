#!/usr/bin/env python3
"""Assemble OSCAL profile and component-definition from trestle authoring markdown."""
from __future__ import annotations

import argparse
import subprocess
import sys
import uuid
from pathlib import Path

from oscal_scope import (
    catalog_by_id,
    control_sort_key,
    is_kernel_control,
    load_json,
    profile_control_ids,
    repo_root,
    write_json,
)

NS_URL = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")
TRESTLE_RULE_NS = "https://oscal-compass.github.io/compliance-trestle/schemas/oscal/cd"


def _uuid(artifact_id: str, suffix: str) -> str:
    return str(uuid.uuid5(NS_URL, f"{artifact_id}:{suffix}"))


def _run_trestle(args: list[str], root: Path) -> None:
    cmd = [sys.executable, "-m", "trestle", *args]
    subprocess.run(cmd, cwd=root, check=True)


def _text(config: dict, key: str, **kwargs: str) -> str:
    template = (config.get("texts") or {}).get(key, "")
    return template.format(**kwargs) if template else ""


def _catalog_upstream_links(config: dict) -> list[dict]:
    upstream = config.get("catalog_upstream") or {}
    blob = upstream.get("blob_url")
    if not blob:
        return []
    last_mod = (upstream.get("catalog_last_modified") or "")[:10]
    commit = (upstream.get("commit") or "")[:12]
    text_template = (config.get("texts") or {}).get("catalog_upstream_link_text")
    if text_template:
        text = text_template.format(catalog_date=last_mod, commit_short=commit)
    else:
        text = f"BSI Grundschutz++ (Stand {last_mod}, commit {commit})"
    return [{"href": blob, "rel": "reference", "text": text}]


def normalize_docs(raw_docs: dict) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for key, value in raw_docs.items():
        if isinstance(value, str):
            out[key] = {"href": value, "text": key.replace("_", " ")}
        elif isinstance(value, dict) and value.get("href"):
            out[key] = {
                "href": value["href"],
                "text": value.get("text") or key.replace("_", " "),
            }
    return out


def ensure_component_skeleton(cd_doc: dict, config: dict, components_cfg: dict) -> dict:
    """Ensure all subsystem components exist before trestle component-generate."""
    artifact_id = config["artifact_id"]
    profile_href = config.get("profile_source_href") or f"trestle://profiles/{artifact_id}/profile.json"
    upstream = config.get("catalog_upstream") or {}
    bsi_href = upstream.get("blob_url") or "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek"
    bsi_text = _text(config, "bsi_link_text") or "BSI Control Layer — aufgelöster Anwenderkatalog Grundschutz++"
    docs = normalize_docs(load_json(repo_root() / config["docs_relative_path"]))

    existing = {c["title"]: c for c in cd_doc["component-definition"]["components"]}
    components_out = list(cd_doc["component-definition"]["components"])

    for comp in components_cfg.get("components") or []:
        title = comp["title"]
        if title in existing:
            continue
        comp_links = []
        for key in comp.get("doc_keys") or []:
            entry = docs.get(key)
            if entry:
                comp_links.append({"href": entry["href"], "rel": "reference", "text": entry["text"]})
        comp_links.append({"href": bsi_href, "rel": "reference", "text": bsi_text})
        components_out.append(
            {
                "uuid": _uuid(artifact_id, f"component:{comp['id']}"),
                "type": comp.get("type", "software"),
                "title": title,
                "description": comp.get("description", ""),
                "links": comp_links,
                "control-implementations": [
                    {
                        "uuid": _uuid(artifact_id, f"control-implementation:{comp['id']}"),
                        "source": profile_href,
                        "description": _text(
                            config,
                            "control_implementation_description",
                            component_title=title,
                            artifact_id=artifact_id,
                        ),
                        "implemented-requirements": [],
                    }
                ],
            }
        )

    cd_doc["component-definition"]["components"] = sorted(
        components_out, key=lambda c: c["title"]
    )
    return cd_doc


def authoring_profile_control_ids(root: Path, config: dict) -> list[str]:
    """Control IDs are defined by markdown files under authoring/profile/."""
    profile_md = root / config["authoring_profile_dir"]
    ids: list[str] = []
    for path in sorted(profile_md.rglob("*.md")):
        cid = path.stem
        if path.stem and path.stem[0].isupper() and "." in path.stem:
            ids.append(cid)
    return sorted(set(ids), key=control_sort_key)


def sync_profile_imports(profile_doc: dict, control_ids: list[str]) -> None:
    prof = profile_doc["profile"]
    imports = prof.get("imports") or []
    if not imports:
        raise SystemExit("Profile has no catalog import block")
    imports[0]["include-controls"] = [{"with-ids": control_ids}]
    prof["imports"] = imports


def sync_component_requirement_stubs(
    cd_doc: dict,
    config: dict,
    root: Path,
) -> dict:
    """Ensure implemented-requirement stubs exist for each component markdown file."""
    artifact_id = config["artifact_id"]
    component_md = root / config["authoring_component_dir"]
    profile_href = config.get("profile_source_href") or f"trestle://profiles/{artifact_id}/profile.json"

    by_title = {c["title"]: c for c in cd_doc["component-definition"]["components"]}
    comp_cfg_by_title = {c["title"]: c for c in load_json(root / config["components_relative_path"]).get("components") or []}
    for comp_dir in sorted(component_md.iterdir()):
        if not comp_dir.is_dir():
            continue
        comp = by_title.get(comp_dir.name)
        if not comp:
            continue
        profile_sub = comp_dir / artifact_id
        if not profile_sub.is_dir():
            continue
        control_ids = sorted(
            {p.stem for p in profile_sub.rglob("*.md") if "." in p.stem and p.stem[0].isupper()},
            key=control_sort_key,
        )
        if not comp.get("control-implementations"):
            comp_id = comp_cfg_by_title.get(comp_dir.name, {}).get("id") or comp_dir.name
            comp["control-implementations"] = [
                {
                    "uuid": _uuid(artifact_id, f"control-implementation:{comp_id}"),
                    "source": profile_href,
                    "description": "",
                    "implemented-requirements": [],
                }
            ]
        ci = comp["control-implementations"][0]
        ci["source"] = profile_href
        existing = {r["control-id"] for r in ci.get("implemented-requirements") or []}
        for cid in control_ids:
            if cid in existing:
                continue
            ci.setdefault("implemented-requirements", []).append(
                {
                    "uuid": _uuid(artifact_id, f"req:{cid}"),
                    "control-id": cid,
                    "description": "",
                    "props": [
                        {
                            "name": "implementation-status",
                            "ns": TRESTLE_RULE_NS,
                            "value": "partial",
                        }
                    ],
                }
            )
        ci["implemented-requirements"] = sorted(
            ci.get("implemented-requirements") or [],
            key=lambda r: control_sort_key(r["control-id"]),
        )
    return cd_doc


PROP_KEY_ORDER = ("name", "uuid", "class", "ns", "value", "remarks")


def _canonical_prop(prop: dict) -> dict:
    """Fix key order so unchanged props don't diff — trestle's own serialization
    order drifts from ours (and itself) across runs otherwise."""
    ordered = {k: prop[k] for k in PROP_KEY_ORDER if k in prop}
    ordered.update({k: v for k, v in prop.items() if k not in ordered})
    return ordered


def enrich_artifacts(root: Path, config: dict) -> None:
    artifact_id = config["artifact_id"]
    profile_path = root / config["profile_output_path"]
    cd_path = root / config["component_definition_output_path"]
    catalog_path = root / config["catalog_relative_path"]
    components_cfg = load_json(root / config["components_relative_path"])
    docs = normalize_docs(load_json(root / config["docs_relative_path"]))
    cat = catalog_by_id(catalog_path)

    profile_doc = load_json(profile_path)
    prof = profile_doc["profile"]
    prof["metadata"]["title"] = config["profile"]["metadata_title"]
    prof["metadata"]["version"] = config["profile"]["metadata_version"]
    prof["metadata"]["oscal-version"] = "1.1.3"
    prof["metadata"]["remarks"] = _text(config, "profile_remarks", slice_id=config.get("scope_id", "rhel-host"))
    links = _catalog_upstream_links(config)
    if links:
        prof["metadata"]["links"] = links

    for cid in profile_control_ids(profile_doc):
        if cid not in cat:
            raise SystemExit(f"Profile control {cid} not found in vendored catalog")
        if not is_kernel_control(cat[cid].get("class")):
            raise SystemExit(f"Profile control {cid} is not a Stand-der-Technik Kernel control")

    write_json(profile_path, profile_doc)

    cd_doc = load_json(cd_path)
    cd_doc = ensure_component_skeleton(cd_doc, config, components_cfg)
    cd = cd_doc["component-definition"]
    cd["metadata"]["title"] = config["component_definition"]["metadata_title"]
    cd["metadata"]["version"] = config["component_definition"]["metadata_version"]
    cd["metadata"]["oscal-version"] = "1.1.3"
    cd["metadata"]["remarks"] = _text(config, "component_definition_remarks")
    if links:
        cd["metadata"]["links"] = links

    upstream = config.get("catalog_upstream") or {}
    bsi_href = upstream.get("blob_url") or "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek"
    bsi_text = _text(config, "bsi_link_text") or "BSI Control Layer — aufgelöster Anwenderkatalog Grundschutz++"

    comp_cfg_by_title = {c["title"]: c for c in components_cfg.get("components") or []}
    for comp in cd["components"]:
        cfg = comp_cfg_by_title.get(comp["title"], {})
        comp_links = {link["href"] for link in comp.get("links") or []}
        for key in cfg.get("doc_keys") or []:
            entry = docs.get(key)
            if entry and entry["href"] not in comp_links:
                comp.setdefault("links", []).append(
                    {"href": entry["href"], "rel": "reference", "text": entry["text"]}
                )
                comp_links.add(entry["href"])
        if bsi_href not in comp_links:
            comp.setdefault("links", []).append(
                {"href": bsi_href, "rel": "reference", "text": bsi_text}
            )

        for ci in comp.get("control-implementations") or []:
            ci["description"] = _text(
                config,
                "control_implementation_description",
                component_title=comp["title"],
                artifact_id=artifact_id,
            )
            for req in ci.get("implemented-requirements") or []:
                for prop in req.get("props") or []:
                    if prop.get("name") == "implementation-status" and not prop.get("ns"):
                        prop["ns"] = TRESTLE_RULE_NS
                req["props"] = [_canonical_prop(p) for p in req.get("props") or []]

    write_json(cd_path, cd_doc)


def profile_control_ids_from_doc(profile_doc: dict) -> list[str]:
    return profile_control_ids(profile_doc)


def load_product_config(root: Path, product_key: str) -> dict:
    path = root / "mappings" / product_key / "artifact.json"
    return load_json(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", default="rhel9")
    parser.add_argument(
        "--skip-assemble",
        action="store_true",
        help="Only run enrichment (metadata, skeleton, validation helpers)",
    )
    args = parser.parse_args()
    root = repo_root()
    config = load_product_config(root, args.product)
    artifact_id = config["artifact_id"]
    config["scope_id"] = load_json(root / config["scope_relative_path"]).get("id", "rhel-host")

    profile_md = root / config["authoring_profile_dir"]
    component_md = root / config["authoring_component_dir"]

    if not args.skip_assemble:
        profile_path = root / config["profile_output_path"]
        profile_doc = load_json(profile_path)
        scope_ids = authoring_profile_control_ids(root, config)
        sync_profile_imports(profile_doc, scope_ids)
        write_json(profile_path, profile_doc)

        _run_trestle(
            [
                "author",
                "profile-assemble",
                "-m",
                str(profile_md.relative_to(root)),
                "-o",
                artifact_id,
                "-n",
                artifact_id,
            ],
            root,
        )
        cd_doc = load_json(root / config["component_definition_output_path"])
        components_cfg = load_json(root / config["components_relative_path"])
        cd_doc = ensure_component_skeleton(cd_doc, config, components_cfg)
        cd_doc = sync_component_requirement_stubs(cd_doc, config, root)
        write_json(root / config["component_definition_output_path"], cd_doc)
        _run_trestle(
            [
                "author",
                "component-assemble",
                "-m",
                str(component_md.relative_to(root)),
                "-o",
                artifact_id,
                "-n",
                artifact_id,
            ],
            root,
        )

    enrich_artifacts(root, config)
    profile_doc = load_json(root / config["profile_output_path"])
    n = len(profile_control_ids_from_doc(profile_doc))
    print(f"Assembled {config['profile_output_path']} and {config['component_definition_output_path']} ({n} controls)")


if __name__ == "__main__":
    main()
