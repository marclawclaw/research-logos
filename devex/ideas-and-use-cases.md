# Waku Ideas Board — Use Cases & Inspiration

> Source: https://ideas.waku.org  
> Researched: 2026-03-14

## Overview

ideas.waku.org is a community-curated collection of project ideas built on Waku. Key note from the board:

> "Numerous traditional chat applications have already harnessed Waku's capabilities. To truly innovate, we encourage hackers to explore untapped possibilities beyond chat."

## Ideas by Category

### 🗳️ Governance & Voting
- **Polling/Voting** — Off-chain vote aggregation, submit results on-chain in one tx
- **DAO/Governance Tooling** — Create/vote/approve proposals
- **Privacy-preserving governance** — Votes NOT linked to wallets (ZK proofs for voting power)
- **Budget approval app** — Community fund management with transparent transactions

### 🛒 Marketplace & DeFi
- **Marketplace** — Off-chain offer/negotiation (NFTs, goods, rideshare, LLM providers)
  - LLM marketplace: multiple AI providers compete to serve user requests
- **Secure DeFi** — Verify correct counterparty address before transaction
- **Crypto ATMs** — Decentralized ATM card approvals

### 🎮 Gaming
- **Multiplayer Games** — Move coordination off-chain; submit final state on-chain for reward
- **P2P Chess** — 2-player staked games, winner takes stake
- **P2P TicTacToe** — Same pattern

### 🏥 IoT & Real-World Data
- **IoT Systems** — Privacy-preserving device data collection
  - ZK credentials for device auth per postcode
  - DeSci open data initiative model
- **Crowd-sourced weather data** — Privacy-preserving, decentralized
- **Indoor air quality sensors** — Health organization data collection (example)
- **Medical systems** — Remote diagnosis via sensor data
- **Privacy-preserving fitness tracker** — Secure health metrics with selective sharing

### 🔔 Infrastructure & Tools
- **Notifications Centre** — Replace Apple/Google push notifications with decentralized alternative
- **API Generator** — Generate Waku protocol + code from OpenAPI specification
- **Leader Election Protocol** — RAFT-like consensus library on top of Waku
- **Privacy-preserving APIs** — REST API layer that hides IP addresses with rate-limiting

### 🤝 Collaboration
- **Collaborative Editing** — Real-time doc editing; versions stored on decentralized storage
- **Decentralised brainstorming tool** — Anonymous idea sharing
- **Federated Learning Platform** — Edge device ML training without raw data sharing

### 🔐 Identity & Privacy
- **Decentralized Wallet Address Ownership Verification** — dApp ↔ wallet communication
- **Reputation Systems** — Reputation scores for wallets, smart contracts
- **Censorship-Resistant Reviews Plugin** — Embeddable, decentralized review system
- **Privacy-Preserving Location Tracker** — Share location without exposing it to others
- **Privacy preserving AI assistant** — AI prompts without revealing user identity
- **Privacy preserving confessions board** — Anonymous, gamified

### 🌐 Other
- **Decentralized Web Walkie-Talkie** — Real-time audio channels
- **Satellite Communication Systems** — Non-centralized satellite comms
- **Decentralized Autonomous Vehicle Coordination** — Self-driving car coordination
- **Decentralized Smart Grid System** — Energy distribution optimization
- **Supply Chain Transparency** — Encrypted stakeholder data sharing
- **News over Waku** — Publishable, votable, commentable news platform
- **Smart Access Cards** — NFC cards for transactions, unlocking devices
- **Hiring Platform** — Bias-less, privacy-preserving HR

## Standout Ideas for Logos PoCs

These are particularly relevant for Franck's PoC work:

### High Priority
| Idea | Why Interesting |
|------|----------------|
| **Privacy-preserving AI assistant** | Relevant to Logos + AI narrative; technical novelty |
| **Notifications Centre** | Replace Google/Apple; fits Logos privacy goals perfectly |
| **API Generator from OpenAPI** | Dev tooling; could be an RFP candidate |
| **Federated Learning Platform** | Strong DeSci/AI angle; novel Waku use |
| **Privacy-preserving governance** | ZK + Waku combo; good technical demo |

### Medium Priority
| Idea | Why Interesting |
|------|----------------|
| **Collaborative Editing** | Demo of Waku for real-time non-chat use |
| **Censorship-Resistant Reviews** | Simple embed plugin; accessible scope |
| **Marketplace (LLM providers)** | AI economy + decentralized coordination |
| **Leader Election / RAFT** | Infrastructure primitive; multiplies Waku utility |

## DX Observation from the Ideas Board

The ideas board implicitly reveals **what's missing** from the Waku SDK:

1. No audio/WebRTC support (Web Walkie-Talkie idea suggests this gap)
2. No easy notification primitive (requires building your own)
3. No off-the-shelf ZK integration example for voting
4. No standard leader election or consensus primitive

These gaps are **opportunities for ecosystem tooling** — primitives that would make Waku much more accessible for specific use cases.
