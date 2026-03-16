---
title: "Blend Network — Message Encapsulation"
tags: [nomos, blend-network, encapsulation, mixnet, cryptography, zero-knowledge]
source: https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
date: 2026-03-16
---

# Blend Network — Message Encapsulation

## Summary

Encapsulation is the core cryptographic technique of the Blend Network — it wraps a block proposal in `h` layers of encryption (one per relay hop) so that each node can only unwrap its own layer, and cannot infer the message's origin or remaining path.

## Relay Path Setup

Before encapsulating, the sender:

1. Chooses `h ≤ h_max` hops (currently `h_max = 3`).
2. Generates `h` **ephemeral key pairs** `(K_i, k_i)` — one per hop.
3. Generates a **Proof of Quota (PoQ)** for each public key via ZK proof demonstrating:
   - Sender is entitled to send (e.g., won consensus lottery)
   - Each key has a unique index within the current session (caps total keys per session → limits messages + hops)
4. Randomly selects `h` nodes from the SDP node set.
5. Generates a **Proof of Selection (PoS)** for each node, proving the selection was pseudorandom (seeded by PoQ-derived randomness) and the nullifier differs from the PoQ nullifier.
6. Derives a **shared key** `κ_i = DH(P_i, k_i)` for each path node using their Provider ID (Ed25519 public key from SDP).

## Encapsulation Steps

Encapsulation proceeds from the **innermost layer (last hop) outward** to the **outermost layer (first hop)**:

For each encapsulation stage `i` (from last to first):

1. **Sign** the current private header stack + payload using the previous layer's public key `K_{i-1}` (for the innermost stage, generate a new ephemeral key `(K_0, k_0)`).
2. **Encrypt the payload** with shared key `κ_i`.
3. **Shift private headers** one position deeper (truncate last); fill the new outermost header with: signature, PoS for this node, and `(K_{i-1}, PoQ_{i-1})`. Set last flag = `true` only for the innermost (final hop) layer.
4. **Encrypt all private headers** with `κ_i`.

After all `h` stages, fill the **public header** with `K_h`, its PoQ, and a signature.

> Unused private header slots (when `h < h_max`) are filled with random data to maintain fixed size and prevent hop-count inference.

## Decapsulation Steps

Every node that receives a message attempts to decapsulate:

1. Compute `κ_i = DH(K_i_from_public_header, p_i_own_private_key)`.
2. Decrypt all private headers with `κ_i`. Verify proofs in the outermost header; check `K_i` has not been seen before (replay protection). If any check fails, discard.
3. Build new public header from outermost private header's `(K, PoQ, Sig)`.
4. Decrypt payload with `κ_i`.
5. Reconstruct the dummy deepest private header using the same PRF seeded by `κ_i` as used during encapsulation.
6. Shift private headers one position up; fill deepest slot with reconstructed dummy.
7. Verify signature over new payload + headers. If valid, the node is a path node.
8. Apply a **random delay**, then disseminate the new message to peers.

Non-path nodes: decapsulation fails silently; the message is simply relayed as-is (gossip).

## Timing: Random Delays

Each path node assigns a random delay before forwarding. This prevents timing correlation between incoming and outgoing messages, even if a global observer tracks traffic patterns.

## Zero-Knowledge Proofs Used

| Proof | What It Proves |
|-------|---------------|
| Proof of Quota (PoQ) | Sender entitlement + unique key index within session |
| Proof of Selection (PoS) | Node was pseudorandomly selected from SDP; nullifier uniqueness |

Both proofs allow verification **without revealing** the sender's identity.

## Related Notes

- [[blend-network-message-structure]] — detailed message format
- [[blend-network-security-properties]] — what encapsulation achieves (unlinkability, stake privacy)
- [[blend-network-overview]] — high-level context
- [[blend-network-cover-traffic]] — how cover messages use the same encapsulation process
