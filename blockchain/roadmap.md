# Logos Blockchain — Roadmap & Milestones

> Last updated: 2026-03-14
> Source: blog.nomos.tech/2025-year-in-review

## 2025 — Completed Milestones

| Date | Milestone |
|------|-----------|
| Jan 2025 | Cryptarchia research refinement; anonymity failure probability modelling |
| Feb 2025 | Mantle specification work begins; Blend economic incentives + deanonymisation calculator |
| Mar 2025 | Key network optimisations; Cryptarchia research pushed forward |
| **Apr 2025** | **Croatia offsite: Sovereign Zone prototypes demonstrated** (including zkEVM rollup with LC verification) |
| May 2025 | New whitepaper; use cases developed |
| **Jun 2025** | **Mantle specification finalized**; Mantle Channels introduced; Blend Protocol design locked |
| Jun–Jul 2025 | Many components finalised and integrated |
| **Aug 2025** | **Complete architecture crystallisation — all design details settled**; full spec set finalised; tokenomics framework + block rewards complete |
| Sep 2025 | Blend: Proof of Quota + Proof of Selection integrated; session transition logic improved |
| Oct 2025 | Service participation rewards fully implemented in ledger; service membership moved into ledger; SDP near-complete; Mantle invalid tx handling added |
| Nov 2025 | Cryptography audit (DA) completed; Blend audit started; Poseidon2 cuts proving time 50%; SDP garbage collection + SRDP logic merged; real mempool replaces mock; ZkSign keys deployed |
| **Dec 2025** | **Spain offsite: LSSA sequencer prototype; final blockchain challenges resolved** |

---

## 2026 — Planned

| Target | Milestone |
|--------|-----------|
| **March 2026** | **First public testnet** — working prototype of full Logos stack; community stress-testing |
| **June 2026** | **Second testnet** — fixes from first testnet; improved network resilience |
| Q4 2026 | Final mainnet preparation |
| **Early 2027** | **Mainnet launch** |

### 2026 New Features Planned
- Decentralised sequencing for Sovereign Zones (avoids centralised sequencer risk)
- Bridging between Zones
- Inter-Zone messaging
- External audits before mainnet

---

## Key Context

- Full specification set completed August 2025 — "source of truth" for all internal dev and third-party audits
- 18 months of intensive research + protocol design preceded the spec finalisation
- LSSA is the first Sovereign Zone shipping at mainnet; Native Zones deferred to post-mainnet
- March 2026 testnet is a critical inflection point — first adversarial test of Cryptarchia in a real environment

---

## Risk Factors

- **30-second block time** — slower than Ethereum; may push latency-sensitive apps to Sovereign Rollups
- **ZK performance** — Risc0 at ~0.3 TPS on RTX 4090 (Nov 2025); proving time improvements ongoing
- **Unproven consensus** — Cryptarchia has not been tested in adversarial mainnet conditions
- **Mainnet 2027** — long timeline compared to existing L1s; competitors will continue to mature
