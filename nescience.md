# Nescience — Deep Dive

> Last updated: 2026-03-14

## What is Nescience?

Nescience is a **privacy-focused execution environment** developed under Vac (now Logos Research) that integrates privacy mechanisms from the ground up rather than as an afterthought. It is closely related to the Logos State Separation Architecture (LSSA) and the broader Logos Blockchain privacy infrastructure.

The name "nescience" means "lack of knowledge" — fitting for a system designed around zero-knowledge proofs.

**Source:** [forum.research.logos.co - IFT Research Call, September 10th 2025](https://forum.research.logos.co/t/ift-research-call-september-10th-2025-updates-on-the-development-of-nescience/566)

---

## Architecture & Design

### Account Storage Model
- Uses a **hashmap structure** mapping addresses to accounts
- Only maintains non-default accounts that have been actively modified
- Accounts never touched default to predefined values (storage efficiency optimization)

### Privacy Approach
- **Privacy-first by design:** Integrated from inception, not retrofitted
- **Selective privacy:** Applications can choose per-transaction whether privacy is necessary
- Private transactions use ZK proofs; public transactions remain efficient and inexpensive
- **Developer accessibility:** Abstracts cryptographic complexity so "developers can work with privacy features without needing deep cryptography knowledge"

### State Separation
Nescience embodies the **State Separation Architecture** concept:
- Clear separation between public and private states
- Both states remain interoperable
- Dual account model supporting public and private transfers

**Source:** [forum.research.logos.co](https://forum.research.logos.co/t/ift-research-call-september-10th-2025-updates-on-the-development-of-nescience/566)

---

## Development History (via Vac/Logos Research)

### 2024 Milestones
- Transitioned from exploration to practical development
- Released comprehensive reviews of **23 existing zero-knowledge virtual machines**
- Benchmarked **6 leading zkVMs** for performance metrics
- Implemented core components: execution types, UTXOs, cryptographic primitives
- Built and tested a **sandboxed testnet**

### 2025 Goals (from Vac 2024 recap)
- Complete **full-node implementation** with real-world scenario testing
- Production-readiness assessment

### September 2025 Research Call
- Updates on development progress shared at IFT Research Call
- Focus on making privacy accessible to developers without deep crypto expertise

**Source:** [research.logos.co/rlog/2024-recap](https://research.logos.co/rlog/2024-recap)

---

## Relationship to Logos Stack

Nescience feeds directly into the **Logos Blockchain** (formerly Nomos):

```
Nescience (privacy research) → LSSA (execution environment) → Logos Blockchain (Bedrock + Zones)
```

- **LSSA** is the first Sovereign Zone on Logos Blockchain, implementing the dual public/private state model that Nescience pioneered
- The Blend Network provides network-level privacy (traffic analysis resistance)
- Cryptarchia consensus adds proposer privacy via ZK proofs
- Together, these create a **multi-layered privacy architecture**

---

## Team & Resources

Nescience is developed by the **Applied Cryptography & ZK (ACZ)** service unit within Vac/Logos Research. The team:
- Researches and implements ZK argument systems
- Develops architectures for private computation
- Has published research on zkVM reviews and benchmarks
- Works on zerokit (ZK toolkit) and stealth address implementations

**Job postings** for "Zero Knowledge Research Engineer - Vac Nescience" have been listed, indicating active hiring.

**Source:** [research.logos.co/vsus](https://research.logos.co/vsus/), [beincrypto.com/jobs](https://beincrypto.com/jobs/p/zero-knowledge-research-engineer-vac-nescience-logos/)

---

## Analysis

### Strengths
- **Thorough research foundation:** Reviewing 23 zkVMs before building is exceptionally diligent
- **Privacy-by-default philosophy:** Not an add-on; architecturally integrated
- **Developer UX focus:** Abstracting crypto complexity is the right approach for adoption
- **Selective privacy model:** Practical — not all transactions need privacy (reduces overhead)

### Concerns
- **Limited public documentation:** Much of the work is discussed in research calls and internal forums, not in polished docs
- **No specific ZK system publicly committed to:** The team reviewed 23 zkVMs but hasn't publicly stated which system(s) they're using
- **Integration complexity:** Privacy at the execution layer is extremely challenging — few projects have achieved this at scale
- **Timeline unclear:** No public milestone dates for Nescience specifically (it's embedded in the LSSA/Blockchain timeline)

### Key Observation
> **Notable:** The 23-zkVM review is one of the most comprehensive comparative analyses in the ZK space. This research-first approach distinguishes Nescience from projects that pick a ZK system first and discover its limitations later. However, the lack of public documentation makes it hard to assess current progress.
