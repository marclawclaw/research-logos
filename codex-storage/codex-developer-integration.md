---
title: "Codex – Developer Integration & REST API"
tags: [logos, codex, storage, api, developer, integration, rest]
created: 2026-03-16
updated: 2026-03-16
sources:
  - https://blog.codex.storage/how-to-interact-with-a-codex-node/
  - https://blog.codex.storage/protocol-breakdown-how-the-codex-p2p-network-works/
  - https://blog.codex.storage/codex-factory-creating-local-codex-clusters-for-developers/
---

# Codex – Developer Integration & REST API

## Node Setup Options

### 1. CLI Installer (Recommended for new users)
- Guides through port forwarding and configuration
- Optional: link ERC-20 wallet address for future incentives
- Auto-reports to testnet metrics dashboard

### 2. Direct Binary
- Configure manually from Codex documentation
- Full control over all parameters

### 3. Dappnode Package
- `codex-storage/DAppNodePackage-codex` on GitHub
- One-click install in Dappnode UI

### 4. Codex Factory (For developers/testing)
- CLI tool for spinning up **local Codex clusters**
- Developed by Adam Uhlíř (Codex team)
- Streamlines multi-node dev/test environments without connecting to testnet

## REST API Reference

Full docs at: https://api.codex.storage

### Key Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/debug` | Node health check |
| POST | `/data` | Upload a file → returns CID |
| GET | `/data/{cid}` | Download file from local node |
| GET | `/data/{cid}/network/` | Download file from network |

### Upload Flow (Persistence Mode)
1. `POST /data` → receive CID
2. Node erasure-codes and builds Verifiable Manifest
3. Submit CID to smart contract for storage request

## Tooling

- **Insomnia / Postman**: recommended for API exploration and manual testing
- **REST API**: all network capabilities exposed programmatically
- **Codex App UI**: browser-based interface for non-technical node interaction

## Default Port Configuration

```
UDP 8090  – peer discovery
TCP 8070  – block exchange
TCP 8080  – REST API
```

Ports are configurable to avoid conflicts.

## Building Applications on Codex

Codex provides building blocks for fully decentralised apps:

- **Storage**: Codex (durable, censorship-resistant)
- **Messaging**: Waku (p2p comms, metadata/link sharing)
- **Access Control**: TACo (decentralised encryption + programmable access conditions)
- **Compute/Hosting**: Akash Network (decentralised compute for node hosting)
- **Blockchain**: Status Network L2 (gasless, for on-chain logic)

### Reference Implementation: Cyphershare
A working dapp demonstrating Codex + Waku + TACo:
- Files encrypted in-browser before upload
- TACo conditions control who can decrypt (e.g. token holders, time windows)
- Waku handles metadata/link delivery
- No central server at any layer
- Live: https://share.hackyguru.com

## Related Notes

- [[codex-p2p-network]] — CIDs, node ports, retrieval
- [[codex-integrations]] — Full list of ecosystem integrations
- [[codex-dde-architecture]] — How data is stored and verified under the hood
