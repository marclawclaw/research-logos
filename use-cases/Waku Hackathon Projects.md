---
topic: use-cases
type: research-notes
tags: [waku, hackathon, poc, prototypes, 2025]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.waku.org/what-we-built-at-the-first-waku-internal-hackathon/
---

# Waku Internal Hackathon Projects (October 2025)

The Waku team ran their first internal hackathon in October 2025 to explore the stack's capabilities, assess library readiness, and build practical prototypes. Several projects have clear real-world potential.

## Waku Sign

**GitHub:** https://github.com/threeproto/waku-sign-extension  
**Category:** Web3 Transaction Signing

Decentralised alternative to WalletConnect. A browser extension that relays web3 transaction RPC requests (including digital signature requests) over the Waku network — no centralised infrastructure required.

- Retains the improved UX of WalletConnect
- Removes centralisation risks (censorship, infrastructure failure)
- Under consideration for integration into Waku SDK or Status app

---

## WhisperBox (also listed separately)

→ See [[WhisperBox Integration]]

---

## Waku Phone

**Application:** https://weboko.github.io/waku-phone/  
**Category:** Voice Communications

Mobile concept app for making **voice calls over the Waku protocol** using your existing contact list.

- Waku handles signalling
- WebRTC handles real-time voice (direct device-to-device)
- No centralised VoIP infrastructure
- Privacy-first alternative to Skype, WhatsApp, Signal calls
- Could be integrated directly into Status app

---

## Passkey for RLN

**GitHub:** https://github.com/waku-org/lab.waku.org/pull/117  
**Category:** Identity / UX Improvement

Explores using **passkeys to simplify RLN (Rate-Limiting Nullifier) credential management**:

- Users register and reconstruct their RLN keystore with a passkey
- Lowers barrier to entry for apps using RLN anti-spam
- Work may resume when real-world RLN integrations begin

---

## Waku Remote

**GitHub:** https://github.com/adklempner/tauri-waku/tree/hackathon  
**Category:** IoT / Device Control

Remote computer control via QR code scan (e.g., adjust volume from phone):

- Demonstrates **device-to-device P2P communication over Waku** — no centralised relay
- PoC for IoT, home servers, staking nodes, self-sovereign device management
- Needs refinement of live connection protocol for low-latency reliability

---

## WNS — Waku Name Service

**GitHub:** https://github.com/gabrielmer/waku-name-service  
**Category:** Identity / Name Resolution

Privacy-preserving name resolution system similar to ENS but:

- Operates over the Waku protocol
- Designed to **avoid linking domain names directly to wallet addresses** (unlike ENS)
- Preserves user privacy while enabling readable identifiers

---

## Summary Table

| Project | Category | Stack | Maturity |
|---------|----------|-------|----------|
| Waku Sign | Tx signing | Waku + browser extension | PoC |
| WhisperBox | Privacy forms | Waku | MVP |
| Waku Phone | VoIP | Waku + WebRTC | Concept |
| Passkey for RLN | Identity UX | Waku RLN | Exploratory |
| Waku Remote | IoT/device control | Waku + Tauri | PoC |
| WNS | Name service | Waku | Concept |

## Relevance to Franck's Work

These hackathon outputs are valuable for:
- Identifying PoC templates to build upon
- Understanding Waku's range of applicable use cases beyond messaging
- Informing Lambda prizes and RFP ideas
