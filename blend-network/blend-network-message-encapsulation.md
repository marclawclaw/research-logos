---
title: "Blend Network – Message Encapsulation"
tags: [nomos, blend-network, encapsulation, cryptography, onion-routing]
source: https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
date: 2026-03-17
topic: blend-network
---

# Blend Network – Message Encapsulation

Encapsulation is the layered encryption technique at the core of how the Blend Network achieves proposer anonymity. It is inspired by mixnet designs but adapted for Nomos' low-bandwidth, scarce-communication context.

## High-Level Flow

1. Sender selects a random relay path of `h ≤ h_max` (currently `h_max = 3`) Blend nodes.
2. Sender wraps the payload in `h` layers of encryption — one per hop.
3. The fully encapsulated message is disseminated (peer-to-peer flood) to **all** Blend nodes.
4. Each Blend node attempts to decrypt; only path nodes succeed (via Diffie-Hellman shared key).
5. A successful path node decrypts one layer, applies a random delay, and re-disseminates.
6. The final node decrypts the payload entirely and broadcasts the block proposal to the Nomos Network.

## Defining the Relay Path

- Sender generates `h` ephemeral key pairs `(K_i, k_i)`.
- **Proof of Quota (PoQ)**: ZK proof that the sender is entitled to send and has not exceeded their message/hop quota for the current session. Enforces spam prevention.
- **Proof of Selection (PoS)**: ZK proof that each path node was selected pseudorandomly (from a PRF seeded by selection randomness derived during PoQ generation). Ensures path integrity.
- Node identity (`Provider ID`) is an Ed25519 public key `P_i` published via the **Service Declaration Protocol (SDP)**.
- Shared key per hop: `κ_i = DH(k_i, P_i)` — only the corresponding path node can recompute it.

## Message Structure

A Blend message has three parts regardless of its position in the relay path:

| Component | Visibility | Contents |
|---|---|---|
| **Public Header** | All nodes | Current ephemeral key `K_h`, PoQ, signature over encrypted portion |
| **Private Header** | Encrypted; one layer per hop | Stack of `h_max` blending headers, each containing: next-hop `K_i`, PoQ, signature, PoS, `last` flag |
| **Payload** | Encrypted | Block proposal (data message) or random bytes (cover message) |

- All messages have identical fixed structure — a node cannot distinguish a data from a cover message until the final decryption.
- The private header stack always has `h_max` entries; unused slots are filled with random data to prevent path-length inference.

## Encapsulation Process (sender side)

Starting from the innermost (last) hop and working outward:

1. Fill dummy values for the last `h` private headers (PRF seeded by `κ_i`).
2. Encrypt private headers progressively: header `i` is encrypted by `κ_1 … κ_i`.
3. For each encapsulation stage `i` (from last hop inward):
   - Sign the concatenation of private headers + payload using the next hop's key.
   - Encrypt payload with `κ_i`.
   - Shift private header stack inward; fill the outermost slot with PoS, ephemeral key, PoQ for hop `i`.
   - Encrypt all private headers with `κ_i`.
4. Final outermost pass fills the public header.

## Decapsulation Process (path node side)

1. Compute `κ_i` from the public key in the public header and the node's own private key.
2. Decrypt all private headers with `κ_i`.
3. Verify proofs (PoQ) and check ephemeral public key is not a replay.
4. Build new public header from outermost decrypted private header.
5. Decrypt payload with `κ_i`.
6. Reconstruct the dummy private header (same PRF as sender) and append to stack bottom.
7. Shift stack upward, discard old outermost header.
8. Verify generated signature matches — confirms message was correctly formed.

## Key Properties Enabled by Encapsulation

- **Path opacity**: even path nodes only know the next hop, not the full path.
- **Ephemeral keys**: a new key per message prevents linking messages from the same sender.
- **Verifiability without de-anonymisation**: ZK proofs allow correctness checks without revealing identity.

## Related Notes

- [[blend-network-overview]]
- [[blend-network-security-properties]]
- [[blend-network-cover-traffic]]
