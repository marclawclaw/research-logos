# Logos DX Pain Points & Improvement Opportunities

> Last updated: 2026-03-14  
> Synthesized from: docs.waku.org, logos-co/logos-docs, ideas.waku.org

## Summary

The Logos stack is technically functional as of March 2026 (Testnet v0.1 live). The primary friction is **documentation and onboarding quality**, not missing functionality. The ongoing rebranding from Waku/Codex/Nomos to unified Logos naming adds temporary confusion.

---

## Critical Pain Points

### 1. Broken Documentation Links
**Severity: High**

Multiple `docs.waku.org` sub-pages return 404:
- `/guides/` → 404
- `/learn/concepts/` → 404
- `/learn/concepts/sdk` → 404
- `/learn/waku-network` → 404

The homepage works, but navigating deeper breaks. Developers who share or bookmark specific URLs hit dead ends. This is the #1 discoverability issue.

**Opportunity:** Open issues on waku-org/docs repo for each broken URL. Simple redirect fixes or content migration would resolve these.

---

### 2. Terminology Confusion from Rebranding
**Severity: High**

- `js-waku` is being called "Logos Delivery Module" / "Logos Chat Module" in new docs
- `Codex` → `Logos Storage` but all existing tutorials say Codex
- `Nomos` → `Logos Blockchain` but GitHub orgs haven't migrated
- npm packages, Docker images, GitHub repos still use old names
- Developers reading old tutorials then looking at new docs face constant mismatch

**Opportunity:** A migration/alias guide ("If you see X, it means Y now") would dramatically reduce confusion.

---

### 3. RLN On-chain Setup Friction
**Severity: Medium**

To use the public Waku Network:
- Need Ethereum Sepolia endpoint
- Need Sepolia ETH wallet
- Need to register RLN membership on-chain

This is Ethereum-native developer knowledge. For web developers building on Waku as a messaging layer, this is unexpected complexity. Many tutorials are on GitHub (not the docs site).

**Opportunity:** Faucet + Infura setup guide embedded directly in the getting-started flow. Or offer a "hosted RLN" option for testnet development.

---

### 4. No Unified Quick-Start
**Severity: Medium**

There's no accessible 5-minute "hello world" path that works today:
- `docs.waku.org/guides/` is 404
- `logos-co/logos-docs` points to Nix build for the full app (heavy)
- `js-waku` quick starts are buried in GitHub

**Opportunity:** A single working CodeSandbox/StackBlitz example for js-waku would convert curious developers into active users.

---

### 5. Storage Docs Fragmentation
**Severity: Medium**

- Storage tutorials live on `logos-storage-docs.netlify.app` (not on a stable domain)
- REST API docs not linked from the main `logos-co/logos-docs` clearly
- Netlify subdomain suggests it's not officially maintained

**Opportunity:** Mirror/redirect storage docs under `docs.logos.co` with a stable URL.

---

### 6. Nim Dominance
**Severity: Low-Medium**

- nwaku (Nim) is the reference implementation
- Logos App requires Nix to build
- Nim is unfamiliar to the vast majority of web/mobile developers

**Opportunity:** Nim isn't going away, but ensuring all developer-facing APIs have good bindings in TypeScript/Go/Rust reduces this barrier significantly. `js-waku` already does this for messaging.

---

### 7. Multiple GitHub Organizations
**Severity: Low**

Active repos spread across:
- `github.com/logos-co`
- `github.com/waku-org`
- `github.com/codex-storage`
- `github.com/logos-blockchain`
- `github.com/logos-messaging`
- `github.com/vacp2p`

Unclear which is canonical; migration is in progress but creates confusion.

**Opportunity:** `logos-co` should be the obvious single home. Clear "canonical org" notice on all migrating repos.

---

## What's Working Well

| Strength | Details |
|----------|---------|
| **Builder Hub** | build.logos.co is a solid developer portal with RFPs, demos, office hours |
| **Office hours** | Direct access to core contributors — excellent for pre-mainnet |
| **Waku protocol docs** | Protocol concepts clearly explained with trade-off analysis |
| **LIP specs** | lip.logos.co has comprehensive protocol specifications |
| **Idea board** | ideas.waku.org is a genuinely useful inspiration resource |
| **Execution Zone** | Working testnet with AMM, tokens, wallet guides available |
| **REST API first** | Storage module accessible via simple HTTP (api.codex.storage) |

---

## Recommended Priority Fixes (for Logos DX Team)

1. **Fix docs.waku.org broken routes** — low effort, high impact
2. **Publish a terminology migration guide** — Waku/Codex/Nomos → Logos naming
3. **Create a working 5-min quick-start** (StackBlitz or CodeSandbox for js-waku)
4. **Inline RLN setup** into a working tutorial (not GitHub links)
5. **Move Storage docs to stable domain** under logos.co
6. **Consolidate GitHub org navigation** — redirect notices + canonical org statement

---

## Opportunity for Franck

The most actionable PoC to demonstrate Logos DX issues:
1. **Attempt a fresh "new developer" onboarding** and document every friction point
2. Open issues or PRs on `logos-co/logos-docs` for each blocker
3. Build a minimal working example (js-waku + Codex REST) as a reference — this would be valuable to the ecosystem
