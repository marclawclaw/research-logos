---
topic: waku
type: concept
tags: [messaging, protocols, relay, filter, store, lightpush, rln]
confidence: high
last_updated: 2026-03-14
sources: [https://docs.waku.org/learn/concepts/protocols]
---

# Waku Protocols

## Summary

Waku provides a modular set of protocols for different messaging needs: Relay for full P2P participation, Filter for lightweight subscription, Store for historical messages, Light Push for resource-constrained devices, and RLN for spam prevention.

## Key Facts

### Relay Protocol

> [!fact] Core messaging protocol
> - **Pub/Sub architecture** for sending/receiving messages
> - Extends **libp2p GossipSub**
> - Provides encryption and censorship protection
> - Scales to many nodes efficiently
> - Full participation in the network

### RLN Relay (Rate Limit Nullifiers)

> [!fact] Spam prevention
> - Extends Relay with **economic spam prevention**
> - Enforces rate limits across all peers
> - **Financial penalties** and network removal for spammers
> - Uses zero-knowledge proofs
> - **RLNv2** released 2024 — stateless, works with light clients

See [[RLN Rate Limiting]] for details.

### Filter Protocol

> [!fact] Lightweight subscription
> - Light nodes subscribe to specific messages via **content topics**
> - Optimises **bandwidth usage**
> - Trade-off: **Less privacy** — must disclose content topic to peers

### Store Protocol

> [!fact] Historical message retrieval
> - Stores messages relayed in the network
> - Enables offline peers to **retrieve missed messages**
> - **Not for long-term data availability** — use Relay/Filter when online
> - Best for: retrieving messages when a DApp starts

### Light Push Protocol

> [!fact] Request/Response for constrained devices
> - For nodes with **limited bandwidth and short connection windows**
> - Client receives **acknowledgement** when message received by remote peer
> - Remote peer forwards to Relay network
> - **No guarantee** of network-wide propagation

### Waku Message Format

Messages include:
- `content_topic` — for filtering
- `payload` — actual data
- `meta` — application-specific metadata
- `timestamp` — when generated
- `ephemeral` — whether to store or not

## How it relates to Logos

These protocols form the **communication primitives** for the Logos stack:
- Relay/RLN for main network participation
- Filter/Light Push for mobile and browser clients
- Store for reconnection scenarios

## Open Questions

- What are the typical bandwidth numbers for each protocol?
- How do content topics impact privacy in practice?
- Store retention policy — how long are messages kept?
- RLN stake requirements?

## Sources

- https://docs.waku.org/learn/concepts/protocols
- https://rfc.vac.dev/vac/32/rln-v1/
- https://vac.dev/rln-relay
