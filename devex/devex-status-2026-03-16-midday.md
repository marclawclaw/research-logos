# Logos DX — Status 2026-03-16 (12:30 AEST — Midday)

> Sources: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org
> Run type: Midday check

## Summary

No major structural changes since the 00:30 check. docs.waku.org content stable at 11 JavaScript guides. logos-co/logos-docs remains dormant (now 6 days without commits). ideas.waku.org held at 47 ideas — no new additions since the overnight burst. Protocols documentation fully confirmed and catalogued this run.

---

## docs.waku.org

**No new guides detected. Content stable.**

### Build / JavaScript (11 guides — unchanged)
1. Send and Receive Messages in a Reliable Channel
2. Send and Receive Messages Using Light Push and Filter
3. Retrieve Messages Using Store Protocol
4. Encrypt, Decrypt, and Sign Your Messages
5. Build React DApps Using @waku/react
6. Scaffold DApps Using @waku/create-app
7. Set Up a Local Development Environment *(added 2026-03-16 overnight)*
8. Bootstrap Nodes and Discover Peers
9. Run @waku/sdk in a NodeJS Application
10. Debug Your Waku DApp and WebSocket
11. Manage Your Filter Subscriptions

### Run a Node (nwaku — unchanged)
- Primary path: Docker Compose via `nwaku-compose` repo
- System requirements: 2GB RAM (Relay-only: 0.5GB)
- Setup flow: clone `nwaku-compose`, copy `.env.example`, edit settings, `docker-compose up -d`
- Pre-requisites for joining public network: Ethereum Sepolia HTTPS endpoint + wallet with Sepolia ETH (<0.1 ETH) for RLN membership registration
- Old Sepolia ETH requirement has been replaced — **now Linea Sepolia** (confirmed in Grafana/env docs)
- Grafana dashboard available for node monitoring

### Learn — Protocols (confirmed full catalogue)

| Protocol | Purpose | Trade-off |
|----------|---------|-----------|
| **Relay** | GossipSub-based pub/sub for p2p messaging | Full node, best privacy |
| **RLN Relay** | Relay + Rate Limit Nullifiers for spam prevention | On-chain membership cost |
| **Filter** | Light-node selective subscription by content topic | Reveals content topic to peers |
| **Store** | Historical message retrieval for offline peers | No availability guarantee |
| **Light Push** | Send messages with receipt ack (low bandwidth) | No propagation guarantee |
| **Waku Message** | Standard message format | — |

Key message fields: `content_topic`, `payload`, `meta`, `timestamp`, `ephemeral`.

### Network Architecture
- Public Waku Network: open-access, privacy-preserving, scalable to resource-restricted devices
- DoS/spam protection: Privacy-preserving Rate-Limiting Nullifiers (RLN)
- Scalability: 8 pubsub topic shards with automatic content-topic-based shard selection
- Services for light nodes: Store (historical), Filter (selective delivery)
- Incentivisation vectors for node operators in development
- **Migrating from:** old `/waku/2/default-waku/proto` shared topic — all projects encouraged to migrate to public Waku Network

### Use Cases (from homepage)
- Chat messengers (censorship-resistant)
- Voting/proposals (off-chain aggregation → on-chain submit)
- NFT marketplace bids/offers
- State channels
- Multi-sig wallet signature exchange
- P2P gaming communication
- L2 coordination (spam-protected mempool)
- Social media platforms

### Case Studies
- The Graph (2024-05-13)
- Railgun (2024-04-26)

---

## logos-co/logos-docs

**No new commits. Last commit: `91a65d9` on 2026-03-11 (6 days ago).**

### Stack Architecture (confirmed from README)
The Logos stack is now officially described as:

```
Dapps
  └── Blockchain (Logos Execution Zone + Data Availability/Consensus)
  └── Messaging (Logos Delivery/Chat Module — built on Waku)
  └── Storage (Logos Storage Module — built on Codex)
  └── User Modules (wallet, identity, access control, module installer)
      └── Discovery, Peering, Mix-net (shared networking + AnonComms)
          └── Logos Kernel (lowest layer — runtime foundation)
```

### Available Developer Journeys (as of 2026-03-16)
| Area | Journey |
|------|---------|
| Logos App | Build from source (Nix), run with all modules |
| Execution Zone | Wallet quickstart, token transfer, custom token creation, AMM liquidity pool |
| Blockchain | Start a node via CLI |
| Storage | Storage module API, Simple Filesharing App |
| Messaging | Delivery Module API, Chat Module API |
| AnonComms | Mixnet demo app (discover nodes, send messages anonymously) |

### Naming Consolidation Status (from README)
> "We are unifying public naming: Nomos → Logos Blockchain, Codex → Logos Storage, Waku → Logos Messaging. Legacy names still appear in repos and specs but Logos-first names will be used in docs going forward."

This signals active work but creates ongoing dual-naming confusion until fully resolved.

### 2026 Documentation Roadmap
- Operator guides for Logos Blockchain node operators
- Developer guides for dApp builders (blockchain + storage + messaging)
- Phased releases aligned to project milestones

**Known gap:** No confirmed timelines — "timelines may adjust as the system evolves."

### Open PRs/Issues (10 total — unchanged since morning)

| # | Type | Title | Age |
|---|------|-------|-----|
| 186 | PR | Tutorial: Building modules for Logos Core | 20 days |
| 185 | Issue | Tutorial: Building modules for Logos Core | 20 days |
| 184 | PR | Dk/node cli journey | 21 days |
| 183 | PR | Blockchain Node Journey | 25 days |
| 182 | PR | fix(LEZ): update references to LSSA, rename to LEZ | 25 days |
| 181 | PR | Enhance quickstart template | 28 days |
| 177 | Issue | Improve Quickstart template | 31 days |
| 170 | PR | Set doc packet as pull request template | 34 days |
| 169 | Issue | Set doc packet as pull request template | 35 days |
| 166 | PR | feat: initial documentation for Logos Storage | 41 days |

**PR #166 (Logos Storage docs) is 41 days old and still unmerged — critical gap.** Storage is the weakest-documented pillar of the stack.

---

## ideas.waku.org

**Count: 47 ideas — unchanged since overnight burst (+3 ideas yesterday afternoon).**

### Idea Category Distribution
| Category | Examples |
|---------|---------|
| Infrastructure/Privacy | IoT systems, notifications centre, privacy-preserving APIs, federated learning |
| Governance/DAO | Polling/voting, DAO tooling, budget approval, privacy-preserving governance |
| Marketplace | Buy/sell/NFT, ride-share, LLM marketplace, crypto ATMs |
| Gaming | P2P chess, P2P TicTacToe, multiplayer games |
| Social | Censorship-resistant reviews, news over Waku, decentralised brainstorming, confessions board |
| Health/DeSci | Medical remote diagnosis, fitness tracker, crowd-sourced weather, indoor air quality IoT |
| Identity/Security | Wallet address ownership verification, 2FA, smart access cards, reputation systems |
| AI | Privacy-preserving AI assistant, API generator from OpenAPI spec |
| Transport/Infrastructure | Autonomous vehicle coordination, smart grid, satellite comms |
| Finance/DeFi | Secure DeFi, multi-sig wallets, state channels |

### Notable Ideas (Alignment with Logos Stack)
- **Privacy-preserving AI assistant** — strong fit with Logos Messaging + identity modules
- **Leader Election Protocol (RAFT on Waku)** — infrastructure primitive with broad applicability
- **API Generator from OpenAPI spec** — developer tooling, directly reduces integration friction
- **Decentralised Wallet Address Ownership Verification** — wallet/identity module alignment
- **Notifications Centre (replacing Apple/Google push)** — censorship-resistant, privacy-native

---

## DX Status Tracker (2026-03-16 Midday)

| Issue | Status | Trend |
|-------|--------|-------|
| Old `/guides/` URLs broken (no redirects) | ❌ Unresolved | Unchanged |
| RLN setup friction (Linea Sepolia ETH required) | ❌ Unresolved | Unchanged |
| Storage docs on Netlify subdomain | ❌ Unresolved | Unchanged |
| React Native unsupported | ❌ Documented gap | Unchanged |
| logos-docs dormant | ❌ 6 days no commits | Worsening |
| PR #166 (Storage docs) 41 days unmerged | ❌ Critical | Worsening |
| Naming dual-track confusion | ⚠️ In progress | Slowly improving |
| Local dev setup guide | ✅ Added overnight | Improved |
| Waku Network public shards | ✅ Available | Stable |
| Execution Zone testnet | ✅ Live | Stable |
| @waku/create-app scaffolding | ✅ Available | Stable |

---

## Action Items

1. **Ping logos-docs contributors** — 6 days without commits, 6 open PRs including 41-day-old Storage docs. Review cycle may be stalled.
2. **Try the new "Local Dev Setup" guide** — added this morning; validate it works end-to-end.
3. **File `/guides/` redirect issue** on docs.waku.org repo — has no owner tracking it.
4. **Document naming map** — consider a PR to logos-docs adding a `NAMING.md` alias guide.
5. **Explore ideas.waku.org for PoC candidates** — "API Generator from OpenAPI spec" and "Leader Election Protocol" are both infrastructure-level and could make strong RFP submissions.
