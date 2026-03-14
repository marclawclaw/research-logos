---
topic: use-cases
type: research-notes
tags: [codex, ai, machine-learning, datasets, decentralised-ai]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.codex.storage/exciting-use-cases-for-decentralised-storage-in-2025-and-beyond/
  - https://blog.codex.storage/revolutionising-ai-with-decentralised-storage/
---

# Codex × AI — Decentralised Storage for Machine Learning

## Why AI Needs Decentralised Storage

AI and ML models require massive, high-quality datasets for training. Traditional centralised storage (AWS, Google Cloud) introduces:

- **Prohibitive costs** — only the biggest providers can afford at scale
- **Centralisation risk** — single points of failure, outages, breaches
- **Limited transparency** — training data provenance opaque to regulators/users
- **Scalability ceiling** — monolithic data centres expensive and slow to expand

Codex addresses all of these through horizontal scaling: every new node adds capacity and redundancy.

## Key AI Use Cases

### 1. Training Dataset Storage & Access

- Store massive ML datasets immutably and cost-efficiently
- Codex scales horizontally — total storage grows with the number of nodes
- Enables AI companies to store and share datasets without centralised intermediaries
- Data stored with verifiable provenance (important for regulatory compliance)

### 2. Training Data Transparency & Provenance

A critical emerging requirement:
- Regulators and users increasingly demand visibility into what AI was trained on
- Codex enables transparent, verifiable records of training data on a distributed network
- Supports accountability for bias, accuracy, and compliance

### 3. AI Agent Persistent Storage

Decentralised storage enables AI agents to:
- **Persistently store, retrieve, and share data autonomously** in a trustless way
- Operate without reliance on centralised infrastructure
- Maintain public, censorship-resistant records of their configuration and training

### 4. Federated Learning Support

- In federated learning, models are trained across multiple devices/nodes without centralising raw data
- Codex provides durable distributed storage for intermediate model weights and datasets
- Improves data privacy — sensitive data never leaves its source

### 5. Monetised AI Models & Data Markets

- AI developers can publish models on Codex with smart contract-gated access
- Training data providers can monetise access to datasets
- Enables an open, collaborative AI economy without centralised gatekeepers

## Market Context

- Global decentralised cloud storage market projected to surpass **$4.5 billion by 2034**
- Global daily data generation exceeds **400 million terabytes**
- AI is the primary driver of the next wave of storage demand

## Codex Positioning vs. Filecoin/IPFS

Codex's "Decentralised Durability Engine" design differentiates it:
- Stronger **data durability guarantees** (erasure coding + storage proofs)
- Designed for **large, persistent datasets** not just file distribution
- Built to persist data even if the original uploader goes offline

## Relevance to Franck's Work

Strong basis for:
- RFP submissions targeting AI tooling and data infrastructure on Logos
- Identifying potential partnerships with AI data marketplaces
- PoC ideas: AI agent that stores its memory/state on Codex
