# Logos DX — Status 2026-03-16 (12:30 AEST)

> Sources: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org
> Run type: Overnight/Early morning check

## Summary

Three new ideas appeared on ideas.waku.org (44 → 47) since yesterday's midday check. The docs.waku.org Build/JavaScript section now lists 11 guides (previously 10), with a new "Set Up a Local Development Environment" page. The logos-co/logos-docs repo remains dormant — no commits since 2026-03-11 and 10 open issues/PRs, several going stale.

## docs.waku.org

**One new guide detected in Build/JavaScript section.**

- **Build/JavaScript** — now **11 guides** (was 10 at midday 2026-03-15):
  1. Send and Receive Messages in a Reliable Channel
  2. Send and Receive Messages Using Light Push and Filter
  3. Retrieve Messages Using Store Protocol
  4. Encrypt, Decrypt, and Sign Your Messages
  5. Build React DApps Using @waku/react
  6. Scaffold DApps Using @waku/create-app
  7. **Set Up a Local Development Environment** ← NEW
  8. Bootstrap Nodes and Discover Peers
  9. Run @waku/sdk in a NodeJS Application
  10. Debug Your Waku DApp and WebSocket
  11. Manage Your Filter Subscriptions

- **Run Node** — unchanged. Docker Compose primary method, 2GB RAM recommendation, Linea Sepolia RPC, Grafana dashboard. A "Waku Node Operator Cheatsheet" PDF is available.
- **Learn** — same 5 concept categories (Protocols, Content Topics, Network Domains, Transports, Peer Discovery) plus Security Features, Research, Waku vs libp2p, Glossary, FAQ. No new pages.
- **Homepage** — unchanged. Build / Run Node / Learn nav, 8 use cases, case studies (The Graph, Railgun).
- **Old `/guides/` URLs** — still 404, no redirects in place.
- React Native still listed as "NOT compatible" with future support planned.

## logos-co/logos-docs

**No new commits.** Last commit remains `91a65d9` (2026-03-11) — "remove erroneous line for node running from logos app section." Now 5 days without activity.

**Open Issues/PRs (10 total):**

| # | Type | Title | Opened |
|---|------|-------|--------|
| 186 | PR | Tutorial: Building modules for Logos Core | 2026-02-24 |
| 185 | Issue | Tutorial: Building modules for Logos Core | 2026-02-24 |
| 184 | PR | Dk/node cli journey | 2026-02-23 |
| 183 | PR | Blockchain Node Journey | 2026-02-19 |
| 182 | PR | fix(LEZ): update references to LSSA, rename to LEZ | 2026-02-19 |
| 181 | PR | Enhance quickstart template with more descriptive steps | 2026-02-16 |
| 177 | Issue | Improve Quickstart template for more descriptive steps | 2026-02-13 |
| 170 | PR | Set doc packet as pull request template | 2026-02-10 |
| 169 | Issue | Set doc packet as pull request template | 2026-02-09 |
| 166 | PR | feat: initial documentation for Logos Storage | 2026-02-03 |

Notable: 6 PRs open, oldest from Feb 3. Several appear stale (no merges in 2+ weeks). The Logos Storage docs PR (#166) has been open for 6 weeks.

## ideas.waku.org

**Count change: 44 → 47 ideas** (+3 since midday 2026-03-15)

Categories span gaming, privacy/security, infrastructure, marketplaces, governance/DAOs, health, decentralisation, communication, and AI/data. The 3 new ideas could not be individually identified by title (no timestamps on the page), but the total count is confirmed at 47.

Previously captured ideas (privacy-preserving governance platform, privacy-preserving APIs, 2FA with Waku, Decentralised GitHub, brainstorming tool, confessions board) all remain present.

## DX Pain Points Update

| Pain Point | Yesterday Status | Today Status |
|------------|-----------------|--------------|
| Old `/guides/` URLs return 404 | No redirects | **Unchanged** |
| RLN setup requires Linea Sepolia ETH | Active friction | **Unchanged** |
| Storage docs on separate Netlify domain | Fragmented | **Unchanged** |
| React Native unavailable | Documented gap | **Unchanged** |
| logos-docs repo activity low | No commits since Mar 11 (4d) | **Unchanged** (now 5 days) |
| Stale PRs in logos-docs | Not tracked | **NEW** — 6 open PRs, oldest 6 weeks |
| New local dev setup guide | Not available | **Improved** — new guide added |

## Action Items

1. **Review new "Set Up a Local Development Environment" guide** — verify it works end-to-end and check whether it addresses the RLN/Linea Sepolia friction point.
2. **Flag stale logos-docs PRs** — PR #166 (Logos Storage docs) open 6 weeks; PRs #183/#184 (blockchain/node CLI journeys) open nearly a month. These would improve DX if merged.
3. **File `/guides/` redirect issue** — still no redirects; old links from blog posts and tutorials remain broken.
4. **Track ideas.waku.org growth** — 3 new ideas in ~12 hours; community is actively contributing.
5. **Investigate React Native timeline** — still listed as not compatible; no visible progress indicators.
6. **Monitor logos-docs for merge activity** — several PRs appear review-ready but unmoved.
