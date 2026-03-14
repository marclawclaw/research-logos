---
topic: use-cases
type: research-notes
tags: [codex, personal-storage, backup, tool, poc]
confidence: high
last_updated: 2026-03-15
sources:
  - https://blog.codex.storage/exploring-filehog-decentralised-personal-storage-with-codex/
---

# FileHog — Decentralised Personal Folder Backup

## Summary

FileHog is a PoC CLI tool that watches a local folder and continuously uploads its contents to the Codex decentralised storage network. Designed for non-technical users as a privacy-preserving, cloud-free alternative to Google Drive / iCloud / Dropbox.

**GitHub:** https://github.com/benbierens/codex-filehog

## What It Does

- **Watch a folder** → auto-upload all files to Codex on change
- **Persistent contracts** → automatically renews storage contracts when they expire or fail
- **Retrieval log** → stores CIDs, timestamps, and purchase IDs in an output folder for future recovery
- **Background operation** → no ongoing user interaction needed once running

## Design Constraints (Current)

- File size: **1 MB – 1 GB** per file
- User must provide their own Codex node endpoint
- **No encryption in current Codex binary** (0.2.4) — users must pre-encrypt sensitive files
- Symmetric encryption expected in incentivised testnet release (TBA)
- Files assumed immutable after upload (no deletion/modification tracking yet)
- No GUI — headless, server-friendly

## Architecture Notes

Originally built as part of Codex's internal stress-testing suite. Key design question debated:

| Option | Pros | Cons |
|--------|------|------|
| Upload files individually | Selective retrieval | Inefficient if many small files (each needs its own contract) |
| Bundle into archives (tarballs) | Fewer contracts, less overhead | Can't retrieve individual files |
| **Hybrid (by subfolder/size)** | Balanced | More complex logic |

Proposed compromise: treat subfolders as datasets, use a dynamic size threshold to decide bundling.

## Origin

Developed by **Ben Bierens** from the Codex team. Presented at an internal Learn-Up session.

## Status

- **Stage:** Specification / PoC — working but not production-hardened
- Symmetric encryption integration coming with incentivised testnet
- Identified as an ideal entry point for contributor extensions (access control, multi-user sharing, encryption)

## Relevance to Franck's Work

- Directly relevant to Logos use case pitch: "privacy-first personal backup"
- Good PoC template for a polished product — UI layer + encryption wrapper would make this compelling
- RFP angle: durable personal storage as a Google Drive replacement on Logos stack
- Could extend with Waku for sharing CIDs between users (as demonstrated in the Codex+Waku file-sharing tutorial)
