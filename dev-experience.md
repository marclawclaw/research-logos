# Developer Experience

> Last updated: 2026-03-14

## Overview

The Logos developer experience is in a **transitional state** due to the late-2025 rebranding. Documentation, SDKs, and tooling are being consolidated under the Logos brand, but legacy resources (Waku, Codex, Nomos) still exist and often contain more detailed information.

---

## SDKs & Implementations

### Messaging (Waku)

| SDK | Language | Status | Notes |
|-----|----------|--------|-------|
| **nwaku** | Nim | Most mature | Reference implementation; production-used by Status |
| **js-waku** | JavaScript/TypeScript | Active development | v0.37.0 in prep (Oct 2025); React support; browser-compatible |
| **go-waku** | Go | Being phased out | Replaced by nwaku bindings in Status |

**js-waku features:**
- LightPush v3 with improved error handling
- Experimental reliable channels
- Health Indicator improvements
- RLN credentials manager
- Local development harness for browser testing
- WebRTC signaling (early development)

### Storage (Codex)

| SDK | Language | Version | Notes |
|-----|----------|---------|-------|
| **logos-storage-nim** | Nim | v0.3.0–v0.3.2 | Primary implementation |
| **logos-storage-go-bindings** | Go | v0.0.29–v0.0.30 | Go bindings |

- **REST API** at `api.codex.storage` for application integration
- CLI Installer available for testnet onboarding

### Blockchain (Nomos)

- Primary implementation in Nim/Rust
- Node quickstart guide available
- Testnet v0.1 FAQs published
- Repos: [github.com/logos-co/nomos](https://github.com/logos-co/nomos)

---

## Documentation Quality

### Current State

| Resource | URL | Assessment |
|----------|-----|------------|
| Logos main docs | [docs at build.logos.co](https://build.logos.co) | New; consolidating |
| Waku docs | [docs.waku.org](https://docs.waku.org) | **404 on overview page** (March 2026) |
| Codex docs | [docs.codex.storage](https://docs.codex.storage) | Includes whitepaper; decent |
| Nomos docs | [nomos.tech/about/architect](https://nomos.tech/about/architect) | Redirects to logos.co |
| RFC/Specs | [lip.logos.co](https://lip.logos.co) | Comprehensive protocol specs |
| Research forum | [forum.research.logos.co](https://forum.research.logos.co) | Active discussions |

### Documentation Issues
1. **URL rot in progress:** Old URLs (waku.org, codex.storage, nomos.tech, vac.dev) redirect but intermediate pages may 404
2. **Terminology inconsistency:** Old and new names used interchangeably across resources
3. **Fragmentation:** Documentation spread across build.logos.co, docs.waku.org, docs.codex.storage, lip.logos.co, roadmap.logos.co
4. **2026 plan:** Unified developer documentation is planned "in phases aligned with project milestones"

---

## Developer Entry Points

### Builder Hub ([build.logos.co](https://build.logos.co))
Central developer portal offering:
- **Logos Basecamp** — Complete distribution with wallet, chat, file-sharing, explorer
- **RFPs** — Funded project opportunities
- **Demo apps** — Atomic Swaps, Multisig wallet
- **Community ideas** — Project proposals
- **Office hours** — Direct access to core contributors

### Getting Started Path
1. Visit [build.logos.co](https://build.logos.co)
2. Install Logos Basecamp from GitHub releases
3. Review Logos Docs for architecture overview
4. Run a node via Node Quickstart Guide
5. Explore RFPs or community ideas for project opportunities
6. Schedule office hours for technical guidance

---

## Tooling

### Development Tools
- **Logos Basecamp** — Full development distribution
- **CLI Installer** — Streamlined testnet onboarding (Codex)
- **Local dev harness** — Browser testing for js-waku
- **Nim tooling** — Maintained by Vac: compiler, Nimble (with SAT solver), nim-suggest, VSCode extension

### Testing Infrastructure
- **Vac QA** — Interoperability testing framework for all major Waku protocols
- **Vac DST** — Distributed systems testing at scale (thousands of nodes)
- **Certora** — Formal verification for smart contracts

### Specifications
- **LIP (Logos Improvement Proposals)** — Formerly Vac RFCs, at [lip.logos.co](https://lip.logos.co)
- Protocol specifications for all Waku protocols
- Consensus-oriented specification methodology

---

## Integration Patterns

### Messaging Integration
```
Application → js-waku SDK → LightPush → Relay Network → Store (for offline)
```
- Use LightPush for resource-constrained devices (browsers, mobile)
- Use Filter to subscribe to specific content topics
- Use Store for message history retrieval

### Storage Integration
```
Application → REST API (api.codex.storage) → Codex Node → P2P Network
```
- Upload via `/data` endpoint
- Receive CID (Content Identifier)
- For persistence: erasure coding + marketplace allocation

---

## GitHub Organizations

| Org | Purpose | Note |
|-----|---------|------|
| [github.com/logos-co](https://github.com/logos-co) | Main Logos org | Primary |
| [github.com/waku-org](https://github.com/waku-org) | Waku/Messaging | May be migrating to logos-messaging |
| [github.com/codex-storage](https://github.com/codex-storage) | Codex/Storage | May be migrating |
| [github.com/logos-blockchain](https://github.com/logos-blockchain) | Blockchain | Newer org |
| [github.com/logos-messaging](https://github.com/logos-messaging) | Messaging | Newer org |
| [github.com/vacp2p](https://github.com/vacp2p) | Vac/Research | May be migrating |

> **Warning:** Repository migration is in progress. Check both old and new org names when looking for repos.

---

## Analysis

### Strengths
- **Builder Hub** is a solid developer entry point
- **Office hours** with core contributors is excellent for a pre-mainnet project
- **RFC/specification culture** ensures protocol interoperability
- **js-waku** provides accessible browser integration for web developers
- **Formal verification** (Certora) for smart contracts shows security commitment

### Concerns
- **Documentation in flux:** The rebranding has created significant URL rot and terminology confusion
- **Nim barrier:** Primary implementations in Nim limit the contributor pool
- **Multiple GitHub orgs:** Confusing for newcomers; unclear which repos are canonical
- **Pre-production:** Most SDKs are pre-v1.0; APIs are still evolving
- **No unified API reference:** Developer reference docs are fragmented across projects

### Recommendations for Improvement
1. Prioritize the unified documentation consolidation planned for 2026
2. Create clear migration guides from old to new URLs/orgs
3. Provide more language bindings beyond Nim (Rust, Go, TypeScript)
4. Build a single, comprehensive API reference site
5. Expand the RFP program significantly to attract ecosystem builders

### Key Observation
> **Notable:** The developer experience is currently the weakest aspect of the Logos ecosystem. This is expected for a pre-mainnet project undergoing rebranding, but it represents a significant barrier to adoption. The planned 2026 documentation consolidation is critical.
