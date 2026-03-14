---
topic: waku
type: concept
tags: [protocol, p2p, gossipsub, pubsub, relay]
confidence: high
last_updated: 2026-03-14
sources: [https://rfc.vac.dev/spec/11/, https://arxiv.org/pdf/2207.00038]
---

# Waku Relay

## Summary

Waku Relay (11/WAKU2-RELAY) is the core pub/sub protocol in the [[Waku]] family, built on libp2p's GossipSub. It enables privacy-preserving, censorship-resistant message propagation across a decentralized network of peers.

## Key Facts

> [!fact] Confirmed from specs and papers
> - Built on GossipSub (libp2p)
> - Uses pubsub topics for message routing (e.g., `/waku/2/default-waku/proto`)
> - Full nodes participate directly in the relay mesh
> - Supports sharding for scalability
> - Can be combined with [[RLN Rate Limiting]] for spam protection

### Protocol Flow

1. Publisher sends message to local Waku node
2. Node propagates message via GossipSub to connected peers
3. Peers forward to their connections (epidemic gossip)
4. All subscribed nodes receive the message

### Node Roles

- **Full Relay Nodes** — Participate in mesh, forward all messages
- **Light Nodes** — Don't participate; use [[Waku Lightpush]] to publish, [[Waku Filter]] to subscribe

## How it relates to Logos

Waku Relay is the backbone of [[Waku]] messaging. It provides the core message propagation mechanism that other protocols build upon. In the [[Logos]] stack, it enables real-time communication between applications.

## Performance Considerations

> [!analysis] Based on research papers
> - Latency depends on network topology and hop count
> - Bandwidth scales with number of topics subscribed
> - Sharding helps partition traffic for scalability
> - RLN adds minimal latency overhead per message

## Open Questions

- What is the current shard configuration on mainnet?
- How are pubsub topics managed and discovered?
- What are the bandwidth requirements for running a full relay node?

## Sources

- https://rfc.vac.dev/spec/11/ — 11/WAKU2-RELAY specification
- https://arxiv.org/pdf/2207.00038 — Waku academic paper
