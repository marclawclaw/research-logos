---
title: "Blend Network – Message Lifecycle"
tags: [nomos, blend-network, message-lifecycle, protocol-flow]
source: https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
date: 2026-03-17
topic: blend-network
---

# Blend Network – Message Lifecycle

End-to-end flow of a data message (block proposal) through the Blend Network.

## Step-by-Step

1. **Win consensus lottery** — A node wins Cryptarchia's private leadership election and obtains a proof of leadership, entitling it to emit a data message. The payload is a block proposal.

2. **Select relay path** — The winning node selects a path of Blend core nodes from the SDP registry. Path randomness is cryptographically provable via Proofs of Selection (PoS).

3. **Generate keys and proofs** — Sender generates ephemeral key pairs and ZK proofs (PoQ + PoS) for each hop.

4. **Encapsulate** — The payload is encrypted in layers (one per hop). A Blend message with public header, private header stack, and encrypted payload is produced.

5. **Disseminate** — Sender floods the encapsulated message to all its Blend core node peers; these relay it peer-to-peer across the network.

6. **First path node receives** — The first path node successfully decrypts the private header (others fail silently). It verifies the PoQ and checks for replay.

7. **Random delay + re-disseminate** — The path node assigns a random hold delay, then releases the decapsulated message to its peers.

8. **Intermediate hops repeat** — Steps 6–7 repeat for each subsequent path node.

9. **Final node broadcasts** — The last path node decapsulates the final layer, extracts the block proposal, applies a random delay, and broadcasts the plaintext proposal to the entire Nomos validator network (including edge nodes).

## Key Timing Properties

- Random delays at **every hop** prevent timing correlation between input and output messages.
- Messages are released in FIFO order after their delay, not batched, to keep latency bounded.

## Participation Levels

| Participant | Role |
|---|---|
| **Core Blend node** | Stakes + declares via SDP; processes/relays messages; generates cover traffic |
| **Edge node** | Can submit proposals via Blend without being a declared core node |
| **Validator network** | Receives final broadcast from last Blend path node |

## Related Notes

- [[blend-network-overview]]
- [[blend-network-message-encapsulation]]
- [[blend-network-cover-traffic]]
- [[blend-network-security-properties]]
