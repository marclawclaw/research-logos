---
topic: use-cases
type: research-notes
tags: [codex, waku, taco, access-control, encryption, privacy]
confidence: high
last_updated: 2026-03-14
sources:
  - https://blog.codex.storage/leveraging-taco-for-decentralised-access-control-on-codex/
  - https://blog.waku.org/waku-x-taco-p2p-comms-with-decentralised-encryption/
---

# Codex + TACo + Waku — Fully Decentralised Private Storage & Comms

## What Is TACo?

TACo (Threshold Access Control) provides **programmable, decentralised encryption** and access control.

Unlike centralised key management (AWS KMS, etc.), TACo:
- Distributes key management across a threshold network of nodes
- Allows access conditions to be expressed as smart contract logic
- Enables fine-grained, revocable permissions without any central authority

## The Stack: Waku + TACo + Codex

Each protocol solves a different layer:

| Layer | Protocol | Function |
|-------|----------|----------|
| Communication | Waku | P2P real-time messaging |
| Access Control | TACo | Decentralised encryption & permissions |
| Storage | Codex | Durable, censorship-resistant file storage |

Together they enable applications that are:
- **Private** — data encrypted, keys managed without centralised authority
- **Censorship-resistant** — no single point for takedown
- **Durable** — data persists even if nodes leave

## Waku × TACo

TACo encrypts messages sent over Waku, ensuring:
- Only authorised recipients can decrypt messages
- Encryption keys managed by a decentralised threshold network (not a server)
- Suitable for sensitive communication: whistleblowing, healthcare data, legal documents

## Codex × TACo

TACo provides decentralised access control for files stored on Codex:
- Files stored in encrypted form; only authorised parties can request decryption keys
- Access conditions can be time-limited, wallet-gated, or based on on-chain state
- Enables selective sharing of sensitive archival data (e.g., medical records, legal documents)

## Use Case Examples

1. **Encrypted collaborative research** — publish dataset on Codex, gate access via TACo to verified institutions
2. **Journalist secure drop** — receive sensitive documents over Waku (encrypted with TACo), stored on Codex
3. **Healthcare records** — patient data stored on Codex, access controlled by TACo (patient holds the key)
4. **Private AI training data marketplace** — datasets on Codex, TACo gates access based on payment/smart contract

## Relevance to Franck's Work

- Strong privacy-focused narrative combining three Logos stack components
- Codex + TACo combination is particularly relevant for enterprise and regulated industries
- PoC opportunity: access-controlled document vault using all three protocols
- Worth tracking as TACo integrations mature — good RFP angle
