---
topic: use-cases
type: infrastructure
tags: [waku, logos-messaging, incentivisation, service-marketplace, economics]
confidence: high
last_updated: 2026-03-17
source: https://blog.waku.org/first-steps-toward-incentivising-waku-2/
related:
  - Waku Hackathon Projects
  - _index
---

# Waku Service Incentivisation

## Overview

Waku service nodes (running Store, Filter, Lightpush) currently operate on a **voluntary, best-effort basis** with no compensation. This is unsustainable and creates centralisation risk. The team published a PoC in 2025 demonstrating the first steps toward a **decentralised Waku Service Marketplace**.

## Why Incentivise?

Light protocol services (Lightpush, Store, Filter) are critical for resource-constrained devices (mobile, browser) that can't run a full relay node. Service nodes do the heavy lifting but receive nothing. Problems:
- Unsustainable long-term for node operators
- Risk of centralisation (few altruistic nodes)
- dApp builders forced to self-host infrastructure

## PoC: Incentivised Lightpush

**Lightpush** was chosen as the first target because the economic relationship is simple and verifiable: edge node pays, service node publishes using its RLN credentials.

### Mechanism

**Eligibility** (checked by service node):
- Edge node attaches a transaction hash (payment proof) on Linea Sepolia testnet
- Payment must be in ETH, correct amount, correct address, not previously used
- Service node verifies on-chain before fulfilling the request

**Reputation** (tracked by edge node):
- Failed/unresponsive nodes get a "bad" reputation mark
- Reliable nodes get upgraded to "good"
- Future requests prefer good-reputation nodes

### Test Setup
Four nwaku nodes: Alice (edge), Bob + Charlie (service), Dave (relay).

> PoC guide: https://github.com/waku-org/nwaku/blob/feat/service-incentivization-poc/docs/service-incentivization.md

## Toward a Service Marketplace

Long-term vision (from [Vac Forum proposals](https://forum.vac.dev/t/waku-as-a-decentralized-service-marketplace/282)):

- Dynamic pricing by service nodes
- Discovery for comparing available providers
- Subscription / pre-paid balance / metered billing models
- Decentralised shared reputation systems
- Expand to Store and Filter (subscription model vs. per-message)
- Potentially evolve into a **generalised service marketplace** beyond messaging

## Status (as of 2025)

- Still in research / PoC phase
- November 2025 update: active alignment across teams on service incentivisation design and payment protocol strategy, pseudonymous payments explored
- RLN testnet dogfooding ongoing

## Relevance for Franck

High. This is the sustainability layer that makes Waku/Logos Messaging viable at scale. Any PoC app built on Waku currently free-rides altruistic nodes — once the marketplace is live, apps need to factor in messaging costs. Good to understand the tokenomics direction early.
