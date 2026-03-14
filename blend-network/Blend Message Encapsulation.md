---
topic: nomos
subtopic: blend-network
type: deep-dive
tags: [blend, encapsulation, encryption, mixnet, cryptography, zk-proofs, nomos]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
---

# Blend Message Encapsulation

Encapsulation is the layered encryption technique at the core of how the Blend Network achieves proposer anonymity. This note covers the full technical process: path selection, message structure, encapsulation, and decapsulation.

---

## The Core Idea

A proposer doesn't send their block proposal directly. Instead:

1. They encrypt the proposal in **h layers** (one per hop), selecting h ≤ h_max relay nodes.
2. They disseminate the fully-encrypted message to the entire network at once.
3. Each relay node can only peel off its own layer — it can't read ahead or look back.
4. After each decryption, the node randomly delays and re-disseminates.
5. The final node reveals the plaintext proposal and broadcasts it to the network.

> This is inspired by modern mixnets (e.g. Sphinx), adapted for Nomos's scarce-communication use case.

**Current parameters**: `h_max = 3`

---

## Security Properties

### Unlinkability
Even if an adversary controls multiple nodes, they **cannot link incoming and outgoing messages by content** unless they control *all* nodes on a specific path. Cryptographic transformation at every hop makes messages look completely different before and after processing.

### Preventing Message Association
Ephemeral key pairs are generated fresh for every message. Keys are **derived anew per message**, so an adversary cannot group messages by a common origin based on key reuse.

### Verifiability
Despite strong anonymity, nodes can still verify:
- Message is correctly formed
- Path was chosen randomly (Proof of Selection)
- Sender hasn't exceeded their quota (Proof of Quota)

ZK proofs and cryptographic signatures enable this **without compromising anonymity**.

---

## Step 1: Defining the Relay Path

Before encrypting, the sender must set up the relay path and prove it was constructed honestly.

### Key Generation
- Sender chooses h ≤ h_max hops
- Generates **h ephemeral key pairs** `(K_i, k_i)` — one per hop

### Proof of Quota (PoQ)
A **zero-knowledge proof** asserting two things:
1. The sender is entitled to send (e.g. won the Cryptarchia leadership lottery, or is eligible for cover messages)
2. The public key `K_i` has a unique index within the current **session** (basic time unit of Blend Protocol)

Since the index cannot exceed a cap, PoQ enforces an upper bound on:
- Total messages from a sender per session
- Total hops per message

PoQ also generates:
- **Selection randomness** — seeded from proof inputs
- **Nullifier** — prevents proof reuse

### Node Selection
- Sender draws h random nodes from the full set of Blend core nodes (obtained from SDP)
- Generates a **Proof of Selection (PoS)** for each: proves the node's index is derived from a pseudorandom function seeded by selection randomness
- PoS nullifier ≠ PoQ nullifier (checked to prevent cross-proof reuse)

### Shared Key Derivation
For each path node i, the sender derives a **shared key κ_i** using Diffie-Hellman:

```
κ_i = DH(k_i, P_i)
```

Where `P_i` is the path node's Ed25519 Provider ID (public key from SDP).  
Only node i can reproduce κ_i (using its own private key `p_i` and the sender's ephemeral `K_i`).

---

## Step 2: Message Structure

All Blend messages have the **same fixed structure** regardless of where they are in the relay path. This uniformity is intentional — nodes process all messages identically.

### Three Components

```
┌─────────────────────────┐
│      Public Header      │  ← Visible to all nodes
├─────────────────────────┤
│   Encrypted Private     │  ← Stack of h_max blending headers
│       Header            │
├─────────────────────────┤
│        Payload          │  ← Block proposal or cover data
└─────────────────────────┘
```

### Public Header (plaintext)
| Field | Purpose |
|-------|---------|
| `K_h` | Current hop's ephemeral public key (used to derive κ_i) |
| PoQ | Proof of Quota for current hop |
| Signature | Over the encrypted portion; verifiable with `K_h` |

### Private Header (encrypted stack)
Contains **h_max blending headers** stacked. Only the current path node can decrypt the outermost one. Each blending header contains:

| Field | Purpose |
|-------|---------|
| `K_i` | Ephemeral public key for the **next** hop |
| PoQ | Proof of Quota for next hop |
| Signature | Signature for next hop |
| PoS | Proof that next node was randomly selected |
| Last flag | Boolean — is this the final hop? |

The private header is encrypted in a nested/layered fashion: outermost header encrypted once (by κ_1), next encrypted twice (κ_1 then κ_2), etc.

### Payload
- **Data messages**: contains the actual block proposal
- **Cover messages**: contains random data (indistinguishable from real proposals until the final decryption)

---

## Step 3: Encapsulation

Encapsulation works **innermost-first** (last hop → first hop).

### Initialization
Fill the last h blending headers with dummy values (generated by PRF seeded with κ_i for hop i). Any remaining headers (when h < h_max) are filled with random data — this prevents premature decryption and preserves fixed message size.

### Per-layer Encapsulation (i = h down to 1)

For each layer i:

1. **Sign**: Produce signature over `(current private headers ‖ payload)` using the *previous layer's* public key `K_{i-1}`. (For the first encapsulation layer i=h, generate a fresh key pair `(K_0, k_0)` for signing.)
2. **Encrypt payload**: Encrypt with `κ_i`
3. **Shift private headers**: Shift all headers one position deeper (truncating the last). Fill the new outermost header with: the signature from step 1, PoS for path node i, `K_{i-1}`, and `PoQ_{i-1}`.
   - Last flag = `false` for all but the final encapsulation layer
   - For the final layer (i=h): use the new key `K_0`, fill PoQ with random data, set last flag = `true`
4. **Encrypt headers**: Encrypt all private headers with `κ_i`

### Final Step
When the outermost layer is done, fill the public header with `K_h`, its PoQ, and a signature over the final payload using `K_h`.

---

## Step 4: Decapsulation

Every node that receives a Blend message **attempts decapsulation**. Most fail (they're not on the path). Path nodes succeed.

### Decapsulation Steps (for path node i)

1. **Derive shared key**: `κ_i = DH(K_i from public header, p_i)`. This matches the sender's κ_i only if the node is a path node.
2. **Decrypt private headers** with κ_i. Verify proofs in the outermost header; check that `K_i` hasn't been seen (replay protection). Discard if invalid.
3. **Update public header**: extract `K`, PoQ, and signature from outermost private header → becomes new public header.
4. **Decrypt payload** with κ_i.
5. **Reconstruct dummy header**: use the same PRF (seeded with κ_i) as during encapsulation to regenerate the innermost dummy.
6. **Shift private headers up**: truncate outermost header, fill deepest with reconstructed dummy.
7. **Verify signature**: generate signature over new payload + headers. If it doesn't match the signature in the new public header, discard.

After decapsulation, the node **randomly delays** and re-disseminates the resulting message (one layer thinner) to all its peers.

### Final Node
When the node with the `last flag = true` blending header successfully decapsulates:
- It extracts the plaintext block proposal
- Broadcasts it to the full Nomos network after a random delay

---

## Dissemination vs. Routing

| Property | Blend (Dissemination) | Classic Onion Routing (e.g. Tor) |
|----------|----------------------|----------------------------------|
| Message delivery | Broadcast to all peers at each step | Point-to-point routing |
| Next-hop visibility | Unknown until decryption succeeds | Known from encrypted header |
| Anonymity model | "Hiding in the crowd" | Circuit-based |
| Bandwidth model | Higher (flood-based) but quota-capped | Lower per message |
| Eclipse resistance | More robust | Vulnerable to routing table poisoning |

---

## Key Design Choices

| Choice | Rationale |
|--------|-----------|
| Ephemeral keys per message | Prevents cross-message correlation |
| Fixed h_max headers (always 3) | All messages identical size; no hop-count leakage |
| Dissemination (not point-to-point) | Observer can't determine intended next hop |
| ZK proofs (PoQ + PoS) | Verifiable correctness without leaking identity |
| Random delays | Prevents timing-based linkage of in/out messages |
| Nullifiers | Prevents proof reuse and message replay |

---

## Analysis

### Strengths
- **Information-theoretic path hiding**: no node learns the full path; even path nodes only know they're *on* the path, not where
- **Replay protection**: nullifiers on PoQ and PoS prevent message replay
- **Fixed-size messages**: eliminates structural fingerprinting
- **No trusted coordinator**: path selection and proof generation done entirely by proposer

### Limitations / Open Questions
- **Sender complexity**: generating h PoQs, h PoSs, and the full encapsulation is non-trivial compute
- **ZK proof overhead**: PoQ and PoS generation latency at proposal time adds to slot timing budget
- **h_max = 3**: currently fixed at 3; increasing improves anonymity but increases latency and bandwidth
- **PRF-based dummy reconstruction**: relies on the PRF being deterministic and known only to path nodes — must be secure against pre-image attacks

---

## Further Reading

- [Message Encapsulation in the Nomos Blend Network](https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/)
- [Blend Network Overview](https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/)
- [[Blend Network Overview]] — architecture and privacy metrics
- [[Blend Proposer Anonymity]] — cover traffic, message lifecycle
- [[Cryptarchia]] — leadership lottery that generates the PoQ entitlement
