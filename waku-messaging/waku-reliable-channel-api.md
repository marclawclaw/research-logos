---
topic: waku-messaging
type: concept
tags: [waku, reliable-channel, api, developer-experience, sds, reliability, messaging]
confidence: medium
last_updated: 2026-03-16
sources:
  - https://blog.waku.org/waku-monthly-update-october-2025/
  - https://blog.waku.org/logos-messaging-monthly-update-november-2025/
---

# Waku Reliable Channel API

## Summary

The **Reliable Channel API** is an effort to provide developers with a simple, high-level messaging interface that includes built-in reliability guarantees — abstracting away the complexity of Waku's underlying protocol suite. The concept was formally kick-started by Waku lead **Franck Royer** in a Vac forum post in October 2025.

## Background

Waku's core protocols (Relay, Filter, Store, LightPush) are powerful but low-level. Developers building applications must manually:
- Choose which combination of protocols to use
- Handle message deduplication and ordering
- Implement retry and acknowledgement logic
- Manage offline delivery via Store queries

The Reliable Channel API aims to hide this complexity behind a single, batteries-included interface.

## Key Facts

- **Origin:** Proposed by Franck Royer (Waku lead) on the Vac Research Forum, October 2025
- **Foundation:** Builds on **SDS** (Secure Delivery System) work
- **SDS status:** Integration in status-go reached green CI (Nov 2025), cleared for first merge
- **SDS in js-waku:** Experimental SDS-R integration begun in js-waku (Oct 2025)
- **API focus areas:** Send API, Storage API, Health API (across nwaku and js-waku implementations)
- **Goal:** A unified, standardised API across all Waku implementations

## SDS (Secure Delivery System)

SDS is the underlying protocol layer providing the reliability guarantees:
- Message acknowledgements and retries
- Detection of missing messages (for requesting via Store)
- Causal ordering support
- Integration path: Relay/Filter for live messages + Store for historical gap-fill

## Why It Matters

Without a Reliable Channel API, every Waku-based application independently reimplements delivery guarantees. This:
- Creates fragmented, inconsistent user experiences
- Raises the barrier to developer adoption
- Makes cross-app compatibility harder

A standard API enables the "plug Waku in and it just works" experience that drives adoption.

## Developer Experience Context

The API work sits within a broader developer experience push:
- Local development environment docs published (Nov 2025)
- WebRTC for low-latency browser meshes under discussion (potential alternative transport)
- API standardisation across nwaku and js-waku implementations — a key November offsite topic

## Open Questions

- What is the final API surface for the Send API? (streaming vs. callback patterns)
- How does the Health API expose node/network status to applications?
- Will the Reliable Channel API become the primary Waku developer entry point?
- Timeline to stable, documented release?

## Related Notes

- [[waku-protocols]] — underlying Relay, Store, Filter, LightPush protocols
- [[waku-chat-sdk]] — Chat SDK builds on similar reliability foundations
- [[nwaku-logos-delivery]] — nwaku reference implementation
- [[waku-use-cases]] — developer-facing applications

## Sources

- https://blog.waku.org/waku-monthly-update-october-2025/
- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
