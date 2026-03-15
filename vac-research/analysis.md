# Vac Research — Analysis & Observations

> Last updated: 2026-03-15

## TL;DR

Vac is the **unsung backbone of the entire IFT ecosystem**. Every Logos-stack component (Waku, Codex, Nomos, Status) depends on Vac's work. Understanding Vac is essential for any PoC or integration built on the Logos stack.

---

## Strengths

### 1. Exceptional Organizational Breadth
Nine specialized units covering the full technical stack: P2P networking → cryptography → testing → QA → smart contracts → specifications → language tooling → security → token economics. Rare for a crypto research org.

### 2. Cross-Cutting Impact
Vac acts as shared infrastructure for all IFT projects, preventing duplication. nim-libp2p alone serves Waku (messaging), Codex (storage), and Nimbus (Ethereum client).

### 3. Research Rigor
- 23 zkVM reviews (ACZ/Nescience)
- Certora formal verification for smart contracts
- Monthly regression testing at thousands-of-nodes scale (DST Vac Lab)

### 4. Open-Source Ethos
All specs, papers, and tools are publicly available. Specs at [lip.logos.co](https://lip.logos.co/) follow IETF conventions — professionally maintained.

### 5. Active Upstream Contribution
Contributes back to libp2p community (GossipSub improvements), Nim ecosystem (SAT solver in Nimble, compiler work). Not just consuming open-source — extending it.

---

## Concerns / Watch Points

### 1. Nim Dependency
Heavy reliance on the Nim ecosystem. Nim has a smaller developer pool than Rust, Go, or TypeScript. The Nim service unit's work (compiler, Nimble, LSP) is critical infrastructure — if it slips, everything downstream suffers.

### 2. Research-to-Production Gap
Strong research output, but some innovations are still pending production deployment:
- **Decentralized MLS** — researched and papered, not yet in production
- **libp2p-mix / mixnet** — proof-of-concept stage
- **Nescience** — major undertaking, full-node implementation is the 2025 goal

### 3. Domain Migration Turbulence
vac.dev → research.logos.co and rfc.vac.dev → lip.logos.co transitions may leave broken links in external docs, tutorials, and third-party content.

### 4. Team Size Opacity
Limited public information about team sizes per unit. Hard to gauge capacity or velocity from outside.

---

## Key Observations for PoC Work

### nim-libp2p is the networking layer for everything
Any PoC integrating Waku or Codex runs on nim-libp2p. Watch:
- QUIC transport addition (2025 goal) — will improve performance significantly
- GossipSub improvements — directly affects Waku message propagation

### RLN is Vac's flagship anti-spam primitive
Rate Limiting Nullifier (v1 stable, v2/v3 in progress) is used in Waku for spam prevention. For PoCs requiring rate limiting without central authority, RLN is the tool.

### Specs at lip.logos.co are authoritative
When implementing against Waku, Codex, or Nomos protocols, the LIP specs are the ground truth. Contributions welcome via PR to vacp2p/rfc-index.

### Nescience = privacy layer for Logos
If a PoC needs privacy-preserving computation at the protocol level (not just transport encryption), Nescience is the relevant Vac effort. Still pre-production.

---

## Ecosystem Map (Vac's Role)

```
IFT Projects
├── Waku (messaging)     ← nim-libp2p (P2P), RLN (ACZ), specs (RFC), TKE
├── Codex (storage)      ← nim-libp2p (P2P), incentives (TKE), SC, DST
├── Nomos (blockchain)   ← DST testing, TKE, specs (RFC)
├── Status (social)      ← QA, SC, TKE
└── Nimbus (Ethereum)    ← nim-libp2p (P2P)

Vac Foundational
├── nim-libp2p           ← P2P unit
├── zerokit (RLN)        ← ACZ unit
├── lip.logos.co specs   ← RFC unit
├── Certora contracts    ← SC unit
└── Nescience            ← ACZ + VIP
```

---

## Recommended Follow-Up

- [ ] Deep-dive: [roadmap.vac.dev](https://roadmap.vac.dev/) — current unit roadmaps and progress
- [ ] Read: Nescience architecture blog post
- [ ] Monitor: nim-libp2p QUIC transport PR (2025 goal)
- [ ] Check: lip.logos.co for any new Waku or Codex specs relevant to active PoCs
- [ ] Forum: [forum.vac.dev](https://forum.vac.dev/) for R&D discussions
- [x] Verified sources 2026-03-15 — content matches original research
