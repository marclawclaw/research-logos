---
title: "Codex Decentralised Storage — Overview"
tags: [codex, logos, storage, decentralised, DDE]
sources:
  - https://blog.codex.storage
  - https://logos.co/tech-stack
created: 2026-03-14
updated: 2026-03-14
status: current
---

# Codex Decentralised Storage — Overview

## What Is Codex?

Codex is the **Logos storage module** — a privacy-preserving, decentralised storage system providing censorship resistance and data durability. Previously known as "Codex", it is now officially branded as the **Logos Storage** module within the Logos technology stack.

> "Prevents data manipulation and ensures that no single entity owns or controls the stored information."

The project self-describes as a **Decentralised Durability Engine (DDE)** — going beyond basic decentralised storage by adding robust reliability, fault-tolerance, and verifiability.

## Core Value Proposition

- **Censorship resistance** — no single entity can censor or remove stored data
- **Data durability** — erasure coding + repair incentives prevent data loss
- **Privacy-preserving** — zero-knowledge proofs for storage verification without data exposure
- **Permissionless** — open marketplace; no KYC, no manual onboarding
- **Logos ecosystem fit** — enables decentralised dapp frontend delivery within the Logos stack

## Status (as of March 2026)

- Rebranded from Codex → **Logos Storage** (late 2025)
- `codex.storage/about/faq` now redirects to `logos.co/tech-stack`
- Testnet paused in August 2025 for core architecture revision
- New testnet in development, building on feedback from prior testnet phase
- Implementation repo: `github.com/logos-storage/logos-storage-nim` (previously `codex-storage/nim-codex`)

## Key Differentiators vs. Other DSNs

| Feature | Codex/Logos Storage | IPFS/Filecoin |
|---|---|---|
| Redundancy method | Erasure coding + parity | Replication |
| Proof mechanism | ZK proofs (Poseidon2) | Proof-of-Replication |
| Marketplace | Automatic free-market contracts | Manual deal-making |
| Repair incentives | Built-in, incentivised | Provider-managed |
| KYC requirement | None | Filecoin+ requires KYC |

## Related Notes

- [[codex-p2p-protocol]] — How the P2P network and data flow works
- [[codex-tokenomics]] — CDX token and economic model
- [[codex-roadmap-2025]] — Milestones and current status
- [[codex-vs-filecoin]] — Detailed comparison
- [[codex-use-cases]] — Applications and integrations
- [[codex-implementation]] — nim-codex / logos-storage-nim repo
