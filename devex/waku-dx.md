# Waku Developer Experience

> Source: https://docs.waku.org
> Researched: 2026-03-15 (updated from 2026-03-14)

## What Is Waku?

Waku is the messaging layer of the Logos stack (Logos Messaging). It's a family of censorship-resistant, privacy-focused peer-to-peer communication protocols for Web3 applications. Key properties:

- **Not a blockchain** — no gas fees, no long-term storage
- **Ephemeral messaging** — short-lived, real-time messaging
- **Resource-restricted friendly** — works in browsers and mobile via LightPush/Filter

## Core Protocols

| Protocol | Role | Notes |
|----------|------|-------|
| **Relay** | GossipSub-based P2P pub/sub | Privacy-focused; scales via sharding |
| **RLN Relay** | Relay + spam protection | Uses Rate Limiting Nullifiers; requires on-chain registration |
| **Filter** | Light node subscription | Selective message subscription; less privacy (reveals content topic) |
| **Store** | Message history | Retrieve missed messages; not guaranteed availability |
| **Light Push** | Low-bandwidth publishing | Req/response; ACK on receipt but no propagation guarantee |

### Waku Message Format

A `WakuMessage` has these fields:
- `content_topic` — routing/filtering key (like a channel)
- `payload` — actual message data
- `meta` — optional application-specific metadata
- `timestamp` — message creation time
- `ephemeral` — if true, don't store

## The Waku Network (Public Shared Infrastructure)

The **public Waku Network** is a shared p2p network with:
- DoS/spam protection via **Rate Limiting Nullifiers (RLN)**
- Traffic sharded across **8 pubsub topics** for scalability
- Auto shard selection based on content topic
- Services for resource-restricted nodes (store, filter, lightpush)

### Prerequisites to Use the Waku Network

> ⚠️ **DX friction point**: Running a node requires Ethereum Sepolia dependencies

1. Ethereum Sepolia HTTPS endpoint (Infura free tier works)
2. Sepolia wallet with ~0.1 ETH (testnet)
3. Wallet used to register RLN membership on-chain

This is a non-trivial setup for web developers unfamiliar with Ethereum tooling.

**Deprecation note**: Old default pubsub topic `/waku/2/default-waku/proto` is being retired. Migration to public Waku Network required for DoS protection and scalability.

## SDK Options

### js-waku (JavaScript/TypeScript)
- **Primary SDK for web/browser integrations**
- Browser-compatible, React-compatible
- Supports LightPush, Filter, Store, Relay
- Actively maintained; npm package `@waku/sdk`
- Integration pattern: LightPush to publish → Filter to subscribe → Store for history
- **`@waku/create-app`** — project scaffolding CLI for bootstrapping new projects
- **`@waku/react`** — React integration package for seamless component binding
- **`@waku/message-encryption`** — encryption package for secure messaging
- **React Native:** not currently supported, planned for future
- **10 guides available** at `docs.waku.org/build/javascript/` covering: Reliable Channels, Light Push & Filter, Store Protocol, Message Encryption, React Integration, Project Scaffolding, Node Discovery, NodeJS Usage, Debugging, Filter Management

### nwaku (Nim)
- Reference/full node implementation
- Most complete; production-used by Status
- Not for application-layer integrations (node operators)

### go-waku
- Go bindings to nwaku
- Being phased out in Status; nwaku bindings preferred

### waku-rust-bindings
- Rust bindings available
- Status: production-capable

## Typical Integration Pattern

```
Web App → js-waku (LightPush) → Waku Network relay → 
    ↳ js-waku (Filter) to subscribe to specific content_topics
    ↳ js-waku (Store) on startup to retrieve message history
```

## Documentation Assessment

**URL:** https://docs.waku.org

### What works
- Main landing page (`/`) — clean overview of capabilities
- `/learn/` — "The Waku Network" page with prerequisites
- `/learn/concepts/protocols` — solid protocol explanations with trade-off notes
- Case studies: The Graph, Railgun

### URL Restructure (Updated March 15, 2026)

**Resolved:** The site has been reorganised with three clear sections:
- `/build/javascript/` — JS SDK guides (10 guides, replaces old `/guides/`)
- `/run-node/` — Node operator setup (Docker Compose recommended)
- `/learn/` — Concepts, protocols, FAQ, glossary (now loads correctly)

**Still broken:** Old `/guides/*` URLs return 404 with no redirects to new paths.

> **Note**: A Docusaurus baseUrl configuration banner was observed on the homepage, suggesting possible ongoing deployment work.

### Getting Started UX
`@waku/create-app` scaffolding tool now provides a quick-start path. Installation: `npm install @waku/sdk` with protobufjs dependency. CDN access also available.

## Use Cases (from docs)

| Use Case | Pattern |
|----------|---------|
| Chat messengers | Standard relay/filter |
| Voting/proposals | Off-chain aggregation → submit on-chain |
| NFT marketplace bids | Off-chain negotiation |
| State channels | Message exchange without blockchain |
| Multi-sig wallets | Signature exchange |
| P2P gaming | Game move coordination |
| Layer 2 coordination | Mempool privacy |
| Social platforms | Decentralized feeds |

## DX Strengths

- Well-structured protocol documentation
- Clear trade-off explanations (anonymity trilemma)
- Multiple SDK options for different languages
- Active development with frequent releases
- Good conceptual clarity (not just a chat protocol)

## DX Weaknesses

- Old documentation URLs still 404 (no redirects from `/guides/` → `/build/javascript/`)
- RLN on-chain requirement adds setup friction (now Linea Sepolia, not just Sepolia)
- React Native not yet supported
- Sepolia ETH requirement may confuse web2 developers
- Terminology shift (js-waku → "Logos Delivery Module") creates confusion
