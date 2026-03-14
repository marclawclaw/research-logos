# logos-co/logos-docs Analysis

> Source: https://github.com/logos-co/logos-docs  
> Researched: 2026-03-14

## Repo Purpose

The `logos-docs` repo is the **single source of truth** for building on the unified Logos stack. It consolidates previously fragmented documentation from Nomos, Codex, and Waku into one coherent developer experience.

## Unified Naming (Rebranding in Progress)

| Old Name | New Name | Domain |
|----------|----------|--------|
| Waku | Logos Messaging | P2P communication |
| Codex | Logos Storage | Decentralized storage |
| Nomos | Logos Blockchain | Consensus + compute |

> Legacy names still appear in repos and specs; docs-first terminology will use new names going forward.

## Stack Architecture

```
┌──────────────────────────────────────────────────┐
│              dApps / Applications                 │
├───────────────┬──────────────┬───────────────────┤
│  Blockchain   │  Messaging   │     Storage        │
│ (Logos Chain) │  (Waku)      │   (Codex)          │
├───────────────┴──────────────┴───────────────────┤
│           Discovery / Peering / Mix-net           │
│                  AnonComms                         │
├──────────────────────────────────────────────────┤
│                 Logos Kernel                       │
└──────────────────────────────────────────────────┘
```

Also includes **User Modules** (wallet, identity, access control, key management).

## Available Developer Journeys (as of March 2026)

### Logos App
- Build from source using **Nix** (dependency manager)
- Access Testnet v0.1 UIs

### Execution Zone (Blockchain)
- Set up wallet for Logos Execution Zone
- Transfer native tokens
- Create and transfer custom tokens
- Create and use AMM liquidity pools

### Blockchain Node
- Start a node via CLI
- Quickstart guide

### Storage (Logos Storage / Codex)
- Use Storage Module API from an app — via `logos-storage-docs.netlify.app`
- Store/retrieve files via Simple Filesharing App
- Storage tutorials hosted on Netlify (not in the main docs repo)

### Messaging (Logos Messaging / Waku)
- Use **Logos Delivery Module API** from an app
- Use **Logos Chat Module API** from an app
- These are the new names for the underlying Waku APIs

### AnonComms
- Discover nodes and send messages via Mixnet demo app
- Privacy-focused: metadata anonymity layer

## DX Observations

### Strengths
- **Journey-based documentation** — "do X from an app" framing is developer-friendly
- **Unified entry point** — single repo covers the full stack
- **Honest status communication** — README acknowledges consolidation is ongoing
- **DX intent is clear** — "reduce cognitive load" is explicitly stated as a goal

### Weaknesses

1. **Nix requirement for Logos App** — Nix is unfamiliar to most web/mobile developers; high friction barrier
2. **Netlify for Storage docs** — `logos-storage-docs.netlify.app` is separate from the main docs; fragmentation persists
3. **"In phases" timeline** — Operator/developer guides promised for 2026 but no specific dates
4. **Legacy names everywhere** — logos-co/logos-docs is the goal, but most linked resources still use Waku/Codex/Nomos branding
5. **No API reference** — All docs are journey-based; no generated API reference linked
6. **Issues-as-support** — "If you get stuck, open an issue" is the official support path; no forum or Discord linked from the README

## Key Insight: Documentation Gap vs. Technology Gap

The Logos stack is technically functional (Testnet v0.1 live, Execution Zone working, Waku Network active). The DX gap is primarily **documentation and onboarding**, not missing features. This means:

- A developer who finds the right resources CAN build
- The **discoverability** and **coherence** of those resources is the bottleneck
- The 2026 documentation consolidation is the most impactful DX improvement underway

## What to Build on Today

If building a PoC on Logos right now, the most mature/accessible entry points are:

1. **Messaging (Waku)** via `js-waku` — best docs, active community, browser-ready
2. **Storage (Codex)** via REST API at `api.codex.storage` — simple HTTP, no SDK required
3. **Blockchain** via Execution Zone wallet + CLI node — testnet working, AMM/token guides available
