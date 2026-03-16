# Logos DX — Status 2026-03-17 (00:30 AEST — Overnight)

> Sources: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org
> Run type: Overnight check

## Summary

Quiet overnight. logos-co/logos-docs now **7 days without a commit** — the longest dormancy streak recorded in this tracker. docs.waku.org content unchanged at 11 JavaScript guides. ideas.waku.org stable at ~47 ideas. One notable discrepancy found: the `/learn` page still references **Ethereum Sepolia** for RLN prerequisites, while the Grafana/env docs (confirmed midday yesterday) reference Linea Sepolia — this is an inconsistency that will confuse node operators.

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

### Broken URL Patterns (still unresolved)
- `/guides/` prefix paths → 404 (no redirects)
- `/guides/js-waku/` → 404
- `/build` → 404
- These broken links remain unfiled and untracked publicly

### RLN Prerequisites — Inconsistency Detected ⚠️
The `/learn` page still reads:
> "Wallet with Sepolia Ethereum (less than 0.1 Sepolia ETH)"
> "Ethereum Sepolia HTTPS endpoint"

But the `nwaku-compose` env docs reference **Linea Sepolia** (confirmed in yesterday's midday run). Two docs contradict each other for the same setup step. High friction for first-time node operators.

### Protocol Catalogue (unchanged)

| Protocol | Purpose | Trade-off |
|----------|---------|-----------|
| Relay | GossipSub p2p pub/sub | Full node, best privacy |
| RLN Relay | Relay + spam protection | On-chain membership cost |
| Filter | Light-node selective sub | Reveals content topic |
| Store | Historical retrieval | No availability guarantee |
| Light Push | Send with ack | No propagation guarantee |

### Network Architecture (stable)
- Public Waku Network: open-access, p2p, 8 pubsub topic shards
- Automatic content-topic-based shard selection
- DoS/spam: privacy-preserving RLN
- Migration note: projects on `/waku/2/default-waku/proto` encouraged to migrate
- Incentivisation for node operators still "in development"

---

## logos-co/logos-docs

**Last commit: `91a65d9` on 2026-03-11 (7 days ago — new streak high)**

### PR Queue (10 open — no movement overnight)

| # | Type | Title | Age |
|---|------|-------|-----|
| 186 | PR | Tutorial: Building modules for Logos Core | 21 days |
| 185 | Issue | Tutorial: Building modules for Logos Core | 21 days |
| 184 | PR | Dk/node cli journey | 22 days |
| 183 | PR | Blockchain Node Journey | 26 days |
| 182 | PR | fix(LEZ): update references to LSSA, rename to LEZ | 26 days |
| 181 | PR | Enhance quickstart template | 29 days |
| 177 | Issue | Improve Quickstart template | 32 days |
| 170 | PR | Set doc packet as pull request template | 35 days |
| 169 | Issue | Set doc packet as pull request template | 36 days |
| 166 | PR | feat: initial documentation for Logos Storage | **42 days** |

**PR #166 now 42 days unmerged. Storage docs remain the biggest documentation gap.**

### Stack Architecture (confirmed stable)
```
Dapps
  └── Blockchain (Logos Execution Zone + Data Availability/Consensus)
  └── Messaging (Logos Delivery/Chat Module — built on Waku)
  └── Storage (Logos Storage Module — built on Codex)
  └── User Modules (wallet, identity, access control, module installer)
      └── Discovery, Peering, Mix-net (shared networking + AnonComms)
          └── Logos Kernel (lowest layer — runtime foundation)
```

### Developer Journeys (unchanged since March 11)
| Area | Journey |
|------|---------|
| Logos App | Build from source (Nix), run with all modules |
| Execution Zone | Wallet quickstart, token transfer, custom token creation, AMM liquidity pool |
| Blockchain | Start a node via CLI |
| Storage | Storage module API, Simple Filesharing App |
| Messaging | Delivery Module API, Chat Module API |
| AnonComms | Mixnet demo app |

---

## ideas.waku.org

**Count: ~47 ideas — no change since yesterday's midday burst.**

Full idea list (confirmed this run):

| # | Idea | Category |
|---|------|----------|
| 1 | Polling/Voting | Governance |
| 2 | Marketplace (goods, NFTs, ride-share, LLM) | Commerce |
| 3 | Collaborative Editing | Productivity |
| 4 | Multiplayer Games | Gaming |
| 5 | IoT Systems | Infrastructure |
| 6 | Decentralised Wallet Address Ownership Verification | Identity |
| 7 | Notifications Centre | Infrastructure |
| 8 | API Generator from OpenAPI spec | Developer Tooling |
| 9 | Leader Election Protocol (RAFT on Waku) | Infrastructure |
| 10 | Reputation Systems | Identity/Social |
| 11 | Censorship-Resistant Reviews Plugin | Social |
| 12 | Privacy-Preserving Location Tracker | Privacy |
| 13 | Medical Systems for Remote Diagnosis | Health/DeSci |
| 14 | Decentralised Smart Grid System | Infrastructure |
| 15 | Decentralised Autonomous Vehicle Coordination | Infrastructure |
| 16 | Crowd-Sourced Weather Data Network | DeSci |
| 17 | P2P Chess | Gaming |
| 18 | P2P TicTacToe | Gaming |
| 19 | Privacy-Focused Fitness Tracker | Health/Privacy |
| 20 | Decentralised & Privacy-Focused Hiring Platform | HR/Social |
| 21 | DAO/Governance Tooling | Governance |
| 22 | Satellite Communication Systems | Infrastructure |
| 23 | Decentralised Web Walkie-Talkie | Comms |
| 24 | Crypto ATMs | Finance |
| 25 | Smart Access Cards | Identity/IoT |
| 26 | Secure DeFi | Finance |
| 27 | News over Waku | Social/Media |
| 28 | Budget Approval App | Governance |
| 29 | Privacy-Preserving AI Assistant | AI/Privacy |
| 30 | Federated Learning Platform | AI/Privacy |
| 31 | Supply Chain Transparency Solution | Commerce/Infrastructure |
| 32 | Decentralised Brainstorming Tool | Productivity |
| 33 | Privacy-Preserving Confessions Board | Social |
| 34 | Privacy-Preserving Governance Platform | Governance |
| 35 | Privacy-Preserving APIs and Data Sources | Infrastructure |
| 36–47 | Additional ideas (page truncated) | Various |

### Top PoC Candidates for RFP Alignment
1. **Leader Election Protocol (RAFT on Waku)** — infrastructure primitive, broad applicability
2. **API Generator from OpenAPI spec** — reduces integration friction, developer tooling
3. **Privacy-Preserving AI Assistant** — Logos Messaging + identity modules fit
4. **Federated Learning Platform** — DeSci/AI angle, privacy-native
5. **Supply Chain Transparency** — enterprise use case with measurable impact

---

## DX Status Tracker (2026-03-17 Overnight)

| Issue | Status | Trend |
|-------|--------|-------|
| Old `/guides/` URLs broken (no redirects) | ❌ Unresolved | Unchanged |
| `/build` URL broken (404) | ❌ Unresolved | Unchanged |
| RLN docs inconsistency (Sepolia vs Linea Sepolia) | ❌ **New find** | Newly flagged |
| RLN setup friction (requires ETH + RPC endpoint) | ❌ Unresolved | Unchanged |
| Storage docs on Netlify subdomain | ❌ Unresolved | Unchanged |
| React Native unsupported | ❌ Documented gap | Unchanged |
| logos-docs dormant | ❌ **7 days no commits** | Worsening |
| PR #166 (Storage docs) 42 days unmerged | ❌ Critical | Worsening |
| Naming dual-track confusion | ⚠️ In progress | Slowly improving |
| Local dev setup guide | ✅ Available | Stable |
| Waku Network public shards | ✅ Available | Stable |
| Execution Zone testnet | ✅ Live | Stable |
| @waku/create-app scaffolding | ✅ Available | Stable |

---

## New Finding This Run

**RLN Network Prerequisites Inconsistency:**
- `/learn` page → references Ethereum Sepolia (Infura)
- `nwaku-compose` env docs → references Linea Sepolia
- Impact: first-time node operators following the getting-started flow will hit a dead end when they get to the "join the network" step and find conflicting chain requirements
- Action: file an issue on waku-org/nwaku or waku-org/docs pointing out the inconsistency; this is a concrete, low-effort improvement

---

## Action Items

1. **File inconsistency issue** — `/learn` vs `nwaku-compose` Sepolia/Linea Sepolia mismatch. Direct, actionable, good community contribution.
2. **Ping logos-docs contributors** — 7 days without commits, PR #166 at 42 days. Review pipeline appears stalled.
3. **File `/guides/` broken URL issue** — concrete 404 fix, good first contribution.
4. **Consider PoC: API Generator from OpenAPI spec** — strong RFP candidate, directly solves integration friction, no one has built it yet.
5. **Consider PoC: Leader Election Protocol** — RAFT on Waku is a missing infrastructure primitive; could unblock many app categories.
