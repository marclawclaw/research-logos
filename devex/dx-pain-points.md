# Logos DX Pain Points & Improvement Opportunities

> Last updated: 2026-03-15
> Synthesized from: docs.waku.org, logos-co/logos-docs, ideas.waku.org

## Summary

The Logos stack is technically functional as of March 2026 (Testnet v0.1 live). The primary friction is **documentation and onboarding quality**, not missing functionality. The ongoing rebranding from Waku/Codex/Nomos to unified Logos naming adds temporary confusion.

---

## Critical Pain Points

### 1. Broken Documentation Links (Partially Resolved)
**Severity: Medium** *(downgraded from High on 2026-03-15)*

**Update 2026-03-15:** docs.waku.org has restructured its URL layout. Most content is now accessible:
- `/build/javascript/` → ✅ replaces old `/guides/` (10 guides now available)
- `/run-node/` → ✅ replaces old `/guides/nwaku/run-node`
- `/learn/` → ✅ now loads (previously 404)

**Still broken:**
- Old `/guides/*` URLs → 404 (no redirects to new paths)
- Direct links shared before March 2026 still fail

**Opportunity:** Set up 301 redirects from old `/guides/` paths to new `/build/javascript/` equivalents. The content exists — it's a routing/redirect issue now, not missing content.

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

### 4. Quick-Start Path (Improved but Still Fragmented)
**Severity: Low-Medium** *(downgraded from Medium on 2026-03-15)*

**Update 2026-03-15:** A quick-start path now exists via `@waku/create-app` (project scaffolding CLI) documented at `docs.waku.org/build/javascript/`. This is a significant improvement.

**Remaining issues:**
- `logos-co/logos-docs` still points to Nix build for the full Logos App (heavy)
- The Waku quick-start and Logos quick-start are separate experiences
- `@waku/create-app` needs end-to-end testing to confirm it works smoothly

**Opportunity:** Link `@waku/create-app` from the logos-co/logos-docs README as the recommended messaging quick-start. A CodeSandbox/StackBlitz demo would still add value.

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
