---
title: Codex Integrations and Use Cases
aliases: [Codex use cases, Codex integrations]
tags: [logos, codex, integrations, use-cases, waku, bittorrent, taco, akash, AI]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/
  - https://blog.codex.storage/bridging-protocols-integrating-codex-with-bittorrent/
  - https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
  - https://blog.codex.storage/deploying-a-codex-node-on-akash-network/
  - https://blog.codex.storage/revolutionising-ai-with-decentralised-storage/
  - https://blog.codex.storage/exciting-use-cases-for-decentralised-storage-in-2025-and-beyond/
---

# Codex Integrations and Use Cases

## Logos Stack Integrations

### Codex + Waku
- Codex stores files; Waku distributes the CID over P2P messaging
- Enables **censorship-resistant file sharing apps**
- Both are Logos stack components — natural composability
- Tutorial: [Building a Censorship-Resistant File Sharing App](https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/)
- Example use: `Qaku` — decentralised Q&A with Codex-persisted data

## External Protocol Integrations

### BitTorrent
- v1 integration completed Q1 2025 (single-file)
- Allows Codex to interoperate with existing BitTorrent content
- Bridges legacy P2P file-sharing ecosystem with incentivised durability
- Repo: `codex-storage/bittorrent-codex-docs`

### TACo (Threshold Access Control)
- TACo provides programmable, decentralised encryption
- Combined with Codex: **access-controlled durable storage**
- Use case: store encrypted data on Codex; TACo manages who can decrypt
- Enables user sovereignty over both storage and access

### Akash Network
- Deploy Codex nodes on Akash's decentralised compute marketplace
- Akash = decentralised compute; Codex = decentralised storage
- Complementary: Akash provides infra, Codex provides persistent storage layer

## Use Case Categories

### Decentralised AI
- Store AI training datasets without centralised cloud
- Model weights, checkpoints, and inference artefacts
- Global storage demand amplified by ML — Codex positioned as solution

### Long-Term Archival
- Immutable, durable archival of historical records
- Blockchain archival (e.g., old blocks, state snapshots)
- Journalism / whistleblower data protection

### dApp Infrastructure
- Host dapp frontends on Codex (no centralised server)
- Smart contract front-ends that survive domain seizure
- Decentralised social media data persistence

### Personal Storage
- **FileHog** — upload entire folders to Codex network
- Censorship-resistant personal backup
- Privacy-first cloud replacement

### Decentralised Identity
- Store verifiable credentials and DIDs
- No centralised identity provider dependency

## Developer Tools

| Tool | Purpose |
|---|---|
| Codex CLI Installer | Install node + join testnet |
| Codex Factory | Spin up local Codex clusters for dev/testing |
| REST API (`api.codex.storage`) | App integration |
| C API + Go bindings | Native library integration |
| Rust bindings | `nipsysdev/storage-rust-bindings` |
