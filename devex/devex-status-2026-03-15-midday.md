# Logos DX — Midday Check 2026-03-15 (12:30 AEST)

> Sources: docs.waku.org, github.com/logos-co/logos-docs, ideas.waku.org
> Run type: Midday verification (second run today)

## Summary

Minor delta from the morning run. The docs.waku.org site structure remains stable after the morning-detected navigation restructure. No new commits to logos-co/logos-docs. The ideas.waku.org board now shows **44 ideas** (up from 42 in the morning snapshot), with 2 new entries detected.

## docs.waku.org

**No changes detected since morning run.** All sections verified:

- **Homepage** — Same structure: Build / Run Node / Learn navigation. Hero section, use cases (8), case studies (The Graph, Railgun) all unchanged. No new banners or announcements.
- **`/build/javascript/`** — Same 10 guides as morning: Reliable Channels, Light Push & Filter, Store Protocol, Message Encryption, React Integration, Project Scaffolding, Node Discovery, NodeJS Usage, Debugging, Filter Management. React Native still listed as "NOT compatible" with future support planned.
- **`/run-node/`** — Unchanged. Docker Compose primary method, 2GB RAM recommendation, Linea Sepolia RPC, Grafana dashboard, health endpoint all as documented this morning.
- **`/learn/`** — Same 5 concept categories (Protocols, Content Topics, Network Domains, Transports, Peer Discovery) plus Security Features, Research, Waku vs libp2p, Glossary, FAQ. No new pages.

**Old `/guides/` URLs** — Still no redirects in place (confirmed broken).

## logos-co/logos-docs

**No new commits.** Last commit remains `91a65d9` (2026-03-11) — "remove erroneous line for node running from logos app section." No activity in 4 days.

## ideas.waku.org

**Count change: 42 → 44 ideas** (+2 since morning run)

New ideas detected (positioned at end of list):
1. **Privacy preserving governance platform** — governance tooling using Waku for private voting/deliberation
2. **Privacy preserving APIs and Data sources** — privacy layer for API interactions

Previously captured ideas (2FA with Waku, Decentralised GitHub, brainstorming tool, confessions board) remain present.

## DX Pain Points Update

| Pain Point | Morning Status | Midday Status |
|------------|---------------|---------------|
| Old `/guides/` URLs return 404 | Medium — no redirects | **Unchanged** |
| RLN setup requires Linea Sepolia ETH | Active friction | **Unchanged** |
| Storage docs on separate Netlify domain | Fragmented | **Unchanged** |
| React Native unavailable | Documented gap | **Unchanged** |
| logos-docs repo activity low | No commits since Mar 11 | **Unchanged** (4 days) |

No pain points resolved or newly introduced since the morning run.

## Action Items

1. **Track ideas.waku.org growth** — 2 new ideas since morning; community is actively contributing. Worth monitoring for DX-relevant proposals.
2. **Carry forward morning recommendations** — `@waku/create-app` end-to-end testing, `/guides/` redirect filing, React Native timeline inquiry all still pending.
3. **No urgent changes** — docs.waku.org structure appears stable post-restructure; no regressions detected.
