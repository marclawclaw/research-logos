---
topic: use-cases
type: use-case
tags: [the-graph, indexing, graphcast, waku, production]
confidence: high
last_updated: 2026-03-14
sources: [https://blog.waku.org/2024-05-13-the-graph-case-study/]
---

# The Graph Integration

## Summary

The Graph uses Waku via Graphcast to enable decentralised communication between indexers, replacing centralised servers and chat-based coordination with peer-to-peer messaging for subgraph versioning and data sync.

## Key Facts

> [!fact] Production integration
> - **Project:** The Graph — decentralised indexing protocol
> - **Use case:** Indexer-to-indexer communication
> - **Component:** Graphcast (domain-specific gossip network)
> - **Team:** GraphOps (core developer team)
> - **Waku implementation:** Rust bindings (nwaku)

### What Graphcast Solves

Before Waku, indexers used:
1. **On-chain comms** — expensive, doesn't scale
2. **Group chats** — centralised, single point of failure
3. **Bots on centralised servers** — security risks

Waku provides decentralised, censorship-resistant alternative.

### Technical Details

- All downstream "radios" act as **Waku relay nodes**
- Uses unique **pubsub topic** for Graphcast
- GraphOps runs dedicated **nwaku fleet**
- **Subgraph radios:** Real-time streaming of data updates

### Exploring

- **js-waku integration** for web interface
- Subgraph versioning sync via Waku messaging

## How it relates to Logos

The Graph demonstrates Waku as **infrastructure coordination layer** — not just chat, but critical backend communication. This validates Waku for:
- Decentralised indexing networks
- Node coordination without trusted servers
- Real-time data sync across distributed systems

## Open Questions

- What's the message volume for Graphcast?
- How does RLN integrate (or not)?
- Latency characteristics for indexer coordination?

## Sources

- https://blog.waku.org/2024-05-13-the-graph-case-study/
- https://thegraph.com/blog/subgraph-radio-information-exchange/
