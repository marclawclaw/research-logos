---
topic: waku-messaging
type: implementation
tags: [waku, nwaku, nim, logos-delivery, node, implementation, sdk]
confidence: high
last_updated: 2026-03-14
sources:
  - https://github.com/waku-org/nwaku
  - https://github.com/logos-messaging/logos-delivery
---

# nwaku / logos-delivery — Nim Implementation

## Summary

**nwaku** (now mirrored/redirected as `logos-messaging/logos-delivery`) is the **reference Nim implementation** of Waku protocols. It provides a full node, a C library for FFI integration, and a CLI application for running Logos Messaging network nodes.

## Key Facts

- **Language:** Nim (with Rust toolchain required for some components)
- **Build system:** Nimbus build system (make-based)
- **Repo redirect:** `github.com/waku-org/nwaku` → `github.com/logos-messaging/logos-delivery`
- **Specs implemented:** https://github.com/vacp2p/rfc-index/tree/main/waku
- **Binary name:** `wakunode2`
- **DNS bootstrapping** supported for peer discovery

## What It Provides

1. **Nim implementation** of all Waku specs (Relay, RLN Relay, Filter, Store, LightPush)
2. **C library** — exposes protocols via FFI for embedding in other runtimes
3. **CLI application** — run an LMN (Logos Messaging Node)
4. **Examples and tests**

## Building

```bash
make wakunode2
# Run with DNS bootstrapping
./build/wakunode2 --dns-discovery --dns-discovery-url=<DNS_BOOTSTRAP_URL>
```

Requires: C compiler, GNU Make, Bash, Git, Rust toolchain (rustc + cargo via rustup)

## Running Options

- Binary from source: `make wakunode2`
- Docker: `docs.waku.org/guides/nwaku/run-docker`
- Docker Compose: `docs.waku.org/guides/nwaku/run-docker-compose`

## Other Implementations

| Implementation | Language | Repo |
|---------------|----------|------|
| nwaku / logos-delivery | Nim | github.com/logos-messaging/logos-delivery |
| js-waku | TypeScript | github.com/waku-org/js-waku |
| go-waku | Go | github.com/waku-org/go-waku |

**js-waku** is the primary SDK for browser and Node.js integrations (used by Safe Harbour).

## Development Status (Nov 2025)

- libwaku validated running on **Windows** and **Status Desktop**
- API advancing across browser and nwaku implementations
- Local dev environment docs published
- Send and Health APIs in active development
- WebRTC integration being explored for low-latency browser meshes

## Sources

- https://github.com/waku-org/nwaku
- https://github.com/logos-messaging/logos-delivery
- https://docs.waku.org/guides/nwaku/build-source
