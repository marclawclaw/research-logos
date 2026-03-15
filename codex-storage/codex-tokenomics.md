---
title: Codex Tokenomics — CDX Token
aliases: [CDX token, Codex CDX]
tags: [logos, codex, tokenomics, CDX, incentives, storage-contracts]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/the-codex-roadmap-for-2025-and-beyond/
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
  - https://docs.codex.storage/learn/tokenomics-litepaper
---

# Codex Tokenomics — CDX Token

## Overview

The **CDX token** is the native utility token for the Codex/Logos Storage network. It operates on the **Ethereum network** (Codex is linked to Ethereum for public proof publication).

Tokenomics Litepaper published: Q1 2025.

## Token Utility

| Use | Description |
|---|---|
| Payment | Clients pay storage providers for hosting data |
| Collateral | Providers post CDX as collateral — slashed on failure |
| Security | Validators mark missed proofs; earn rewards |
| Repair Incentives | Incentivises data repair to maintain durability |

## Participants in the Economy

- **Clients** — upload data, pay for storage
- **Storage Providers** — host data, earn CDX, post collateral
- **Validators** — verify proof submissions, earn rewards for catching missed proofs

## Storage Contracts

- Smart contracts between clients and providers
- Proof-of-storage mechanism: providers must submit periodic ZK proofs
- **Slot recovery**: if a provider fails, the slot can be recovered by another
- Pricing determined by free-market real-time negotiation

## Key Design Principles

- Collateral slashing aligns economic incentives with data reliability
- No manual bidding — providers set pre-configured thresholds
- Repair incentives are first-class (not bolt-on)
- Public proofs posted to Ethereum → publicly verifiable by anyone

## Future Token Features (Post-Mainnet)

- Bandwidth incentives
- Aggregator Network rewards
- Proof Aggregation to reduce on-chain costs
