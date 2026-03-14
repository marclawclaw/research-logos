---
topic: use-cases
type: use-case
tags: [railgun, privacy, defi, relayer, waku, production]
confidence: high
last_updated: 2026-03-14
sources: [https://blog.waku.org/2024-04-26-railgun-case-study/]
---

# RAILGUN Integration

## Summary

RAILGUN uses Waku as its decentralised relayer network, enabling privacy-preserving DeFi transactions on EVM chains. Relayers advertise fees via Waku and users select relayers to submit their private transactions to the blockchain.

## Key Facts

> [!fact] Production integration
> - **Project:** RAILGUN — on-chain privacy for EVM chains
> - **Use case:** Relayer network for private transactions
> - **Tech:** ZK cryptography, smart contracts
> - **Waku role:** Relayer discovery, fee advertising, transaction relay

### What RAILGUN Does

- **Private DeFi:** Lending, borrowing, swapping without transparent tx history
- **ZK-powered:** Uses Zero-Knowledge proofs
- **Self-custodial:** No bridge risk, as secure as underlying EVM chain
- **No new L2:** Works on existing chains

### Architecture

```
User Wallet (js-waku) → Waku Network → Relayer (nwaku) → Blockchain
```

- **nwaku nodes:** Self-federated relayer network
- **js-waku:** User-facing wallet integration
- **REST API:** nwaku communication interface

### Privacy Preservation

Relayers cannot see transaction contents (ZK proofs), only relay encrypted data. Waku provides the transport without compromising privacy.

## How it relates to Logos

RAILGUN demonstrates Waku for **privacy-critical financial infrastructure**:
- Relayer networks without trusted coordinators
- Fee market via P2P messaging
- Browser-compatible privacy (js-waku)

> [!analysis] Analyst inference
> This is Waku's most compelling privacy use case — actual DeFi transactions with real financial risk, not just chat. Validates the privacy claims.

## Open Questions

- Relayer economics — how profitable?
- Message latency for transaction submission?
- How many active relayers?

## Sources

- https://blog.waku.org/2024-04-26-railgun-case-study/
- https://www.railgun.org
