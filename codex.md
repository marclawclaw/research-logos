# Codex (Logos Storage) — Deep Dive

> Last updated: 2026-03-14
> **Note:** Codex was rebranded to "Logos Storage" in late 2025. codex.storage now redirects to logos.co/tech-stack.

## What is Codex?

Codex is "a state-of-the-art, decentralized storage protocol that provides a solution for highly durable data storage with high decentralization." It is designed to be a **privacy-preserving, censorship-resistant** storage system that ensures data durability without single points of failure.

Within the Logos stack, Storage enables "delivery of frontends for dapps, allowing truly decentralised, privacy-preserving deployment."

**Source:** [codex.storage](https://codex.storage) (now redirects), [blog.codex.storage](https://blog.codex.storage/)

---

## Architecture

### P2P Network Layer

Codex nodes operate on two ports:
- **UDP 8090** (default) — Peer discovery
- **TCP 8070** — Inbound requests

New nodes connect via **bootstrap nodes** that provide **Signed Peer Records (SPRs)** listing available peers.

### Data Storage Modes

#### 1. Altruistic Mode (Non-Incentivized)
- Files upload via REST API to `/data` endpoint
- Data splits into **64KB blocks** with cryptographic hashing
- Hashes combine into a **Merkle tree**
- Root hash becomes the **Content Identifier (CID)**
- Basic Manifest stores metadata in the Repo Store

#### 2. Persistence Mode (Incentivized)
- Files undergo **erasure coding** to generate parity blocks
- Original + parity blocks distribute across multiple nodes
- Storage providers **passively monitor the blockchain** for matching storage requests
- No manual bidding — providers configure rules (min price/byte/second, max contract length, max collateral)
- Automatic slot reservation when request matches provider config

**Source:** [blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works](https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/)

---

## Key Technical Features

### Erasure Coding
Codex transforms files into a more robust structure by generating **additional parity blocks** from original data blocks. This allows the system to recover data even if parts become unavailable. The architecture prevents concentration of data in few large nodes.

### Lazy Repair
Rather than eagerly replicating data, Codex uses **lazy repair** — data is only re-encoded and redistributed when storage nodes go offline and availability drops below threshold. This reduces bandwidth overhead.

### Zero-Knowledge Proofs (Verification)
- Uses **Poseidon2 hashing** for data integrity proofs
- Data breaks into **2KB cells** organized hierarchically:
  - Cells → Block roots → Slot roots → Verification root
- The verification root captures integrity of the entire erasure-coded dataset
- Any modification to file or parity data changes the root

### Marketplace
- **No auction/bidding** — deterministic matching
- Providers set constraints: minimum price per byte per second, max contract length, max collateral
- Storage requests posted to blockchain; matching providers automatically reserve slots
- Smart contracts with **Certora formal verification** (via Vac)

**Source:** [blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works](https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/), [codex.storage/about/architect](https://codex.storage/about/architect/)

---

## Roadmap & Status

| Period | Milestone | Status |
|--------|-----------|--------|
| Q1 2025 | Tokenomics Litepaper released | ✅ Completed |
| Q1 2025 | BitTorrent content v1 integrated | ✅ Completed |
| Q1 2025 | CLI Installer for testnet onboarding | ✅ Completed |
| H1 2025 | Non-incentivized testnet | ✅ Launched, then paused for reassessment |
| Q3 2025 | Mainnet readiness target (original) | ⏸️ Paused |
| H2 2025 | Incentivized testnet (tokenomics model) | 🔄 In progress |
| 2026 | Widespread adoption target | 🎯 Goal |

### Strategic Pause (2025)
The team **deliberately paused** the existing testnet to reassess core design principles. Rather than pursuing broader functionality, Storage now focuses specifically on "node-side content storage and retrieval functionality" aligned with the wider Logos vision. This enables better integration with messaging and blockchain components.

**Source:** [blog.codex.storage/the-codex-roadmap-for-2025-and-beyond](https://blog.codex.storage/the-codex-roadmap-for-2025-and-beyond/), [press.logos.co/article/2025-dev-retrospective](https://press.logos.co/article/2025-dev-retrospective)

---

## Developer Access

- **REST API:** Available at `api.codex.storage` during testnet phase
- **Go bindings:** logos-storage-go-bindings (v0.0.29-v0.0.30 as of Jan 2026)
- **Nim implementation:** logos-storage-nim (v0.3.0-v0.3.2 as of Jan 2026)
- **Docs:** [docs.codex.storage](https://docs.codex.storage)
- **Whitepaper:** [docs.codex.storage/learn/whitepaper](https://docs.codex.storage/learn/whitepaper)

**Source:** [news.free.technology/monthly/2026-01.html](https://news.free.technology/monthly/2026-01.html)

---

## Use Cases

1. **Censorship-resistant file sharing** — Demo app combining Codex + Waku shown at IFT meetup (April 2025)
2. **DApp frontend hosting** — Truly decentralized deployment of web frontends
3. **AI data storage** — Long-term vision for AI training data archival
4. **Blockchain archival** — Historical chain data storage
5. **Decentralized identity** — Credential and attestation storage

**Source:** [blog.codex.storage/the-codex-roadmap-for-2025-and-beyond](https://blog.codex.storage/the-codex-roadmap-for-2025-and-beyond/), [press.logos.co/article/april-2025](https://press.logos.co/article/april-2025)

---

## Comparison with Filecoin

Codex published a comparative analysis highlighting **durability advantages over Filecoin** (April 2025). Key differentiators:
- Erasure coding + lazy repair vs Filecoin's replication model
- Deterministic marketplace matching vs auction-based
- Smaller node requirements (higher decentralization)
- Privacy-preserving by design

**Source:** [press.logos.co/article/april-2025](https://press.logos.co/article/april-2025)

---

## Analysis

### Strengths
- **Novel marketplace design:** No-bidding, constraint-based matching is elegant and reduces complexity
- **Strong erasure coding:** Well-thought-out data durability with lazy repair
- **ZK verification:** Poseidon2-based proofs for data integrity
- **Integration with Logos stack:** Combined Codex+Waku demos show cross-component potential

### Concerns
- **Strategic pause:** The testnet pause signals potential architectural rethinking — timeline uncertainty
- **Behind schedule:** Original Q3 2025 mainnet target was missed; current timeline unclear
- **Competition:** Filecoin, Arweave, and other storage protocols are already in production
- **Tokenomics:** Litepaper released but incentivized testnet still pending

### Key Observation
> **Notable:** The strategic pause in 2025 is significant. The team chose to slow down and re-align with the broader Logos vision rather than ship prematurely. This suggests strong architectural integrity discipline but introduces timeline risk.
