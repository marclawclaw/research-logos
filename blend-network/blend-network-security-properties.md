---
title: "Blend Network — Security Properties"
tags: [nomos, blend-network, unlinkability, stake-privacy, adversary-model]
source: https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
date: 2026-03-16
---

# Blend Network — Security Properties

## Summary

The Blend Network is designed to withstand a broad adversary model and deliver two core privacy properties: **unlinkability** and **stake privacy**.

## Adversary Model

| Axis | Variants |
|------|----------|
| Activity | Active (can modify node behaviour) vs. Passive (observe only) |
| Scope | Global (full network view) vs. Local (only compromised nodes) |
| Position | External observer vs. Full participant |

Security analyses assume worst-case behaviour, provided a majority of honest stake is maintained.

## Core Privacy Properties

### Unlinkability
A proposer cannot be linked to their proposal based on network observation. Even an adversary controlling multiple Blend nodes cannot correlate incoming and outgoing messages unless they control **every node on the specific message path**.

Cryptographic transformation at each hop ensures messages look completely different before and after processing. Combined with random delays, this defeats timing analysis.

### Stake Privacy
Because proposal frequency is proportional to stake, deanonymisation enables stake inference. Blend makes this impractical:

- **Without Blend:** TTI ≈ 24 days for a 0.1% stake node
- **With Blend (3 hops, 10% adversary stake):** TTI > 10 years at 60% confidence

### Preventing Message Association
Ephemeral key pairs are generated fresh for every message, so an adversary cannot group messages by their sender based on key reuse.

### Verifiability
Despite strong anonymity, nodes can verify:
- Messages are correctly formed
- Path was randomly selected (Proof of Selection)
- Sender has not exceeded their quota (Proof of Quota)

Verification is done via **zero-knowledge proofs** embedded in each message — anonymity is not compromised.

## Related Notes

- [[blend-network-overview]] — why Blend exists
- [[blend-network-encapsulation]] — how unlinkability is implemented cryptographically
- [[blend-network-cover-traffic]] — how cover traffic supports these properties
