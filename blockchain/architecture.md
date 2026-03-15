# Logos Blockchain — Architecture

> Last updated: 2026-03-14

## Overview

The Logos Blockchain uses a **modular two-layer architecture** with three main concerns separated across layers:

```
┌────────────────────────────────────────────┐
│           Sovereign Zones / LSSA           │  ← Application layer
├────────────────────────────────────────────┤
│                  Mantle                    │  ← Execution layer
├────────────────────────────────────────────┤
│                  Bedrock                   │  ← Consensus + DA
└────────────────────────────────────────────┘
```

---

## Bedrock (Base Layer)

The base chain providing:
- **Consensus** via Cryptarchia (private PoS)
- **Data availability** (NomosDA — blob-based)
- **Settlement** for upper layers
- Bedrock does not attempt to validate or interpret Sovereign Rollup data — blobs are opaque to it

### Bedrock Services
Node operators can participate in Bedrock Services to earn rewards:
- **Service Declaration Protocol (SDP):** Registration and role declaration for service providers
- **Service Reward Distribution Protocol (SRDP):** Distributes rewards based on session tracking + activity verification
- SDP implementation was near-complete as of November 2025

---

## Mantle (Execution Layer)

Manages state updates from upper layers:
- **Mantle Channels:** Permissioned virtual blockchains for tracking Sovereign Zone state updates
- **Leadership lottery** that preserves winner anonymity (no hidden note information required)
- Transaction framework + mempool improvements throughout 2025
- Specification finalized: June 2025
- Redesigned in 2025 to exclusively support public notes (Sovereign Zones use private execution separately)
- Invalid transaction handling added to prevent block production disruptions (October 2025)

---

## Sovereign Zones

Blockchain execution environments built on Bedrock:
- Adhere to Nomos common specifications
- Constrained by ZK performance limitations (trade-off for privacy)
- First demonstrated prototype: **zkEVM rollup with state transitions verified by light clients** (April 2025)
- Planned 2026 features: decentralised sequencing, bridging, inter-Zone messaging

### Why Sovereign Rollups (not Ethereum-style rollups)?
Empirical data from Ethereum rollups justifies the Sovereign Rollup design:
- **14,500 users** used Optimism's LayerZero (non-canonical bridge) in a single week
- Only **243 users** used Optimism's canonical bridge
- Most rollup value is stored in assets NOT secured by L1 at all — making canonical bridges irrelevant

This validates the Logos approach: skip bridge contracts, give rollups full sovereignty.

### Sovereign Rollups (vs. Native Zones)
Logos also supports pure **Sovereign Rollups** — completely independent modular blockchains using Bedrock only for consensus ordering and data availability:
- Full freedom to define their own execution environment
- No on-chain smart contract verification required (unlike Ethereum L2s)
- State validity determined solely by rollup validators
- Data posted as blobs to NomosDA; blob commitments written on-chain
- Can use ZK validity proofs, fraud proofs, or re-execution — rollup's choice
- Suited for: gaming (fast state, isolated), high-frequency DeFi, web apps

### Native Zones (deferred)
Native Zones sharing a common ledger were deprioritized in 2025 in favor of Sovereign Zones. Left for a future release post-mainnet.

---

## LSSA (Logos State Separation Architecture)

The first Sovereign Zone — the primary home for Logos applications:
- **Dual account model:** public accounts + private (shielded) accounts
- Supports public and private transfers
- Smart contract execution environment
- Relies on Bedrock for consensus + data availability
- Sequencer prototype demonstrated at Spain offsite (December 2025)
- LSSA is the primary focus for mainnet launch; other Zones will follow

**GitHub:** https://github.com/logos-blockchain/lssa

---

## Tokenomics

- Full tokenomics framework established: August 2025
- Block rewards + execution markets designed
- Minimum stake estimation analysis completed for SDP
- Block reward evaluations used as inputs for protocol implementation
- Economic model includes incentives for Bedrock Service providers (SDP rewards)
