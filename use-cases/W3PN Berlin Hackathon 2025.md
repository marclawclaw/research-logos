---
topic: use-cases
type: case-study
tags: [waku, hackathon, privacy, p2p, messaging, wallet-connect, geolocation]
confidence: high
source: https://blog.waku.org/waku-powers-p2p-comms-at-w3pn-berlin-hackathon/
event_date: 2025-06-13
---

# W3PN Berlin Hackathon 2025 — Waku Projects

**Event:** W3PN Hacks, Berlin — June 13–15, 2025  
**Organiser:** Web3Privacy Now (W3PN)  
**Focus:** Digital sovereignty, civil liberties, surveillance resistance  
**Waku projects:** 3 winners used Waku for p2p comms

---

## Aside

- **GitHub:** https://github.com/xAlisher/aside
- **Type:** Ephemeral, private messaging channel
- **Use case:** "Incognito Mode for conversations" — step outside a centralised messenger for sensitive discussions

### How it works
- Real-time p2p messaging via Waku with **zero persistence**
- No accounts, no media, no retry logic
- Messages only delivered when both participants are online; session ends → everything vanishes
- Session invites shared via clipboard; minimal bare-bones UI (intentionally)

### Why Waku
Waku's lightweight, decentralised design fits perfectly with the no-storage, no-tracking philosophy. No central relay to surveil or censor.

---

## Portal

- **GitHub:** https://github.com/sunsakis/portal/tree/waku2
- **Type:** Geolocation-based group chat with privacy
- **Use case:** Discover local chat rooms on a map, join discussions, no central infrastructure

### How it works
- Waku used as messaging transport with two channels: chat messages + friend requests/key exchanges
- Map-based room discovery
- PoC used Supabase for message history persistence; future intent is to replace with decentralised storage (e.g., Codex) for full trustlessness

### Potential
Could evolve into a fully autonomous comms layer for hyperlocal conversations — community notice boards, local activism, event coordination — without ever touching a central server.

---

## Open Lavatory

- **GitHub:** https://github.com/v3xlabs/open-lavatory
- **Type:** Decentralised dapp ↔ wallet connection protocol
- **Use case:** Replace WalletConnect's centralised relay server with a p2p alternative

### Problem
WalletConnect v2 (via @reown/appkit) hardcodes a central relay server — a centralised RPC endpoint that can be censored or captured.

### How it works
1. Dapp generates a keypair and shares a connection URL via QR code
2. Both peers use Waku for the **signalling phase** (replaces centralised relay)
3. After handshake, shifts to direct WebRTC communication with asymmetric encryption
4. Encrypted JSON-RPC messaging directly between devices — no intermediary

### Note
The team didn't fully integrate Waku during the hackathon itself, but the architecture design explicitly positions Waku as the decentralisation layer for wallet-dapp signalling.

---

## Takeaways for Logos Stack

| Theme | Insight |
|-------|---------|
| Ephemeral comms | Strong demand for zero-persistence chat — Waku's natural fit |
| Geolocation + privacy | Novel use case; Portal shows Waku + Codex as full decentralised stack |
| Wallet infrastructure | WalletConnect centralisation is a known pain point; Waku Sign (internal hackathon) + Open Lavatory both targeting this gap |
| Civil liberties tools | Non-commercial, principle-first builders are natural early adopters of Waku |

---

*See also:* [[Waku Hackathon Projects]] (internal Waku team hackathon — Waku Sign, Waku Phone, etc.), [[RealFi Hackathon 2025]]
