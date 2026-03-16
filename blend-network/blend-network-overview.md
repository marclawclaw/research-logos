---
title: "Blend Network — Overview"
tags: [nomos, blend-network, proposer-anonymity, privacy, mixnet]
source: https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
date: 2026-03-16
---

# Blend Network — Overview

## Summary

The Nomos Blend Network is an anonymous broadcasting protocol and Bedrock Service designed to protect block proposers from deanonymisation via network analysis. It extends the privacy guarantees of Cryptarchia (Private PoS) by obfuscating the link between a proposal and its proposer.

## Key Points

- **Purpose:** Prevent adversaries from linking a block proposal to its proposer through network observation.
- **Mechanism:** Proposals travel through multiple intermediary nodes before being broadcast, using layered encryption, random delays, and artificial cover traffic.
- **Role in Nomos:** A [Bedrock Service](https://blog.nomos.tech/participating-in-nomos-bedrock-services/) — participation requires staking and registration via the Service Declaration Protocol (SDP).
- **Design goals:** Minimise bandwidth usage vs. general-purpose mixnets; maximise decentralisation by involving all participating nodes.

## Why Blend Exists

Cryptarchia's private leadership election keeps the proposer schedule secret, but once a block is proposed the proposer's identity can still be inferred by monitoring network traffic. The Blend Network addresses this residual exposure:

- Without Blend: an adversary can infer a node's relative stake in ~24 days for a node holding 0.1% stake.
- With Blend (3-hop path, adversary controlling 10% stake): **TTI > 10 years** at 60% confidence; **TTL > 10 years** at 50% confidence.

## Participation

| Role | Description |
|------|-------------|
| Core node | Declared, staked, maintains minimum peer connections, subject to message quota |
| Edge node | Can send proposals into the network; does not relay |

## Related Notes

- [[blend-network-encapsulation]] — layered encryption detail
- [[blend-network-message-structure]] — public/private header breakdown
- [[blend-network-security-properties]] — unlinkability, stake privacy
- [[blend-network-cover-traffic]] — artificial traffic mechanism
