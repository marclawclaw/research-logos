---
topic: waku-messaging
type: concept
tags: [waku, mixnet, anonymity, privacy, libp2p, lightpush, metadata-protection]
confidence: medium
last_updated: 2026-03-15
sources:
  - https://blog.waku.org/waku-monthly-update-october-2025/
  - https://blog.waku.org/logos-messaging-monthly-update-november-2025/
---

# Waku Mixnet Integration

## Summary

Waku is integrating a **libp2p-based mixnet** layer for enhanced metadata protection — going beyond message content encryption to hide *who is talking to whom* and *when*. As of October 2025, mixnet integration was functionally complete: libp2p mix is now part of [[Waku Lightpush|LightPush]] and tested across multi-node simulations.

## Key Facts

- **What it is:** A mix network adds latency-based routing to break traffic analysis correlation
- **Integration point:** libp2p mix protocol, integrated into LightPush as of Oct 2025
- **Status:** Static mix node configurations deployed on the test network (Oct 2025)
- **Discovery research:** Active work on improved mix node discovery mechanisms (Nov 2025)
- **Rendezvous updates:** nim-libp2p received rendezvous improvements to aid mix node discovery

## Why Mixnet?

Standard Waku Relay and LightPush encrypt message *content* but do not prevent traffic analysis:
- An observer can see which node sends a message at what time
- Correlation attacks can link pseudonymous senders to real identities
- This is the **Anonymity Trilemma** trade-off: anonymity vs. scalability vs. latency

A mix network addresses this by:
1. Batching messages and introducing random delays
2. Routing through a sequence of mix nodes
3. Making timing correlation attacks infeasible for passive adversaries

## Implementation Status (as of Mar 2026)

| Component | Status |
|-----------|--------|
| libp2p mix integration in LightPush | ✅ Complete |
| Multi-node simulation testing | ✅ Done |
| Static mix node configs on testnet | ✅ Deployed |
| Mix node discovery mechanism | 🔄 Research ongoing |
| Production deployment | ⏳ Not yet |

## Relation to Logos Philosophy

Mixnet is a direct expression of the Logos "[[ZK in Logos|zero-knowledge as design philosophy]]" principle — privacy through architecture, not just encryption. The goal is a system where even infrastructure operators cannot reconstruct communication graphs.

This positions Logos Messaging ahead of most Web3 messaging protocols (including Whisper/Waku v1) in terms of metadata protection guarantees.

## Open Questions

- What are the latency trade-offs of the libp2p mix layer vs. standard Relay?
- How will mix node discovery integrate with the broader [[waku-discovery|peer discovery]] architecture?
- Will mixnet be opt-in (per-application) or default for all LightPush messages?
- What is the economic model for mix node operators?

## Related Notes

- [[waku-overview]] — core protocol overview
- [[waku-protocols]] — LightPush and Relay protocols
- [[waku-discovery]] — peer and mix node discovery
- [[waku-service-incentivisation]] — economic model for service nodes
- [[Vac]] — research team studying anonymity properties

## Sources

- https://blog.waku.org/waku-monthly-update-october-2025/
- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
