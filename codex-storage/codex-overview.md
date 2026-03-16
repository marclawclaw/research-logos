---
title: "Codex – Decentralised Storage Overview"
tags: [logos, codex, storage, decentralised, web3]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://codex.storage/about/faq
  - https://blog.codex.storage
  - https://github.com/codex-storage/nim-codex
---

# Codex – Decentralised Storage Overview

## What It Is

Codex is the **storage module of the Logos technology stack** (formerly known as "Codex Storage"). It is a privacy-preserving, decentralised storage system that provides censorship resistance and data durability.

Its core design principle is the **Decentralised Durability Engine (DDE)** — extending the traditional DSN (Decentralised Storage Network) model with robust reliability guarantees, verifiable proofs, and an open marketplace.

## Core Goals

- Prevent data manipulation and censorship
- Ensure no single entity owns or controls stored information
- Enable delivery of dapp frontends (truly decentralised deployments)
- Serve as the storage layer for the broader Logos ecosystem

## Position in the Logos Stack

| Module | Former Name | Role |
|---|---|---|
| Blockchain | Nomos | Trustless agreements layer |
| **Storage** | **Codex** | **Durable, private, censorship-resistant storage** |
| Messaging | Waku | P2P communication layer |

## Implementation

- **Language:** Nim (`nim-codex` on GitHub)
- **Network:** P2P, libp2p-based
- **Smart contracts:** On-chain storage requests and ZK proof verification

## Current Status (as of early 2026)

- Testnet paused (August 2025) for core architecture redesign
- Next phase: stronger foundations and revisited core design
- New testnet in development — incentivised testnet planned before mainnet
- Undergoing "evolution" to align more closely with the Logos ecosystem vision

## Key Links

- Docs: https://docs.codex.storage
- API: https://api.codex.storage
- GitHub: https://github.com/codex-storage/nim-codex
- Blog: https://blog.codex.storage
- Discord: https://discord.gg/KsKzNKVq

## Related Notes

- [[codex-dde-architecture]] — DDE, erasure coding, proofs
- [[codex-p2p-network]] — Node bootstrapping, file sharing modes
- [[codex-storage-marketplace]] — Incentivised storage contracts
- [[codex-developer-integration]] — REST API, node setup
- [[codex-vs-filecoin]] — Comparison with Filecoin
- [[codex-integrations]] — TACo, Waku, Akash, Dappnode
