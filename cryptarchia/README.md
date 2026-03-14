# Cryptarchia Consensus — Research Notes

> Last updated: 2026-03-14
> Sources: [Nomos Blog](https://blog.nomos.tech/nomos-cryptarchia-improving-on-ouroboros-crypsinous/), [logos-blockchain-specs](https://github.com/logos-blockchain/logos-blockchain-specs/tree/master/cryptarchia), [consensus-research](https://github.com/logos-co/consensus-research)

---

## What Is Cryptarchia?

Cryptarchia is a **Private Proof of Stake (PPoS)** consensus protocol developed by the Nomos/Logos team. It is the third generation of the Ouroboros family:

1. **Ouroboros Praos** — foundational PoS with provable security
2. **Ouroboros Crypsinous** — first formally-analysed PPoS protocol
3. **Cryptarchia** — Nomos's improvement on Crypsinous, designed for real-world implementation

It serves as the consensus layer for the **Logos Blockchain** (formerly Nomos), sitting within the Bedrock (L1) layer.

---

## Core Design Goals

- **Proposer privacy**: block proposers are never revealed (no public validator schedule)
- **Stake privacy**: relative stake cannot be inferred from on-chain activity
- **Low barrier to entry**: any amount of stake can participate
- **Fork-safe liveness**: honest nodes can bootstrap without trust assumptions
- **No wealth concentration**: avoids the PoS rich-get-richer problem

---

## Time Structure

Cryptarchia inherits the Ouroboros time model:

```
Slots → Epochs
- One block can be added per slot (most slots have no leader)
- Epochs group slots together and refresh leadership parameters
```

### Epoch Schedule (3 Periods)

| Period | Slots | Purpose |
|--------|-------|---------|
| **Stake Distribution Snapshot** | First 30% | Snapshot of eligible notes taken; finalised by end of period |
| **Buffer (Nonce Buffer)** | Next 30% | Wait for at least one honest leader to contribute randomness |
| **Lottery Constants Finalisation** | Final 40% | Epoch nonce for *next* epoch revealed; leadership window begins |

**Key**: The epoch nonce η_{ep+1} is set at the *end of the buffer period* of epoch ep, and revealed at the start of the finalisation period.

---

## Notes (vs. Coins in Crypsinous)

Cryptarchia replaces Crypsinous "coins" with **notes** — a more general data primitive, private by default.

### Note Fields (all private)
| Field | Description |
|-------|-------------|
| `state` | Arbitrary private data attached to the note |
| `v` | Value associated with the note (e.g. asset amount) |
| `U` (unit) | "Type" of the note; determines covenants (spending rules) |
| `nonce` | Ensures note uniqueness |
| `ZoneID` | Identifier of the Nomos zone where the note resides |

Notes are transferred using the **UTXO model**: sender spends a note, creating a new note of equal value for the recipient. Transaction data is hidden; validity is verified with zero-knowledge proofs.

### Note Commitment

```
commitment = Hash("NOMOS_NOTE_CM", state, value, unit, nonce, pk, zone_id)
nullifier  = Hash("NOMOS_NOTE_NF", commitment, sk)
```

---

## Zone Ledgers

Each Nomos zone maintains its own ledger with two data structures:

### 1. Commitment Set (Merkle Mountain Range — MMR)
- Stores commitments to all notes created in the zone
- Uses MMR structure: efficient append-only, only frontier nodes stored
- Proving note existence = Merkle membership proof

### 2. Nullifier Set (Indexed Merkle Tree — IMT)
- Stores nullifiers of spent notes (like serial numbers)
- IMT: sorted leaves with next-highest-value pointers → enables **non-membership proofs**
- To spend a note: prove nullifier is NOT in the set (ZK non-membership proof)
- This is more private than Crypsinous (which just reveals the serial number)

> **Why IMT?** Proofs of non-membership require a sorted structure. IMTs support this efficiently.

> **Side effect**: Cryptarchia doesn't need Crypsinous's "coin evolution" tactic because nullifier non-membership proofs don't leak coin data.

---

## Leadership Election

### Eligibility
- A note must have existed since the **start of the previous epoch** to be eligible
- Validators snapshot eligible notes at each epoch boundary

### Lottery Mechanism
Each eligible note runs a **local lottery** per slot:

```python
ticket = Hash("LEAD", η_ep, slot, commitment, sk)
threshold = phi(f, relative_stake)  # phi = 1 - (1-f)^alpha
win if ticket < threshold
```

Where:
- `η_ep` = epoch nonce (changes every epoch)
- `f` = active slot coefficient (0.05 — target block rate)
- `alpha` = note value / total estimated stake (relative stake)
- `phi()` is approximated with a **2nd-order Taylor expansion** (for ZK proof efficiency)

### Epoch Nonce Calculation
Each block contributes randomness:
```
η'_block = Hash("EPOCH_NONCE", η'_parent, ρ_slot, slot)
ρ_slot   = Hash(slot, nullifier_of_winning_note)
```
The tentative nonce at end of buffer period → becomes next epoch's nonce η_{ep+1}.

### Key Deletion (Forward Secrecy)
Secret keys use a **Merkle tree structure** (2^25 leaves):
- Each leaf = one slot's key, derived deterministically from the previous
- Leaf deleted after slot passes
- Prevents adaptive adversaries from retroactively generating Proofs of Leadership for past slots

---

## Proof of Leadership (PoL)

The ZK proof submitted with each new block proves:
1. Nullifier, commitment, and secret key were calculated correctly
2. Note's commitment is in the aged-notes set
3. Note's nullifier is NOT in the nullifier set (unspent)
4. Ticket and threshold calculated correctly
5. Ticket < threshold (i.e. won the lottery)
6. Leader knows the secret key leaf for this slot
7. Randomness contribution calculated correctly

---

## Estimating Total Stake

Crypsinous left this problem unsolved. Cryptarchia's formula:

```
D^{ep+1} = D^ep - β * (D^ep / log(1/(1-f))) * (log(1/(1-f)) - N/T)
```

Where:
- `D^ep` = current total stake estimate
- `N/T` = observed blocks per slot (N blocks over T slots, T = first 3/5 of epoch)
- `log(1/(1-f))` = target blocks per slot when all stake held by one party
- `β = 0.8` = learning rate coefficient

**Convergence**: formula reaches equilibrium ~2 epochs after a 50% stake change.

**Relative stake** = note value `v` / `D^{ep+1}`

---

## Fork Choice Rule

Inherits from **Ouroboros Genesis**:

| Fork Depth | Rule |
|-----------|------|
| Shallow fork | Longest chain wins |
| Deep fork | Densest chain wins (most blocks in a given window) |

Two modes in the spec implementation:
- `BOOTSTRAPPING`: uses `maxvalid_bg` (genesis rule, density-based)
- `ONLINE`: uses `maxvalid_mc` (max chain, length-based)

The **Last Immutable Block (LIB)** is the k-th block from the tip (k=2160 in v0.0.1). Blocks behind LIB cannot be reverted.

---

## Key Parameters (v0.0.1)

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `k` | 2160 | Depth before block is immutable |
| `f` (active_slot_coeff) | 0.05 | Target block rate per slot |
| `β` (learning rate) | 0.8 | How fast total stake estimate adjusts |
| `slot_duration` | 1s (spec) / 30s (production) | Time per slot |
| Epoch length | derived from k/f | ~43,200 slots (12h at 1s slots) |

---

## Improvements Over Crypsinous

| Issue in Crypsinous | Cryptarchia Solution |
|--------------------|---------------------|
| No method for estimating total stake | Derived estimation formula via block rate observation |
| Coin evolution tactic needed | Eliminated by ZK non-membership proofs |
| Stake inference via network analysis | Mitigated by Nomos anonymous network layer (Blend) |
| Network-based block proposer identification | Anonymous proposal via Blend Network |
| Tagging attacks | Partially addressed; some remain WIP |
| Outdated cryptographic primitives | Updated; uses blake2b/sha256, Merkle trees |
| No full implementation spec | Python reference spec in logos-blockchain-specs |

---

## Known Remaining Issues / WIP

- Some **tagging attack** vectors remain open
- **Network-level anonymity** depends on Blend Network (external to Cryptarchia itself)
- **Finality time** not fully specified in public documentation
- **ZK proofs** (full implementation) still being built — spec uses `MockLeaderProof`

---

## Wealth Concentration

DarkFi (another privacy chain) abandoned Crypsinous specifically due to wealth concentration concerns, moving to PoW (RandomX). Nomos research found:

> Cryptarchia **does not exhibit wealth concentration** when using the stake relativisation formula above.

Relevant research:
- [Tackling the Challenge of Wealth Concentration in PoS Blockchains](https://blog.nomos.tech/tackling-the-challenge-of-wealth-concentration-in-pos-blockchains/)
- [Preventing Wealth Concentration: Fork-Choice Rule and Stake Relativisation](https://blog.nomos.tech/preventing-wealth-concentration-in-pos-systems-the-role-of-fork-choice-rule-and-stake-relativization/)

---

## Spec / Code Locations

| Resource | URL |
|----------|-----|
| Python reference spec | [logos-blockchain/logos-blockchain-specs/cryptarchia/](https://github.com/logos-blockchain/logos-blockchain-specs/tree/master/cryptarchia) |
| Blog post | [blog.nomos.tech/nomos-cryptarchia-improving-on-ouroboros-crypsinous/](https://blog.nomos.tech/nomos-cryptarchia-improving-on-ouroboros-crypsinous/) |
| Crypsinous paper | [eprint.iacr.org/2018/1132](https://eprint.iacr.org/2018/1132.pdf) |
| Consensus research (Snow/Claro) | [github.com/logos-co/consensus-research](https://github.com/logos-co/consensus-research) |

> Note: `consensus-research` focuses on the **Snowball/Claro** family (avalanche-style protocols), not Cryptarchia directly. Cryptarchia's Python spec lives in `logos-blockchain-specs`.

---

## Analysis

### Strengths
- **Genuinely novel**: PPoS with local lottery and ZK proofs for proposer anonymity — no major L1 does this
- **Formally grounded**: built on Ouroboros Praos/Genesis security proofs
- **No public leader schedule**: unlike Ethereum's RANDAO-based public schedule, no advance knowledge of proposers
- **Sybil-resistant and stake-private**: ZK proofs hide validator identity and relative stake
- **Low min stake**: any amount participates — avoids Ethereum's 32 ETH gatekeeping

### Risks
- **Unproven at scale**: no adversarial mainnet conditions tested yet (testnet March 2026)
- **Complexity**: ZK proof generation, key deletion, MMR/IMT — significant implementation surface
- **Blend dependency**: proposer anonymity relies on external network layer
- **Slow block time**: 30s production target vs Ethereum's 12s — limits latency-sensitive use cases
- **Open tagging attacks**: some attack vectors still WIP

### Key Observation
> The stake relativisation formula is the most underappreciated part of Cryptarchia. Without it, PPoS likely concentrates wealth — DarkFi proved this empirically. With it, Cryptarchia avoids the failure mode that killed Crypsinous adoption.
