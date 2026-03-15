---
topic: nomos
subtopic: blend-network
type: overview
tags: [blend, anonymity, mixnet, privacy, proposer, nomos, bedrock-service]
confidence: high
last_updated: 2026-03-15
sources:
  - https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
  - https://blog.nomos.tech/stirring-mixing-blending-different-approaches-to-proposer-anonymity/
---

# Blend Network Overview

## What Is It?

The Blend Network is a **Nomos Bedrock Service** — an anonymous broadcasting protocol for block proposals. It sits on top of Cryptarchia's private leadership election to close the gap between "the proposer wins privately" and "the proposer remains anonymous after they broadcast."

**The problem it solves**: Cryptarchia's Private Proof of Stake (PPoS) hides *which* node won the leadership lottery — but the moment that node sends a block proposal to the network, a passive adversary watching traffic patterns can link the proposal to its origin IP/node. The Blend Network prevents this.

---

## Why "Blend"?

"Blending" refers to making proposal messages indistinguishable from each other and from artificial cover traffic. The three core techniques:

1. **Layered encryption (encapsulation)** — message passes through multiple nodes, each removing one encryption layer. No node sees the full path.
2. **Random timing delays** — each node assigns a random delay before forwarding, defeating timing correlation attacks.
3. **Cover traffic** — synthetic messages with identical structure to real proposals, flooding the network with noise.

---

## Adversary Model

Blend was designed to resist all of the following:

| Adversary Type | Description |
|----------------|-------------|
| **Passive global** | Observes all network traffic but doesn't interfere |
| **Active local** | Controls some nodes; can modify their behaviour |
| **Active global** | Controls nodes AND observes all traffic (worst-case) |
| **Internal participant** | Runs as a full Blend node |

Security holds as long as a **majority of stake remains honest** (same assumption as Cryptarchia).

---

## Privacy Metrics

Two key metrics quantify privacy:

| Metric | Definition |
|--------|------------|
| **TTL** (Time to Link) | Time for adversary to link a proposal to its proposer with ≥50% probability |
| **TTI** (Time to Infer) | Time for adversary to infer a proposer's relative stake with ≥60% probability |

### Baseline (without Blend)
- TTI for a node with 0.1% stake: **~24 days**

### With Blend (3-hop path, adversary controls 10% of stake)
- TTL: **>10 years** (at ≥50% confidence)
- TTI: **>10 years** (at ≥60% confidence)

---

## Limitations of Private Leadership Elections Alone

Even with Cryptarchia's PPoS, **unlinkability** (proposer ↔ proposal) is not guaranteed without Blend:

- After proposing, a node's identity can be inferred from network traffic
- Prolonged observation reveals *how often* a node proposes → leaks relative stake
- **Weak unlinkability** enables self-censorship (proposers avoid including controversial txs to avoid being identified)

---

## Network Architecture

### Node Types

| Type | Role |
|------|------|
| **Core nodes** | Full Blend participants. Must stake, declare via SDP, maintain minimum peer connections, respect message quotas. |
| **Edge nodes** | Can send proposal messages into the Blend Network but don't relay or process. |

### Service Declaration Protocol (SDP)
- Publishes public metadata for every participating core node
- Provides the node set from which relay paths are randomly selected
- Also publishes each node's Ed25519 Provider ID (public key `P_i`)

### Bandwidth Design
- Quotas cap messages per node per session
- Max 3 hops per message path
- Result: low bandwidth overhead vs general-purpose mixnets

---

## Message Dissemination

Blend uses a **dissemination-first** strategy (not point-to-point routing):

1. The proposer sends the encrypted message to **all** its peers.
2. Every node relays it peer-to-peer until the entire network has seen it.
3. Simultaneously, each node attempts to decrypt — only path nodes succeed.
4. Path nodes forward the decrypted (next-layer) message after a random delay.

This means an observer can't tell from delivery patterns which node is the intended next hop — the message arrives everywhere at once.

---

## Relationship to Cryptarchia

| Cryptarchia | Blend Network |
|-------------|---------------|
| Hides *who* won the lottery | Hides *who* sent the proposal |
| Private leadership election | Anonymous proposal broadcasting |
| First line of defence | Second line of defence |
| ZK proof of leadership | ZK proof of quota + selection |

Together they provide end-to-end proposer privacy: from leadership election through block broadcast.

---

## Analysis

### Strengths
- **Practical privacy**: >10 year TTL/TTI for small stakeholders against a 10% adversary is strong
- **Scalable design**: dissemination avoids routing tables; all nodes participate
- **Low bandwidth**: quota system keeps it viable as a Bedrock Service
- **Composable with Cryptarchia**: neither system depends on the other's internals

### Risks / Open Questions
- **Cover traffic rate**: too little cover = easier to spot real proposals; too much = bandwidth pressure
- **Path length tradeoff**: shorter paths = lower latency but weaker anonymity
- **Eclipse attacks**: if adversary controls proposer's peers, dissemination pattern may leak
- **Quota design**: if quota is too tight, liveness can be affected during high-proposal periods

---

## Further Reading

- [Stirring, Mixing, Blending: Different Approaches to Proposer Anonymity](https://blog.nomos.tech/stirring-mixing-blending-different-approaches-to-proposer-anonymity/)
- [Message Encapsulation in the Nomos Blend Network](https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/)
- [[Blend Message Encapsulation]] — detailed technical breakdown
- [[Blend Proposer Anonymity]] — privacy guarantees and cover traffic
- [[Cryptarchia]] — the PPoS consensus layer Blend complements
