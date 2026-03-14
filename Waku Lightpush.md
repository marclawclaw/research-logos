---
topic: waku
type: concept
tags: [protocol, light-client, publishing]
confidence: high
last_updated: 2026-03-14
sources: [https://rfc.vac.dev/spec/19/, https://forum.vac.dev/t/incentivized-lightpush-a-roadmap-to-waku-service-incentivization/322]
---

# Waku Lightpush

## Summary

Waku Lightpush (19/WAKU2-LIGHTPUSH) allows resource-constrained edge nodes to publish messages to the [[Waku]] network via a service node, without participating in the [[Waku Relay]] mesh directly.

## Key Facts

> [!fact] Confirmed from specs and forum
> - Edge node sends message to service node
> - Service node publishes to Relay network on behalf of client
> - Essential for mobile/browser clients that can't maintain Relay connections
> - Part of the light protocol suite (with [[Waku Filter]], [[Waku Store]])

### Protocol Flow

1. Light client composes message
2. Client sends message to Lightpush service node
3. Service node publishes to Relay network
4. Service node returns acknowledgment to client

### Incentivization

> [!analysis] From incentivization roadmap (Sept 2024)
> - Lightpush is a key candidate for service incentivization
> - Service nodes provide value by accepting and relaying messages
> - Roadmap proposes payment for Lightpush services
> - This could enable sustainable service node economics

## How it relates to Logos

Lightpush enables mobile-first applications to publish messages without the overhead of maintaining Relay connections. Combined with [[Waku Filter]] (for receiving) and [[Waku Store]] (for history), it completes the light client experience for [[Logos]] apps.

## Trust Model

> [!analysis] Security considerations
> - Client trusts service node to actually publish the message
> - Service node could theoretically drop messages
> - Incentivization may include proof-of-publication mechanisms
> - Multiple service nodes can provide redundancy

## Open Questions

- What proof mechanism ensures messages are actually published?
- How does pricing work in the incentivized model?
- Is there a reputation system for service nodes?

## Sources

- https://rfc.vac.dev/spec/19/ — 19/WAKU2-LIGHTPUSH specification
- https://forum.vac.dev/t/incentivized-lightpush-a-roadmap-to-waku-service-incentivization/322 — Incentivization roadmap
