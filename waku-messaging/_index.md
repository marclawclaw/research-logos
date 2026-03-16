---
topic: waku-messaging
type: index
tags: [waku, logos-messaging, p2p, privacy, messaging]
last_updated: 2026-03-17
research_refresh: 2026-03-17
sources:
  - https://docs.waku.org
  - https://blog.waku.org
  - https://github.com/waku-org/nwaku
  - https://lip.logos.co/messaging/standards/core/
  - https://forum.vac.dev/c/waku/5
---

# Waku / Logos Messaging — Research Index

> **Note (Nov 2025):** Waku has been officially rebranded as **Logos Messaging** as part of the unified Logos technology stack identity. Protocols and SDKs are unchanged. See [[Logos Messaging Rebrand]].

## Overview

Waku is a family of P2P communication protocols providing **censorship-resistant, privacy-preserving messaging** for Web3. It is the messaging layer of the [[Logos Stack]], complementing [[Codex]] (storage) and [[Nomos]] (blockchain/consensus).

## Atomic Notes

| Note | Description |
|------|-------------|
| [[waku-overview]] | Core overview — what Waku is, key properties, Logos positioning |
| [[waku-protocols]] | Full protocol suite: Relay, RLN Relay, Filter, Store, LightPush, WakuMessage format |
| [[waku-content-topics]] | Content topics — format, k-anonymity patterns, privacy trade-offs |
| [[waku-spec-10]] | 10/WAKU2 formal spec — libp2p IDs, network domains, sub-specs |
| [[waku-rln-spam-protection]] | Rate-Limiting Nullifier — ZK-based spam prevention and economic rate limiting |
| [[waku-service-incentivisation]] | LightPush incentivisation PoC — toward a Waku Service Marketplace |
| [[waku-use-cases]] | Real-world integrations: Safe Harbour, The Graph, Railgun, Status |
| [[nwaku-logos-delivery]] | nwaku / logos-delivery — Nim reference implementation and SDKs |
| [[logos-messaging-rebrand]] | November 2025 rebrand: Waku → Logos Messaging |
| [[waku-discovery]] | Peer discovery mechanisms — Peer Exchange, discv5, DHT research |
| [[waku-chat-sdk]] | Chat SDK — Noise, Double Ratchet, De-MLS, Status integration |
| [[waku-mixnet]] | Mixnet — libp2p mix integration into LightPush for metadata protection |
| [[waku-reliable-channel-api]] | Reliable Channel API — SDS-based developer-facing reliability layer |

## Quick Reference

**Core Protocols:**
- **Relay** — GossipSub pub/sub, the primary message transport
- **RLN Relay** — Relay + ZK-based rate limiting (spam protection)
- **Filter** — Light node selective subscription by content topic
- **Store** — Historical message retrieval for offline/startup use
- **LightPush** — Delegated publishing for bandwidth-constrained clients

**Implementations:**
- `logos-messaging/logos-delivery` (Nim / nwaku) — reference node
- `waku-org/js-waku` (TypeScript) — browser and Node.js SDK
- `waku-org/go-waku` (Go) — Go SDK

**Key URLs:**
- Docs: https://docs.waku.org
- Blog: https://blog.waku.org
- Ideas: https://ideas.waku.org
- Specs (canonical): https://lip.logos.co/messaging/standards/core/
- Specs (source): https://github.com/vacp2p/rfc-index/tree/main/docs/messaging

## Active Development Areas (as of 2026-03-17)

- Service incentivisation (LightPush PoC → Store/Filter → Service Marketplace)
- RLN testnet and browser credential workflows
- Chat SDK cryptographic foundations (Noise, Double Ratchet, De-MLS)
- API standardisation across nwaku and js-waku
- WebRTC integration for browser low-latency meshes
- Logos Messaging docs migration and brand consolidation
- Mixnet integration for enhanced anonymity
- DHT / metastable network research for peer discovery
- Chat SDK: De-MLS group key agreement, Ratcheting Private Identifiers, WebRTC browser meshes
- Mixnet: libp2p mix deployed in LightPush on testnet; mix node discovery research ongoing
- Reliable Channel API: SDS integration in status-go merged; Franck Royer leading standardisation effort

## Related Research Areas

- [[Vac]] — R&D team behind Waku specs and RLN
- [[Codex]] — storage layer; Logos Storage integration with Status Desktop
- [[Nomos]] — blockchain layer; on-chain RLN membership and payment settlement
- [[ZK in Logos]] — zero-knowledge as a design philosophy across the stack
- [[Logos Overview]] — parent organisation and movement
