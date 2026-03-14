---
topic: codex
type: concept
tags: [storage, p2p, decentralization, erasure-coding]
confidence: high
last_updated: 2026-03-14
sources: [https://github.com/codex-storage/nim-codex, https://api.codex.storage]
---

# Codex

## Summary

Codex (officially "Logos Storage") is a decentralized durability engine that enables private file sharing in peer-to-peer networks. It provides persistent storage capabilities for the [[Logos]] ecosystem, complementing [[Waku]]'s ephemeral messaging.

## Key Facts

> [!fact] Confirmed from GitHub README
> - Written in Nim (nim-codex is the main implementation)
> - Pre-alpha status as of 2026
> - Exposes REST API for interaction (documented at api.codex.storage)
> - Provides C library bindings for language interop
> - Go bindings available, Rust bindings via separate repo

### Configuration Methods (priority order)
1. CLI options
2. Environment variables  
3. Configuration file

### Language Bindings
- **C** — Core library (libstorage.so / libstorage.dylib / libstorage.dll)
- **Go** — Via codex-go-bindings-example repo
- **Rust** — Via nipsysdev/codex-rust-bindings

## How it relates to Logos

Codex is the **storage layer** of the [[Logos]] stack. While [[Waku]] handles ephemeral real-time messaging, Codex provides durable, persistent storage for larger data that needs to survive beyond immediate transmission.

## Technical Details

> [!analysis] Inferred from documentation
> - Uses erasure coding for data redundancy
> - Marketplace component for storage incentives (likely similar to Filecoin model)
> - Designed for privacy-preserving file sharing

## Open Questions

- What erasure coding scheme is used?
- How does the storage marketplace work? What are the economics?
- What is the relationship between Codex and IPFS/Filecoin?
- What are the storage guarantees and SLAs?
- How does data durability work without a blockchain anchor?

## Sources

- https://github.com/codex-storage/nim-codex — Main implementation (redirects to logos-storage/logos-storage-nim)
- https://api.codex.storage — REST API documentation
