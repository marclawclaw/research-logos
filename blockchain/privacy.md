# Blend Network — Proposer Anonymity

> Last updated: 2026-03-14
> Sources: blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees, blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network

## What is the Blend Network?

The Blend Network is a privacy-preserving communication service built into the Logos Blockchain. Its primary purpose: **hide the link between block proposers and their proposals**, preventing deanonymisation via network-level surveillance.

Without Blend, an adversary observing the network could identify which IP address first broadcast a block proposal, linking the proposer to their identity.

---

## How It Works

### Core-Edge Architecture
- **Edge nodes:** Connect directly to the wider network; act as entry/exit points
- **Core nodes:** Inner mix network; handle message routing anonymously
- **Proxy service:** Manages communication between edge and core layers

### Message Encapsulation
Messages are wrapped in cryptographic layers (onion routing style):
- Each hop unwraps one layer, revealing only the next hop
- Cryptographic validation at each hop
- Encapsulation is the core mechanism preventing proposer deanonymisation

### Mixing Strategies
The Blend Network uses a **blending** approach (as opposed to stirring/mixing):
- **Stirring:** Simple delay — weak against timing analysis
- **Mixing:** Batch + reorder — stronger but latency-heavy
- **Blending:** Continuous mixing with cover traffic — balances privacy and latency

### Anonymity Guarantees
- Maximum anonymity achieved when random time-interval graphs remain connected (validated via simulation, November 2025)
- Analysed corrupted-receiver and corrupted-sender scenarios — documented anonymity boundaries in adversarial conditions
- Research explores the relationship between **controllability and observability** in control systems and how these map to anonymity guarantees in anonymous communication systems

---

## Technical Status (as of November 2025)

### Research
- Blend Protocol design finalised: June 2025
- Proof of Quota and Proof of Selection integrated: September 2025
- Cryptography audit in progress (started November 2025)
- Analytical results for anonymity failure probabilities validated
- Cover message generation, queuing, and release formally specified

### Development
- Merkle path generation bug fixed
- Old-session token handling corrected
- Clean shutdown for core services implemented
- Reward-calculation logic under review (includes Blend activity proofs)
- Session transition logic improved and tested

### Concrete Anonymity Numbers
Without the Blend Network, an adversary can infer a node's relative stake by observing how frequently it proposes blocks:
- **TTI (Time To Infer) for 0.1% stake node: ~24 days**
- Proportionally faster for larger stake holders
- Blend Network makes this inference computationally intractable

This is not a theoretical threat — it's a practical metric the Logos team calculated and used to justify mandatory Blend participation.

---

## Integration with Cryptarchia

The Blend Network and Cryptarchia work together:
1. Cryptarchia uses ZK proofs so proposers don't reveal stake when winning the lottery
2. Blend Network obfuscates the network path of the proposal broadcast
3. Combined: **cryptographic + temporal + network-level** proposer privacy

This is the most technically distinctive feature of the Logos Blockchain stack. No major L1 offers comparable proposer anonymity.

---

## Why It Matters for PoC Builders

If building on Logos Blockchain:
- Block proposers are not publicly identifiable — important for high-stakes applications
- The Blend Network could be adapted/used for application-level message privacy
- Node operators running Bedrock Services participate in Blend and earn rewards
