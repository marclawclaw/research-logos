---
topic: waku
type: concept
tags: [protocol, light-client, filtering, bandwidth]
confidence: high
last_updated: 2026-03-14
sources: [https://rfc.vac.dev/spec/12/, https://arxiv.org/pdf/2207.00038]
---

# Waku Filter

## Summary

Waku Filter (12/WAKU2-FILTER) is a light protocol that enables bandwidth-constrained devices to subscribe to specific content topics without participating in the full [[Waku Relay]] mesh. A service node filters messages server-side and pushes only matching messages to the client.

## Key Facts

> [!fact] Confirmed from specs
> - Designed for resource-restricted devices (mobile, IoT, browsers)
> - Server-side filtering reduces client bandwidth
> - Client specifies content topics of interest
> - Service node pushes matching messages to client
> - Does NOT participate in GossipSub mesh

### Protocol Flow

1. Light client connects to a Filter service node
2. Client subscribes to specific content topics
3. Service node monitors Relay network for matching messages
4. Service node pushes matching messages to client

### Trade-offs

| Aspect | Filter | Relay |
|--------|--------|-------|
| Bandwidth | Low (filtered) | High (all messages) |
| Latency | Slightly higher | Lower |
| Trust | Requires trusted service node | Trustless |
| Censorship | Service node can censor | Censorship-resistant |

## How it relates to Logos

Waku Filter is part of the light protocol suite (with [[Waku Lightpush]] and [[Waku Store]]) that enables resource-constrained devices to interact with [[Waku]]. This is crucial for mobile-first applications in the [[Logos]] ecosystem.

## Privacy Considerations

> [!analysis] Privacy implications
> - Service nodes learn which topics clients are interested in
> - This is a privacy trade-off for bandwidth savings
> - Trusted service node selection is important
> - Future: incentivized filter with reputation systems

## Open Questions

- How do clients discover trustworthy filter nodes?
- What happens if a filter node goes offline?
- Is there redundancy/failover built into client libraries?

## Sources

- https://rfc.vac.dev/spec/12/ — 12/WAKU2-FILTER specification
- https://arxiv.org/pdf/2207.00038 — Waku academic paper
