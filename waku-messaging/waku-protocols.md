---
topic: waku-messaging
type: reference
tags: [waku, protocols, relay, filter, store, lightpush, rln, gossipsub]
confidence: high
last_updated: 2026-03-14
sources:
  - https://docs.waku.org/learn/concepts/protocols
---

# Waku Protocol Suite

## Summary

Waku takes a **modular approach**, providing a family of composable protocols. Applications select and combine protocols based on their trade-offs between anonymity, scalability, and latency. All protocols are built on [[libp2p]].

## Core Protocols

### Relay (WakuRelay)
- **Architecture:** Pub/Sub via GossipSub extension
- **Purpose:** Primary message routing — sending and receiving among peers
- **Properties:** Privacy-focused, encrypted channels, censorship protection, scales efficiently with many nodes
- **When to use:** Primary protocol for always-online nodes

### RLN Relay (Rate-Limiting Nullifier Relay)
- **Extends:** Relay protocol
- **Purpose:** Economic spam prevention without identity disclosure
- **Mechanism:** [[RLN]] (Rate Limit Nullifiers) — ZK proofs enforce per-peer message rate limits
- **Penalties:** Financial penalties + network removal for spammers
- **Membership:** On-chain smart contract registration, credentials stored via [[zerokit]] in browser
- **See:** [[RLN Rate Limiting]]

### Filter
- **Architecture:** Request/Response
- **Purpose:** Allows light nodes to selectively subscribe to specific messages by [[Content Topics]]
- **Trade-off:** Bandwidth-efficient but **reduced privacy** — must disclose content topic to service node
- **Best for:** Resource-constrained devices (mobile, browser)

### Store
- **Purpose:** Historical message retrieval — stores relayed messages for later querying
- **Use case:** Offline peers retrieving missed messages upon reconnection, DApp startup
- **Caveat:** Does NOT guarantee data availability; use Relay/Filter when node is online

### Light Push
- **Architecture:** Request/Response
- **Purpose:** Message publishing for nodes with limited bandwidth or short connection windows
- **Mechanism:** Client sends via service node; receives ACK when at least one peer has received it
- **Caveat:** ACK does NOT guarantee network-wide propagation
- **Incentivisation:** Subject of active PoC work (see [[Waku Service Incentivisation]])

## Message Format (WakuMessage)

| Field | Purpose |
|-------|---------|
| `content_topic` | Content-based filtering identifier |
| `payload` | Actual message data (application-defined) |
| `meta` | Additional protocol/application metadata |
| `timestamp` | Message generation time (sender-side) |
| `ephemeral` | If true, network should NOT store the message |

## Content Topics

Content topics are namespaced identifiers enabling selective message retrieval without reading all traffic. Format: `/{application-name}/{version}/{content-topic-name}/{encoding}`

## Network Domains

- **GossipSub domain** — Relay mesh for efficient broadcast
- **Request/Response domain** — Filter, Store, Light Push (direct interactions)

## Sources

- https://docs.waku.org/learn/concepts/protocols
