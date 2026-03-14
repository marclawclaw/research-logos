# Logos Ecosystem — Quick Reference Card

> Last updated: 2026-03-14

## Stack at a Glance

| Component | Former Name | What It Does | Status |
|-----------|------------|--------------|--------|
| **Blockchain** | Nomos | Consensus, execution, settlement | Testnet March 2026; Mainnet early 2027 |
| **Messaging** | Waku | P2P censorship-resistant communication | Most mature; used by Status |
| **Storage** | Codex | Decentralized durable file storage | Testnet paused; refocusing |
| **Nescience** | — | ZK privacy layer (research) | R&D phase |
| **Vac/Research** | Vac | R&D arm (9 service units) | Active |

---

## Key URLs

| Resource | URL |
|----------|-----|
| Main site | [logos.co](https://logos.co) |
| Tech stack | [logos.co/tech-stack](https://logos.co/tech-stack) |
| Builder Hub | [build.logos.co](https://build.logos.co) |
| Research | [research.logos.co](https://research.logos.co) |
| Roadmap | [roadmap.logos.co](https://roadmap.logos.co) |
| Specifications | [lip.logos.co](https://lip.logos.co) |
| Blog / Press | [press.logos.co](https://press.logos.co) |
| Forum | [forum.logos.co](https://forum.logos.co) |
| Research Forum | [forum.research.logos.co](https://forum.research.logos.co) |
| IFT (parent) | [free.technology](https://free.technology) |
| IFT News | [news.free.technology](https://news.free.technology) |

## Blogs (Legacy, Still Active)

| Blog | URL |
|------|-----|
| Waku/Messaging | [blog.waku.org](https://blog.waku.org) |
| Codex/Storage | [blog.codex.storage](https://blog.codex.storage) |
| Nomos/Blockchain | [blog.nomos.tech](https://blog.nomos.tech) |

---

## GitHub Organizations

| Org | Purpose |
|-----|---------|
| [logos-co](https://github.com/logos-co) | Main Logos org |
| [logos-blockchain](https://github.com/logos-blockchain) | Blockchain (new) |
| [logos-messaging](https://github.com/logos-messaging) | Messaging (new) |
| [waku-org](https://github.com/waku-org) | Waku (legacy) |
| [codex-storage](https://github.com/codex-storage) | Codex (legacy) |
| [vacp2p](https://github.com/vacp2p) | Vac/Research (legacy) |

---

## Key People

| Person | Role |
|--------|------|
| Jarrad Hope | IFT Co-founder |
| Carl Bennetts | IFT Co-founder |
| Dr. Corey Petty | Logos Programme Lead |
| Franck Royer | Waku/Messaging Lead |

---

## Key Protocols (Messaging/Waku)

| Protocol | RFC | Purpose |
|----------|-----|---------|
| Relay | 11/WAKU2-RELAY | Core pub/sub via GossipSub |
| Store | 13/WAKU2-STORE | Historical message retrieval |
| Filter | 12/WAKU2-FILTER | Bandwidth-efficient filtering |
| LightPush | 19/WAKU2-LIGHTPUSH | Publishing for light nodes |
| RLN | 17/WAKU2-RLN-RELAY | ZK spam protection |
| DiscV5 | 33/WAKU2-DISCV5 | Peer discovery |

---

## Key Technical Concepts

| Concept | Component | What It Is |
|---------|-----------|------------|
| **Cryptarchia** | Blockchain | Private PoS consensus with ZK leader election |
| **Sovereign Zones** | Blockchain | App-specific chains on Bedrock |
| **LSSA** | Blockchain | Dual public/private state execution |
| **Blend Network** | Blockchain | Traffic analysis resistant networking |
| **RLN** | Messaging | ZK-based rate limiting (no accounts needed) |
| **Erasure Coding** | Storage | Data durability via parity blocks |
| **Lazy Repair** | Storage | On-demand data re-encoding |
| **Poseidon2** | Storage | ZK-friendly hash for data proofs |

---

## SDKs

| SDK | Language | Component |
|-----|----------|-----------|
| nwaku | Nim | Messaging (reference impl) |
| js-waku | JS/TS | Messaging (browser/Node) |
| go-waku | Go | Messaging (being phased out) |
| logos-storage-nim | Nim | Storage |
| logos-storage-go-bindings | Go | Storage |

---

## Community

| Channel | Link |
|---------|------|
| Discord | [discord.com/invite/logosnetwork](https://discord.com/invite/logosnetwork) |
| X (Twitter) | [@Logos_network](https://x.com/Logos_network) |
| YouTube | [@LogosNetwork](https://youtube.com/@LogosNetwork) |
| Events | [luma.com/logosevents](https://luma.com/logosevents) |

---

## Timeline

| Date | Event |
|------|-------|
| 2017 | Status founded |
| 2022 | Logos founded |
| 2023 | IFT established; Logos public launch |
| Late 2025 | Brand unification (Nomos/Waku/Codex → Logos) |
| March 2026 | First public blockchain testnet |
| June 2026 | Second testnet iteration |
| Early 2027 | Mainnet launch target |

---

## Vac Research Service Units

P2P · Token Economics · DST · QA · Smart Contracts · Nim · Applied Crypto & ZK · RFC · Security
