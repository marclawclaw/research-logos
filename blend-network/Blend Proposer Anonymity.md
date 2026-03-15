---
topic: nomos
subtopic: blend-network
type: deep-dive
tags: [blend, proposer-anonymity, stake-privacy, unlinkability, cover-traffic, nomos, privacy]
confidence: high
last_updated: 2026-03-15
sources:
  - https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
  - https://blog.nomos.tech/stirring-mixing-blending-different-approaches-to-proposer-anonymity/
---

# Blend Proposer Anonymity

This note covers the privacy guarantees the Blend Network provides to block proposers: unlinkability, stake privacy, cover traffic, and the full message lifecycle.

---

## The Problem

Cryptarchia's Private Proof of Stake uses a **private leadership election**: no one knows who won until they broadcast a block. But the moment a proposer sends that block over the network, traffic analysis can link the message origin to the proposer's identity.

Two key privacy properties that the Blend Network aims to guarantee:

| Property | Definition |
|----------|------------|
| **Unlinkability** | An adversary cannot link a block proposal to its proposer (the node that sent it) |
| **Stake Privacy** | An adversary cannot infer a proposer's relative stake from network observation |

Unlinkability is a prerequisite for stake privacy: if proposals are linked to proposers, proposal frequency leaks relative stake.

---

## Why Stake Privacy Matters

In Proof of Stake, the probability of winning the leadership lottery scales with your relative stake. An adversary who can link proposals to proposers can:

1. Count how often a specific node proposes
2. Divide by observation time
3. Compare to expected proposal rate → **infer relative stake**

**Without Blend**: TTI (Time to Infer) for a node with 0.1% stake ≈ **24 days**

That's a serious data leak. Relative stake is financially sensitive and enables targeted attacks.

---

## Why Unlinkability Matters Beyond Privacy

Weak unlinkability doesn't just leak financial data — it has second-order effects:

- **Self-censorship**: if proposers know they'll be identified, they may avoid including controversial or politically sensitive transactions
- **Targeted attacks**: known high-stake proposers become DDoS or physical targets
- **Proposer neutrality**: blocks should be built on economic incentives, not fear of identification

---

## Privacy Guarantees With Blend

For a proposer with **0.1% relative stake**, with a **3-hop path**, against an adversary controlling **10% of total stake**:

| Metric | Without Blend | With Blend |
|--------|--------------|------------|
| TTI (stake inference, 60% confidence) | ~24 days | **>10 years** |
| TTL (proposal linkage, 50% confidence) | Very fast | **>10 years** |

These estimates assume worst-case adversarial behaviour consistent with Nomos's honest majority assumption.

---

## The Three Anonymity Mechanisms

### 1. Message Encapsulation (Layered Encryption)
See [[Blend Message Encapsulation]] for the full technical breakdown.

- Proposal encrypted in h ≤ 3 layers, one per relay node
- Each node decrypts one layer; cannot see past or future layers
- Incoming and outgoing messages look completely different (no content linkage)
- Full dissemination at each hop: observer cannot tell which node was the intended next recipient

### 2. Random Timing Delays
If messages are rare, even identical-looking encrypted messages can be linked by timing:

> "Node X sent message at T=0, Node Y received similar message at T=0.1s → Y received from X"

Blend defeats this by having **each path node assign a random delay** before re-disseminating. Messages are released in the order received, after their individual delay expires.

Effect: arrival times of incoming vs outgoing messages at any node are decorrelated.

### 3. Cover Traffic
Block proposals are rare events. If every encrypted message in the Blend Network corresponds to a real proposal, observers can still narrow down when and where proposals originate just by spotting activity spikes.

**Cover messages** solve this by generating a constant stream of indistinguishable fake traffic:

- Core and edge nodes generate cover messages with random payloads
- Cover messages are processed identically to data messages at every hop
- Encrypted cover payloads and encrypted data payloads are **completely indistinguishable** — even to adversary-controlled path nodes
- Cover messages follow the same path selection, encapsulation, and relay process

#### Cover Traffic Quota
To prevent the network from being overwhelmed, each node has a **quota** limiting:
- Number of cover messages per session
- Number of hops per message

The **Proof of Quota (PoQ)** in every message header enforces this quota cryptographically.

---

## Participation Model

### Core Nodes
- Must stake and declare via Service Declaration Protocol (SDP)
- Maintain minimum peer connections
- Cannot exceed message frequency quota
- Participate in message relay, decryption attempts, and cover traffic generation

### Edge Nodes
- Can submit proposal messages to the Blend Network
- Do not relay or participate in cover traffic
- Useful for light clients and validators not running full Blend infrastructure

---

## Message Lifecycle (End-to-End)

1. **Leadership win**: Node wins Cryptarchia consensus lottery → receives proof of leadership entitling it to emit a data message
2. **Path selection**: Node randomly selects h Blend core nodes as relay path; generates ZK Proofs of Selection for each
3. **Key + proof generation**: Generates h ephemeral key pairs, Proofs of Quota for each hop
4. **Encapsulation**: Encrypts payload h times; builds blending headers; assembles full Blend message
5. **Dissemination**: Sends message to all peer core nodes; it propagates across the entire Blend Network
6. **Hop 1 — Decrypt & delay**: First path node decrypts outer layer, verifies PoQ, assigns random delay, re-disseminates
7. **Hops 2–h**: Repeat — each path node decrypts, verifies, delays, re-disseminates
8. **Final hop**: Last path node decrypts final layer, extracts plaintext block proposal
9. **Broadcast**: Final node broadcasts block proposal to the entire Nomos Network (validators + edge nodes) after a random delay

At no point does any single node (other than the original proposer) know both the proposer's identity and the content of the proposal.

---

## Comparison to Similar Systems

| System | Approach | Blend Difference |
|--------|----------|-----------------|
| **Tor** | Onion routing, point-to-point circuits | Blend uses dissemination — no routing tables, harder to circuit-sniff |
| **Zcash Shielded** | Transaction content privacy | Blend targets *network-level* proposer anonymity, not tx content |
| **DAS / Ethereum PBS** | Proposer/builder separation | PBS separates builder identity but proposer still public; Blend hides proposer entirely |
| **Nym mixnet** | General-purpose mixnet | Blend optimised for scarce/bursty proposal traffic with lower bandwidth overhead |

---

## Key Design Tensions

| Tension | Tradeoff |
|---------|---------|
| More hops → stronger anonymity | More hops = higher latency; must fit within slot timing |
| More cover traffic → harder to spot real proposals | More cover traffic = higher bandwidth per node |
| Shorter delays → lower latency | Shorter delays = easier timing correlation |
| Larger quota → more cover diversity | Larger quota = more bandwidth per session |

Current `h_max = 3` is a deliberately conservative starting point; it will likely be tuned based on mainnet behaviour.

---

## Analysis

### Strengths
- **Multi-layer defence**: encapsulation + delays + cover traffic — attacking one mechanism doesn't break anonymity
- **Complements Cryptarchia**: together they provide leader election privacy *and* broadcast anonymity
- **Verifiable without leaking identity**: ZK proofs let honest nodes verify message validity
- **Low bandwidth design**: quota system makes it viable as a constant-on Bedrock Service

### Weaknesses / Open Questions
- **Assumes honest majority**: like Cryptarchia, breaks down if adversary controls majority of stake
- **Cover traffic calibration**: insufficient cover = weaker hiding; excessive cover = bandwidth cost
- **Latency budget**: random delays + multi-hop add latency; tight slot timing in Cryptarchia is a constraint
- **Cold start**: a newly launched network with few cover messages has weaker anonymity until participation scales

---

## Further Reading

- [The Blend Network: Improving Nomos' Privacy Guarantees](https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/)
- [Stirring, Mixing, Blending: Different Approaches to Proposer Anonymity](https://blog.nomos.tech/stirring-mixing-blending-different-approaches-to-proposer-anonymity/)
- [Message Encapsulation in the Nomos Blend Network](https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/)
- [[Blend Message Encapsulation]] — the full technical encapsulation/decapsulation process
- [[Blend Network Overview]] — architecture, adversary model, network design
- [[Cryptarchia]] — PPoS consensus; source of the leadership proof that entitles a proposer to send
