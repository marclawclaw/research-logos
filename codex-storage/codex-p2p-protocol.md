---
title: "Codex P2P Protocol — Technical Architecture"
tags: [codex, logos, storage, p2p, protocol, merkle, erasure-coding, zk-proofs]
sources:
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
created: 2026-03-14
updated: 2026-03-14
status: current
---

# Codex P2P Protocol — Technical Architecture

## Network Bootstrap

1. New node starts and connects to a known **bootstrap node**
2. Bootstrap node returns peer list via **Signed Peer Records (SPRs)**
3. Node joins wider Codex P2P network and discovers further peers

**Default ports:**
- `UDP 8090` — peer discovery
- `TCP 8070` — inbound requests (must be publicly reachable for full participation)

## Storage Modes

### 1. Altruistic Mode (Non-Incentivised)

Casual/temporary file sharing with no payment or persistence guarantees.

**Upload flow:**
1. User POSTs file to local Codex node REST API at `/data`
2. File split into **64KB blocks**
3. Each block cryptographically hashed
4. Hashes recursively combined into a **Merkle tree**
5. Merkle root = unique file fingerprint
6. Merkle root + metadata → **Basic Manifest** (stored with its own CID)
7. CID stored in local **Repo Store**

**Retrieval:**
- Any node with the CID can fetch; **Block Exchange Engine** serves data from Repo Store
- Requester node fetches Basic Manifest, interprets block layout, reconstructs file

### 2. Persistence Mode (Incentivised)

For durable storage with uptime guarantees; paid via smart contracts.

**Upload flow (extended from Altruistic):**
1. File uploaded, chunked as above
2. **Erasure coding** applied — parity blocks generated from data blocks
3. Parity + original blocks arranged into a linear dataset
4. New Merkle tree constructed → **Protected Manifest**
5. Blocks split into **2KB cells**, hashed with **Poseidon2** (ZK-optimised)
6. Each block = small Merkle tree of cell hashes (block root)
7. Blocks grouped into **slots** → each slot has a Merkle root
8. All slot roots combined into final tree → **Verification Root**
9. **Verifiable Manifest** (verification root + slot roots + metadata) stored with CID
10. CID submitted to blockchain via smart contract storage request

## Storage Provider Matching

- Providers do **not** bid manually; they passively monitor blockchain for storage requests
- Each provider pre-configured with constraints:
  - Minimum price per byte/second
  - Maximum contract length
  - Maximum collateral
- When request matches constraints → provider auto-reserves slot and stores data
- Fully automatic and decentralised

## Zero-Knowledge Proof System

- Storage proofs use ZK proofs so providers prove data possession **without revealing it**
- Poseidon2 hash function used (optimised for ZK circuits)
- Proofs published **on-chain** → publicly verifiable by any blockchain node
- Failed proofs → collateral slashed

## Data Dispersal Strategy

Codex's DDE architecture **strategically disperses** blocks across multiple nodes, ensuring:
- Original and parity blocks for any given segment are on **different nodes**
- No single point of failure
- Network can recover from node loss using parity data

## API

REST API available at `api.codex.storage`. Key endpoint:
- `POST /data` — upload file
- Retrieve by CID

## Related Notes

- [[codex-overview]] — What Codex is
- [[codex-tokenomics]] — CDX token and smart contract economics
- [[codex-implementation]] — Nim implementation details
