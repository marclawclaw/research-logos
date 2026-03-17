# Logos Blockchain — Architecture

> Last updated: 2026-03-14

## Overview

The Logos Blockchain uses a **modular two-layer architecture** with three main concerns separated across layers:

```
┌────────────────────────────────────────────┐
│           Sovereign Zones / LSSA           │  ← Application layer
├────────────────────────────────────────────┤
│                  Mantle                    │  ← Execution layer
├────────────────────────────────────────────┤
│                  Bedrock                   │  ← Consensus + DA
└────────────────────────────────────────────┘
```

---

## Bedrock (Base Layer)

The base chain providing:
- **Consensus** via Cryptarchia (private PoS)
- **Data availability** (NomosDA — blob-based)
- **Settlement** for upper layers
- Bedrock does not attempt to validate or interpret Sovereign Rollup data — blobs are opaque to it

### Bedrock Services
Node operators can participate in Bedrock Services to earn rewards:
- **Service Declaration Protocol (SDP):** Registration and role declaration for service providers
- **Service Reward Distribution Protocol (SRDP):** Distributes rewards based on session tracking + activity verification
- SDP implementation was near-complete as of November 2025

---

## Mantle (Execution Layer)

Manages state updates from upper layers:
- **Mantle Channels:** Permissioned virtual blockchains for tracking Sovereign Zone state updates
- **Leadership lottery** that preserves winner anonymity (no hidden note information required)
- Transaction framework + mempool improvements throughout 2025
- Specification finalized: June 2025
- Redesigned in 2025 to exclusively support public notes (Sovereign Zones use private execution separately)
- Invalid transaction handling added to prevent block production disruptions (October 2025)

---

## Sovereign Zones

Blockchain execution environments built on Bedrock:
- Adhere to Nomos common specifications
- Constrained by ZK performance limitations (trade-off for privacy)
- First demonstrated prototype: **zkEVM rollup with state transitions verified by light clients** (April 2025)
- Planned 2026 features: decentralised sequencing, bridging, inter-Zone messaging

### Why Sovereign Rollups (not Ethereum-style rollups)?
Empirical data from Ethereum rollups justifies the Sovereign Rollup design:
- **14,500 users** used Optimism's LayerZero (non-canonical bridge) in a single week
- Only **243 users** used Optimism's canonical bridge
- Most rollup value is stored in assets NOT secured by L1 at all — making canonical bridges irrelevant

This validates the Logos approach: skip bridge contracts, give rollups full sovereignty.

### Sovereign Rollups (vs. Native Zones)
Logos also supports pure **Sovereign Rollups** — completely independent modular blockchains using Bedrock only for consensus ordering and data availability:
- Full freedom to define their own execution environment
- No on-chain smart contract verification required (unlike Ethereum L2s)
- State validity determined solely by rollup validators
- Data posted as blobs to NomosDA; blob commitments written on-chain
- Can use ZK validity proofs, fraud proofs, or re-execution — rollup's choice
- Suited for: gaming (fast state, isolated), high-frequency DeFi, web apps

### Native Zones (deferred)
Native Zones sharing a common ledger were deprioritized in 2025 in favor of Sovereign Zones. Left for a future release post-mainnet.

---

## LSSA / LEZ (Logos State Separation Architecture / Logos Execution Zone)

> **Note:** LSSA has been renamed to **LEZ (Logos Execution Zone)** as of early 2026. The name change reflects a shift from "state separation" to "execution zone" terminology. PR #182 in logos-docs captures this rename.

The first Sovereign Zone — the primary home for Logos applications:
- **Dual account model:** public accounts + private (shielded) accounts
- Supports public and private transfers
- Smart contract execution environment
- Relies on Bedrock for consensus + data availability
- Sequencer prototype demonstrated at Spain offsite (December 2025)
- LSSA is the primary focus for mainnet launch; other Zones will follow

**GitHub:** https://github.com/logos-blockchain/lssa

### NSSA / LSSA / LEZ — History and Architecture

> **Note:** NSSA → LSSA → LEZ are all the same project, just renamed over time. NSSA = Nescience State Separation Architecture, later renamed to Logos State Separation Architecture, then to Logos Execution Zone.

> ℹ️ The project is currently under development, and certain components may still change or be optimized. The purpose of this document is to provide an overview of Nescience's progress and background, offering context and references to supporting resources. For official specifications and the rationale behind specific design choices, please refer to the official documentation and related materials linked in the [resources section](https://www.notion.so/NSSA-Nescience-State-Separation-Architecture-2928f96fb65c80cc9f30e5a81bd1747f?pvs=21).

#### Background

Typically, public blockchains maintain a fully transparent state, where the mapping from addresses to account values is entirely visible. In NSSA, we introduce a parallel *private state*, a new layer of accounts that coexists with the public one. The public and private states can be viewed as a partition of the address space: accounts with public addresses are openly visible, while private accounts are accessible only to holders of the corresponding viewing keys. Consistency across both states is enforced through zero-knowledge proofs (ZKPs).

Public accounts are represented on-chain as a visible map from addresses to account states and are modified in-place when their values change. Private accounts, by contrast, are never stored in raw form on-chain. Each update creates a new commitment, which cryptographically binds the current value of the account while preserving privacy. Commitments of previous valid versions remain on-chain, but a nullifier set is maintained to mark old versions as spent, ensuring that only the most up-to-date version of each private account can be used in any execution.

#### Programmability and Selective Privacy

Our goal is to enable full programmability within this hybrid model, matching the flexibility and composability of public blockchains. Developers write and deploy programs in NSSA just as they would on any other blockchain. Privacy, along with the ability to execute programs involving any combination of public and private accounts, is handled entirely at the protocol level and available out of the box for all programs. From the program's perspective, all accounts are indistinguishable. This abstraction allows developers to focus purely on business logic, while the system transparently enforces privacy and consistency guarantees.

To the best of our knowledge, this approach is unique to Nescience. Other programmable blockchains with a focus on privacy typically adopt a developer-driven model for private execution, meaning that dApp logic must explicitly handle private inputs correctly. In contrast, Nescience handles privacy at the protocol level, so developers do not need to modify their programs—private and public accounts are treated uniformly, and privacy-preserving execution is available out of the box.

#### Token Creation and Transfers (Example)

**1. Token creation (public execution):**
- Alice submits a transaction to execute the token program create function on-chain.
- A new public token account is created, representing the token.
- The minted tokens are recorded on-chain and fully visible on Alice's public account.

**2. Transfer from public to private (local / privacy-preserving execution):**
- Alice executes the token program transfer function locally, specifying a Bob's private account as recipient.
- A ZKP of correct execution is generated.
- The proof is submitted to the blockchain, and validator nodes verify it.
- Alice's public account balance is modified accordingly.
- Bob's private account and balance remain hidden, while the transfer is provably valid.

**3. Transfer from private to public (local / privacy-preserving execution):**
- Bob executes the token program transfer function locally, specifying a Charlie's public account as recipient.
- A ZKP of correct execution is generated.
- Bob's private account and balance still remain hidden.
- Charlie's public account is modified with the new tokens added.

**4. Transfer from public to public (public execution):**
- Alice submits a transaction to execute the token program transfer function on-chain, specifying Charlie's public account as recipient.
- The execution is handled on-chain without ZKPs involved.
- Alice's and Charlie's accounts are modified according to the transaction.

**Key points:**
- The same token program is used in all executions.
- The difference lies in execution mode: public executions update visible accounts on-chain, while private executions rely on ZKPs.
- Validators only need to verify proofs for privacy-preserving transactions, keeping processing efficient.

#### The Account Model

To achieve both state separation and full programmability, NSSA adopts a stateless program model and a data layout similar to Solana's. Programs do not hold internal state; instead, all persistent data resides in accounts explicitly passed to the program during execution. This design enables fine-grained control over access and visibility while maintaining composability across public and private states.

#### Execution Types

Execution is divided into two fundamentally distinct types based on how they are processed: **public execution**, which is executed transparently on-chain, and **private execution**, which occurs off-chain. For private execution, the blockchain relies on ZKPs to verify the correctness of execution and ensure that all system invariants are preserved.

Both public and private executions of the same program are enforced to use the same Risc0 VM bytecode. For public transactions, programs are executed directly on-chain like any standard RISC-V VM execution, without generating or verifying proofs. For privacy-preserving transactions, users generate Risc0 ZKPs of correct execution, and validator nodes only verify these proofs rather than re-executing the program. This design ensures that from a validator's perspective, public transactions are processed as quickly as any RISC-V–based VM, while verification of ZKPs keeps privacy-preserving transactions efficient as well. Additionally, the system naturally supports parallel execution similar to Solana, further increasing throughput. The main computational bottleneck for privacy-preserving transactions lies on the user side, in generating ZKPs.

#### Resources

- [IFT Research call](https://forum.vac.dev/t/ift-research-call-september-10th-2025-updates-on-the-development-of-nescience/566)
- [Goals for Q4 Testnet](https://www.notion.so/State-separation-architecture-PoC-27a8f96fb65c80eb9fe7dbe0ee97843a?pvs=21)
- [NSSA vs other privacy projects](https://www.notion.so/Privacy-projects-comparison-2688f96fb65c8096b694ecf7e4deca30?pvs=21)
- [Choice of VM/zkVM](https://www.notion.so/Conclusion-on-the-chosen-VM-and-zkVM-for-LSSA-2318f96fb65c806a810ed1300f56992d?pvs=21)
- [NSSA state model](https://www.notion.so/State-model-decision-2388f96fb65c80758b20c76de07b1fcc?pvs=21)
- [NSSA v0.2 specs](https://www.notion.so/NSSA-v0-2-specifications-2848f96fb65c800c9818e6f66d9be8f2?pvs=21)
- [NSSA sequencer specs](https://www.notion.so/Sequencer-specs-2428f96fb65c802da2bfea7b0b214ecb?pvs=21)
- [NSSA sequencer code](https://www.notion.so/LSSA-sequencer-pseudocode-2508f96fb65c805e8859e047dffd6785?pvs=21)
- [NSSA key protocol](https://www.notion.so/Concrete-key-protocol-specifications-23b8f96fb65c8011b488c8fe0d2f87ae?pvs=21)
- [NSSA Token program design](https://www.notion.so/Token-program-design-2538f96fb65c80a1b4bdc4fd9dd162d7?pvs=21)
- [NSSA cross program calls](https://www.notion.so/LSSA-cross-program-calls-Tail-call-model-proposal-extended-version-2838f96fb65c8096b3a2d390444193b6?pvs=21)
- [NSSA AMM specs](https://www.notion.so/AMM-spec-28a8f96fb65c80bf93edde876c5a6932?pvs=21)
- [Client-side proving benchmarks](https://www.notion.so/Client-side-proving-benchmarks-2a38f96fb65c80019e6cea87b0ff3331?pvs=21)
- [Transactions processing performance](https://www.notion.so/Performance-tests-report-2968f96fb65c800bb96bd1a10fc95739?pvs=21)

---

## Aztec Network (Privacy-First Ethereum Rollup)

*Aztec* is a Layer-2 zk-rollup on Ethereum that focuses on privacy. It is essentially an off-chain network where transactions are processed with encryption and then verified on Ethereum via ZKPs. Aztec uses a hybrid model combining UTXO-style notes with smart contract programmability. In Aztec's new design, an entire smart contract's state can be represented inside a UTXO (note) committed to the rollup.

### Similarities to NSSA

Both Aztec and NSSA support hybrid public/private execution. Aztec is often called the first hybrid ZK rollup because it plans to support normal public smart contract functions alongside private ones. This is analogous to NSSA's dual execution types since Aztec allows some contract calls to be public (for efficiency) and others to be private as needed. Both systems use a form of UTXO model for private assets: Aztec's internal notes system is akin to UTXOs, helping hide values and parties similar to NSSA's private state.

### Key Differences

- Aztec's privacy model is more developer-driven whereas NSSA's is user-driven. In Aztec, programmable privacy means dApp developers decide what parts of a contract are secret or public in the code. For example, a developer might design a confidential voting contract on Aztec where votes are hidden by default. By contrast, NSSA lets the user choose per transaction (public, private, shielded, deshielded), even within the same dApp. This gives NSSA greater flexibility: privacy isn't all-or-nothing at the application level, but adjustable by end-users as needs change.
- Another difference is platform and security model: Aztec operates as an L2 rollup, inheriting Ethereum's security and consensus. NSSA is an L1 architecture (or an L2 framework deployable on any chain), which means it could run as a sovereign chain or as a rollup on various L1s.
- Aztec's reliance on Ethereum means data availability and throughput are tied to Ethereum (all Aztec transactions ultimately settle on Ethereum), whereas NSSA could potentially be tailored for higher throughput by being its own chain or a rollup with dedicated data availability solutions.

### Why NSSA Might Do Better

- User empowerment and flexibility are NSSA's strong points. Unlike Aztec where privacy features are baked into the dApp by the developer, NSSA's selective privacy lets users decide the privacy level of each interaction. This could cater to a broader range of use-cases. For instance, casual users can default to transparency (for simplicity or lower cost) and only use privacy when needed, whereas power users or sensitive transactions can opt into full anonymity. Such flexibility can drive adoption by easing users in, rather than requiring everything be private from the start.
- NSSA's public execution mode avoids ZKPs overhead when privacy isn't needed, giving it a performance edge in scenarios where full privacy is overkill. Aztec, on the other hand, is privacy-by-default within its rollup, which maximizes anonymity but means even simple transactions incur zk proving costs (Aztec is addressing this by mixing public contracts, but proofs are still central).
- Finally, because NSSA can be deployed on any base chain, it is more ecosystem-agnostic. Projects don't have to leave their L1 to gain NSSA's capabilities. NSSA could run as a modular rollup attached to those ecosystems. Aztec is currently tied to Ethereum, so projects on other chains can't easily benefit from it without bridging.

In summary, NSSA offers more adaptability: it can achieve privacy where needed while preserving transparency and efficiency elsewhere, which is a compelling advantage in terms of usability and integration.

---

## Aleo (Private Smart Contract L1)

*Aleo* is a Layer-1 blockchain built for privacy-preserving smart contracts. It employs the paradigm of execute off-chain, verify on-chain using ZKPs, based on the academic ZEXE model. In Aleo, transactions are executed privately by the user off-chain (computing the state changes and a proof), and a succinct ZKP of the execution is posted on-chain to verify and update the ledger state. The core state model is the record model, an evolution of the UTXO model from Zcash, which allows storing arbitrary data in encrypted records rather than just currency amounts. This means Aleo can support complex application state and multiple assets, all kept private within these records. There is no global account balance visible on-chain: all we see are commitments to records and proofs of valid state transitions. Aleo provides a new programming language (Leo) for developers to write programs that compile into zk circuits, enabling general-purpose private applications. It's essentially privacy-by-default and programmable: every execution yields a proof, and by design users' inputs, outputs, and identities can be concealed.

### Similarities to NSSA

- Both Aleo and NSSA aim for general-purpose privacy beyond simple token transfers. Each supports private state based on a UTXO-like model: Aleo's records vs NSSA's private notes, which means they can conceal user balances and contract storage in a way that account-model chains cannot.
- Both also strive for scalability via off-chain execution: Aleo avoids on-chain execution cost by having miners only verify proofs (no gas for running transaction logic), and NSSA similarly avoids zk costs when not needed and only verifies proofs for private txns.
- In terms of capabilities, each allows smart contract logic with privacy.

### Key Differences

- Aleo is privacy-by-default and does not natively support transparent transactions or accounts: every meaningful action produces a ZKP and touches the shielded state. This maximizes the size of the shielded set (everyone is using privacy, boosting anonymity), but it also means Aleo lacks flexibility for those who might want plain public transactions. NSSA, by contrast, allows opting out of privacy per transaction. Users can have public interactions that are handled normally and choose privacy only when needed. This selective approach means NSSA can accommodate scenarios Aleo finds challenging, for example, revealing certain data to satisfy regulations or audits without exposing everything.
- Aleo built a new blockchain from the ground up optimized for zk, even choosing custom elliptic curves and cryptographic primitives that suit zk. Aleo's all-new L1 may achieve tighter integration of ZKPs at the protocol level, but it comes with the challenge of attracting users and developers to a new ecosystem. NSSA's approach, on the other hand, can leverage existing consensus and cryptographic frameworks. As a standalone chain, NSSA will have to establish its own network and security, but it may adopt proven consensus mechanisms and widely used cryptographic libraries rather than inventing everything from scratch.

### Why NSSA Might Do Better

- NSSA's selective privacy model provides more flexibility than Aleo's privacy-by-default approach. Users can choose public or private execution per transaction, accommodating regulatory compliance, audit scenarios, or simply cost-conscious users who don't always need full privacy.
- NSSA's hybrid execution (public + private in the same program) reduces overhead when full privacy isn't required, potentially offering better performance for common use cases.
- NSSA's ability to run as a modular rollup on various L1s (rather than being locked to its own L1) provides deployment flexibility that Aleo's L1-only model lacks.

---

## Mina Protocol (Succinct Blockchain with zkApps)

*Mina protocol* is an L1 blockchain known for its tiny blockchain size (~22 KB) and use of recursive zk-SNARKs to maintain a constant-sized proof of the network state. Privacy in Mina comes into play through zkApps. Unlike Aleo, Mina's base ledger is account-based and transparent: account balances and addresses are public, and transactions are visible on-chain. Privacy is achieved at the application layer by incorporating proofs in transactions. For example, a Mina zkApp could let a user prove they possess certain credentials or attributes without disclosing them, or prove that a secret computation yielded a certain result, all within a transaction that updates the on-chain state minimally.

### Similarities to NSSA

- Both Mina and NSSA use ZKPs to enable privacy at the application level. Mina's zkApps can hide certain transaction details while proving validity, similar to how NSSA's private transactions use ZKPs.
- Both support hybrid models: Mina has a transparent base layer with optional privacy at the app level, while NSSA has public and private execution modes within the same architecture.
- Both aim for scalability through ZKPs — Mina's recursive proofs keep the chain small, while NSSA's off-chain execution with on-chain verification reduces on-chain computation.

### Key Differences

- Mina's privacy is opt-in at the application level (developers must build zkApps), whereas NSSA provides privacy at the protocol level, making it available for any transaction without special developer effort.
- Mina uses an account-based model for its transparent state, while NSSA uses a UTXO-like model for private state (similar to Aztec/Aleo).
- Mina's unique value proposition is constant chain size (~22KB), which is a different design goal from NSSA's state separation architecture.

### Why NSSA Might Do Better

- NSSA's protocol-level privacy means every user automatically gets privacy benefits without requiring developers to build custom zk circuits. This lowers the barrier to entry for privacy-preserving applications.
- NSSA's hybrid public/private execution model is more flexible than Mina's app-layer approach, allowing users to switch between public and private modes without changing applications.
- NSSA's selective privacy model provides better UX for gradual adoption, as users can start with transparent transactions and opt into privacy as needed.

---

## Tokenomics

- Full tokenomics framework established: August 2025
- Block rewards + execution markets designed
- Minimum stake estimation analysis completed for SDP
- Block reward evaluations used as inputs for protocol implementation
- Economic model includes incentives for Bedrock Service providers (SDP rewards)
