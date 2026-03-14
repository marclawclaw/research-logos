# Vac (Logos Research) — Overview

> Last updated: 2026-03-14
> **Note:** vac.dev now redirects to research.logos.co. Vac operates as the research arm of the Logos ecosystem.

## What is Vac?

Vac is "a principle-driven R&D team providing technical support to IFT startups." It combines "hands-on development with in-depth research" to create foundational components and protocols for decentralized technologies.

Vac develops:
- Foundational protocol components
- Unopinionated specifications and libraries
- Applied research driving protocol innovation
- Publications and technical standards

**Source:** [research.logos.co](https://research.logos.co/)

---

## R&D Service Units

Vac operates through **9 specialized service units:**

### 1. P2P
- Develops **nim-libp2p**
- Improves libp2p protocols with focus on **GossipSub**
- Published performance evaluation of IDONTWANT messaging
- Submitted specification improvements to libp2p community
- 2025 goals: Add QUIC and web transport to nim-libp2p

### 2. Token Economics (TKE)
- Designs token economies, incentives, and markets for IFT projects
- Skills: dynamic systems modeling, theoretical modeling, cryptoeconomics
- Key work: Codex storage incentives, Status Network structure, Nomos economic modeling, Waku RLN payment mechanisms

### 3. Distributed Systems Testing (DST)
- Develops testing software for understanding node scaling behavior
- Transitioned to dedicated **Vac Lab** — simulations scaled from hundreds to **thousands of nodes**
- Monthly regression simulations for Waku and nim-libp2p
- 2025 goals: Expand testing to Codex and Nomos

### 4. Quality Assurance (QA)
- Comprehensive test plans: unit and interoperability testing
- Matured Waku interop testing framework (all major protocols covered)
- Began collaboration with Nomos on testing
- Partnered with Status on message reliability under poor network conditions

### 5. Smart Contracts (SC)
- Develops, maintains, and audits smart contracts
- Uses **Certora formal verification** to mathematically prove contract specifications
- Deployed SNT staking protocol testnet
- Created formal specs for Codex and Status contracts
- Educational sessions on stealth addresses, NFTs, EVM architecture

### 6. Nim
- Maintains **Nim compiler**, Nimble package manager, nim-suggest
- Introduced **SAT solver** to Nimble for improved dependency resolution
- Stabilized Nim Language Server and VSCode extension
- Released 7 versions of nim-libp2p in 2024 (v1.2.0–v1.7.1)

### 7. Applied Cryptography & ZK (ACZ)
- ZK proofs, RLN implementations, zerokit backend
- Decentralized MLS (Message Layer Security)
- Network security protocols
- **Nescience** development (23 zkVM reviews, benchmarking)
- libp2p mix protocol proof-of-concept
- Released Zerokit v0.5.0, v0.6.0 and Stealth Address Kit

### 8. RFC
- Shepherds and edits specifications for all IFT projects
- Ensures standardized and interoperable protocols
- Transitioned to consensus-oriented specification methodology
- RFCs now at [lip.logos.co](https://lip.logos.co) (formerly rfc.vac.dev)

### 9. Security
- Security audits for IFT projects
- Security plan development

**Source:** [research.logos.co/vsus](https://research.logos.co/vsus/), [research.logos.co/rlog/2024-recap](https://research.logos.co/rlog/2024-recap)

---

## Published Research & Papers (2024–2025)

| Paper/Publication | Area |
|-------------------|------|
| Comprehensive review of 23 zkVMs | Nescience/ACZ |
| Benchmarking of 6 leading zkVMs | Nescience/ACZ |
| NSSA architecture exploration | Nescience |
| "Verifying RLN Proofs in Light Clients with Subtrees" | ACZ |
| "RLN-v3: Towards a Flexible and Cost-Efficient Implementation" | ACZ |
| "Libp2p GossipSub IDONTWANT Message Performance Impact" | P2P |
| Decentralized MLS paper and blog posts | ACZ |

**Source:** [research.logos.co/rlog/2024-recap](https://research.logos.co/rlog/2024-recap)

---

## Key Projects Supported

| Project | How Vac Supports It |
|---------|---------------------|
| Waku/Messaging | RLN, nim-libp2p, QA testing, specifications, mixnet research |
| Codex/Storage | Tokenomics, smart contract verification, testing expansion |
| Nomos/Blockchain | Economic modeling, testing collaboration, specifications |
| Nescience | Core ZK research, zkVM evaluation, implementation |
| Status | Message reliability testing, smart contract verification |
| Nimbus | nim-libp2p improvements |

---

## Community & Resources

| Resource | URL |
|----------|-----|
| Main site | [research.logos.co](https://research.logos.co/) |
| Forum | [forum.research.logos.co](https://forum.research.logos.co/) |
| RFCs/Specs | [lip.logos.co](https://lip.logos.co/) |
| GitHub | [github.com/vacp2p](https://github.com/vacp2p) |
| DST Roadmap | [roadmap.vac.dev/dst/preview](https://roadmap.vac.dev/dst/preview) |

---

## 2025 Strategic Priorities

1. Strengthen RFC culture across all portfolio projects
2. Establish diverse external research community engagement
3. Deepen partnerships with libp2p, Ethereum, and Nim ecosystems
4. Create internal knowledge repository and identify project synergies
5. Nescience: Complete full-node implementation
6. DST: Expand testing to Codex and Nomos
7. P2P: Add QUIC and web transport to nim-libp2p
8. ACZ: Finalize libp2p mix and decentralized MLS for production

**Source:** [research.logos.co/rlog/2024-recap](https://research.logos.co/rlog/2024-recap)

---

## Analysis

### Strengths
- **Exceptional breadth:** 9 specialized units covering everything from ZK cryptography to Nim compiler maintenance
- **Cross-cutting impact:** Vac supports every IFT project, creating shared infrastructure and preventing duplication
- **Research rigor:** Systematic approaches (23 zkVM reviews, Certora formal verification, monthly regression testing)
- **Open-source ethos:** Specifications, papers, and tools are publicly available
- **Community contribution:** Active contributions back to libp2p ecosystem

### Concerns
- **Rebranding in progress:** vac.dev → research.logos.co transition; some links may be broken
- **Research-to-production gap:** Strong research output, but production deployment of some innovations (decentralized MLS, mixnet) still pending
- **Nim dependency:** Heavy reliance on Nim ecosystem, which has a smaller developer community than Rust/Go/TypeScript
- **Team distribution visibility:** Limited public information about team sizes per unit

### Key Observation
> **Notable:** Vac/Logos Research is the unsung backbone of the entire IFT ecosystem. The quality of their R&D service units — particularly the DST simulation capabilities (thousands of nodes) and ACZ's ZK research — is world-class. The 9-unit structure is unusually well-organized for a crypto research org.
