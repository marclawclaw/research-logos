---
topic: competitors
type: summary
tags: [comparison, alternatives, index]
confidence: medium
last_updated: 2026-03-14
sources: [https://docs.waku.org, various]
---

# Competitors Research

Analysis of comparable projects to the [[Logos Overview|Logos]] stack components.

## Messaging Layer (vs Waku)

- [[Waku vs libp2p]] — foundation comparison
- [[Matrix Protocol]] — decentralised messaging (TODO)
- [[Whisper Protocol]] — predecessor to Waku (TODO)

## Storage Layer (vs Codex)

- [[IPFS Comparison]] — content-addressed storage (TODO)
- [[Filecoin Comparison]] — incentivised IPFS layer (TODO)
- [[Arweave Comparison]] — permanent storage (TODO)
- [[Storj Comparison]] — enterprise decentralised storage (TODO)

## Blockchain Layer (vs Nomos)

- [[Celestia Comparison]] — modular DA layer (TODO)
- [[Cosmos Zones]] — sovereign chains (TODO)
- [[Polkadot Parachains]] — shared security (TODO)

## Quick Comparison Matrix

| Project | Layer | Privacy Focus | Incentives | Status |
|---------|-------|---------------|------------|--------|
| libp2p | Networking | Low | None | Production |
| IPFS | Storage | Low | None built-in | Production |
| Filecoin | Storage | Low | Strong | Production |
| Arweave | Storage | Low | Strong | Production |
| Celestia | DA | Medium | Strong | Production |
| Matrix | Messaging | Medium | None | Production |

> [!analysis] Logos differentiation
> Primary differentiator is **privacy-first design** across all layers, plus **unified stack** (messaging + storage + consensus integrated from the start).
