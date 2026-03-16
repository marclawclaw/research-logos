---
title: "Blend Network – Security Properties"
tags: [nomos, blend-network, security, unlinkability, stake-privacy, zk-proofs]
source: https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
date: 2026-03-17
topic: blend-network
---

# Blend Network – Security Properties

## Adversary Model

Blend is designed to protect against a broad adversary class:

| Adversary Type | Description |
|---|---|
| **Passive** | Observes network traffic but does not modify behaviour |
| **Active** | Controls some nodes; can modify their behaviour |
| **Global observer** | Sees all network traffic simultaneously |
| **Local observer** | Only sees traffic at compromised nodes |
| **Internal** | Participates as a full Blend node |
| **External** | Monitors communications from outside |

Security analyses assume worst-case behaviour, provided the majority-honest-stake assumption holds.

## Core Security Properties

### Unlinkability

Even with multiple compromised nodes, an adversary **cannot link** incoming and outgoing messages unless they control every node in a message's path. Each hop cryptographically transforms the message, so content-based linking is infeasible across hops. Combined with random delays, timing-based linking is also prevented.

### Preventing Message Association

Ephemeral key pairs are generated fresh per message. Keys are session-scoped and quota-limited, preventing an adversary from grouping multiple messages from the same sender based on key reuse or shared metadata.

### Verifiability

Despite strong anonymity guarantees, nodes can verify:
- Messages are correctly formed (via cryptographic signatures embedded in headers).
- The relay path was randomly selected (Proof of Selection / PoS).
- Senders have not exceeded their message quota (Proof of Quota / PoQ).

This is achieved using **zero-knowledge proofs**, preserving anonymity while enabling correctness checks.

### Stake Privacy

Because proposals cannot be linked to proposers, adversaries cannot count how often a node proposes and therefore cannot infer relative stake. TTI (time to infer) with Blend exceeds **10 years** for a 0.1%-stake node against a 10%-stake adversary.

## Quota System (Anti-Spam)

Two quota mechanisms prevent Blend from being abused:

- **PoQ per ephemeral key**: limits number of keys (and thus messages/hops) per session.
- **Nullifiers**: prevent proof reuse across messages or sessions.

## Random Delays

Messages are assigned a randomised hold delay at each hop before re-dissemination. This breaks timing correlation between incoming and outgoing messages, preventing a global observer from linking message streams across nodes even when content has been transformed.

## Related Notes

- [[blend-network-overview]]
- [[blend-network-message-encapsulation]]
- [[blend-network-cover-traffic]]
