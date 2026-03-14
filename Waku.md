---
topic: waku
type: concept
tags: [messaging, p2p, privacy, libp2p, protocols]
confidence: high
last_updated: 2026-03-14
sources: [https://docs.waku.org, https://github.com/waku-org, https://arxiv.org/pdf/2207.00038]
---

# Waku

## Summary

Waku is a family of robust, censorship-resistant, peer-to-peer communication protocols that enable privacy-focused messaging for Web3 applications. Built on libp2p, it provides decentralized communication features without compromising security or privacy, operating without gas fees.

## Key Facts

> [!fact] Confirmed from official docs
> - Waku is NOT a blockchain — no gas fees required
> - Focuses on short, ephemeral, real-time messaging (not long-term storage)
> - Built on libp2p foundation
> - Multiple protocol implementations: [[nwaku]] (Nim), [[js-waku]] (TypeScript), go-waku (Go)

### Protocol Family

The Waku protocol family includes:

1. **[[Waku Relay]]** — Core GossipSub-based pub/sub for message propagation
2. **[[Waku Store]]** — Historical message retrieval from archive nodes  
3. **[[Waku Filter]]** — Server-side filtering for bandwidth-constrained devices
4. **[[Waku Lightpush]]** — Delegate publishing to service nodes
5. **[[RLN Rate Limiting]]** — Zero-knowledge spam protection

### Node Types

- **Full nodes** — Participate in Relay mesh, store messages, serve light clients
- **Edge/Light nodes** — Resource-constrained; use Lightpush, Filter, Store via service nodes

## How it relates to Logos

Waku is the **messaging layer** of the [[Logos]] stack. It enables private, censorship-resistant communication between applications and users, complementing [[Codex]] (storage) and [[Nomos]] (blockchain).

## Use Cases

> [!analysis] Community-curated use cases
> - Chat messengers (private, decentralized)
> - Voting and proposals (off-chain for gas savings)
> - NFT marketplaces (off-chain bids/offers)
> - State channels (message exchanges)
> - Multi-sig wallet signature exchange
> - Game mechanics communication
> - L2 coordination (mempool, transaction aggregation)
> - Social media platforms

## Open Questions

- What is the current network size and message throughput?
- How does Waku handle message ordering and delivery guarantees?
- What is the incentive structure for running full nodes?
- How does sharding work for scaling?

## Sources

- https://docs.waku.org — Official documentation
- https://github.com/waku-org — GitHub organization
- https://arxiv.org/pdf/2207.00038 — Academic paper on Waku protocols
- https://blog.waku.org — Official blog with case studies
