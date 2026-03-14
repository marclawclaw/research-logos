# Waku (Logos Messaging) — Deep Dive

> Last updated: 2026-03-14
> **Note:** Waku was rebranded to "Logos Messaging" in late 2025. waku.org now redirects to logos.co/tech-stack.

## What is Waku?

Waku is "a family of robust, censorship-resistant, peer-to-peer communication protocols that enable privacy-focused messaging for Web3 applications."

Key characteristics:
- **Not a blockchain** — no gas fees, no consensus needed
- **Ephemeral focus** — designed for real-time messaging, not long-term storage
- **Privacy-first** — encrypted, censorship-resistant communication
- **Built on libp2p** — extends the libp2p networking stack
- **Protobuf by default** — all protocols use Protocol Buffers

**Source:** [docs.waku.org](https://docs.waku.org), [rfc.vac.dev/waku](https://rfc.vac.dev/waku) (now [lip.logos.co/waku](https://lip.logos.co/waku))

---

## Protocol Architecture

Waku is a modular stack of protocols built on its core **Relay** protocol for pub/sub communication, with additional "value-added" service protocols.

### Core Protocols

| RFC | Protocol | Purpose |
|-----|----------|---------|
| 11/WAKU2-RELAY | **Relay** | Core pub/sub message propagation via GossipSub |
| 13/WAKU2-STORE | **Store** | Historical message retrieval for offline nodes |
| 12/WAKU2-FILTER | **Filter** | Bandwidth-efficient message filtering for light nodes |
| 19/WAKU2-LIGHTPUSH | **LightPush** | Message publishing for resource-constrained devices |
| 17/WAKU2-RLN-RELAY | **RLN Relay** | Privacy-preserving spam protection (experimental) |
| 14/WAKU2-MESSAGE | **Message** | Message payload format specification |
| 33/WAKU2-DISCV5 | **DiscV5** | Ambient peer discovery (modified Ethereum Node Discovery v5) |
| 34/WAKU2-PEER-EXCHANGE | **Peer Exchange** | Peer sharing between nodes |
| 23/WAKU2-TOPICS | **Topics** | Content topic naming conventions |
| 26/WAKU-PAYLOAD | **Payload** | Payload encryption and signing |

**Full RFC index:** [lip.logos.co/waku](https://lip.logos.co/waku) (formerly rfc.vac.dev/waku)

### How It Works

1. **Relay** forms the backbone — nodes form a GossipSub mesh and propagate messages
2. **LightPush** allows lightweight clients (browsers, phones) to publish messages through relay nodes without joining the mesh
3. **Filter** lets light clients subscribe to specific content topics without downloading all traffic
4. **Store** enables nodes that were offline to retrieve missed messages from store-capable peers
5. **RLN (Rate-Limiting Nullifier)** prevents spam using zero-knowledge proofs — users prove membership in a set without revealing identity, with rate limits enforced cryptographically

**Source:** [rfc.vac.dev/waku/standards/core/10/waku2](https://rfc.vac.dev/waku/standards/core/10/waku2)

---

## Implementations

### nwaku (Nim)
The reference implementation, written in Nim. Used in production by Status Desktop.
- **Repo:** [github.com/waku-org/nwaku](https://github.com/waku-org/nwaku) (now [github.com/logos-messaging/logos-messaging-nim](https://github.com/logos-messaging/logos-messaging-nim))
- Mature, full protocol support
- Being integrated into Status Desktop (replacing go-waku)

### js-waku (JavaScript/TypeScript)
Browser and Node.js SDK for building Waku-powered applications.
- Latest: js-waku v0.37.0 (preparation as of Oct 2025)
- Features: LightPush v3, improved peer longevity, experimental reliable channels
- React framework support added
- **Repo:** [github.com/waku-org/js-waku](https://github.com/waku-org/js-waku)

### go-waku (Go)
Go implementation, primarily used in Status mobile. Being phased out in favor of nwaku bindings.

**Source:** [blog.waku.org monthly updates](https://blog.waku.org/)

---

## Key Features & Recent Developments (2025)

### LightPush v3
Optimizations and error-handling improvements for resource-constrained devices. Includes mixnet integration.

### RLN (Rate-Limiting Nullifier)
- Privacy-preserving spam protection without accounts or fees
- Uses permissioned membership commitments
- All RLN tests in nwaku pass with updated contract architecture (major 2025 milestone)
- RLN v3 specification published: "Towards a Flexible and Cost-Efficient Implementation"

### Mixnet Integration
- libp2p mix integrated into LightPush
- Tested across multi-node simulations
- Provides network-level privacy (protects against traffic analysis)

### Reliable Channels
- "Reliable Channel API" proposed by lead Franck Royer
- Layered model separating message routing from application-level features (segmentation, rate limiting, data sync)
- End-to-end reliability integration with Status nearing completion

### Chat SDK
- Draft Noise protocol supporting multiple patterns (KN, KX, NN, XX)
- Segmentation specifications completed
- Private Chat SDK API roadmap under development

### AnonComms Enhancements (2026 roadmap)
- Capability discovery
- Mixnet deployment
- De-MLS (decentralized Message Layer Security) for group messaging

**Source:** [blog.waku.org/waku-monthly-update-october-2025](https://blog.waku.org/waku-monthly-update-october-2025/)

---

## Use Cases

1. **Chat applications** resistant to censorship (Status app)
2. **Off-chain voting** mechanisms
3. **NFT marketplace** interactions
4. **State channel** establishment
5. **Multi-signature wallet** coordination (Safe Harbour integration)
6. **Decentralized gaming** infrastructure
7. **Layer 2** transaction broadcasting
8. **Decentralized social media** platforms
9. **Threshold Access Control** for encrypted communications

**Source:** [docs.waku.org](https://docs.waku.org)

---

## Network & Adoption

### Known Integrations
- **Status** — Primary consumer; nwaku being integrated into Status Desktop
- **Safe Harbour** — Decentralized multisig operations
- **OpChan** — Privacy-preserving communications platform
- **RealFi Hackathon** winners: Shielded Micropay, Tohaku

### Community Events
- P2P Privacy Hacker Lounge (Buenos Aires, Nov 2025)
- Logos Circle events in 15+ cities globally
- RealFi Hackathon

**Source:** [blog.waku.org](https://blog.waku.org/), [press.logos.co](https://press.logos.co)

---

## Analysis

### Strengths
- **Production-ready:** The most mature component of the Logos stack; already deployed in Status
- **Modular design:** Clean separation of concerns across protocols
- **Privacy innovation:** RLN + Mixnet + Noise protocols provide layered privacy
- **Active development:** Monthly updates, regular releases, responsive to community
- **libp2p compatibility:** Builds on proven networking primitives

### Concerns
- **Rebranding disruption:** waku.org redirect and repo moves may confuse developers mid-integration
- **SDK maturity:** js-waku still pre-v1.0, API surface still evolving
- **Incentivization:** Still researching micropayment models for relay node operators (off-chain vs on-chain)
- **Documentation:** docs.waku.org had a 404 on the overview page during research (March 2026)

### Key Observation
> **Notable:** Waku is arguably the most production-tested part of the Logos stack, thanks to Status integration. However, the 2025 rebranding and repo migration (waku-org → logos-messaging) creates a transitional period where developer-facing resources are inconsistent.
