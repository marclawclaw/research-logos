---
topic: waku
type: concept
tags: [messaging, p2p, privacy, protocol]
confidence: high
last_updated: 2026-03-14
sources: [https://docs.waku.org, https://waku.org/about]
---

# Waku Protocol Overview

## Summary

Waku is a family of peer-to-peer communication protocols enabling privacy-focused, censorship-resistant messaging for Web3 applications. It provides decentralised communication without gas fees, designed for real-time ephemeral messaging rather than long-term storage.

## Key Facts

> [!fact] From official documentation
> - **Not a blockchain** — no gas fees, operates as a separate network layer
> - **Not just for chat** — supports complex applications requiring secure data transmission
> - **Not for long-term storage** — focuses on short, ephemeral, real-time messaging
> - **Built on** libp2p GossipSub protocol
> - **Integrated in** Status Mobile app

### Core Capabilities

1. **Privacy-preserving** — encrypted communication channels
2. **Censorship-resistant** — peer-to-peer, no central chokepoints
3. **Modular** — applications control trade-offs (anonymity vs scalability vs latency)
4. **Scalable** — efficient handling of many nodes

### What Waku Addresses

The [Anonymity Trilemma](https://eprint.iacr.org/2017/954.pdf) — trade-offs between:
- Anonymity
- Scalability  
- Latency

Applications can tune these based on their needs.

## How it relates to Logos

Waku is the **messaging layer** of the Logos stack, enabling communication between:
- Users (chat, coordination)
- Applications (signalling, state updates)
- Infrastructure (node coordination)

Complements [[Codex Storage|Codex]] (storage) and [[Nomos Blockchain|Nomos]] (consensus).

## Open Questions

- How does message persistence work when combined with Codex?
- What are bandwidth requirements for different use cases?
- How mature is mobile support?
- Integration patterns with Nomos for on-chain coordination?

## Sources

- https://docs.waku.org
- https://waku.org/about
- https://docs.waku.org/learn/concepts/protocols
