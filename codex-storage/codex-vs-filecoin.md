---
title: "Codex vs Filecoin – Decentralised Storage Comparison"
tags: [logos, codex, filecoin, storage, comparison, ipfs, dde]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
---

# Codex vs Filecoin – Decentralised Storage Comparison

## Background

**Filecoin** — well-established DSN built by Protocol Labs on top of IPFS. Public storage marketplace, dual market for storage and retrieval. Uses FIL token.

**Codex** — newer protocol, part of the Logos stack. DDE architecture. Emphasis on cryptographic durability guarantees and permissionless access.

## Protocol Design Comparison

| Feature | Filecoin | Codex |
|---|---|---|
| Underlying P2P layer | IPFS | libp2p (custom) |
| Redundancy | Replication (multiple full copies) | Erasure coding + parity blocks |
| Storage efficiency | Low (linear overhead per replica) | High (tunable via coding params) |
| Proof mechanism | PoRep (Proof of Replication) + PoSt (Proof of Spacetime) | ZK proofs (Poseidon2, on-chain verifiable) |
| Verifier | Internal network consensus | Public blockchain nodes |
| Provider onboarding | Manual; Filecoin Plus requires KYC | Permissionless, automatic matching |
| Pricing | Negotiated / market rates | Real-time, based on operator costs |
| Retrieval market | Dual market (storage + retrieval miners) | Planned incentivised retrieval marketplace |
| Hot storage | Storacha (built on IPFS/Filecoin) | Planned; no separate hot layer yet |
| Repair incentives | Limited (provider-operated) | Built into protocol |

## Durability Approaches

### Filecoin
- Durability via **replication**: clients specify replication factor
- Storage providers responsible for their own fault tolerance (e.g. ZFS snapshots)
- Proofs verify possession but not cross-node dispersal

### Codex
- Durability via **erasure coding**: parity data mathematically reconstructs lost blocks
- **Strategic dispersal**: original and parity blocks for any segment are spread across different nodes (enforced by protocol)
- **Incentivised repair**: protocol-level rewards for nodes that repair degraded data
- Proofs are ZK-based and publicly verifiable on-chain

## Retrieval

| | Filecoin | Codex |
|---|---|---|
| Direct retrieval | From storage provider (FIL fee) | From storage provider (planned) |
| Network retrieval | Via IPFS nodes (if available) | Via P2P network |
| Hot layer | Storacha (separate service, 5 GB free) | Not yet separate |

## Access & Permissions

- **Filecoin**: open, but Filecoin Plus program (for cheaper storage) requires human-based KYC
- **Codex**: fully permissionless — no KYC, no human gatekeeping at any layer

## Summary

Codex aims to be a more durability-focused, verifiable, and permissionless alternative to Filecoin. Its key differentiators are:
1. Erasure coding over replication (efficiency + durability)
2. Strategically enforced data dispersal
3. On-chain ZK proofs verifiable by anyone
4. Fully permissionless marketplace (no manual bidding, no KYC)
5. Protocol-native repair incentives

## Related Notes

- [[codex-dde-architecture]] — How erasure coding and ZK proofs work in Codex
- [[codex-storage-marketplace]] — Codex marketplace mechanics
- [[codex-overview]] — Codex position in Logos stack
