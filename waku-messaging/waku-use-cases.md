---
topic: waku-messaging
type: reference
tags: [waku, use-cases, safe, multisig, dapp, web3, integrations]
confidence: high
last_updated: 2026-03-14
sources:
  - https://docs.waku.org
  - https://blog.waku.org/safe-uses-waku-to-power-decentralised-multisig-operations-with-harbour/
---

# Waku Use Cases & Real-World Integrations

## Summary

Waku is a general-purpose P2P communications stack — not just for chat. It replaces centralised APIs, relays, and databases with a decentralised network of peers exchanging information in real time.

## Official Use Case Categories

| Use Case | How Waku Helps |
|----------|---------------|
| Chat Messengers | Private, decentralised, censorship-resistant messaging |
| Voting & Proposals | Off-chain vote exchange to save gas; aggregate results on-chain |
| NFT Marketplaces | Off-chain bids/offers + social features (likes, comments) |
| State Channels | Message exchange and updates without blockchain interaction |
| Multi-Sig Wallets | Private, secure signature exchange between signers |
| Game Mechanics | P2P game state comms without centralised infrastructure |
| L2 Coordination | Broadcast/aggregate L2 txns; spam-protected mempool |
| Social Media | Decentralised news feeds, multimedia sharing platforms |

## Notable Production Integrations

### Safe Harbour (Multi-Sig)
**Safe** (leading smart contract wallet infrastructure) uses Waku in its **Harbour** project:
- Problem: Multisig coordination relied on centralised off-chain queuing services
- Solution: Waku replaces centralised relay — signers and validators communicate directly P2P
- Implementation: JS-Waku SDK in Safe's web interface
- Why Waku: Resilience (no trusted relay), light-node friendly, easy to integrate
- ERC-4337: Parallel signature submissions, paymaster contract for fee logic

### The Graph
- Used Waku for P2P coordination; full case study at https://blog.waku.org/2024-05-13-the-graph-case-study/

### Railgun
- Privacy-focused DeFi protocol using Waku; case study at https://blog.waku.org/2024-04-26-railgun-case-study/

### Status (Primary Integration)
- Status Mobile and Desktop are the primary consumers of Waku
- Status Communities run over Waku for real-time group communication
- libwaku validated running on Windows (Nov 2025 update)

### TACo + Codex Collaboration
- Waku (P2P comms) + TACo (Threshold Access Control, decentralised encryption) + [[Codex]] (storage)
- Demonstrates composability of Logos stack for fully decentralised, private applications

## Hackathon / Community

- **W3PN Berlin Hackathon** (June 2025) — Waku powered P2P comms at Web3Privacy Now hacks event
- **RealFi Hackathon** — Logos sponsored tracks: "Resilient Activist Technology" + "Logos x Tor Privacy Infrastructure"
- **ideas.waku.org** — Community-curated inspiration for builders
- **Awesome Waku** — https://github.com/waku-org/awesome-waku/

## Logos Stack Positioning

Waku becomes most powerful when combined with the full stack:
- **Waku/Logos Messaging** → real-time communication layer
- **Codex/Logos Storage** → persistent/archival storage layer  
- **Nomos/Logos Blockchain** → trust, consensus, and economic layer

This positions Logos as a complete decentralised application infrastructure, not just a messaging protocol.

## Sources

- https://docs.waku.org
- https://blog.waku.org/safe-uses-waku-to-power-decentralised-multisig-operations-with-harbour/
