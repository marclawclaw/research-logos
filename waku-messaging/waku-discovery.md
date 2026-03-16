---
topic: waku-messaging
type: concept
tags: [waku, discovery, peer-exchange, dht, discv5, bootstrap, network, libp2p]
confidence: medium
last_updated: 2026-03-16
sources:
  - https://lip.logos.co/messaging/standards/core/10/waku2.html
  - https://blog.waku.org/logos-messaging-monthly-update-november-2025/
  - https://docs.waku.org/learn/concepts/protocols
---

# Waku Peer Discovery

## Summary

Waku's **discovery domain** governs how nodes find each other in the P2P network. Multiple mechanisms are available, from static bootstrapping to dynamic DHT-based discovery. Active research (as of late 2025) is exploring DHT and metastable networks for improved reliability and censorship resistance.

## Key Facts

- Waku is built on [[libp2p]], using its peer discovery primitives as a foundation
- Three interaction domains per 10/WAKU2 spec: **gossip, discovery, request/response**
- Discovery is a distinct domain — separate from message routing (gossip/relay)
- Current mechanisms include peer exchange and DNS-based bootstrapping
- **34/WAKU2-PEER-EXCHANGE** (`/vac/waku/peer-exchange/2.0.0-alpha1`) is the formal spec

## Current Discovery Mechanisms

### Peer Exchange (34/WAKU2-PEER-EXCHANGE)
- Nodes can request a list of peers from a known node
- Enables bootstrapping without centralised infrastructure
- Still in alpha — subject to change

### DNS-based Bootstrapping
- Standard `discv5`-style DNS records listing known entry points
- Easy to configure, but introduces DNS as a trust dependency

### Discv5
- Ethereum's node discovery protocol, adapted for Waku
- Built on Kademlia-style DHT for decentralised peer finding

## Active Research (Nov 2025)

From the November 2025 Logos Messaging update:
- **DHT exploration** for improved peer finding — more decentralised than static bootstrapping
- **Metastable network research** — how to maintain stable mesh topology under node churn
- Discussions at the Budapest offsite on replacing or augmenting current discovery with more resilient mechanisms

## Why It Matters

Good discovery is critical for:
1. **Censorship resistance** — if bootstrap nodes are blocked, the network fails
2. **Mix node integration** — [[Mixnet]] nodes need discovery to form anonymous routing paths
3. **Service node marketplace** — edge nodes must find incentivised service nodes dynamically
4. **Browser/mobile** — light nodes need lightweight discovery that works from restricted environments

## Relation to Service Incentivisation

The [[waku-service-incentivisation|service marketplace]] requires discovery so edge nodes can:
- Find available service nodes (Lightpush, Store, Filter providers)
- Compare pricing and reputation dynamically
- Avoid bad-reputation nodes automatically

## Open Questions

- Will production Waku move to a DHT-first discovery model?
- How does metastable network design handle adversarial node behaviour?
- What is the bootstrapping story for fully offline-first / airgapped deployments?
- How will mix node discovery integrate with relay peer discovery?

## Sources

- https://lip.logos.co/messaging/standards/core/10/waku2.html
- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
