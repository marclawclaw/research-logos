---
topic: use-cases
type: integration
tags: [codex, akash, decentralised-compute, infrastructure, node-deployment]
confidence: medium
source: https://blog.codex.storage/deploying-a-codex-node-on-akash-network/
published: 2025
---

# Codex × Akash Network

**What:** Deploy and run a Codex storage node on Akash Network's decentralised compute marketplace — no local hardware required, no centralised cloud.

---

## Why It Matters

Codex needs a distributed network of compute nodes to store and serve files. Akash provides infrastructure where those nodes can live. Together they form a **fully decentralised stack** for file storage and serving:

- Codex = decentralised storage protocol (durability, censorship resistance)
- Akash = decentralised compute marketplace (buy/sell compute power via SDL deployments)

Neither requires a centralised cloud provider. This is the Web3-native infrastructure pairing.

---

## How It Works

1. Use the [Awesome-Akash Codex template](https://github.com/akash-network/awesome-akash/tree/master/codex) (SDL YAML file)
2. Import into Akash's SDL Builder, customise compute resources + env vars
3. Deploy — Codex node spins up in **Altruistic Mode** on Akash
4. Confirm participation via DHT debug endpoint (healthy DHT = peer discovery working)
5. Interact via SSH into Akash deployment for file uploads/retrieval by CID

### Current limitations
- Altruistic Mode only (no payment/marketplace guarantees yet — testnet was paused Aug 2025)
- Manual CID entry cumbersome via SDL Builder console; SSH strongly preferred
- Incentivised testnet + storage marketplace coming in future releases

---

## Strategic Value

| Angle | Detail |
|-------|--------|
| Decentralised infra stack | Codex + Akash = storage + compute both permissionless |
| Node operator accessibility | Run a node without owning hardware; lower barrier to participation |
| Censorship resistance | No AWS/GCP dependency in the full stack |
| Future marketplace | When Codex incentivised testnet launches, Akash nodes can participate as storage providers earning fees |

---

## Relevance for PoC Ideas

- Any Logos PoC that needs persistent storage without local hardware → Codex on Akash
- Combine with Waku for p2p comms layer: full Logos stack, zero centralised infra
- Good demo story: "Here's a fully decentralised app with no AWS anywhere in the stack"

---

*See also:* [[Codex Archival Storage]], [[Codex BitTorrent Integration]], [[FileHog]]
