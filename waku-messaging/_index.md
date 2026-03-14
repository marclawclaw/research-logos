---
topic: waku-messaging
type: index
tags: [waku, logos-messaging, p2p, privacy, messaging]
last_updated: 2026-03-15
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
- Specs: https://github.com/vacp2p/rfc-index/tree/main/waku

## Active Development Areas (as of 2026-03-14)

- Service incentivisation (LightPush PoC → Store/Filter → Service Marketplace)
- RLN testnet and browser credential workflows
- Chat SDK cryptographic foundations (Noise, Double Ratchet, De-MLS)
- API standardisation across nwaku and js-waku
- WebRTC integration for browser low-latency meshes
- Logos Messaging docs migration and brand consolidation
- Mixnet integration for enhanced anonymity

## Related Research Areas

- [[Vac]] — R&D team behind Waku specs and RLN
- [[Codex]] — storage layer; Logos Storage integration with Status Desktop
- [[Nomos]] — blockchain layer; on-chain RLN membership and payment settlement
- [[ZK in Logos]] — zero-knowledge as a design philosophy across the stack
- [[Logos Overview]] — parent organisation and movement
