---
topic: use-cases
type: integration
tags: [waku, logos-messaging, taco, encryption, access-control, cyphershare]
confidence: high
last_updated: 2026-03-17
source: https://blog.waku.org/waku-x-taco-p2p-comms-with-decentralised-encryption/
related:
  - Cyphershare
  - Codex TACo Integration
  - _index
---

# Waku × TACo Integration

## Overview

Waku + TACo (Threshold Access Control) provides a **P2P messaging layer with programmable, decentralised encryption and access control** — no centralised key server required.

> Codex is the optional third leg: Waku (transport) + Codex (storage) + TACo (access control) = complete decentralised stack.

## What Each Layer Does

| Layer | Protocol | Role |
|-------|----------|------|
| Transport | Waku / Logos Messaging | Real-time P2P message routing, censorship-resistant |
| Storage | Codex | Durable, immutable data persistence |
| Access Control | TACo | Decentralised encryption + programmable access conditions |

## How TACo Works

TACo uses a **distributed cohort of nodes** that collaboratively generate public keys — no single authority holds the decryption key. Access conditions can include:
- Token ownership
- Group membership
- Time-bounded availability
- Custom on-chain conditions

## Use Cases Enabled

- **Collaboration tools**: docs synced via Waku, stored on Codex, protected by TACo conditional access
- **Governance/voting**: votes encrypted until final tally revealed
- **Social platforms**: content access managed without centralised gateways
- **Data markets**: sell/license access to data with fine-grained control

## Reference Implementation: Cyphershare

[Cyphershare](https://share.hackyguru.com/) — encrypted file sharing, live PoC.

- Files encrypted **in-browser** before upload
- Encrypted data stored on **Codex**
- **Waku** distributes metadata/notifications (serverless)
- **TACo** defines who can decrypt (token, group, or time-window conditions)

See also: [[Cyphershare]]

## Status

- Both Waku and TACo are live in production contexts (Waku: RAILGUN, The Graph, Portrait; TACo: mainnet)
- Cyphershare is a live PoC demonstrating the full Waku+Codex+TACo stack
- Integration docs: https://docs.taco.build/for-developers/integrations/waku-+-codex

## Relevance for Franck

Strong PoC opportunity. Cyphershare demonstrates the full Logos stack integration. Good reference for any RFP or PoC that requires encrypted, censorship-resistant data sharing with programmable access.
