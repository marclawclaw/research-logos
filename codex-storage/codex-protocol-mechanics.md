---
title: Codex Protocol Mechanics
aliases: [Codex P2P Network, Codex Storage Protocol]
tags: [logos, codex, protocol, p2p, erasure-coding, zk-proofs, merkle]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
---

# Codex Protocol Mechanics

## Network Joining

1. Node starts → connects to a **bootstrap node** (public entry point)
2. Receives **Signed Peer Records (SPRs)** with peer list
3. Joins wider P2P network
4. Two ports: UDP 8090 (peer discovery), TCP 8070 (inbound requests)

## Two Storage Modes

### Altruistic Mode (non-incentivised)

- Free file sharing, no payment, no persistence guarantees
- Upload via REST POST to `/data`
- File split into **64 KB blocks**
- Blocks hashed → **Merkle tree** → Merkle root = Content Identifier (CID)
- CID + metadata = **Basic Manifest** stored in Repo Store
- Any peer with CID can retrieve via Block Exchange Engine

### Persistence Mode (incentivised)

- User pays providers to host data for a specified duration
- Providers must provide cryptographic proof of storage
- Providers **passively monitor blockchain** for storage requests matching their config
  - Config: min price/byte/sec, max contract length, max collateral
  - Providers auto-reserve slots — no manual bidding
- File → erasure coded → parity blocks generated
- Combined blocks dispersed across **multiple nodes** (original + parity never co-located)

## Erasure Coding

- Generates parity blocks from original data
- Allows recovery even if some blocks are unavailable
- More storage-efficient than simple replication
- Enables large file support with fault tolerance

## Verifiable Storage (ZK Proofs)

1. Blocks → split into **2 KB cells**
2. Cells hashed with **Poseidon2** (ZK-optimised hash function)
3. Each block = small Merkle tree of cell hashes → **block root**
4. Blocks grouped into **slots** → each slot has a **slot root**
5. All slot roots → final Merkle tree → **Verification Root**
6. **Verifiable Manifest** = verification root + slot roots + metadata + CID
7. CID referenced in smart contract on blockchain
8. Providers prove possession via ZK proofs without revealing data

## Data Identifiers

| Identifier | What It Represents |
|---|---|
| CID (Basic) | Non-incentivised file |
| CID (Verifiable Manifest) | Erasure-coded, ZK-verifiable file |
| Verification Root | Integrity hash of entire dataset |
| Slot Root | Integrity hash of a storage slot |

## Developer API

- REST API at `api.codex.storage`
- Upload: `POST /data`
- Integrates with Waku for censorship-resistant file sharing apps
- See: [Codex + Waku file sharing example](https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/)
