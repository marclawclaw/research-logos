---
topic: competitors
type: competitor
tags: [waku, libp2p, comparison, networking]
confidence: high
last_updated: 2026-03-14
sources: [https://docs.waku.org/learn/waku-vs-libp2p]
---

# Waku vs libp2p

## Summary

Waku is built on top of libp2p but adds privacy preservation, spam protection (RLN), incentive mechanisms, and protocols for resource-limited devices. libp2p is a lower-level networking library without these application-layer features.

## Key Facts

> [!fact] From official docs
> - **Relationship:** Waku is built ON TOP of libp2p
> - **Shared:** Concepts, terminologies, transport layer
> - **Different:** Scope and application-layer features

### Key Differences

| Feature | libp2p | Waku |
|---------|--------|------|
| **Scope** | Networking library | Service network |
| **Incentives** | None | Planned mechanisms |
| **Infrastructure** | You deploy your own | Can use existing network |
| **Spam protection** | None | RLN Relay |
| **Offline support** | Limited | Store/Light Push/Filter |
| **Privacy** | Basic | Privacy-preserving protocols |
| **Platform** | Various | Platform agnostic |

### What Waku Adds

1. **Incentive mechanisms** — run nodes for rewards (planned)
2. **Service network** — don't need your own infrastructure
3. **Privacy protocols** — censorship resistance built-in
4. **Resource-limited support** — Store, Light Push, Filter protocols
5. **Spam protection** — RLN Relay (Rate Limit Nullifiers)

### libp2p Strengths

- **Lower-level** — more flexible for custom use cases
- **Wider adoption** — used by IPFS, Filecoin, Ethereum, Polkadot
- **More implementations** — Go, Rust, JS, etc.
- **Mature** — longer production history

## How it relates to Logos

Understanding the libp2p foundation helps when:
- Debugging Waku issues
- Understanding transport layer
- Comparing with other libp2p-based projects (IPFS, etc.)

> [!analysis] Strategic positioning
> Waku positions itself as "libp2p + application layer features for Web3 messaging." Not competing directly — building on top with specific focus areas.

## Open Questions

- How much overhead does Waku add over raw libp2p?
- Can libp2p GossipSub users migrate to Waku easily?
- Interop between Waku and plain libp2p networks?

## Sources

- https://docs.waku.org/learn/waku-vs-libp2p
