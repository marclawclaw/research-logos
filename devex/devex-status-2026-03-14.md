# Logos DX Status Snapshot — 2026-03-14

> Verification run: Saturday, 2026-03-14 @ 14:30 AEST  
> Sources checked: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org

## docs.waku.org — Link Health Check

| URL | Status | Notes |
|-----|--------|-------|
| `/` (homepage) | ✅ 200 | Loads correctly |
| `/learn/concepts/protocols` | ✅ 200 | Protocol docs intact |
| `/learn/waku-network` | ❌ 404 | Broken |
| `/guides/` | ❌ 404 | Broken |
| `/guides/js-waku/` | ❌ 404 | Broken |
| `/guides/js-waku/light-send-receive` | ❌ 404 | Broken |
| `/guides/nwaku/run-node` | ❌ 404 | Broken |
| `/guides/getting-started` | ❌ 404 | Broken |

**Verdict:** The 404 epidemic on docs.waku.org is confirmed and unchanged. All `guides/` and most `learn/` sub-pages are inaccessible via direct URL. Only the root and `/learn/concepts/protocols` are confirmed working.

---

## logos-co/logos-docs — Repo Activity

- **Last commit:** 2026-03-11 by `chair28980`
  - Message: "remove erroneous line for node running from logos app section"
  - Minor fix — removed an incorrect line in the Logos App build guide
- **Activity level:** Low (1 commit in the last 3 days)
- **Structure:** Unchanged from prior analysis — journey-based docs, Nix required for full app, Storage docs still on Netlify

### Confirmed Working Journeys (from README, March 14):
- Build Logos App from source (Nix)
- Wallet setup for Logos Execution Zone
- Transfer native/custom tokens
- AMM liquidity pool (Execution Zone)
- Start Logos blockchain node via CLI
- Use Logos Storage module API (via logos-storage-docs.netlify.app)
- Simple Filesharing App (Storage demo)
- Use Logos Delivery Module API (messaging, formerly Waku)
- Use Logos Chat Module API (chat, formerly js-waku Chat API)
- AnonComms Mixnet demo app

---

## ideas.waku.org — Content Verified

All 40+ ideas confirmed present. Key categories:
- Governance/Voting, Marketplace/DeFi, Gaming, IoT, Infrastructure, Collaboration, Identity/Privacy

Top ideas for Franck's PoC work (highlighted in `ideas-and-use-cases.md`):
- Privacy-preserving AI assistant
- Decentralized Push Notifications (replace Apple/Google)
- API Generator from OpenAPI spec
- Privacy-preserving governance (ZK + Waku)
- Federated Learning Platform

---

## Delta from Previous Research

**No major changes since the initial DX deep-dive (earlier today).**

- 404 issues on docs.waku.org: **still present** — no signs of fix
- logos-co/logos-docs: 1 minor commit (typo/error removal), no structural changes
- ideas.waku.org: stable content, community-maintained

---

## Open Questions / Things to Watch

1. **Will docs.waku.org fix the 404s?** The pattern suggests a broken Docusaurus routing or missing build artifact — could be resolved anytime.
2. **Logos Storage docs domain** — still on Netlify subdomain, not migrated to logos.co
3. **Logos Delivery Module API journey** — links to GitHub markdown, not a rendered docs page. Usability unclear without testing the actual guide.
4. **RLN testnet status** — Sepolia-based RLN membership registration still required; no "hosted/managed RLN" option announced.

---

## Recommendation for Next Steps

1. **Try the Logos Delivery Module API journey end-to-end** — actually attempt the GitHub markdown guide and log friction points
2. **Check if logos-storage-docs.netlify.app is still accessible** and document what's there
3. **Monitor logos-co/logos-docs** for the anticipated "operator/developer guides for 2026" timeline
4. **Open issues** on waku-org/docs repo for the broken guide routes (if not already filed)
