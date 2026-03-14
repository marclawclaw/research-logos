---
topic: waku
type: concept
tags: [protocol, storage, history, archive]
confidence: high
last_updated: 2026-03-14
sources: [https://rfc.vac.dev/spec/13/, https://forum.vac.dev]
---

# Waku Store

## Summary

Waku Store (13/WAKU2-STORE) is a light protocol that allows clients to query archive nodes for historical messages that were previously relayed in the [[Waku]] network. It enables offline message retrieval and catch-up after reconnection.

## Key Facts

> [!fact] Confirmed from specs
> - Allows querying historical messages from store nodes
> - Two modes: full-mode (persist messages) and light-mode
> - `store-capacity` parameter limits number of persisted messages
> - Query by content topic, time range, pagination supported

### Use Cases

- Retrieve missed messages after going offline
- Load chat history in messaging apps
- Audit trail for message verification
- State reconstruction for dApps

### Protocol Flow

1. Client connects to a Store node
2. Client sends query with filters (topic, time range, etc.)
3. Store node returns matching historical messages
4. Client processes messages locally

## How it relates to Logos

Waku Store complements [[Waku Relay]] by providing historical message access. While Relay handles real-time propagation, Store enables catch-up and history retrieval. This is essential for mobile apps that frequently go offline.

## Considerations

> [!analysis] Operational considerations
> - Store nodes require significant storage capacity
> - Privacy implications: store nodes see message metadata
> - Incentivization needed for running store nodes (see incentive roadmap)
> - Message retention policies vary by node operator

## Open Questions

- What is the typical message retention period on public store nodes?
- How is storage incentivized currently?
- What are the query performance characteristics?
- Is there encrypted store functionality for enhanced privacy?

## Sources

- https://rfc.vac.dev/spec/13/ — 13/WAKU2-STORE specification
- https://forum.vac.dev — Discussions on incentivization
