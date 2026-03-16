---
topic: waku-messaging
type: concept
tags: [waku, chat-sdk, noise-protocol, double-ratchet, de-mls, group-chat, cryptography, status]
confidence: medium
last_updated: 2026-03-16
sources:
  - https://blog.waku.org/logos-messaging-monthly-update-november-2025/
  - https://blog.waku.org/waku-monthly-update-october-2025/
---

# Waku Chat SDK

## Summary

The **Waku Chat SDK** is an emerging library providing higher-level cryptographic messaging primitives on top of the Waku transport layer. It implements secure 1:1 and group messaging protocols — including Noise, Double Ratchet, and De-MLS — targeting the Chat SDK as the foundation for Status and future Logos communication apps.

## Key Facts

- Separate from the core Waku P2P transport — Chat SDK is an **application-layer SDK**
- Primary consumer: **Status** (Desktop, Mobile, future web)
- Written to be portable across backends (nwaku / js-waku / logos-delivery)
- Active development as of H2 2025

## Cryptographic Stack

### Noise Protocol Framework
- Provides secure channel establishment (key exchange + authentication)
- Noise examples were implemented and tested (Nov 2025)
- Foundation for 1:1 encrypted sessions before Double Ratchet upgrade

### Double Ratchet
- Provides **forward secrecy** and **break-in recovery** for 1:1 messaging
- Scaffolding and cleanup in progress as of Nov 2025
- Standard component — same protocol used in Signal, WhatsApp

### Ratcheting Private Identifiers
- Initial draft produced Nov 2025
- Aims to prevent correlating messages to a single long-term identity
- Enhances metadata protection beyond message content encryption

### De-MLS (Decentralised MLS)
- **MLS** = Messaging Layer Security (IETF RFC 9420) — standard for group key agreement
- **De-MLS** = decentralised variant for P2P group chats without a central server
- Architecture reviewed for Chat SDK security model (Nov 2025)
- Goal: secure group messaging (Status Communities equivalent) without server-held group state

## Integration Concerns

### Key Storage & Database Patterns
- Discussions around how Chat SDK manages key persistence
- Important for Status backend compatibility and migration
- Trade-offs between security (keys in secure enclave) and portability

### Status Backend Integration
- Chat SDK is being designed to slot into the existing Status backend
- Must remain compatible with `status-go` (the current Status implementation)
- SDS (Secure Delivery System) integration in status-go reached green CI (Nov 2025)

### WebRTC Browser Meshes
- Discussion of integrating **WebRTC** for low-latency P2P meshes in browser contexts
- Would complement the Waku relay for latency-sensitive chat use cases
- Status: exploratory / under discussion as of Nov 2025

## Why It Matters for Logos

The Chat SDK is the primary user-facing interface to Logos Messaging for most people:
- Status Mobile + Desktop = most visible Logos consumer application
- A robust Chat SDK enables Logos to compete with Signal/WhatsApp/Matrix on privacy
- De-MLS design is critical for group messaging at scale without centralised key servers

## Open Questions

- When will De-MLS be production-ready for Status Communities?
- How does Double Ratchet interact with Waku content topic privacy model?
- Will Chat SDK be published as a standalone open-source library for third parties?
- What is the performance profile of De-MLS at scale (large groups)?

## Related Notes

- [[waku-overview]] — transport layer the Chat SDK runs on
- [[waku-rln-spam-protection]] — spam protection for messages Chat SDK sends
- [[waku-use-cases]] — Status as primary consumer
- [[Logos Overview]] — broader mission context

## Sources

- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
