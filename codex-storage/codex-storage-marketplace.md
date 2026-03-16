---
title: "Codex – Storage Marketplace & Incentives"
tags: [logos, codex, storage, marketplace, incentives, smart-contracts, zk-proofs]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
  - https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
---

# Codex – Storage Marketplace & Incentives

## Design Philosophy

Codex uses a **free-market, permissionless** storage contract system:
- No manual bidding
- No KYC or onboarding requirements
- Pricing determined in real-time based on operator costs
- Clients don't choose providers directly — providers opt in automatically

## How Storage Contracts Work

### Provider Side (Passive Monitoring)
1. Each storage provider **monitors the blockchain** for storage requests
2. Provider is pre-configured with constraints:
   - Minimum price per byte per second
   - Maximum contract length
   - Maximum collateral
3. When a request matches constraints → provider **automatically reserves a slot** and stores data

### Client Side (Requesting Storage)
1. Upload file locally → erasure-coded → Verifiable Manifest generated (see [[codex-dde-architecture]])
2. CID of Verifiable Manifest submitted to **smart contract on-chain**
3. Contract specifies: duration, slots needed, collateral requirements
4. Providers fill slots autonomously

## Proof Challenges & Verification

- Storage providers must periodically submit **ZK proofs** that data is still intact
- Proofs reference the **Verification Root** from the Verifiable Manifest
- Proofs verified by **public blockchain nodes** (no trusted third party)
- Failure to provide proof → provider loses collateral

## Retrieval Incentives

- Retrieval marketplace **planned but not yet fully implemented** at time of research
- Will allow clients to send retrieval requests and receive competitive offers from providers
- Retrieval pricing factored into streaming/download cost

## Key Differences from Filecoin

| Feature | Filecoin | Codex |
|---|---|---|
| Provider selection | Manual negotiation / bidding | Automatic matching to pre-set criteria |
| KYC required | Filecoin Plus requires human KYC | No KYC, fully permissionless |
| Proof system | PoRep / PoSt | ZK proofs (Poseidon2, on-chain) |
| Retrieval | FIL payment to provider; IPFS hot retrieval | Incentivised marketplace (in development) |
| Redundancy | Replication | Erasure coding + strategic dispersal |

## Collateral & Slashing

- Providers stake collateral when reserving slots
- Data loss or proof failure → collateral slashed
- Creates economic incentive for data durability

## Related Notes

- [[codex-dde-architecture]] — Erasure coding, Verifiable Manifest, ZK proof generation
- [[codex-p2p-network]] — Altruistic vs. persistence mode
- [[codex-vs-filecoin]] — Full protocol comparison
