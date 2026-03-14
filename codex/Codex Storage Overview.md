---
topic: codex
type: concept
tags: [storage, decentralised, privacy, censorship-resistance]
confidence: high
last_updated: 2026-03-14
sources: [https://logos.co/tech-stack, https://press.logos.co/article/2024-roundup, https://blog.codex.storage]
---

# Codex Storage Overview

## Summary

Codex is a privacy-preserving, decentralised storage system providing censorship resistance and data durability. It prevents data manipulation, ensures no single entity controls stored information, and enables truly decentralised deployment of dApp frontends within the Logos ecosystem.

## Key Facts

> [!fact] From official sources
> - **Purpose:** Censorship-resistant, durable storage
> - **Key feature:** Prevents data manipulation
> - **Use case:** Storing dApp frontends for truly decentralised deployment
> - **Whitepaper:** Released 2024
> - **Public testnet:** Launched 2024 (now paused)

### Architecture (from 2024 Roundup)

- **Erasure coding** for data durability
- **Marketplace** for storage providers
- **Integration with Waku** for coordination

### Current Status (Aug 2025)

> [!outdated] Check for updates
> - Non-incentivised testnet **paused**
> - Team shifted focus to **core protocol design and specifications**
> - Collaborating with **Qubetics** on AI product stack integration
> - **Guru PoC:** Integrated with Waku and Status Network for feedback platform

## How it relates to Logos

Codex is the **storage layer** of the Logos stack:
- Stores dApp frontends (truly decentralised apps)
- Archives important data for communities
- Complements [[Waku Protocol Overview|Waku]] (messaging) and [[Nomos Blockchain|Nomos]] (consensus)

> [!analysis] Analyst inference
> Without durable storage, Logos applications would depend on centralised hosting (IPFS gateways, cloud providers), defeating the purpose. Codex fills this critical gap.

## Key Differentiators

Compared to alternatives like IPFS/Filecoin:
- **Privacy-preserving** by design
- **Integrated** with Logos messaging and consensus
- **Designed for** censorship-resistance use cases

## Open Questions

- Testnet restart timeline?
- Incentive model (token economics)?
- Storage pricing mechanism?
- Erasure coding parameters (durability vs overhead)?
- Integration complexity with Waku/Nomos?

## Sources

- https://logos.co/tech-stack
- https://press.logos.co/article/2024-roundup
- https://blog.codex.storage/codex-2024-year-in-review/
- https://blog.codex.storage/codex-august-updates-2/
