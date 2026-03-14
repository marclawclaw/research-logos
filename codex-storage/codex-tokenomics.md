---
title: "Codex Tokenomics — CDX Token & Economic Model"
tags: [codex, logos, storage, tokenomics, CDX, incentives, marketplace]
sources:
  - https://blog.codex.storage/the-codex-roadmap-for-2025-and-beyond/
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
  - https://docs.codex.storage/learn/tokenomics-litepaper
created: 2026-03-14
updated: 2026-03-14
status: current
---

# Codex Tokenomics — CDX Token & Economic Model

## Overview

Codex published its **Tokenomics Litepaper** in Q1 2025, outlining the economic model for the incentivised network. The CDX token underpins payments, staking, and collateral.

Full litepaper: `docs.codex.storage/learn/tokenomics-litepaper`

## CDX Token Utility

| Use | Description |
|---|---|
| **Payment** | Clients pay storage providers in CDX for hosting data |
| **Collateral** | Providers post CDX as stake; slashed if proofs fail |
| **Incentives** | Validators earn CDX for marking missed proofs |
| **Repair incentives** | Built-in incentives for maintaining data integrity |

## Network Participants

- **Clients** — upload data, pay for storage contracts
- **Storage Providers** — host data, post collateral, submit storage proofs
- **Validators** — monitor proof submissions, mark missed proofs, earn rewards

## Storage Contract Mechanics

1. Client posts storage request on-chain with CID of Verifiable Manifest
2. Providers monitor blockchain; auto-fill slots matching their config
3. Provider posts CDX collateral to secure the contract
4. Provider must periodically submit ZK storage proofs
5. Failed proof → collateral slashed → contract may trigger repair

## Pricing Model

- Free-market pricing — determined by provider costs (storage + repair mechanisms)
- No manual bidding; providers set min/max thresholds
- Retrieval fees (when implemented) also market-priced
- Contrasts with Filecoin's dual storage/retrieval market with more manual setup

## Blockchain Integration

- Codex DDE linked to **Ethereum network**
- Storage proofs published on-chain for public verification
- CDX token operates on Ethereum
- Smart contracts enforce SLAs and collateral slashing

## Incentivised Testnet (H2 2025 target)

- First live implementation of tokenomics
- Introduces real CDX rewards for node operators
- Purpose: drive decentralisation, test economic model, gather operator feedback
- Testnet **paused** in August 2025 for architecture revision — new testnet upcoming

## What's Not Yet Implemented (at testnet pause)

- Bandwidth incentives
- Mutable data support
- Aggregator network
- Proof aggregation
- Full retrieval marketplace

## Related Notes

- [[codex-overview]] — What Codex is
- [[codex-p2p-protocol]] — How storage proofs work technically
- [[codex-roadmap-2025]] — Timeline for tokenomics rollout
- [[codex-vs-filecoin]] — CDX vs FIL comparison
