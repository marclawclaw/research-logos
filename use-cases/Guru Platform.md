---
topic: use-cases
type: case-study
tags: [codex, waku, status-network, feedback, dapp, poc, 2025]
confidence: medium
last_updated: 2026-03-16
sources:
  - https://blog.codex.storage/codex-august-updates-2/
  - https://x.com/hackyguru/status/1952733529676075010
---

# Guru — On-Chain Feedback Exchange Platform

## Summary

Guru is an on-chain feedback exchange and management platform built by Codex DevRel Engineer [@hackyguru](https://x.com/hackyguru) (Vaclav Pavlin's colleague). It uses **Waku for real-time messaging**, **Codex for persistent storage**, and runs on the **Status Network gasless L2 blockchain**.

Announced: August 2025

## What It Does

- Users can submit and exchange feedback on-chain
- Leverages the Status Network (gasless L2) for on-chain settlement without gas friction
- Waku handles the real-time P2P communication layer
- Codex stores feedback data persistently in a decentralised manner

## Stack

| Layer | Technology |
|-------|-----------|
| Messaging | Waku (Logos Messaging) |
| Storage | Codex |
| Blockchain | Status Network L2 (gasless) |
| Frontend | Not specified |

## Why It's Significant

Guru is a **full-stack Logos application** — it demonstrates how Waku, Codex, and the Status Network can be combined in a single dapp:

- Not just a PoC for one layer — integrates three Logos stack components
- Shows the gasless L2 (Status Network) as a practical settlement layer for dapps
- Real-world use case: feedback/review systems are a common enterprise and community need

## Relevance to Franck's Work

- Strong example of a full Logos stack integration for RFP submissions or PoC docs
- Status Network L2 gasless pattern is underexplored in Franck's current PoC library
- Demonstrates a practical pattern: Waku (comms) + Codex (storage) + L2 (settlement)

## Related

- [[Qaku Integration]] — another full-stack Logos dapp (Waku + Codex, but no L2)
- [[Cyphershare]] — Waku + Codex + TACo encrypted file sharing
