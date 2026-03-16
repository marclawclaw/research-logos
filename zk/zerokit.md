---
topic: zk
type: library
tags: [zk, rln, rust, wasm, circom, groth16, privacy, spam-protection]
confidence: high
last_updated: 2026-03-16
sources:
  - https://github.com/vacp2p/zerokit
  - https://rfc.vac.dev/vac/raw/rln-v2
---

# Zerokit

**Repo:** https://github.com/vacp2p/zerokit  
**Org:** vacp2p (VAC / Logos)  
**Language:** Rust  
**License:** MIT / Apache 2.0  
**Published:** https://crates.io/crates/rln

## What It Is

Zerokit is a collection of Zero Knowledge cryptographic modules written in Rust, designed to be embedded in other system-level environments. It is the foundational ZK library for the Logos/Waku stack.

Current primary focus: **Rate-Limiting Nullifier (RLN)** — specifically RLNv2.

## Why It Exists

The Logos stack (Waku in particular) needs ZK capabilities embedded at the protocol level for spam protection, anonymous rate limiting, and privacy-preserving membership proofs. Zerokit provides these as portable, performant Rust primitives.

## Core Features

| Feature | Detail |
|---------|--------|
| **RLN Implementation** | Rate-Limiting Nullifier using zkSNARK (Groth16) |
| **Circom Compatibility** | ZK circuits written in Circom, loaded via ark-circom |
| **Cross-Platform** | Multi-arch via cross-rs (x86_64, ARM, etc.) |
| **FFI-Friendly** | C-compatible FFI for use in Nim, Go, and other languages |
| **WASM Support** | Compiles to WebAssembly for browser/JS environments |

## RLN Implementation Detail

- Based on spec: `https://rfc.vac.dev/vac/raw/rln-v2` (Logos LIP #106, status: raw)
- Uses **Circom circuits** through `ark-circom` for proof generation
- Proof system: **Groth16** (via `ark-circom`)
- Witness calculation: based on `circom-witnesscalc` by iden3
- RLNv2 adds configurable rate limits (messages per epoch per user)

### RLNv2 Sub-Protocols

RLNv2 generalises v1 (which was fixed at 1 message/epoch) and defines two subprotocols:

**RLN-Same** — uniform rate limit for all users  
**RLN-Diff** — per-user rate limits based on public data (e.g. stake, reputation)

Both follow the same three-step flow: **Registration → Signalling → Verification & Slashing**

### RLNv2 Circuit Math

For proof generation, the user submits:
```
identity_secret, path_elements (Merkle proof), x (signal_hash),
message_id, external_nullifier, message_limit
```

Output calculated as:
```
a_0 = identity_secret_hash
a_1 = poseidonHash([a_0, external_nullifier, message_id])
y   = a_0 + x * a_1
internal_nullifier = poseidonHash([a_1])
```

The circuit enforces that `internal_nullifier` repeats only if `message_id` exceeds the limit — triggering secret recovery (slashing) via Shamir's Secret Sharing.

### Circuit Parameters

- `DEPTH` — depth of membership Merkle tree (compile-time constant)
- `LIMIT_BIT_SIZE` — bit size of limit numbers (e.g. 16-bit → max limit 65535)

### RLN-Diff Registration

Recommended approach: publish `identity_secret_hash` (= `poseidonHash(identity_secret)`) and `user_message_limit` publicly. Smart contract / server computes:
```
rate_commitment = poseidonHash(identity_secret_hash, userMessageLimit)
```
Merkle tree leaves are `rate_commitments`, not raw `id_commitments`. Avoids expensive on-chain zkSNARK verification at registration time.

## Who Uses It

| Consumer | Notes |
|----------|-------|
| **nwaku** | Nim implementation of Waku v2 — primary production consumer |
| **js-rln** | JavaScript bindings for RLN (browser/Node apps) |

## Tech Stack / Dependencies

- `ark-circom` — Circom circuit loading + Groth16 proof gen
- `circom-witnesscalc` (iden3) — witness calculation (borrowed, not depended upon, due to type incompatibilities)
- `cross-rs` — cross-compilation for release assets
- Nix dev shell available (`nix develop`)

## Build Quick Reference

```bash
make installdeps   # install system deps
make build         # build all crates
make test          # run tests
cargo doc --open   # browse docs

# Cross-compile for specific target:
cross build --target x86_64-unknown-linux-gnu --release -p rln
```

## Relationship to Logos Stack

```
Logos Stack
└── Waku (privacy messaging layer)
    └── RLN (spam prevention + anonymous rate limiting)
        └── Zerokit (ZK primitives — Rust)
            ├── nwaku (Nim FFI)
            └── js-rln (JS/WASM bindings)
```

Zerokit sits at the cryptographic foundation. If Waku RLN is the policy layer, Zerokit is the proof engine.

## Open Questions / Gaps

- Is RLNv3 planned? The spec is at v2 (LIP #106, status: raw) — what's on the roadmap?
- Which chain hosts the RLN membership registry (Ethereum? Sepolia? Waku-internal)?
- Is there a benchmarking suite for proof generation latency on constrained devices (Raspberry Pi)?
- Are there plans to support proof systems beyond Groth16 (e.g., PLONK, Nova)?
- RLN-Diff allows stake/reputation-based rate limits — are there live examples of this being used?

## Acknowledgements (from repo)

- Inspired by [Applied ZKP](https://zkp.science/) group / [zk-kit](https://github.com/appliedzkp/zk-kit)
- Groth16 proof generation via [ark-circom](https://github.com/gakonst/ark-circom)
- Witness calculation via iden3's [circom-witnesscalc](https://github.com/iden3/circom-witnesscalc)
