---
title: "Codex – Decentralised Durability Engine (DDE) Architecture"
tags: [logos, codex, storage, dde, erasure-coding, zk-proofs, durability]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
---

# Codex – Decentralised Durability Engine (DDE) Architecture

## What Is the DDE?

The **Decentralised Durability Engine (DDE)** is Codex's expanded architecture on top of the standard DSN (Decentralised Storage Network) model. It adds:

- Redundancy mechanisms (erasure coding + replication)
- Remote auditing protocols
- Repair incentives
- Strategic data dispersal
- Zero-knowledge proof-based storage verification

## File Ingestion Pipeline

### Step 1 — Chunking
- Files uploaded via REST API to local Codex node
- Split into **64 KB fixed-size blocks**
- Each block is cryptographically hashed

### Step 2 — Merkle Tree
- Block hashes are recursively combined into a **Merkle tree**
- The **Merkle root** uniquely represents file contents

### Step 3 – Basic Manifest (Altruistic Mode)
- Merkle root + metadata (block size, total size, encoding format) → **Basic Manifest**
- Manifest stored as a data block, assigned a **CID (Content Identifier)**
- Saved in the local **Repo Store**

### Step 4 – Erasure Coding (Persistence Mode)
- Additional **parity blocks** generated from original data blocks
- Parity enables data recovery even when parts of the network are unavailable
- More storage-efficient than pure replication
- Combined original + parity blocks form a new linear dataset

### Step 5 – Protected Manifest
- New Merkle tree built over erasure-coded dataset
- Root used as basis of **Protected Manifest** (includes erasure coding params)

### Step 6 – Strategic Dispersal
- Original and parity blocks for any data segment are spread across **different nodes**
- Prevents single points of failure

## Verifiable Proofs (Zero-Knowledge)

For incentivised storage, Codex generates **ZK proofs** to verify storage providers hold data:

1. Blocks broken into **2 KB cells**
2. Cells hashed with **Poseidon2** (ZK-optimised hash function)
3. Each block → small Merkle tree of cell hashes → **block root**
4. Blocks grouped into **slots**, each with a **slot root**
5. All slot roots → final Merkle tree → **Verification Root**
6. **Verifiable Manifest** = verification root + all slot roots + metadata
7. CID of Verifiable Manifest referenced in an on-chain smart contract

Proofs are **publicly verifiable** via blockchain nodes — no trusted verifier needed.

## Key Design Differences vs. Replication-Only Systems

| Feature | Replication (e.g. Filecoin) | Codex DDE |
|---|---|---|
| Redundancy method | Multiple full copies | Erasure coding + parity |
| Storage efficiency | Low (e.g. 3x overhead) | High (tunable parity ratio) |
| Fault verification | Provider-operated (ZFS snapshots) | On-chain ZK proofs |
| Repair incentives | Limited | Built into protocol |
| Data dispersal | Provider choice | Strategically enforced |

## Related Notes

- [[codex-overview]] — High-level position in Logos stack
- [[codex-p2p-network]] — How nodes share and retrieve data
- [[codex-storage-marketplace]] — How storage contracts and proofs interact financially
