# Research Queue — Logos Ecosystem

Each cron-triggered researcher session pops the next PENDING topic, researches it thoroughly, marks it DONE, and commits.

## Queue

| Priority | Topic | Status | Notes |
|----------|-------|--------|-------|
| 1 | Waku — core protocol (relay, store, filter, lightpush) | PENDING | Start: github.com/waku-org, docs.waku.org |
| 2 | Waku — RLN rate limiting & privacy | PENDING | VAC research papers, forum.vac.dev |
| 3 | Codex — storage architecture & erasure coding | PENDING | github.com/codex-storage |
| 4 | Codex — marketplace & economics | PENDING | github.com/codex-storage, blog posts |
| 5 | Nomos — consensus & blockchain | PENDING | github.com/logos-co/nomos-node |
| 6 | Logos — ecosystem overview & vision | PENDING | logos.co, blog, announcements |
| 7 | Use cases — apps building on Logos stack | PENDING | forum.vac.dev, github search, status.im |
| 8 | Competitors — libp2p, IPFS, Filecoin | PENDING | docs, comparisons, community discussion |
| 9 | Competitors — Matrix, Nostr, Farcaster | PENDING | protocol comparisons |
| 10 | Developer experience — SDK quality & pain points | PENDING | GitHub issues, forums, developer feedback |
| 11 | Community — active projects & contributors | PENDING | GitHub activity, forum threads |
| 12 | VAC research — latest papers & RFCs | PENDING | vac.dev/research, forum.vac.dev |

## Completed

_(none yet)_

## Instructions for researcher sessions

1. Find the first PENDING topic in this table
2. Change its status to IN_PROGRESS and commit
3. Research it thoroughly — crawl all listed sources plus anything you find
4. Write atomic notes to `research/logos/<topic-slug>/`
5. Update `_index.md` for that folder
6. Change status to DONE with a brief summary
7. Commit everything and push
8. Exit — the next cron trigger will pick up the next topic
