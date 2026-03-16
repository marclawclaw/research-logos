---
title: "Codex – Ecosystem Integrations & Use Cases"
tags: [logos, codex, storage, integrations, taco, waku, akash, dappnode, ai, bittorrent]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
  - https://blog.codex.storage/deploying-a-codex-node-on-akash-network/
  - https://blog.codex.storage/bridging-protocols-integrating-codex-with-bittorrent/
  - https://blog.codex.storage/exploring-filehog-decentralised-personal-storage-with-codex/
  - https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/
  - https://blog.codex.storage/codex-august-updates-2/
---

# Codex – Ecosystem Integrations & Use Cases

## Core Logos Stack Integrations

### Waku (P2P Messaging)
- Handles metadata and sharing link delivery between users
- Enables dapps where storage (Codex) and comms (Waku) are both decentralised
- Example: file-sharing app where CIDs are exchanged over Waku channels
- Both built on libp2p — natural compatibility

### Logos Blockchain (formerly Nomos)
- On-chain smart contracts anchor storage requests
- Verifiable Manifest CIDs submitted to blockchain
- ZK proof verification happens at blockchain layer
- Status Network L2 (gasless) used in some PoC demos

## External Integrations

### TACo (Threshold Access Control)
- Adds **programmable, decentralised encryption** to Codex-stored files
- Content encrypted in-browser; decryption gated by on-chain conditions
- Conditions can be: token holdings, time windows, custom predicates
- Keys generated/shared via distributed key generation (no central key server)
- **Cyphershare** = reference dapp using Codex + TACo + Waku
  - Live at: https://share.hackyguru.com
  - Code: https://docs.taco.build/for-developers/integrations/waku-+-codex

### Akash Network
- Decentralised compute marketplace
- Codex nodes can be deployed on Akash using SDL-based deployment
- Enables hosting Codex storage nodes without traditional cloud providers

### Dappnode
- One-click Codex node setup via Dappnode package
- `codex-storage/DAppNodePackage-codex` on GitHub
- Targets non-technical users who want to contribute storage

### BitTorrent (Protocol Bridge)
- Research/integration into bridging Codex with BitTorrent protocol
- BitTorrent has massive active communities and archive content
- Potential for data migration and cross-protocol content discovery

### Qubetics (AI Use Case)
- Integrated Codex into AI-centric product stack
- QubeQobe libraries stored in SLM format on Codex
- Demonstrates Codex for **AI training data persistence**:
  - Durable, censorship-resistant storage at scale
  - Immutable provenance for training datasets
  - Accountability for AI data pipelines

## Application Patterns

### Censorship-Resistant File Sharing
- Stack: Codex (storage) + Waku (comms) + TACo (access control)
- Files persist without central servers
- Sharing links transmitted peer-to-peer

### Decentralised Personal Storage (FileHog Pattern)
- Upload entire folders to Codex
- Simple CLI/tool wrapping the REST API
- Focus on ease of use for privacy-conscious individuals

### On-Chain Feedback Platform (Demo)
- Built by Codex DevRel team
- Uses Waku + Codex + Status Network L2 (gasless)
- Demonstrates integration depth across Logos stack

### Dapp Frontend Hosting
- Codex can host static frontends for dapps
- Combined with Logos blockchain: no centralised hosting needed at any layer
- True "unstoppable app" architecture

## Related Notes

- [[codex-overview]] — Codex in the Logos stack
- [[codex-developer-integration]] — Building with Codex REST API
- [[codex-p2p-network]] — Network fundamentals
