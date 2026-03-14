---
topic: waku-messaging
type: concept
tags: [waku, content-topics, privacy, k-anonymity, filtering, protobuf]
confidence: high
last_updated: 2026-03-15
sources:
  - https://docs.waku.org/learn/concepts/content-topics
  - https://lip.logos.co/messaging/standards/core/10/waku2.html
---

# Waku Content Topics

## Summary

Content topics are metadata strings attached to outgoing messages that enable **protocol-level filtering** across [[Waku Relay]], [[Waku Filter]], and [[Waku Store]]. They're the primary mechanism for selectively retrieving only relevant messages without reading all traffic on a shard.

## Key Facts

- **Not encrypted** — content topics are visible to service nodes and peers
- **Privacy risk** — Filter, Store, and LightPush all share content topics with peers, enabling IP + interest correlation
- **Relay is safest** — GossipSub recipient anonymity can still be compromised if content topics expose user information
- **Format:** `/{application-name}/{version}/{content-topic-name}/{encoding}`
- **Recommended encoding:** Protocol Buffers (`proto`) for efficiency

## Format Breakdown

```
/{application-name}/{version}/{content-topic-name}/{encoding}

Example:
/supercrypto/1/notification/proto
/supercrypto/1/private-message/proto
```

| Segment | Purpose |
|---------|---------|
| `application-name` | Unique DApp name — prevents topic namespace collisions |
| `version` | Starts at 1; increment on breaking message format changes |
| `content-topic-name` | Descriptive topic name for the feature/type |
| `encoding` | Serialisation format (`proto` recommended) |

## Privacy Patterns

### 1. Avoid PII in Content Topics
Using personally identifiable information (e.g., a public key as content topic) is a **privacy leak**. Prefer bucket-based approaches.

### 2. K-Anonymity via Unified Topics
Using **one content topic per feature** (not per user) means multiple users share it — increasing the set of possible senders/receivers.

With 10,000 users on a single topic: **k = 10,000**.

### 3. Bucket-Based Traffic Distribution
For high-traffic apps using request/response protocols (Filter, Store), hash a unique identifier (recipient ID, public key, domain) and use the first byte as a bucket suffix:
- Topic: `/my-app/0/a/proto` (where `a` = first byte of hash)
- Divides traffic into 16 buckets (0–f in hex)
- Trades some k-anonymity for bandwidth efficiency
- k-value with 10,000 users: **10,000 / 16 = 625** per bucket

### 4. Use Protobuf for Feature Multiplexing
Rather than creating separate content topics per feature, use a **single topic with a Protobuf union message type**:

```protobuf
message NotificationPayload { ... }
message FeatureAbcPayload { ... }

// Only one field is set at a time
message Payload {
  NotificationPayload notification = 1;
  FeatureAbcPayload feature_abc = 2;
}
```

This maximises k-anonymity while retaining fine-grained functionality.

## How Protocols Use Content Topics

| Protocol | How it uses content topics | Privacy impact |
|----------|---------------------------|----------------|
| [[Waku Relay]] | Message routing via GossipSub shards | Best — recipient anonymity within mesh |
| [[Waku Filter]] | Client tells server: "subscribe to this topic" | Reduced — server learns your interests |
| [[Waku Store]] | Query by content topic for historical messages | Reduced — server learns your interests |
| [[Waku Lightpush]] | Embedded in forwarded messages | Medium — service node sees content topic |

## How it Relates to Logos

Content topics are a core building block for any application on the [[Logos Stack]] using Waku. Privacy-conscious design of content topic structure is essential to ensure Logos applications actually deliver on the stack's privacy-preserving promises. The [[Status]] app (built on Waku) has to carefully design topics to avoid leaking community membership or contact information.

## Open Questions

- Can content topic disclosure to Filter/Store service nodes be mitigated via ZK proofs (e.g., PIR — private information retrieval)?
- How does the [[Mixnet]] integration affect content topic privacy at the transport layer?
- Is there a standardised registry or catalogue of content topic namespaces to prevent collision?

## Sources

- https://docs.waku.org/learn/concepts/content-topics
- https://rfc.vac.dev/waku/informational/23/topics
