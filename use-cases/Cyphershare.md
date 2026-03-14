---
topic: use-cases
type: research-notes
tags: [codex, waku, taco, file-sharing, encryption, access-control, poc]
confidence: high
last_updated: 2026-03-15
sources:
  - https://blog.waku.org/waku-x-taco-p2p-comms-with-decentralised-encryption/
  - https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
---

# Cyphershare — Decentralised Encrypted File Sharing

## Summary

Cyphershare is a PoC app demonstrating the full Logos stack (Waku + Codex + TACo) working together to deliver private, censorship-resistant, access-controlled file sharing — entirely in-browser, no servers.

**Live app:** https://share.hackyguru.com  
**Origin:** Built by Guru (IFT contributor), originally a Waku+Codex PoC, later extended with TACo

## How It Works

| Component | Role |
|-----------|------|
| **Codex** | Stores the encrypted file durably on the decentralised network |
| **Waku** | P2P transport for metadata (file CIDs, notifications, sharing events) — serverless |
| **TACo** | Decentralised access control — defines who can decrypt and under what conditions |

### Flow

1. User selects a file in the browser
2. File is **encrypted client-side** before upload
3. Encrypted data is uploaded to Codex → CID generated
4. Waku broadcasts metadata (CID + access policy) to the intended recipient
5. TACo access conditions determine who can decrypt (token ownership, group membership, time window, etc.)
6. Recipient downloads encrypted file from Codex, requests decryption key from TACo cohort

## What TACo Adds

Traditional E2E encryption puts trust in a single key server or client. TACo instead:
- Uses a **decentralised cohort of nodes** for collaborative key generation
- Conditions are **programmable**: "decrypt only if holder of NFT X" / "decrypt only before timestamp T"
- No single point of failure or censorship

## Use Case Examples Enabled by This Stack

- **Secure document sharing**: Researchers sharing datasets with conditional access
- **Governance voting**: Votes encrypted until tally time via TACo time-lock
- **Token-gated content**: Creators selling encrypted media — access unlocked on token ownership
- **Whistleblower tools**: Submit files that only authorised parties can read

## Status

- **Stage:** Live PoC (not production-hardened)
- Waku and TACo both under active development
- TACo mainnet production-ready with full decentralised key generation

## Related

- [[Codex TACo Integration]] — deeper dive on Codex+TACo pairing
- [[Waku Hackathon Projects]] — WhisperBox uses similar Waku-only pattern for forms

## Relevance to Franck's Work

- Best single demo of the full Logos stack working end-to-end
- Strong candidate for a polished PoC or Lambda prize pitch
- Illustrates the "three legs" thesis: Waku (comms) + Codex (storage) + TACo (access) = sovereign app infra
