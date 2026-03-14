---
topic: use-cases
type: research-notes
tags: [codex, archival, ethereum, enterprise, blockchain-data]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.codex.storage/exciting-use-cases-for-decentralised-storage-in-2025-and-beyond/
  - https://blog.codex.storage/state-of-the-decentralised-storage-space-in-2024-and-predictions-for-2025/
---

# Codex — Archival Storage Use Cases

## The Problem

As global data generation grows, centralised archival becomes:
- Expensive and environmentally costly (large data centres)
- Single-point-of-failure for historical data
- Controlled by a handful of corporate entities

## Key Archival Use Cases

### 1. Blockchain Historical Data (Ethereum Archive Nodes)

Ethereum generates enormous volumes of historical data — transactions, interactions, state changes — that must remain accessible for:
- Validation and auditing
- Developer tooling and indexing
- Long-term historical research

Currently, this data is concentrated with a few centralised providers (Infura, Alchemy, etc.). Codex enables:
- Persistent, censorship-resistant storage of Ethereum historical state
- Distributed across thousands of independent nodes
- Accessible and durable without relying on any single company

**See also:** https://blog.codex.storage/scaling-the-archive-ethereums-quest-for-data-abundance/

### 2. Enterprise Hybrid Cloud ("Cold" Archival Tier)

Enterprises are integrating Codex alongside centralised cloud (AWS, GCP) for:
- **Hybrid cloud architecture**: operational data on cloud, archival on Codex
- Immutable, tamper-proof long-term records
- Geographically distributed redundancy (replicating what enterprises already do manually, but more efficient)
- Regulatory compliance (data retention requirements)

Key selling point: Codex offers a **new class of data durability** — not just geo-redundancy but cryptographically-guaranteed persistence.

### 3. Decentralised Collaboration and File Sharing

Use cases:
- **Researchers** sharing open-access scientific datasets across institutions
- **Journalists** sharing sensitive information securely across borders
- **Artists** distributing creative work directly without platform intermediaries

Technical framing: Codex as "**BitTorrent with persistence**" — peer-to-peer sharing where files remain accessible even after the original uploader goes offline or the network loses nodes.

### 4. Decentralised Identity and Document Management

- Medical records stored with user-controlled access
- Legal documents with robust security and privacy
- Personal identity data with no centralised custodian
- Smart contract-based access control (integrates with TACo for fine-grained access)

## Market Context

- Decentralised cloud storage market: projected to surpass **$4.5B by 2034**
- Enterprise adoption of hybrid cloud growing — Codex targets the durability tier
- Increasing regulatory pressure on data retention drives demand for provably durable storage

## Technical Differentiation

Codex vs traditional archival solutions:
| Property | Traditional Cloud | Codex |
|----------|------------------|-------|
| Data durability | SLA-based | Cryptographic proofs |
| Censorship resistance | No | Yes |
| Centralisation | High | None |
| Transparency | Opaque | Verifiable |
| Cost scaling | Linear (expensive) | Horizontal (cheaper at scale) |

## Relevance to Franck's Work

- Strong narrative for enterprise-facing RFPs
- Ethereum archival data use case directly relevant to Logos ecosystem positioning
- Consider PoC: archiving eco-prio or RFP submissions on Codex with Waku-based access notifications
