#!/usr/bin/env python3
"""Run researcher agent for logos.co ecosystem research."""
import subprocess, sys

researcher_soul = open("/home/marclaw/.openclaw/workspace/agents/researcher/soul.md").read()

prompt = f"""{researcher_soul}

---

## Task: Deep Research — Logos Ecosystem

You have been given 72 hours to research the Logos ecosystem as thoroughly as possible.

### Scope
Research and document everything you can find on:

1. **Logos** (logos.co) — mission, roadmap, governance, funding, team
2. **Waku** — messaging protocol, architecture, RLN, light push, store, relay, SDK, js-waku, nwaku
3. **Codex** — decentralized storage, architecture, erasure coding, marketplace, status
4. **Nomos** — blockchain layer, consensus, architecture, status
5. **Nescience** — privacy layer, ZK proofs, what it is, current state
6. **Vac** — research arm, what they work on, published papers, DST simulations, QA
7. **IFT (Institute of Free Technology)** — parent org, structure, relationship to Logos components
8. **Use cases** — what applications are being built on Logos stack, RFPs, Lambda prizes
9. **Developer experience** — SDKs, docs quality, tooling, integration patterns
10. **Competitive landscape** — how Logos stack compares to alternatives (libp2p, IPFS, Ethereum L2s, etc.)

### Sources to crawl
- https://logos.co
- https://waku.org
- https://docs.waku.org
- https://codex.storage
- https://nomos.tech
- https://vac.dev
- https://roadmap.logos.co
- https://github.com/waku-org
- https://github.com/codex-storage
- https://github.com/logos-co
- https://github.com/vacp2p
- https://forum.vac.dev (if accessible)
- https://discuss.status.im (Logos-related threads)
- Any RFP or Lambda prize pages you find

### Output structure
Create the following files in this repo:

- `README.md` — overview and index of all research
- `logos-overview.md` — Logos mission, structure, roadmap
- `waku.md` — Waku deep dive
- `codex.md` — Codex deep dive
- `nomos.md` — Nomos deep dive
- `nescience.md` — Nescience deep dive
- `vac.md` — Vac research arm overview
- `use-cases.md` — applications, RFPs, Lambda prizes
- `dev-experience.md` — SDK quality, docs, tooling
- `competitive.md` — comparison with alternatives
- `quickref.md` — quick reference card (key APIs, repos, contacts)

### Rules
- Cite every claim with a URL
- Flag if a source is outdated (>6 months old)
- Separate facts from your analysis
- Commit after each major section is complete
- If you find something surprising or important, note it prominently

When completely finished, run:
openclaw system event --text "Research done: logos.co ecosystem fully documented" --mode now
"""

result = subprocess.run(
    ["/home/marclaw/.local/bin/claude",
     "--permission-mode", "bypassPermissions", "--print", prompt],
    cwd="/home/marclaw/src/marclawclaw/research-logos",
    capture_output=False
)
sys.exit(result.returncode)
