# Cryptarchia — Private Proof of Stake

> Last updated: 2026-03-14
> Source: blog.nomos.tech/nomos-cryptarchia-improving-on-ouroboros-crypsinous, blog.nomos.tech/comparing-consensus-bitcoin-ethereum-and-logos

## What is Cryptarchia?

Cryptarchia is the Logos Blockchain's custom consensus protocol. It combines:
- **Nakamoto-style longest-chain simplicity** (liveness over safety)
- **Proof of Stake** energy efficiency
- **Zero-knowledge cryptography** for proposer privacy

The name derives from the goal: hidden ("crypto") leadership ("archia").

> "The values that Cryptarchia optimizes for are resilience and privacy. These come at the cost of block times and finality."
> — Cryptarchia v1 Protocol Specification

---

## How It Works

1. **Slot-based time:** Time divided into fixed slots (30-second block times)
2. **Decentralised leadership lottery:** Each slot, participants independently run a local lottery
3. **ZK proof of winning:** Winners prove lottery success via a zero-knowledge proof — without revealing their stake amount
4. **Block proposal:** Winners propose blocks for their slot
5. **Fork choice:** Longest-chain rule (variant of Nakamoto) — prioritises liveness
6. **Lottery difficulty adjustment:** Adjusts based on network activity to maintain target block times

### Key Properties
- **No public leader schedule** (unlike Ethereum's predictable validator schedule)
- **Any stake amount** can participate — low barrier to entry
- **Private stake amounts** — stake is not revealed on-chain
- Up to **50% dishonest participants** tolerated (like Bitcoin/Ethereum)

---

## Comparison with Bitcoin & Ethereum

| Feature | Bitcoin (Nakamoto PoW) | Ethereum (Gasper PoS) | Logos (Cryptarchia PPoS) |
|---------|----------------------|----------------------|--------------------------|
| Block time | ~10 min | 12 sec | **30 sec** |
| Finality | ~60 min (6 blocks) | ~13 min (checkpointing) | Probabilistic (slower) |
| Min participation | Mining hardware | 32 ETH | **Any stake amount** |
| Proposer privacy | No (pool signatures, IP) | No (public validator registry) | **Yes (ZK proofs + Blend)** |
| Energy use | Very high | Low | Low |
| Safety vs liveness | Liveness | Liveness | **Liveness** |
| Leader predictability | None (mining race) | Public schedule | **No schedule** |

### Why liveness over safety?
The team explicitly chose liveness (keeps producing blocks during failures) over safety (halts on disagreement). This allows:
- Permissionless participation
- No quorum-based coordination
- Network remains operational even with partial failures

BFT-style protocols (safety-first) require known participant sets and large staking requirements, which the Logos team rejected as incompatible with their decentralisation goals.

---

## Based on Ouroboros Crypsinous

Cryptarchia builds on **Ouroboros Crypsinous** (IOHK), the first provably secure private PoS protocol. Key improvements Cryptarchia makes:
- Simplified to avoid unnecessary complexity from Ouroboros Crypsinous
- Adapted for the specific needs of the Logos Blockchain architecture
- Integrated with the Blend Network for network-level proposer privacy
- Lottery difficulty adjusts dynamically (Ouroboros uses fixed epochs)

---

## ZK Infrastructure

- **ZKVM benchmarking** ongoing — Risc0 clocks ~0.3 TPS on RTX 4090 (as of November 2025)
- **Poseidon2** hash compression updates cut proving times in half (November 2025)
- Cryptography audit for Data Availability: completed November 2025
- Cryptography audit for Blend: started November 2025
- ZK IDs + ed25519 keys used for node authentication in testnet simulations

---

## Security Considerations

- Cryptarchia is unproven at mainnet scale
- 30-second block times may limit time-sensitive use cases
- No detailed public finality model yet (probabilistic only)
- March 2026 testnet will be the first adversarial test
