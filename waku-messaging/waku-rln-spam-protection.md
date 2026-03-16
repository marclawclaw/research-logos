---
topic: waku-messaging
type: concept
tags: [waku, rln, spam, zero-knowledge, zk, rate-limiting, nullifier, membership]
confidence: high
last_updated: 2026-03-16
sources:
  - https://docs.waku.org/learn/concepts/protocols
  - https://rfc.vac.dev/vac/32/rln-v1/
  - https://blog.waku.org/first-steps-toward-incentivising-waku-2/
---

# RLN — Rate-Limiting Nullifier (Waku Spam Protection)

## Summary

**RLN (Rate-Limiting Nullifier)** is a zero-knowledge-based mechanism that enables Waku to enforce per-node message rate limits without revealing identities. It economically disincentivises spam by combining ZK proofs with on-chain membership and financial penalties.

## Key Facts

- **Type:** Zero-knowledge proof system
- **Spec:** https://rfc.vac.dev/vac/32/rln-v1/
- **Purpose:** Enforce message rate limits across all peers without central authority
- **Membership:** Scarce, registered via on-chain smart contract
- **Implementation:** [[zerokit]] — browser-compatible ZK credential management
- **Related protocol:** [[RLN Relay]] (extends [[Waku Relay]])

## How It Works

1. Nodes register membership on-chain (smart contract), acquiring rate-limit credentials
2. Each message is accompanied by a ZK proof demonstrating the sender holds valid membership
3. The proof encodes a **nullifier** — if the same member exceeds the rate limit, the nullifier reveals their identity (enabling slashing)
4. Spammers face **financial penalties** and **network removal**

## Economic Model

- Membership is **scarce and valuable** — limits total network publishing capacity
- Service node incentivisation PoC leverages this: edge nodes pay service nodes that own RLN credentials (see [[Waku Service Incentivisation]])
- Creates direct economic relationship between publishing capacity and membership cost

## Browser Support

- [[zerokit]] handles ZK credential workflows in browser environments
- RLN membership registration portal documentation in progress (as of Nov 2025)
- Browser-based credential management is an active development area

## Testnet

RLN Relay testnet active as of late 2025 — coordinated with service incentivisation work.

## Relation to Logos

RLN is a key [[Vac]] research output applied to Waku. It exemplifies the Logos stack's philosophy: using ZK proofs not just for privacy but as a **design philosophy** for building trust-minimised systems.

## Related Notes

- [[Waku Protocols]] — full protocol suite
- [[Waku Service Incentivisation]] — RLN role in payment PoC
- [[ZK in Logos]] — broader ZK applications in the stack
- [[Vac]] — research team behind RLN

## Sources

- https://docs.waku.org/learn/concepts/protocols
- https://rfc.vac.dev/vac/32/rln-v1/
- https://vac.dev/rln-relay
