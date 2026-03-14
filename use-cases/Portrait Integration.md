---
topic: use-cases
type: case-study
tags: [waku, social, decentralised-web, p2p, production]
status: beta
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.waku.org/portrait-launches-decentralised-micro-websites-powered-by-waku/
---

# Portrait — Decentralised Micro-Websites Powered by Waku

**Website:** https://portrait.so  
**Category:** Decentralised Social / Personal Web  
**Logos Stack Used:** Waku  
**Status:** Public Beta (Base L2 testnet)

## What It Is

Portrait is a decentralised social platform that lets anyone create, host, and manage their own micro-website (called a "Portrait"). These sites are:

- Owned entirely by their creator
- Stored across a distributed network of hundreds of user devices
- Fully customisable (embed videos, links, text posts, images)

Rather than traditional "follow" mechanics, Portrait uses a **hosting** model: following someone means allocating storage space on your device for their data — like seeding a torrent. With 1GB of storage, you can host up to 50,000 Portraits.

## How Waku Is Used

- Portraits are compressed to fit within Waku message constraints, enabling sharing directly over the P2P network **without centralised storage**
- Hosting nodes are Waku **edge nodes** extended with Portrait-specific functionality
- Service nodes (Waku relay + Store protocol) cache and relay content for resource-constrained clients
- Waku's light protocols enable hosting from browsers and smartphones

## Why This Matters for Logos

Demonstrates Waku's ability to power:
- Censorship-resistant content distribution at scale
- A viable decentralised alternative to Web2 social platforms
- True user data sovereignty (no platform lock-in, no ads)

Quote from co-founder Ryan Shahine:
> "The protocol is truly decentralised, and at enough adoption can exist perpetually, even if our team and company stopped existing."

## Business Model

- One-time fee of $10 to mint a Portrait on mainnet
- No ongoing subscription; network self-sustains via peer hosting

## Relevance to Franck's Work

Strong showcase for Logos Developer Experience pitches — a production-ready app that non-technical users can actually try. Useful for RFP examples of Waku's real-world utility.
