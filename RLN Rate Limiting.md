---
topic: waku
type: concept
tags: [spam-protection, zk-proofs, rate-limiting, privacy]
confidence: high
last_updated: 2026-03-14
sources: [https://eprint.iacr.org/2024/1073.pdf, https://rfc.vac.dev/spec/32/]
---

# RLN Rate Limiting

## Summary

Rate Limiting Nullifiers (RLN) is a zero-knowledge-based spam protection mechanism for [[Waku Relay]]. It enables anonymous rate limiting without revealing user identity, using cryptographic nullifiers to detect and penalize users who exceed their message quota.

## Key Facts

> [!fact] Confirmed from academic paper (2024)
> - Novel approach to spam protection in decentralized networks
> - Uses zero-knowledge proofs to rate-limit anonymously
> - User registers with stake/deposit (slashable if rules violated)
> - Each message includes a ZK proof of membership and rate compliance
> - Double-sending within epoch reveals user's secret key

### How It Works

1. **Registration**: User deposits stake and receives membership credential
2. **Message Sending**: User generates ZK proof showing:
   - They are a valid member
   - They haven't exceeded rate limit in current epoch
3. **Verification**: Network verifies proof without learning user identity
4. **Slashing**: If user double-spends in an epoch, their secret is revealed and stake slashed

### Key Properties

| Property | Description |
|----------|-------------|
| **Privacy** | Verifiers cannot link messages to specific users |
| **Rate Limiting** | Users can only send N messages per epoch |
| **Accountability** | Spam/abuse reveals identity and slashes stake |
| **Decentralized** | No central authority needed |

## How it relates to Logos

RLN is critical infrastructure for [[Waku]] spam protection. Without it, anyone could flood the network with messages. With RLN, the [[Logos]] stack can maintain permissionless access while preventing abuse.

## Performance

> [!analysis] From latency study
> - RLN adds computational overhead for proof generation
> - Study measured message latency impact
> - Generally acceptable for most use cases
> - Trade-off between security and latency

## Open Questions

- What is the current epoch duration?
- How much stake is required for registration?
- What chain is used for the membership registry?
- How does RLN interact with Lightpush (do service nodes generate proofs)?

## Sources

- https://eprint.iacr.org/2024/1073.pdf — "Message Latency in Waku Relay with Rate Limiting Nullifiers"
- https://rfc.vac.dev/spec/32/ — RLN specification
