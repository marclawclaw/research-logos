---
topic: waku-messaging
type: reference
tags: [waku, spec, rfc, 10-waku2, libp2p, gossipsub, protobuf, architecture]
confidence: high
last_updated: 2026-03-17
sources:
  - https://lip.logos.co/messaging/standards/core/10/waku2.html
  - https://github.com/vacp2p/rfc-index
---

# 10/WAKU2 — Formal Specification

## Summary

`10/WAKU2` is the core specification document for Waku v2, maintained by the [[Vac]] team at `vacp2p/rfc-index`. It defines the modular peer-to-peer protocol family for secure, privacy-preserving, censorship-resistant communication. Status: **draft** (Standards Track).

- **Slug:** 10
- **Status:** Draft (Standards Track)
- **Editor:** Hanno Cornelius
- **Key contributors:** Sanaz Taheri, Reeshav Khan, Daniel Kaiser, Oskar Thorén
- **Last significant revision:** February 2026 (math support added — [afd94c8](https://github.com/vacp2p/rfc-index/blob/afd94c8bc1420376ae9af7e14a4feb246f2ed621/docs/messaging/standards/core/10/waku2.md)); previously April 2025 (10/WAKU2 Update)

## Historical Roots

Waku v2 evolves from:
- **Whisper** (EIP-627) — original Ethereum devp2p messaging protocol
- **6/WAKU1** — first iteration, direct Whisper evolution
- **Waku v2 (current)** — complete redesign on [[libp2p]], more modular and scalable

Whisper → WAKU1 → WAKU2 represents a shift from a monolithic, bandwidth-heavy protocol to a lean, composable, libp2p-native stack.

## Core Design Goals

1. **Generalised messaging** — human-to-human, machine-to-machine, or mixed
2. **Peer-to-peer** — censorship-resistant, no single point of failure, shared infrastructure
3. **Runs anywhere** — designed for resource-constrained environments: mobile, browser, low-bandwidth
4. **Privacy-preserving** — pseudonymity, metadata protection, unlinkability
5. **Modular (Adaptive Nodes)** — applications choose which protocols to run; see [30/ADAPTIVE-NODES]

## Network Interaction Domains

Waku defines three distinct interaction domains:

| Domain | Protocols | Purpose |
|--------|-----------|---------|
| **Gossip domain** | Relay, RLN Relay | Pub/Sub message broadcast via GossipSub mesh |
| **Discovery domain** | Peer Exchange, DNS Discovery | Finding and connecting to peers |
| **Request/Response domain** | Filter, Store, Light Push | Direct peer interactions for targeted queries |

## libp2p Protocol Identifiers

Stable identifiers (negotiated via libp2p multistream-select):

| Protocol | Identifier |
|----------|-----------|
| Relay | `/vac/waku/relay/2.0.0` |
| Store Query | `/vac/waku/store-query/3.0.0` |
| Filter | `/vac/waku/filter/2.0.0-beta1` |
| Light Push | `/vac/waku/lightpush/2.0.0-beta1` |

Experimental identifiers:
- `/vac/waku/waku-rln-relay/2.0.0-alpha1`
- `/vac/waku/peer-exchange/2.0.0-alpha1`

## Referenced Sub-Specs

| RFC ID | Name | Purpose |
|--------|------|---------|
| 14/WAKU2-MESSAGE | WakuMessage | Message structure and payload format |
| 17/WAKU2-RLN-RELAY | RLN Relay | ZK-based rate limiting |
| 23/WAKU2-TOPICS | Topics | Content topic conventions |
| 26/WAKU-PAYLOAD | Payload | Application-level payload encoding |
| 27/WAKU2-PEERS | Peers | Peer management recommendations |
| 30/ADAPTIVE-NODES | Adaptive Nodes | Heterogeneous node participation model |
| 34/WAKU2-PEER-EXCHANGE | Peer Exchange | Peer discovery protocol |

## Encoding

All wire formats use **Protocol Buffers (protobuf)** unless otherwise specified. This is consistent with [[libp2p]] conventions.

## How it Relates to Logos

The 10/WAKU2 spec is the authoritative technical reference for anyone building on [[Logos Stack]] messaging layer. The spec is maintained under the `vacp2p/rfc-index` repository, which is governed by [[Vac]]. Understanding this spec is essential for:
- Building RFPs that integrate Waku
- Reviewing PoCs done by colleagues on the Logos stack
- Contributing to Logos ecosystem apps using [[Status SDK]], [[js-waku]], or [[nwaku]]

## Open Questions

- When will the spec graduate from "draft" to "stable"?
- How does the spec versioning relate to production deployment in [[Status]] and [[Safe Harbour]]?
- Is there a conformance test suite for implementations?

## Sources

- https://lip.logos.co/messaging/standards/core/10/waku2.html
- https://github.com/vacp2p/rfc-index/blob/main/docs/messaging/standards/core/10/waku2.md
