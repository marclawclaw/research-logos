# Vac R&D Service Units (VSUs)

> Last updated: 2026-03-14  
> Source: [research.logos.co/vsus](https://research.logos.co/vsus)

Vac operates **9 specialized R&D service units**. Each unit supports IFT projects and contributes to the broader decentralized ecosystem.

---

## 1. P2P

**Focus:** P2P networking layer

- Develops and maintains **[nim-libp2p](https://github.com/vacp2p/nim-libp2p)** — the Nim implementation of the libp2p networking stack
- Improves libp2p protocols with emphasis on **GossipSub** optimization
- Prioritizes requests from IFT projects (Waku, Nimbus, etc.)
- Published performance evaluations of IDONTWANT messaging
- Contributes specification improvements back to the libp2p community

**2025 Goals:**
- Add QUIC transport to nim-libp2p
- Add WebTransport to nim-libp2p
- Continue GossipSub performance optimization

**Key artifact:** [nim-libp2p](https://github.com/vacp2p/nim-libp2p) — see [nim-libp2p.md](nim-libp2p.md)

---

## 2. Token Economics (TKE)

**Focus:** Token economy design, incentives, markets

- Works day-to-day with IFT project teams
- Proactively suggests new strategies (not just reactive)
- Skill spectrum: dynamic systems modeling, theoretical modeling, cryptoeconomics

**Key projects:**
- Codex storage incentives
- Status Network economic structure
- Nomos economic modeling
- Waku RLN payment mechanisms

---

## 3. Distributed Systems Testing (DST)

**Focus:** Scaling behavior, regression testing, simulation

- Builds software for understanding node scaling in large networks
- Operates **Vac Lab** — simulation infrastructure scaled from hundreds to **thousands of nodes**
- Runs monthly regression simulations for Waku and nim-libp2p

**2025 Goals:**
- Expand Vac Lab testing to Codex and Nomos
- Continue monthly regression cycles

---

## 4. Quality Assurance (QA)

**Focus:** Test plans, unit tests, interoperability testing

- Comprehensive test coverage for IFT project implementations
- Tests implementations against defined specifications
- Key achievements:
  - Matured Waku interop testing framework (all major protocols covered)
  - Collaboration with Nomos on testing
  - Partnership with Status on message reliability under poor network conditions

---

## 5. Smart Contracts (SC)

**Focus:** Smart contract development, maintenance, and auditing

- Uses **[Certora](https://www.certora.com/) formal verification** — mathematically proves contract compliance with specifications
- The Certora Prover detects rare, hard-to-find bugs

**Key work:**
- Deployed SNT staking protocol testnet
- Formal specs for Codex and Status contracts
- Educational sessions: stealth addresses, NFTs, EVM architecture
- Enhances existing and develops new contracts for IFT projects

---

## 6. Nim

**Focus:** Nim language tooling and core library maintenance

- Maintains: **Nim compiler**, **Nimble** (package manager), **nim-suggest**
- Plans to maintain core IFT libraries: [Chronos](https://github.com/status-im/nim-chronos), etc.

**Key achievements (2024):**
- Introduced **SAT solver** to Nimble for better dependency resolution
- Stabilized Nim Language Server + VSCode extension
- Released 7 nim-libp2p versions (v1.2.0–v1.7.1)

**Why Nim?** IFT ecosystem heavily uses Nim — Nimbus, nim-libp2p, and other core components are written in it.

---

## 7. Applied Cryptography & ZK (ACZ)

**Focus:** Cryptographic solutions, ZK proofs, network security protocols

**Key protocols & implementations:**
- **RLN (Rate Limiting Nullifier):**
  - [RLNv1](https://rfc.vac.dev/vac/32/rln-v1), [RLNv2](https://rfc.vac.dev/vac/raw/rln-v2), [RLNv3](https://research.logos.co/rlog/rln-v3)
  - Backend: [zerokit](https://github.com/vacp2p/zerokit) — released v0.5.0, v0.6.0
- **Decentralized MLS** (Message Layer Security)
- **libp2p-mix protocol** (anonymization/mixnet)
- **Noise protocol channels**
- **Stealth Address Kit**

**Nescience work:**
- 23 zkVM architecture reviews
- Benchmarking of 6 leading zkVMs
- NSSA (Nescience State Separation Architecture) exploration

**Publications (2024–2025):**
- "Verifying RLN Proofs in Light Clients with Subtrees"
- "RLN-v3: Towards a Flexible and Cost-Efficient Implementation"
- Decentralized MLS paper + blog posts

---

## 8. RFC

**Focus:** Specification shepherding and editing for all IFT projects

- Acts as a central body ensuring standardized, interoperable protocols
- Transitioned to **consensus-oriented specification methodology**
- Specs formerly at rfc.vac.dev — now at **[lip.logos.co](https://lip.logos.co/)**
- Repository: [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)
- Covers: Messaging, Blockchain, Storage, IFT-TS components

---

## 9. Security

**Focus:** Security audits and security planning for IFT projects

- Comprehensive security audit support
- Security plan development
- (Less public-facing; details limited in public docs)

---

## Cross-Unit Research

Vac Research spans primarily **ACZ** and **P2P** units.

Key research focus areas:
- Zero-knowledge proofs (ZKP) and applications
- libp2p GossipSub improvements
- Anonymization networks (mixnet, Nescience)

> "Rather than focusing on academic publications, we aim to actively bridge theory and practice."
