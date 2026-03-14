# Logos Research Discovery

Date: 2026-03-14

## Overview

Logos is a social movement and decentralised technology stack built to revitalise civil society. It operates as a unified ecosystem with three core modules:
- **Blockchain** (formerly Nomos) — scalable, trustless agreements layer
- **Storage** (formerly Codex) — privacy-preserving, decentralised storage
- **Messaging** (formerly Waku) — peer-to-peer communication layer

The stack is private-by-default and modular by design, with a plugin-based runtime for decentralised applications.

---

## Topics

### 1. Logos Tech Stack Architecture
- **Description:** The unified modular architecture combining Blockchain, Storage, and Messaging modules with a plugin-based runtime for building decentralised applications.
- **Sources:**
  - GitHub: https://github.com/logos-co/logos-workspace, https://github.com/logos-co/logos-app, https://github.com/logos-co/logos-liblogos
  - Docs: https://logos.co/tech-stack
  - Blog: https://press.logos.co/article/logos-as-an-operating-system, https://press.logos.co/article/2025-dev-retrospective
  - Discourse: https://forum.vac.dev/c/vac/9
  - Specs: https://lip.logos.co/

### 2. Waku Messaging Protocol
- **Description:** Family of peer-to-peer communication protocols enabling privacy-focused, censorship-resistant messaging for Web3 applications, built on libp2p.
- **Sources:**
  - GitHub: https://github.com/waku-org/nwaku, https://github.com/waku-org/js-waku, https://github.com/waku-org/go-waku
  - Docs: https://docs.waku.org
  - Blog: https://blog.waku.org
  - Specs: https://lip.logos.co/messaging/standards/core/
  - Discourse: https://forum.vac.dev/c/waku/5
  - Reddit: https://www.reddit.com/r/ethereum/comments/f7do8r/waku_spec_v040_this_specification_describes_the/

### 3. RLN Rate Limiting Nullifier
- **Description:** Zero-knowledge spam protection mechanism for Waku that rate-limits resource usage via on-chain smart contracts and cryptographic proofs.
- **Sources:**
  - GitHub: https://github.com/vacp2p/zerokit, https://github.com/waku-org/nwaku (RLN integration)
  - Docs: https://docs.waku.org (RLN sections)
  - Blog: https://blog.waku.org/waku-monthly-update-june-2025/
  - Discourse: https://forum.vac.dev/t/multisig-for-rlnv2-contract/429
  - Specs: https://lip.logos.co/messaging/standards/

### 4. Codex Decentralised Storage
- **Description:** Decentralised Durability Engine (DDE) providing censorship-resistant, persistent data storage with erasure coding and a storage marketplace.
- **Sources:**
  - GitHub: https://github.com/codex-storage/nim-codex
  - Docs: https://codex.storage/about/faq
  - Blog: https://blog.codex.storage, https://blog.codex.storage/the-codex-roadmap-for-2025-and-beyond/
  - Blog: https://blog.codex.storage/codex-storage-vs-filecoin-enhancing-durability-for-decentralised-storage/
  - Discourse: https://forum.vac.dev/c/codex/

### 5. Logos Blockchain (Nomos)
- **Description:** Privacy-preserving blockchain infrastructure for network states, featuring Cryptarchia consensus, Zones architecture, and network-level privacy.
- **Sources:**
  - GitHub: https://github.com/logos-co/nomos, https://github.com/logos-blockchain/nomos
  - Docs: https://nomos.tech/about/architect
  - Blog: https://blog.nomos.tech, https://blog.nomos.tech/2025-year-in-review/
  - Blog: https://blog.nomos.tech/comparing-consensus-bitcoin-ethereum-and-logos/
  - Specs: https://lip.logos.co/blockchain/

### 6. Blend Network (Proposer Anonymity)
- **Description:** Mixnet layer for Logos Blockchain that protects proposers against deanonymisation through message encapsulation and mixing strategies.
- **Sources:**
  - GitHub: https://github.com/logos-co/nomos (blend components)
  - Blog: https://blog.nomos.tech/message-encapsulation-in-the-nomos-blend-network/
  - Blog: https://blog.nomos.tech/the-blend-network-improving-nomos-privacy-guarantees/
  - Blog: https://blog.nomos.tech/stirring-mixing-blending-different-approaches-to-proposer-anonymity/

### 7. Cryptarchia Consensus
- **Description:** Private Proof-of-Stake consensus protocol based on Ouroboros Crypsinous, designed for Logos Blockchain with lottery difficulty adjustments.
- **Sources:**
  - GitHub: https://github.com/logos-co/consensus-research
  - Blog: https://blog.nomos.tech/nomos-cryptarchia-improving-on-ouroboros-crypsinous/
  - Blog: https://blog.nomos.tech/private-proof-of-stake-with-ouroboros-crypsinous/
  - Blog: https://blog.nomos.tech/lottery-difficulty-in-private-pos-the-case-of-cryptarchia/
  - Blog: https://blog.nomos.tech/the-ghost-fork-choice-rule-and-why-nomos-doesnt-use-it/

### 8. Vac Research & Specifications
- **Description:** R&D team providing technical support for IFT startups, developing protocols, specifications (LIPs), and foundational components like nim-libp2p and zerokit.
- **Sources:**
  - GitHub: https://github.com/vacp2p/zerokit, https://github.com/vacp2p/nim-libp2p, https://github.com/vacp2p/rfc-index
  - Docs: https://research.logos.co/, https://lip.logos.co/
  - Discourse: https://forum.vac.dev, https://forum.vac.dev/t/rfc-process/368
  - Blog: https://vac.dev/blog

### 9. Logos Developer Experience
- **Description:** SDKs, tooling, and developer resources for building on Logos including module system, Logos App, and integration patterns.
- **Sources:**
  - GitHub: https://github.com/logos-co/logos-cpp-sdk, https://github.com/logos-co/logos-docs
  - Docs: https://docs.waku.org, https://codex.storage/docs
  - Blog: https://press.logos.co/article/developer-update-feb-2026
  - Blog: https://blog.codex.storage/codex-factory-creating-local-codex-clusters-for-developers/
  - Ideas: https://ideas.waku.org/

### 10. Logos Use Cases & Applications
- **Description:** Real-world applications built on Logos: chat messengers, file sharing, NFT marketplaces, state channels, multi-signature wallets, and social platforms.
- **Sources:**
  - Blog: https://blog.waku.org/safe-uses-waku-to-power-decentralised-multisig-operations-with-harbour/
  - Blog: https://blog.waku.org/portrait-launches-decentralised-micro-websites-powered-by-waku/
  - Blog: https://blog.codex.storage/building-a-censorship-resistant-file-sharing-app-with-codex-and-waku/
  - Blog: https://blog.codex.storage/exciting-use-cases-for-decentralised-storage-in-2025-and-beyond/
  - Docs: https://docs.waku.org (use cases section)
  - Ideas: https://ideas.waku.org/, https://github.com/waku-org/awesome-waku

### 11. Waku Service Incentivisation
- **Description:** Marketplace and micropayment protocols to incentivise service nodes in Waku, ensuring sustainability of the p2p network.
- **Sources:**
  - Blog: https://blog.waku.org/first-steps-toward-incentivising-waku-2/
  - Blog: https://blog.waku.org/explanation-series-waku-service-marketplace/
  - Discourse: https://forum.vac.dev/t/off-chain-micropayments-prior-work-and-design-framework/579
  - Blog: https://blog.waku.org/waku-monthly-update-august-2025/

### 12. Zero Knowledge in Logos
- **Description:** ZK as a design philosophy across Logos: zerokit modules, privacy-preserving proofs, stealth addresses, and decentralised encryption (TACo integration).
- **Sources:**
  - GitHub: https://github.com/vacp2p/zerokit, https://github.com/vacp2p/stealth-address-kit
  - Blog: https://blog.waku.org/beyond-proofs-zero-knowledge-as-a-design-philosophy/
  - Blog: https://blog.waku.org/waku-x-taco-p2p-comms-with-decentralised-encryption/
  - Blog: https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
  - Docs: https://docs.taco.build/for-developers/access-control/integrations/waku

---

## Key Organisations & GitHub Orgs

| Organisation | GitHub | Focus |
|--------------|--------|-------|
| Logos | logos-co | Unified stack, roadmap, apps |
| Waku | waku-org | Messaging implementations |
| Codex | codex-storage | Storage protocol |
| Vac | vacp2p | Research, specs, libp2p, ZK |
| Logos Blockchain | logos-blockchain | Nomos/Blockchain monorepo |

---

## Key Resources

- **Main site:** https://logos.co
- **Tech stack:** https://logos.co/tech-stack
- **Press/Blog:** https://press.logos.co
- **Research:** https://research.logos.co/
- **Specs (LIPs):** https://lip.logos.co/
- **Forum:** https://forum.vac.dev (redirects to forum.research.logos.co)
- **Waku Docs:** https://docs.waku.org
- **Waku Blog:** https://blog.waku.org
- **Codex Blog:** https://blog.codex.storage
- **Blockchain Blog:** https://blog.nomos.tech
