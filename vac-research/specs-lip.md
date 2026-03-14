# Logos LIP — Specs & RFC Index

> Last updated: 2026-03-14  
> Source: [lip.logos.co](https://lip.logos.co/) | Repo: [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)

## What is the LIP Index?

The **Logos LIP (Logos Improvement Proposals) Index** is an IETF-style index of all Logos-managed specifications, maintained by Vac's RFC unit.

> "Collects specifications maintained by IFT-TS across Messaging, Blockchain, and Storage."

- Generated with mdBook from [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)
- Replaces the old rfc.vac.dev domain
- Follows IETF RFC conventions for formatting, status, and review

## Spec Categories

| Component | Description |
|-----------|-------------|
| **Messaging** | Waku protocols, messaging layer specs |
| **Blockchain** | Nomos, consensus, network layer specs |
| **Storage** | Codex storage protocol specs |
| **IFT-TS** | IFT Technical Specifications (cross-cutting) |

## Spec Statuses

| Status | Meaning |
|--------|---------|
| **Stable** | Production-ready, finalized spec |
| **Draft** | Being actively developed |
| **Raw** | Early-stage, experimental |
| **Deprecated** | No longer recommended |
| **Deleted** | Removed from index |

## Contributing

1. Open a pull request against [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)
2. Add or update the RFC in the appropriate component folder
3. Include `status` and `category` metadata in the RFC header table
4. If unsure where a spec belongs, open an issue first

## Key RFCs to Know

| RFC | Title | Status |
|-----|-------|--------|
| vac/32/rln-v1 | Rate Limiting Nullifier v1 | Stable |
| vac/raw/rln-v2 | Rate Limiting Nullifier v2 | Raw |
| RLN-v3 | Rate Limiting Nullifier v3 | (blog post / WIP) |

## Links

| Resource | URL |
|----------|-----|
| LIP Index | https://lip.logos.co/ |
| About | https://lip.logos.co/about.html |
| GitHub repo | https://github.com/vacp2p/rfc-index |
| IFT-TS site | https://vac.dev |
| IETF RFC series | https://www.rfc-editor.org/ |

## Notes

- The RFC unit transitioned to a **consensus-oriented specification methodology** in 2024
- Domain migration: rfc.vac.dev → lip.logos.co (rfc.vac.dev now redirects)
- Specs cover the full IFT stack — relevant for any PoC or integration work targeting Waku, Codex, or Nomos
