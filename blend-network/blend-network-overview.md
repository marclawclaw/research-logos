---
title: "Blend Network – Overview"
tags: [nomos, blend-network, privacy, proposer-anonymity, pos]
source: https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
date: 2026-03-17
topic: blend-network
---

# Blend Network – Overview

The Nomos Blend Network is an anonymous broadcasting protocol designed to sever the link between block proposers and their proposals. It operates as a **Bedrock Service** within the Nomos architecture, complementing the Private Proof of Stake (PPoS) consensus protocol Cryptarchia.

## Problem It Solves

Cryptarchia's private leadership election hides *who will* propose a block before the fact, but once a proposal is broadcast, network analysis can still link the message back to the proposer. Without further protection:

- **Unlinkability** is weak: adversaries can link a proposal to the node that sent it.
- **Stake privacy** is exposed: by observing how often a node proposes, an adversary can infer its relative stake. Time-to-infer (TTI) without Blend ≈ **24 days** for a node with 0.1% stake.

## What Blend Does

Blend routes proposals through several intermediary nodes before broadcasting them to the full Nomos Network, using three main techniques:

1. **Layered encryption (encapsulation)** – each node in the relay path peels one layer, transforming the message.
2. **Random timing delays** – nodes hold messages for a randomised duration before re-disseminating, breaking timing correlation.
3. **Cover traffic** – artificial indistinguishable messages increase network noise.

## Anonymity Guarantees (with Blend)

For an adversary controlling 10% of total stake, with a 3-hop relay path and a target node holding 0.1% stake:

- **Time to link (TTL)** a proposal to its proposer: > 10 years at 50% probability.
- **Time to infer (TTI)** relative stake: > 10 years at 60% probability.

## Design Goals

- **Minimal bandwidth** – lower overhead than general-purpose mixnets.
- **Decentralisation** – all participating (declared) core nodes join the obfuscation.
- **Scalability** – quota system bounds message rate per node.

## Related Notes

- [[blend-network-message-encapsulation]]
- [[blend-network-security-properties]]
- [[blend-network-cover-traffic]]
- [[blend-network-message-lifecycle]]
