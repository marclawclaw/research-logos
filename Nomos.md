---
topic: nomos
type: concept
tags: [blockchain, zk-proofs, privacy, consensus, mix-network]
confidence: high
last_updated: 2026-03-14
sources: [https://github.com/logos-co/nomos-node]
---

# Nomos

## Summary

Nomos (officially "Logos Blockchain") is a privacy-preserving, censorship-resistant blockchain designed for decentralized network states. It combines zero-knowledge proofs, a mix network for anonymity (Blend), and a modular service architecture to provide a foundation for sovereign digital communities.

## Key Facts

> [!fact] Confirmed from GitHub README
> - Written in Rust
> - Uses Cryptarchia Proof-of-Stake consensus
> - UTXO-based ledger model
> - Zero-knowledge proofs via Groth16 over BN254 (arkworks)
> - Mix network called "Blend" for anonymity
> - Modular architecture using Overwatch framework

### Core Components

| Component | Description |
|-----------|-------------|
| **Cryptarchia** | PoS consensus engine with chain sync over libp2p |
| **Blend** | Mix network for traffic anonymity (PoL, PoQ proofs) |
| **ZK Infrastructure** | Groth16 proofs, Poseidon2 hash, ZK signatures |
| **UTXO Ledger** | Privacy-preserving transaction model |
| **KMS** | Key management (Ed25519, X25519, ZK keys) |
| **Zone SDK** | Build zone sequencers and indexers |

### Network Stack
- QUIC transport
- GossipSub for message propagation
- Kademlia DHT for peer discovery
- AutoNAT for NAT traversal

## How it relates to Logos

Nomos is the **blockchain layer** of the [[Logos]] stack. It provides the consensus and settlement layer that anchors [[Waku]] (messaging) and [[Codex]] (storage), enabling trustless coordination and value transfer.

## Architecture Highlights

> [!analysis] Design patterns observed
> - Declarative service composition via Overwatch framework
> - Favors generics and static dispatch over dynamic dispatch
> - Each service has front layer (Overwatch integration) and back layer (business logic)
> - Highly modular — components can be swapped easily

### Directory Structure

```
logos-blockchain/
├── core/             # Blocks, transactions, UTXO notes, proofs
├── consensus/        # Cryptarchia PoS + sync
├── blend/            # Mix network (crypto, proofs, scheduling)
├── zk/               # Zero-knowledge infrastructure
├── ledger/           # UTXO state transitions
├── kms/              # Key management
├── libp2p/           # Networking
├── services/         # Overwatch services
├── wallet/           # Wallet logic
├── zone-sdk/         # Zone sequencer SDK
├── testnet/          # Docker Compose testnets
└── c-bindings/       # C library bindings
```

## Open Questions

- What is a "zone" in the Nomos context? How does the Zone SDK work?
- How does Blend mix network achieve anonymity? What are PoL and PoQ proofs?
- What is the current devnet status and performance metrics?
- How does Cryptarchia consensus differ from other PoS mechanisms?
- What is the token economics model?

## Sources

- https://github.com/logos-co/nomos-node — Main implementation (redirects to logos-blockchain/logos-blockchain)
- https://devnet.blockchain.logos.co/web/ — Devnet dashboard
- Specifications: https://www.notion.so/nomos-tech/Research-Specifications
