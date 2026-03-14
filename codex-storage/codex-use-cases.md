---
title: "Codex — Use Cases & Integrations"
tags: [codex, logos, storage, use-cases, integrations, waku, bittorrent, AI, dapps]
sources:
  - https://blog.codex.storage/codex-august-updates-2/
  - https://blog.codex.storage/codex-july-updates/
  - https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
  - https://blog.codex.storage/bridging-protocols-integrating-codex-with-bittorrent/
  - https://blog.codex.storage/deploying-a-codex-node-on-akash-network/
  - https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/
  - https://blog.codex.storage/exploring-filehog-decentralised-personal-storage-with-codex/
created: 2026-03-14
updated: 2026-03-15
status: current
---

# Codex — Use Cases & Integrations

## Primary Use Cases

### 1. Decentralised Application Frontend Hosting
- Within the Logos stack, Codex/Storage enables **censorship-resistant dapp frontend delivery**
- Frontends stored on Codex can't be taken down by centralised hosting providers

### 2. Data Archiving
- Long-term durable storage with provable integrity
- Built-in repair ensures data doesn't degrade over time

### 3. Content Distribution
- P2P content delivery using CIDs
- BitTorrent v1 integration bridges existing P2P content archives to Codex

### 4. AI Training Data Storage
- August 2025: Collaborated with **Qubetics** to store QubeQobe libraries (SLM format) on Codex
- AI use case: training data persists durably at scale with **immutable provenance**
- Censorship-resistant + distributed = ideal for accountable AI data pipelines

### 5. Decentralised Identities
- Codex identified as key infrastructure for decentralised identity storage
- Data stored with no single controlling entity

### 6. Connected Vehicles
- Modern connected vehicles generate **massive, continuous data streams**
- Distributed storage networks like Codex offer better durability at lower per-GB cost
- Vehicle owners can maintain **data sovereignty** via open-access or permissioned storage
- Strong fit: immutable provenance + censorship resistance for fleet/telematics data

## Integrations

### Waku + Codex (Censorship-Resistant File Sharing)
- **Pattern:** Upload file to Codex → share CID over Waku → peer downloads from Codex node
- Example app: `building-a-censorship-resistant-file-sharing-app-with-codex-and-waku`
- Combines two Logos stack components for full decentralised file sharing

### TACo (Threshold Access Control)
- TACo adds **programmable, decentralised encryption** layer on top of Codex
- Enables per-user or per-condition access control without centralised key management
- Use case: store encrypted data on Codex; control who can decrypt via TACo policies

### BitTorrent Integration
- v1 integration for single-file BitTorrent ↔ Codex bridging (Q1 2025)
- Bridges massive existing P2P content archives to durable Codex storage
- Repo: `github.com/codex-storage/bittorrent-codex-docs`

### Akash Network
- Deploy Codex nodes on **Akash decentralised compute marketplace**
- Combines decentralised compute (Akash) + decentralised storage (Codex)
- SDL-based deployment model

### Status Network (On-Chain Feedback Platform)
- Demo: on-chain feedback exchange using Waku + Codex + Status Network L2 (gasless)
- Shows Logos stack interoperability in production-like scenario

## Developer Tools

### Third Storage (Decentralised Pinning Service)
- AI-enabled decentralised pinning service built on top of the Codex protocol
- Built by Codex/Logos DevRel Guru; **public alpha**, fully open-source
- Runs on the Codex Non-Incentivised Testnet + Logos tech stack
- Features: file upload/download dashboard, RESTful API, Codex Gateway (resolves CIDs for any file on the network)
- Announced: July 2025

### Constellations Protocol / Codex Desktop App
- "Constellations" is an early protocol concept for desktop-level Codex interaction
- Basis for the **Codex Desktop App** — surfaced in July 2025 Learn-Up session
- Goal: make running and using a Codex node accessible to non-technical users
- Part of the broader UX/developer-experience push alongside CLI Installer and Codex Factory

### Codex Factory
- CLI tool for spinning up local Codex clusters for development/testing
- Built by Adam Uhlíř (Codex team)
- Uses Docker; fully isolated from testnet/internet — predictable, repeatable environment
- Open-source; easily extensible
- Simplifies dev environment setup without needing testnet

### FileHog
- Spec for uploading entire folders to Codex
- Simple UX layer for personal decentralised storage
- Designed for real-world use cases (folder-level backups)

### Codex + Waku SDK Pattern
```
1. Run local Codex node
2. Upload file → get CID
3. Broadcast CID via Waku topic
4. Peers subscribe to topic → download file from Codex using CID
```

## Target Sectors (2026 Adoption Goals)

- **AI** — training data persistence with verifiable provenance
- **Archival blockchain storage** — immutable historical records
- **Decentralised identities** — sovereign user data storage
- **dApp deployment** — censorship-resistant frontend hosting
- **Privacy-sensitive applications** — any use case requiring storage with no central control

## Related Notes

- [[codex-overview]] — What Codex is
- [[codex-p2p-protocol]] — How data flows technically
- [[codex-roadmap-2025]] — Timeline for full marketplace and features
