---
topic: waku-messaging
type: concept
tags: [waku, incentivisation, lightpush, rln, service-nodes, poc, linea, marketplace]
confidence: medium
last_updated: 2026-03-15
sources:
  - https://blog.waku.org/first-steps-toward-incentivising-waku-2/
---

# Waku Service Incentivisation

## Summary

Waku's light protocols (Filter, Store, LightPush) currently rely on **voluntary service nodes** providing resources for free. This is unsustainable and creates centralisation risk. The Waku team has produced a PoC for **incentivised LightPush** using on-chain payment proofs, as a first step toward a decentralised **Waku Service Marketplace**.

## Key Facts

- **Current state:** Service nodes volunteer resources, no compensation mechanism
- **Problem:** Unsustainable long-term; creates centralisation and censorship risk; forces app developers to self-host infrastructure
- **PoC focus:** LightPush first (simplest to verify: message either publishes or fails)
- **Payment chain:** Linea Sepolia testnet (native ETH payments)
- **RLN angle:** Edge nodes pay service nodes that hold RLN membership credentials — enabling publishing without owning credentials

## How the PoC Works

### Eligibility (service node side)
Service node verifies incoming LightPush request has a valid payment proof:
- Payment in native ETH
- Exact expected amount
- Sent to correct service address  
- Not previously used (replay protection)

### Reputation (edge node side)
Edge nodes track service node reliability:
- Successful fulfilment → reputation upgraded to "good"
- Failure/error → marked "bad reputation", future requests avoid that node
- Lightweight feedback loop without trusted third party

### Test Setup
Four nwaku nodes: Alice (edge), Bob + Charlie (service), Dave (relay)

## Why LightPush First?

LightPush is uniquely suited for the first PoC because:
1. Binary outcome — message publishes or it doesn't (easy to verify)
2. RLN credentials are scarce and valuable — natural unit of economic exchange
3. Direct, immediate economic relationship between client and service node

Store and Filter are subscription models (ongoing service), making verification harder.

## Roadmap Directions

- Dynamic pricing by service nodes
- Discovery mechanism for finding and evaluating service nodes
- Bulk pre-payments / credit-based systems (vs. per-message payments)
- Generalising to Store and Filter protocols
- Full **Waku Service Marketplace**: decentralised discovery, pricing, and reputation

## Logos Stack Implications

- Connects Waku messaging economics to on-chain infrastructure ([[Nomos]] / Linea)
- Enables truly permissionless node operation without subsidy dependency
- Critical for long-term network sustainability as Status Communities scale up
- Opens possibility of **RPC-as-a-Service** fallback mechanism (mentioned in Nov 2025 update)

## Open Questions

- What chain will production incentivisation target? (Linea Sepolia is testnet)
- How will RLN membership pricing affect cost-per-message?
- When will Store/Filter incentivisation PoCs be ready?
- Will this integrate with Logos's own token economics?

## Sources

- https://blog.waku.org/first-steps-toward-incentivising-waku-2/
- https://blog.waku.org/logos-messaging-monthly-update-november-2025/
