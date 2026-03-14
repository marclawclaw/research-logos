---
topic: developer-experience
type: summary
tags: [dx, sdk, documentation, pain-points, index]
confidence: medium
last_updated: 2026-03-14
sources: [https://docs.waku.org, various]
---

# Developer Experience Research

Research on developer experience across the Logos stack.

## SDK Overview

| Component | SDK | Languages | Status |
|-----------|-----|-----------|--------|
| Waku | js-waku | TypeScript/JS | Production (v0.0.34) |
| Waku | nwaku | Nim | Production (full node) |
| Waku | go-waku | Go | Production |
| Waku | waku-rust-bindings | Rust | Production |
| Codex | codex-storage | Nim | Testnet |
| Nomos | logos-co/nomos | Nim | Development |

## Documentation Sites

- **Waku:** docs.waku.org — comprehensive, regularly updated
- **Codex:** docs.codex.storage — whitepaper available
- **Nomos:** blog.nomos.tech — updates, no full docs yet
- **Logos:** logos-co/logos-docs on GitHub

## Observed Pain Points

> [!analysis] To be validated through community research
> - Multiple implementations can be confusing (which to choose?)
> - Testnet instability (Codex paused)
> - Limited mainnet use cases for full stack
> - Integration complexity between components

## Research To Do

- [ ] SDK quality comparison
- [ ] Documentation gaps analysis
- [ ] Community feedback (Discord, forum)
- [ ] Getting started experience
- [ ] Error handling patterns
