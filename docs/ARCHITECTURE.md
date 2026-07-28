# RH-GSplusplus architecture

This document describes how Red Hat maps **Grundschutz++** (*Anwenderkatalog*) requirements to
**Red Hat product** capabilities in OSCAL, and how those mappings connect to technical compliance
checks (OpenSCAP / ComplianceAsCode today; product-specific automation later).

**RHEL 9 and RHEL 10** are the first products. The same architecture extends to **Red Hat
OpenShift**, **Red Hat Ansible Automation Platform**, and other Red Hat products — each with its
own scoped profile, component definition, and check backend.

It replaces the earlier `rhel9-gsplusplus-full` approach, which incorrectly mapped all 647 catalog
controls onto a single RHEL software component.

## Goals

1. **Filter applicability** — include only controls that a given Red Hat product can meaningfully support.
2. **Document with official sources** — link `implemented-requirement` entries to official Red Hat documentation.
3. **Wire technical checks** — attach machine-verifiable rule IDs where automated evaluation exists for that product.

Customers combine BSI control-layer artifacts with one or more Red Hat implementation-layer
artifacts in their SSP or compliance tooling.

## Layer model

| Layer | Owner | Repository | Role |
|-------|-------|------------|------|
| Control | BSI | [Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek) | Full GS++ ISMS baseline (organizational + technical) |
| Implementation | Red Hat | **RH-GSplusplus** (canonical) | Per-product contribution for applicable controls only |
| Assessment | Customer / CaC / product tooling | ComplianceAsCode, Ansible, OCP compliance | Product-specific scans and policy checks |

Red Hat does **not** claim to implement governance, personnel, physical security, or other
organizational controls. Those remain in the BSI catalog and the customer's SSP.

Each product publishes **only what that product can support**. A customer running RHEL hosts,
OpenShift clusters, and Ansible automation may import **three** implementation artifacts — not
one monolithic “Red Hat implements GS++” bundle.

### Customer workflow

```text
BSI Grundschutz++ catalog (or resolved Anwenderkatalog)
        +
RH profile  {product}-gsplusplus-{scope}   ← auditable applicability filter per product
        +
RH component-definition {product}-gsplusplus-{scope}   ← product responses by subsystem
        +
(optional) product check profile   ← e.g. CaC/OpenSCAP for RHEL; policy packs for OCP/AAP later
```

Example today: `rhel9-gsplusplus-host`. Planned later: `openshift-gsplusplus-platform`,
`ansible-gsplusplus-controller`, and similar scoped artifacts per product line.

## Repository layout

```text
catalogs/bsi-grundschutz-plus-plus/     # vendored BSI snapshot (shared)
docs/ARCHITECTURE.md                    # this document

mappings/
  shared/
    slices/                             # vertical / phased scope (e.g. rhel-audit)
    components/                         # subsystem defs per product family
    controls/                           # per-slice control mappings (tier, prose, rules)
    scope/                              # hybrid filter rules (practice areas, denylists)
  rhel9/                                # first product: OS host scope
    artifact.json
    docs.json
  rhel10/
  openshift/                            # planned: cluster / platform scope
  ansible/                              # planned: automation controller scope

profiles/{product}-gsplusplus-{scope}/
component-definitions/{product}-gsplusplus-{scope}/

scripts/
  generate_component_definition.py      # one generator (--product rhel9|openshift|…)
  fetch_bsi_catalog.sh
```

RHEL 10 follows the same pattern as RHEL 9. Additional products add directories under `mappings/`,
`profiles/`, and `component-definitions/` without changing the OSCAL model.

### DRY across versions and products

| Shared (`mappings/shared/`) | Per product / version (`mappings/rhel9/`, `mappings/openshift/`, …) |
|-----------------------------|---------------------------------------------------------------------|
| GS++ control IDs and cross-product scope baselines | Product-specific applicability filter |
| Reusable Tier-1 prose where capability is identical | docs.redhat.com URL paths and doc keys |
| Component taxonomy patterns (audit, identity, network) | Subsystem list tuned to product architecture |
| Control → component map (where products align) | `rule_ids` and check-backend references |
| Practice-area allowlists / org-control denylists | Artifact UUIDs, titles, CI smoke targets |

When RHEL and OpenShift both address the same control (e.g. logging), **shared curated text** lives
in `mappings/shared/controls/`; product files add deltas (different doc links, different rules,
different `implementation-status`).

## Scope selection (hybrid filter)

Controls enter a product profile through a **hybrid** process (same method, **different** allowlists
per product):

1. Pre-filter using BSI catalog metadata (target object categories where available).
2. Product-specific practice-area allowlist (e.g. RHEL host: `KONF`, `BER`, `DET`, parts of `STM`;
   OpenShift platform: cluster identity, admission, networking, workload isolation; Ansible:
   automation controller hardening, credential handling, job isolation).
3. Explicit denylist for organizational-only controls (shared across products).
4. Human review before merge.

**Inclusion in the profile does not require an automated rule.** Rules are attached separately and
use the check backend appropriate to the product.

## OSCAL artifacts

### Scoped profile (`rhel9-gsplusplus-host`)

- Imports the vendored BSI catalog.
- `include-controls.with-ids` lists only host-applicable control IDs.
- Serves as the auditable filter (not a substitute for the full GS++ baseline).

### Component definition (`rhel9-gsplusplus-host`)

- **Multiple components** by subsystem (`rhel-audit`, `rhel-selinux`, `rhel-network`, …).
- Each component has its own `control-implementations` block referencing the host profile.
- `implemented-requirement` entries carry:
  - English `description` (Tier-1 curated or Tier-2 template),
  - `implementation-status` (Trestle namespace),
  - optional `Rule_Id` props (ComplianceAsCode),
  - `links` to docs.redhat.com.

## Content tiers

| Tier | When | Statement | `Rule_Id` | Typical status |
|------|------|-----------|-----------|----------------|
| **1 — Curated** | Security-critical, scan-backed | Hand-written | Yes | `implemented` / `partial` |
| **2 — Documented** | In scope, not yet automated | Short honest template + doc links | No | `partial` |
| **Excluded** | Organizational / out of product scope | — | — | not in profile |

Keyword heuristics over German control titles (`KEYWORD_RULES`) are **retired**.

## Language

All **user-visible text** in generated OSCAL artifacts (profile and component definition) is **German**:

- `metadata.title`, `metadata.remarks`
- component `title`, `description`, `control-implementations[].description`
- `implemented-requirement.description`
- link `text` values (defined in `{product}/docs.json` alongside `href`)

English is used only for technical identifiers (`Rule_Id`, file paths, repository metadata) and in
this architecture document. Source mappings under `mappings/shared/controls/` are maintained in German.

## Host slice control selection

Vertical slices and host profiles must reference **Stand-der-Technik Kernel** controls
(`class: BSI-Stand-der-Technik-Kernel`) only. Methodik controls (e.g. `GC.*`, `STM.*` with the same
numeric IDs) share identifiers but address ISMS methodology — not product hardening — and must not
appear in host implementation artifacts. The generator enforces this at build time.

## Technical check bridge

A single mapping in `mappings/shared/controls/` generates OSCAL `Rule_Id` (or equivalent) props
and, where applicable, product-specific check artifacts:

| Product | Check backend (current / planned) | OSCAL prop |
|---------|-----------------------------------|------------|
| RHEL 9 / 10 | ComplianceAsCode / OpenSCAP (`ssg-rhel{N}-ds.xml`) | `Rule_Id` (Trestle NS) |
| OpenShift | Cluster compliance operator, CaC OCP content (planned) | TBD — same mapping source |
| Ansible Automation Platform | AAP hardening guides, policy-as-code (planned) | TBD — same mapping source |

For RHEL today:

1. OSCAL `Rule_Id` on `implemented-requirement` entries.
2. (Future) CaC control YAML under `products/rhel9/controls/gsplusplus_*.yml`.

CI smoke tests validate RHEL `rule_ids` against `ssg-rhel{N}-ds.xml`. A separate workflow checks
that every `href` in `{product}/docs.json` responds successfully (`scripts/check_doc_links.py`).
Other products add parallel validation when their backends land — the **mapping source stays one
place**; only the emitter and CI target differ.

## Multi-product roadmap

The repository name **RH-GSplusplus** reflects Red Hat's GS++ implementation layer, not RHEL alone.
Expansion follows the same patterns established for RHEL; only scope, subsystems, and check backends
change.

| Product | Scoped artifact (planned) | Scope focus | Subsystem examples |
|---------|---------------------------|-------------|-------------------|
| **RHEL 9 / 10** | `rhel{N}-gsplusplus-host` | OS host hardening | `rhel-audit`, `rhel-selinux`, `rhel-network` |
| **OpenShift** | `openshift-gsplusplus-platform` | Cluster & workload security | `ocp-auth`, `ocp-network`, `ocp-admission`, `ocp-logging` |
| **Ansible Automation Platform** | `ansible-gsplusplus-controller` | Automation control plane | `aap-auth`, `aap-secrets`, `aap-execution` |
| **Other Red Hat products** | `{product}-gsplusplus-{scope}` | Product-specific | Defined per product team |

Principles for adding a product:

1. **New applicability filter** — do not reuse the RHEL host allowlist; define `{product}/scope`.
2. **New component decomposition** — subsystems match how the product is operated and documented.
3. **Shared mappings where honest** — if two products implement the same control the same way,
   curated prose lives in `mappings/shared/`; otherwise keep product-specific statements.
4. **Separate OSCAL outputs** — one profile + component definition per product (and version line
   where releases diverge, as with RHEL 9 vs 10).
5. **Customer composes in the SSP** — BSI full catalog + RHEL artifact + OpenShift artifact + …;
   no single artifact implies Red Hat covers the entire ISMS.

Near-term work stays on **RHEL host** (PR 1 → 0.1). OpenShift and Ansible are **explicit later
phases** once the generator, mapping layout, and CaC dual-output pipeline are proven on RHEL.

## Phased delivery

| Phase | Scope | Deliverable |
|-------|-------|-------------|
| **PR 1** | RHEL vertical slice: `rhel-audit` | Refactored generator, host profile + component def, remove `*-full` |
| **0.1** | RHEL full host allowlist | Mostly Tier-2; Tier-1 where CaC rules exist |
| **0.5+** | RHEL Tier-1 growth | BSI Beispiel snapshot candidate |
| **1.x** | RHEL 10 host artifact | Same model as RHEL 9 with shared mappings + deltas |
| **2.x** | OpenShift platform artifact | `openshift-gsplusplus-platform`; OCP scope filter + check backend |
| **3.x** | Ansible Automation Platform | `ansible-gsplusplus-controller`; AAP scope filter + check backend |
| **Future** | Additional Red Hat products | Same pattern: `{product}-gsplusplus-{scope}` |

## BSI contribution

Canonical source remains **RH-GSplusplus**. Contributions to
`Stand-der-Technik-Bibliothek/implementation_layer/` are **manual checklist-gated snapshots**
(not the live edit surface).

First planned contribution: `RHEL Beispiel-Components/rhel-audit/` after the vertical slice stabilizes.

Checklist before any BSI PR:

- [ ] Generated from a tagged RH-GSplusplus release
- [ ] Scoped profile only (never “full catalog”)
- [ ] BSI-style metadata aligned with existing Beispiel components
- [ ] README states organizational controls remain in GS++ catalog
- [ ] No keyword-heuristic prose

## References

- [BSI Stand-der-Technik-Bibliothek](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek)
- [NIST OSCAL component definition](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/)
- [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content)
- [compliance-trestle](https://github.com/oscal-compass/compliance-trestle)
