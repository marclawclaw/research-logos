---
topic: nomos
subtopic: blend-network
type: index
tags: [blend, anonymity, mixnet, privacy, proposer, nomos]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
  - https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
---

# Blend Network — Research Index

Research on the Nomos Blend Network — the anonymous broadcasting protocol that protects block proposers from deanonymisation.

## Notes

- [[Blend Network Overview]] — architecture, goals, adversary model, privacy metrics
- [[Blend Message Encapsulation]] — layered encryption, message structure, encapsulation/decapsulation process
- [[Blend Proposer Anonymity]] — unlinkability, stake privacy, cover traffic, message lifecycle

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Purpose | Anonymous block proposal broadcasting |
| Layer | Nomos Bedrock Service |
| Protocol | Blend Protocol (mixnet-inspired) |
| Max hops | 3 (`h_max`) |
| Privacy metric (TTL) | >10 years for 0.1% stake node vs 10% adversary |
| Privacy metric (TTI) | >10 years for stake inference |
| Key tech | Layered encryption, random delays, cover traffic, ZK proofs |
| Participation | Core nodes (staked + SDP declared) + edge nodes (send only) |
| Bandwidth | Low — quota enforced per node |

## Related Notes

- [[Cryptarchia]] — Private PoS consensus; Blend complements its leader election privacy
- [[Nomos Blockchain Overview]] — overall Nomos architecture
