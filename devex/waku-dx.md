# Waku Developer Experience

> Source: https://docs.waku.org  
> Researched: 2026-03-14

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

### Broken/missing (March 2026)
- `/guides/` → 404
- `/learn/concepts/` (index) → 404
- `/learn/concepts/sdk` → 404
- `/learn/waku-network` → 404

> **Issue**: Multiple sub-pages return 404. Navigation from the sidebar likely works but direct URL access fails. This is a critical DX issue for developers who share links or bookmark pages.

### Getting Started UX
No working quick-start guide accessible via direct URL. Developers are pointed to GitHub tutorials for RLN setup.

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

- Broken documentation links (404s on sub-pages)
- RLN on-chain requirement adds setup friction
- No accessible quick-start guide via direct URL
- Sepolia ETH requirement may confuse web2 developers
- Terminology shift (js-waku → "Logos Delivery Module") creates confusion
