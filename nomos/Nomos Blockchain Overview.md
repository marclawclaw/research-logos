---
topic: nomos
type: concept
tags: [blockchain, consensus, privacy, sovereign]
confidence: high
last_updated: 2026-03-14
sources: [https://logos.co/tech-stack, https://press.logos.co/article/2024-roundup, https://blog.nomos.tech]
---

# Nomos Blockchain Overview

## Summary

Nomos is the consensus/blockchain layer of the Logos stack, designed for sovereignty, modularity, and privacy preservation. It provides infrastructure for onchain governmental, financial, and social institutions while enabling network-level privacy for all participants.

## Key Facts

> [!fact] From official sources
> - **Purpose:** Scalable, trustless agreements layer
> - **Design goals:** Sovereignty, modularity, privacy preservation
> - **Status:** v1 specifications complete (Aug 2025)
> - **Internal testnet:** Running as of late 2024

### Architecture Components

1. **Cryptarchia** — consensus protocol using private proof-of-stake
2. **NomosDA** — data availability solution using KZG commitments
3. **Blendnet** (formerly Mixnet) — network privacy layer
4. **Coordination Layer** — cross-zone communication
5. **Native Zones** — sovereign execution environments

### Privacy Features

> [!fact] Key differentiator
> - **Network-level privacy** for users, developers, and validators
> - Location and transaction details not exposed
> - Validators can secure network without revealing identity

### Key Progress (from 2024 Roundup)

- **NomosDA:** Encoding, verification, reconstruction implemented with "very favourable performance times"
- **Dispersal, replication, sampling protocols** running in simulations
- **Cryptarchia** designed and implemented for v1
- **Early private testnet** built for internal testing

## How it relates to Logos

Nomos is the **settlement layer** for the Logos stack:
- Provides consensus for multi-party coordination
- Enables on-chain governance
- Anchors storage proofs from [[Codex Storage Overview|Codex]]
- Coordinates incentives across the network

> [!analysis] Analyst inference
> The "sovereign zones" model suggests communities can run their own execution environments while sharing security. Similar to Cosmos zones or Polkadot parachains but with privacy focus.

## Open Questions

- Mainnet timeline?
- Token model and staking requirements?
- How do Native Zones work technically?
- Interoperability with other chains (bridges)?
- ZK component specifics?

## Sources

- https://logos.co/tech-stack
- https://press.logos.co/article/2024-roundup
- https://blog.nomos.tech/2024-year-in-review/
- https://blog.nomos.tech/why-we-chose-kzg-for-nomosda/
