# nim-libp2p

> Last updated: 2026-03-15  
> Source: [github.com/vacp2p/nim-libp2p](https://github.com/vacp2p/nim-libp2p)
> Note: repo is canonical at vacp2p/nim-libp2p (historical references to status-im/nim-libp2p redirect here)

## Overview

**nim-libp2p** is the Nim implementation of the [libp2p](https://libp2p.io/) peer-to-peer networking stack. It's developed and maintained by Vac's P2P service unit.

| Attribute | Value |
|-----------|-------|
| Language | Nim |
| Stars | 308 |
| Forks | 68 |
| License | MIT / Apache 2.0 (dual) |
| Latest release | v1.15.2 (2026-02-02) |
| Async runtime | [chronos](https://github.com/status-im/nim-chronos) |
| Supported Nim | v2.0.16, v2.2.6 |
| Docs | https://vacp2p.github.io/nim-libp2p/docs/ |

## Install

```
nimble install libp2p
```

## Who Uses It

- **Nimbus** — Ethereum consensus client
- **logos-delivery** — Decentralized messaging protocols (Waku stack)
- **logos-storage** — Decentralized storage protocols (Codex stack)

> Note: logos-delivery and logos-storage are distinct projects from nim-libp2p itself; nim-libp2p is a dependency they build on, not a part of them.

## Architecture

### Core Concepts
Built on the standard libp2p spec with Nim-native async via chronos. Core switch manages connections, multiplexing, protocol negotiation.

### Modules

#### Core
| Module | Description |
|--------|-------------|
| libp2p (switch.nim) | Core switch — the main entry point |
| connmanager | Connection manager |
| identify / push identify | Identify protocol |
| ping | Ping protocol |

#### Transports
| Module | Description |
|--------|-------------|
| libp2p-tcp | TCP transport |
| libp2p-ws | WebSocket & WebSocket Secure |
| libp2p-tor | Tor transport |
| libp2p-quic | QUIC transport |
| libp2p-memory | In-memory transport (testing) |

#### Secure Channels
| Module | Description |
|--------|-------------|
| libp2p-noise | Noise secure channel |
| libp2p-plaintext | Plaintext (dev only) |

#### Stream Multiplexers
| Module | Description |
|--------|-------------|
| libp2p-mplex | MPlex multiplexer |
| libp2p-yamux | Yamux multiplexer |

#### Data Types
| Module | Description |
|--------|-------------|
| peer-id | Cryptographic identifiers |
| peer-store | Address book of known peers |
| multiaddress | Composable network addresses |
| signed-envelope | Signed generic data container |
| routing-record | Signed peer dialing information |
| discovery manager | Peer discovery |

## Stability & Versioning

- Core considered **production stable** (used in Nimbus for years, high-stakes production)
- Versioning: **semver**
  - Procedures marked `.public.` stay compatible across MAJOR versions
  - Other procedures may change at MINOR versions
- Some newer modules (e.g., QUIC) are less stable

## Recent Activity (as of 2026-03-14)

### Recent Commits (2026-03-13)
- Migrate from `options` to `results` library
- Use `newFutureCompleted` (chronos improvement)
- Fix deprecated `Future.cancel()` usage
- Avoid deprecated `ByteAddress` type
- Avoid deprecated callbacks in transport creation

**Theme:** Active deprecation cleanup / modernization for newer Nim/chronos versions.

### Recent Open Issues
- `#2148` — Test ORC memory management
- `#2141` — Fix counting closest peer (KadDHT)
- `#2139` — KadDHT: configurable stale entry purge on bucket refresh
- `#2138` — Interop: script file for running tests
- `#2134` — KadDHT put values never expire (good first issue)

**Theme:** KadDHT stability and interop testing improvements.

### Active Milestone
- **v1 milestone:** 1 open, 17 closed issues

## Community

- Discord: https://discord.com/channels/1204447718093750272/1351621032263417946
- Contributing: `docs/contributing.md`
- Good first issues available — maintainers provide mentorship

## Relevance to Logos Ecosystem

nim-libp2p is the **networking foundation for Waku (logos-delivery) and Codex (logos-storage)**. Improvements to nim-libp2p — especially GossipSub, QUIC, and WebTransport — directly impact the performance and reach of both protocols. Any PoC built on Waku or Codex ultimately runs on nim-libp2p.
