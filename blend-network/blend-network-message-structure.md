---
title: "Blend Network — Message Structure"
tags: [nomos, blend-network, message-format, cryptography, zero-knowledge]
source: https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
date: 2026-03-16
---

# Blend Network — Message Structure

## Summary

All Blend messages share the same fixed structure regardless of where they are in the relay path. This uniformity is essential — it prevents observers from inferring a message's hop count or progress.

## Three-Part Structure

```
┌─────────────────────────────┐
│       Public Header          │  visible to all nodes
├─────────────────────────────┤
│  Private Header (encrypted)  │  stack of h_max blending headers
│  ┌──────────────────────┐   │
│  │ Blending Header 1    │   │  decryptable by node 1
│  │ Blending Header 2    │   │  decryptable by node 2
│  │ ...                  │   │
│  │ Blending Header h_max│   │
│  └──────────────────────┘   │
├─────────────────────────────┤
│    Payload (encrypted)       │  block proposal or cover data
└─────────────────────────────┘
```

## Public Header

Visible to all nodes. Contains:

| Field | Purpose |
|-------|---------|
| Ephemeral Public Key `K_h` | Used by the current path node to derive shared key and decrypt |
| Proof of Quota (PoQ) | ZK proof that sender has not exceeded message allowance |
| Signature | Over the encrypted message; verifiable by current path node |

## Private Header

A fixed-size stack of `h_max` encrypted blending headers (currently `h_max = 3`). Only the current path node can decrypt its corresponding header. Each blending header contains:

| Field | Purpose |
|-------|---------|
| Public Key `K_i` | Ephemeral key for the next hop |
| PoQ | Proof of quota for next hop |
| Signature | For next hop verification |
| Proof of Selection (PoS) | Proves next node was randomly selected from SDP |
| Last flag | Boolean — is this the final hop? |

The fixed size (`h_max` entries) means path length is hidden: unused slots are padded with random data to prevent shortcut inferences.

## Payload

- **Data message:** encrypted block proposal
- **Cover message:** encrypted random data
- Indistinguishable until the final decryption layer is removed — even adversary-controlled nodes cannot tell them apart mid-path.

## Key Derivation

Path nodes derive a **shared key** `κ_i` via Diffie-Hellman:

```
κ_i = DH(K_i [from public header], p_i [node's own private key])
```

This matches the shared key the sender computed using `DH(P_i [node's Ed25519 Provider ID], k_i [sender ephemeral private key])`.

## Related Notes

- [[blend-network-encapsulation]] — how the sender builds this structure
- [[blend-network-overview]] — high-level context
- [[blend-network-security-properties]] — why fixed structure matters for anonymity
