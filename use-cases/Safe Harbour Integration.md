---
topic: use-cases
type: use-case
tags: [safe, multisig, erc-4337, waku, production]
confidence: high
last_updated: 2026-03-14
sources: [https://blog.waku.org/safe-uses-waku-to-power-decentralised-multisig-operations-with-harbour/]
---

# Safe Harbour Integration

## Summary

Safe's Harbour infrastructure uses Waku to enable decentralised multisig transaction coordination, replacing centralised APIs with peer-to-peer signature exchange. Combined with ERC-4337 for account abstraction.

## Key Facts

> [!fact] Production integration — experimental
> - **Project:** Safe — leading smart contract wallet
> - **Use case:** Decentralised signature collection for multisig
> - **Status:** Experimental support live on Harbour web interface
> - **Tech:** ERC-4337 + Waku + Validator Network

### Problem Solved

Traditional multisig coordination:
- **Off-chain queuing** via centralised services
- **Trusted relays** can fail or censor
- **Trade-off** between usability and decentralisation

### Harbour Architecture

```
Signer (js-waku) ↔ Waku Network ↔ Validators (nwaku) → On-chain
```

- **Validators:** Professional actors who lock tokens for submission rights
- **Paymaster:** Manages sponsorship, quotas, anti-abuse
- **Web interface:** Runs Waku edge node to connect to validator network

### Why Waku?

- **Resilience:** No trusted relay to censor/fail
- **Light-node friendly:** Runs in browser (Safe web interface)
- **Easy integration:** Streamlined setup for validators and frontends

### Current Implementation

- **JS-Waku SDK** for web interface
- Future: Waku relay nodes for validators (improved reliability)

## How it relates to Logos

Safe demonstrates Waku for **financial coordination infrastructure**:
- Multisig is critical security (billions in TVL)
- Decentralisation without UX sacrifice
- Validator networks with token staking (economic alignment)

> [!analysis] Analyst inference
> Safe adoption is a major validation. They're the dominant multisig provider — this isn't a toy project. The validator network model with token locking hints at Logos incentive patterns.

## Open Questions

- What's the validator stake requirement?
- How many validators currently active?
- Latency for signature collection?
- Token used for staking?

## Sources

- https://blog.waku.org/safe-uses-waku-to-power-decentralised-multisig-operations-with-harbour/
- https://safe.global/blog/safe-research-decentralized-signature-collection-with-erc-4337
- https://www.safe.dev/harbour/
