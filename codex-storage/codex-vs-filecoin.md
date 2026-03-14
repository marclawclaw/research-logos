---
title: "Codex vs Filecoin — Decentralised Storage Comparison"
tags: [codex, logos, storage, filecoin, IPFS, comparison, competitive]
sources:
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
created: 2026-03-14
updated: 2026-03-14
status: current
---

# Codex vs Filecoin — Decentralised Storage Comparison

## Overview

Both are Decentralised Storage Networks (DSNs), but they take fundamentally different architectural approaches.

**Filecoin** = incentivised persistence layer built on IPFS (Protocol Labs)  
**Codex** = Decentralised Durability Engine (DDE) — extends DSN concept with built-in durability, ZK proofs, and free-market contracts

## Comparison Table

| Dimension | Codex (Logos Storage) | Filecoin |
|---|---|---|
| **Redundancy** | Erasure coding (parity blocks) | Replication (multiple copies) |
| **Efficiency** | More storage-efficient at scale | Less efficient (full copies) |
| **Proof system** | ZK proofs (Poseidon2) | Proof-of-Replication (PoRep) |
| **Verifiability** | Public on-chain ZK proofs | Public chain proofs |
| **Marketplace** | Automatic free-market contracts | Dual storage/retrieval markets, manual deals |
| **KYC requirement** | None | Filecoin+ requires KYC |
| **Repair** | Built-in incentivised repair | Provider-managed (ZFS snapshots etc.) |
| **Blockchain** | Ethereum (proofs + token) | Filecoin chain |
| **Token** | CDX | FIL |
| **Hot storage** | Not yet (retrieval marketplace WIP) | Via Storacha (5GB free) |
| **Data retrieval** | Free-market pricing (WIP) | Direct from provider (FIL fee) or via IPFS |

## Durability Approach

### Filecoin
- Stores multiple replicas of files
- Storage provider-operated solutions (e.g. ZFS snapshots)
- Configurable replication factor

### Codex
- Erasure coding → generates parity blocks from data blocks
- Can recover data even with partial node failure
- Strategic data dispersal: original + parity blocks on *different* nodes
- Incentivised repair mechanisms in smart contracts
- All proofs on Ethereum for public verification

## Marketplace Design

### Filecoin
- Dual markets: storage market + retrieval market
- Clients negotiate directly with storage miners
- Filecoin+ (verified deals) requires human-based KYC
- Retrieval via direct provider request (FIL fee) or IPFS gateway

### Codex
- Single unified free-market approach
- Providers passively monitor blockchain; auto-accept matching requests
- No manual bidding or deal negotiation
- Retrieval marketplace being redesigned (not yet live at testnet pause)
- Pricing based on provider's real costs (storage + repair overhead)

## Token Comparison

| | CDX (Codex) | FIL (Filecoin) |
|---|---|---|
| **Chain** | Ethereum | Filecoin blockchain |
| **Collateral** | Yes — slashed on proof failure | Yes |
| **Payment** | Storage + retrieval | Storage + retrieval |
| **Validator rewards** | Yes (marking missed proofs) | Miners earn block rewards |
| **Status** | Testnet CDX token (early 2026) | Live mainnet |

## UX Comparison

### Filecoin Today
- Account + API key via storage provider (Lighthouse, Storacha)
- 5GB free tier via Storacha
- SDK/CLI for uploads, CID-based retrieval
- Proof of Data Segment Inclusion (PoDSI) for verification

### Codex Today (post-testnet-pause)
- Testnet paused; architecture revision underway
- Previously: CLI installer, Altruistic Mode on non-incentivised testnet
- No live incentivised marketplace yet

## Strategic Positioning

Codex positions itself as **more durable and more verifiable** than Filecoin:
- Erasure coding > replication for large-scale durability
- Automatic repair incentives > manual provider management
- Permissionless + no KYC > Filecoin+ model

## Related Notes

- [[codex-overview]] — Codex fundamentals
- [[codex-p2p-protocol]] — ZK proof and erasure coding details
- [[codex-tokenomics]] — CDX token mechanics
