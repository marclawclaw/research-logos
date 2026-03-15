---
title: Codex / Logos Storage — Overview
aliases: [Logos Storage, Codex DDE, Decentralised Durability Engine]
tags: [logos, codex, storage, decentralised, DDE]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage
  - https://codex.storage/about/faq
  - https://github.com/logos-storage/logos-storage-nim
---

# Codex / Logos Storage — Overview

## What It Is

Codex is the **Logos storage module** — a privacy-preserving, decentralised storage system providing censorship resistance and data durability. It is branded externally as **Codex** but internally renamed to **Logos Storage** (repo: `logos-storage/logos-storage-nim`).

Its core design philosophy is the **Decentralised Durability Engine (DDE)** — going beyond a basic DSN by integrating reliability mechanisms, economic incentives, and cryptographic verification.

## Core Goals

- Censorship-resistant, durable data storage
- No single controlling entity
- Verifiable proof that data is being stored (not just claimed)
- Trustless economic incentives for storage providers
- Privacy-preserving by default

## Position in the Logos Stack

| Layer | Module | Former Name |
|---|---|---|
| Blockchain | Nomos | Nomos |
| Storage | Logos Storage | Codex |
| Messaging | Waku | Waku |

Codex is a first-class primitive for Logos dapps — enables decentralised frontend hosting, data persistence, and censorship-resistant content delivery.

## Implementation

- Written in **Nim**
- Built on **libp2p**
- Licensed under Apache-2.0 / MIT
- REST API: `api.codex.storage`
- C API with Go bindings (Rust bindings: `nipsysdev/storage-rust-bindings`)

## Current Status (as of March 2026)

- Non-incentivised testnet live (Altruistic Mode)
- Incentivised testnet targeted H2 2025
- Mainnet readiness targeted Q3 2025 → now likely late 2025 / 2026
- CDX testnet token not yet live on mainnet

## Key Links

- Blog: https://blog.codex.storage
- Docs: https://docs.codex.storage
- API: https://api.codex.storage
- GitHub: https://github.com/logos-storage/logos-storage-nim
- Discord: https://discord.gg/zsGeeSQs
- Metrics: https://metrics.testnet.codex.storage
