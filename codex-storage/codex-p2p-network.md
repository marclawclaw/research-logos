---
title: "Codex – P2P Network Operation"
tags: [logos, codex, storage, p2p, libp2p, networking, cid]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
  - https://blog.codex.storage/how-to-interact-with-a-codex-node/
---

# Codex – P2P Network Operation

## Node Startup & Bootstrapping

1. User runs a Codex node locally
2. Node connects to a known **bootstrap node** (public entry point)
3. Receives a list of peers via **Signed Peer Records (SPRs)**
4. Joins the wider P2P network and discovers additional peers

### Default Ports

| Port | Protocol | Purpose |
|---|---|---|
| 8090 | UDP | Peer discovery |
| 8070 | TCP | Block exchange (inbound requests) |
| 8080 | TCP | REST API |

> Ports must be accessible (port-forwarded) for full network participation.

## Sharing Modes

### Altruistic Mode (Non-Incentivised)
- File sharing without payment or persistence guarantees
- Useful for casual transfers and protocol testing
- **How it works:**
  1. Upload file via `POST /data` REST endpoint
  2. File chunked into 64 KB blocks, hashed → Merkle tree
  3. Merkle root + metadata = **Basic Manifest** stored with a **CID**
  4. Peers can retrieve any content using its CID
  5. **Block Exchange Engine** handles fetching from Repo Store

### Persistence Mode (Incentivised)
- User pays storage providers to host files for a specified duration
- Providers must submit verifiable ZK proofs that data is intact
- See [[codex-storage-marketplace]] for contract details

## Content Retrieval

- Requester needs only the **CID** of the Basic Manifest
- Node fetches manifest → interprets block retrieval plan → reconstructs file
- `GET /data/{cid}` — local retrieval
- `GET /data/{cid}/network/` — fetch from wider network

## Content Identifiers (CIDs)

- Every file/manifest/block is addressable by a CID
- CID = cryptographic hash of content → content-addressed storage
- Immutable: same content always has the same CID

## Node Management

- **CLI Installer**: easy setup; auto port configuration; links ERC-20 wallet for future incentives
- **Dappnode package**: `codex-storage/DAppNodePackage-codex` — one-click node in Dappnode
- **Testnet metrics**: https://metrics.testnet.codex.storage

## Related Notes

- [[codex-dde-architecture]] — How files are chunked, erasure-coded, and verified
- [[codex-developer-integration]] — REST API reference and tooling
- [[codex-storage-marketplace]] — Incentivised persistence contracts
