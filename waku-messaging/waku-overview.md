---
topic: waku-messaging
type: concept
tags: [waku, messaging, p2p, privacy, logos, censorship-resistance, web3]
confidence: high
last_updated: 2026-03-15
sources:
  - https://docs.waku.org
  - https://blog.waku.org
---

# Waku — P2P Messaging Protocol Overview

## Summary

Waku is a family of robust, censorship-resistant, peer-to-peer communication protocols enabling privacy-focused messaging for Web3 applications. It allows developers to integrate decentralised communication features into dApps without compromising security or privacy. As of November 2025, Waku has been rebranded as **Logos Messaging** as part of the unified Logos technology stack identity.

## Key Facts

- **Not a blockchain** — no gas fees, operates as a separate network layer
- **Not just for chat** — supports any application requiring secure, private data transmission
- **Not long-term storage** — focuses on short, ephemeral, real-time messaging
- **Built on** [[libp2p]] GossipSub protocol
- **Addresses** the [Anonymity Trilemma](https://eprint.iacr.org/2017/954.pdf) — trade-offs between anonymity, scalability, and latency
- **Modular** — applications can tune trade-offs for their specific needs
- **Primary production integrations:** Status Mobile, Safe Harbour (multisig), The Graph, Railgun

### Core Design Principles

1. **Privacy-preserving** — encrypted communication, content topics, RLN spam protection
2. **Censorship-resistant** — pure P2P, no central servers or chokepoints
3. **Modular** — compose only the protocols you need
4. **Resource-aware** — light node support for browsers and mobile devices
5. **Scalable** — efficient GossipSub mesh handles many nodes

## How it Relates to Logos

Waku is the **messaging layer** of the [[Logos Stack]], complementing:
- [[Codex]] — decentralised storage layer
- [[Nomos]] — privacy-preserving blockchain / consensus layer
- [[Vac]] — R&D unit providing cryptographic and protocol research

As of November 2025, Waku was formally folded into the **Logos identity** as "Logos Messaging." The protocols remain open-source and available to any application requiring privacy-preserving P2P communication.

Waku serves as the real-time coordination and communication backbone for Logos-based applications — enabling Status Communities, off-chain voting, multi-sig coordination, and Layer 2 mempool broadcasting.

## Open Questions

- How does Waku message persistence integrate with [[Codex]] archival storage?
- What are the bandwidth/latency characteristics at production scale (e.g., large Status Communities)?
- How mature is the RLN membership on-chain registration process for end users?
- What is the path to fully decentralised service nodes (incentivisation timeline)?
- How does the Logos Messaging rebrand affect documentation and SDKs long-term?

## Sources

- https://docs.waku.org
- https://blog.waku.org
- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
