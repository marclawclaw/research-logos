---
topic: use-cases
type: case-study
tags: [codex, waku, dapp, q-and-a, persistence, poc]
status: poc → production-ready
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.codex.storage/qaku-decentralised-q-a-with-persistence-enabled-by-codex/
---

# Qaku — Decentralised Q&A with Codex + Waku

**Website:** https://qaku.app  
**Builder:** Vaclav Pavlin (Logos Core Contributor / Solution Engineer)  
**Category:** Decentralised Application / Community Tools  
**Logos Stack Used:** Waku + Codex  
**Status:** Working PoC, being hardened for production

## What It Is

Qaku (Questions & Answers over Waku) is a fully Web3-native Q&A board application:

- Users create a Q&A session and share a link
- Participants submit and upvote questions
- Board owners can respond to and moderate questions
- No backend infrastructure — runs entirely on Waku + Codex

## Architecture

### Waku — Real-Time Layer
- Uses `js-waku` (JavaScript/TypeScript implementation)
- Follows **event sourcing model**: stores a sequence of events rather than a full state snapshot
- Uses **RLN (Rate-Limiting Nullifier)** for spam protection without compromising privacy
- Waku store is ephemeral (a few hours to a few days) — not suitable for long-term persistence alone

### Codex — Persistence Layer
- Stores Q&A data permanently on the distributed network
- Initial implementation uses **altruistic mode** (nodes offer free storage for small data)
- A bridge service called **Qaku Cache** runs both a Waku node and a Codex node to:
  - Listen for new Q&A events on Waku
  - Record them to Codex via API
  - Serve cached data from Codex back to users

## Key Technical Insight: Waku + Codex Complementarity

| Concern | Waku | Codex |
|---------|------|-------|
| Real-time messaging | ✅ | ❌ |
| Ephemeral data | ✅ | ❌ |
| Long-term persistence | ❌ | ✅ |
| Large file storage | ❌ | ✅ |
| Spam protection | RLN | — |

This pattern (Waku for transport, Codex for persistence) is a reusable architecture for any dapp needing real-time + durable data.

## Demonstrated At

- Decentralised Data Summit 2024
- Various online Logos/IFT events

## Relevance to Franck's Work

- Excellent PoC template showing how to combine Waku + Codex in a minimal real-world app
- The "Qaku Cache" bridging pattern is reusable for other projects
- Good example for developer documentation and RFP submissions
