# Logos DX Status Snapshot — 2026-03-15

> Verification run: Sunday, 2026-03-15
> Sources checked: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org

## Key Finding: docs.waku.org Navigation Restructured

The most significant change since March 14: **docs.waku.org has reorganised its URL structure**. The old `/guides/` path that returned 404 has been replaced with a new layout:

| Old URL (March 14) | Status | New URL (March 15) | Status |
|---------------------|--------|---------------------|--------|
| `/guides/` | ❌ 404 | `/build/javascript/` | ✅ 200 |
| `/guides/js-waku/` | ❌ 404 | `/build/javascript/` | ✅ 200 |
| `/guides/getting-started` | ❌ 404 | `/build/javascript/` | ✅ 200 |
| `/guides/nwaku/run-node` | ❌ 404 | `/run-node/` | ✅ 200 |
| `/learn/` | ❌ 404 | `/learn/` | ✅ 200 |
| `/learn/waku-network` | ❌ 404 | `/learn/` | ✅ 200 (content present) |
| `/learn/concepts/protocols` | ✅ 200 | `/learn/concepts/protocols` | ✅ 200 |

**Verdict:** The 404 epidemic is partially resolved. The site now has three clear entry points: Build, Run Node, Learn. Old `/guides/` URLs are still broken (no redirects), but equivalent content exists at new paths.

---

## docs.waku.org — New Content Discovered

### JavaScript SDK Guides (at `/build/javascript/`)

New or newly-accessible guides found:

| Guide | Description |
|-------|-------------|
| **Reliable Channels** | Send/receive with convenient SDK functionality |
| **Light Push & Filter** | Messaging on light nodes |
| **Store Protocol** | Historical message retrieval and filtering |
| **Message Encryption** | `@waku/message-encryption` package |
| **React Integration** | `@waku/react` for seamless React app integration |
| **Project Scaffolding** | `@waku/create-app` for bootstrapping projects |
| **Node Discovery** | Bootstrap and peer discovery configuration |
| **NodeJS Usage** | Server-side SDK usage |
| **Debugging** | Troubleshooting DApp issues and WebSocket connections |
| **Filter Management** | Subscription handling and disconnection scenarios |

**Notable new tool:** `@waku/create-app` — a project scaffolding CLI. This significantly lowers the barrier to entry for new developers.

**Note:** React Native support is listed as "currently unavailable but planned."

### Run Node Section (at `/run-node/`)

- Docker Compose recommended as primary deployment method
- System requirement: minimum 2GB RAM (with WSS) or 0.5GB for Relay-only
- RPC endpoint now specified as **Linea Sepolia** (previously noted as just "Sepolia")
- Includes Grafana dashboard at `localhost:3000` and health endpoint at `localhost:8645/health`
- Waku Node Operator Cheatsheet PDF available

### Learn Section (at `/learn/`)

Confirmed working with these concept categories:
- Protocols, Content Topics, Network Domains, Transports
- Peer Discovery, Security Features
- Research materials, Waku vs libp2p comparison
- Glossary, FAQ

---

## logos-co/logos-docs — No Changes

- **Last commit:** 2026-03-11 (`91a65d9`) — "remove erroneous line for node running from logos app section"
- **No new commits** since March 14 snapshot
- README structure unchanged
- Storage docs still hosted on `logos-storage-docs.netlify.app`
- All developer journeys remain as documented in previous analysis

### Notable commits from March 4 batch (first time noting these):

| Date | Commit | Description |
|------|--------|-------------|
| 2026-03-04 | `a2ef4df` | Quickstart guide for Logos Blockchain node via CLI |
| 2026-03-04 | `716a7a1` | Fix URLs formatting and update section titles |
| 2026-03-04 | `01c5b5f` | Refactor README — removed obsolete content |
| 2026-03-04 | `6c727b9` | Updated transfer native tokens guide |
| 2026-03-03 | `3bd5a62` | Content reorg for Testnet v0.1 |

---

## ideas.waku.org — Stable

- **42 ideas** confirmed (unchanged from March 14)
- No new ideas detected
- Two ideas not previously captured in our notes:
  - **2FA with Waku** — Decentralized two-factor authentication
  - **Decentralised and Censorship Resistant GitHub** — Distributed code repository

---

## Delta from March 14

| Area | Change |
|------|--------|
| docs.waku.org URL structure | **Major restructure** — `/guides/` → `/build/javascript/`, `/run-node/` |
| docs.waku.org `/learn/` | **Fixed** — previously 404, now loads |
| JS SDK guide count | **10 guides** now accessible (up from 0 accessible via direct URL) |
| `@waku/create-app` | **New** — project scaffolding tool |
| `@waku/react` | **New** — React integration package documented |
| `@waku/message-encryption` | **New** — encryption package documented |
| Linea Sepolia | RPC endpoint now references Linea Sepolia (not just Sepolia) |
| logos-co/logos-docs | No change since March 11 |
| ideas.waku.org | No change |

---

## Updated DX Assessment

### Improved
- **Quick-start path now exists:** `/build/javascript/` with `@waku/create-app` is a functional onboarding ramp
- **Learn section accessible:** Concept docs reachable via direct URL
- **Guide coverage expanded:** 10 topical guides covering common integration scenarios

### Still Problematic
- **Old URLs not redirected:** Anyone with bookmarks or shared links to `/guides/` still hits 404
- **RLN setup friction persists:** Still requires Linea Sepolia endpoint and ETH
- **Storage docs still fragmented:** Netlify subdomain, not under logos.co
- **React Native gap:** Explicitly listed as unavailable
- **logos-co/logos-docs activity low:** No commits in 4 days; consolidation pace unclear

### New Observation
The Docusaurus configuration banner visible on docs.waku.org homepage suggests possible baseUrl misconfiguration — may indicate an ongoing deployment or migration. Worth monitoring.

---

## Recommendations

1. **Update pain points:** The "broken docs links" severity should be downgraded from Critical to Medium — most content is now accessible at new URLs
2. **Test `@waku/create-app`** end-to-end as a potential quick-start recommendation
3. **File redirect issues** for old `/guides/` URLs → new `/build/javascript/` paths
4. **Monitor Linea Sepolia change** — may affect existing RLN setup instructions that reference plain Sepolia
5. **Check React Native timeline** — significant for mobile developer adoption
