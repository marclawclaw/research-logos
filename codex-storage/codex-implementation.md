---
title: "Codex Implementation — logos-storage-nim (nim-codex)"
tags: [codex, logos, storage, nim, implementation, API, bindings, developer]
sources:
  - https://github.com/codex-storage/nim-codex
  - https://github.com/logos-storage/logos-storage-nim
  - https://api.codex.storage
created: 2026-03-14
updated: 2026-03-14
status: current
---

# Codex Implementation — logos-storage-nim

## Repository

- **Current:** `github.com/logos-storage/logos-storage-nim`
- **Former:** `github.com/codex-storage/nim-codex` (redirects to above)
- **Language:** Nim
- **License:** Apache-2.0 / MIT (dual)
- **Status:** Pre-alpha, active development

> "The Logos Storage project aims to create a filesharing client that allows sharing data privately in p2p networks."

## Building

```bash
# Clone and build
make update && make

# Parallel build (faster)
make -j12 update && make -j12

# Executable placed at:
build/storage
```

## Configuration (Priority Order)

1. CLI options (highest priority)
2. Environment variables
3. Configuration file (lowest priority)

```bash
# Run node
build/storage

# Show all options
build/storage --help
```

## REST API

- Full API docs: `api.codex.storage`
- Key endpoint: `POST /data` — upload a file, returns CID
- All node interactions go through REST API

## Language Bindings

### C API
- Logos Storage exposes a **C API** for cross-language use
- Bindings located in `library/` folder

### Go Bindings
- Provided in the main repo
- Example: `github.com/logos-storage/logos-storage-go-bindings-example`

### Rust Bindings
- External: `github.com/nipsysdev/storage-rust-bindings`

### Building the Library

```bash
# Dynamic library (default) — produces libstorage.so/.dylib/.dll
make libstorage

# Static library — produces libstorage.a
make STATIC=1 libstorage
```

**Important:** Callbacks into the library must be **fast and non-blocking** — slow callbacks will hang the working thread.

## Code Formatting

- Uses **nph** formatter (required for contributions)
- Setup: `make build-nph`
- Format files: `make nph/<file-or-folder>`
- Git pre-commit hook: `make install-nph-commit`
- VSCode: enable `nim.formatOnSave` with NimLang extension

## Versioning

- v0.2.0 — introduced Codex CLI Installer (Q1 2025)
- Tags: `github.com/codex-storage/nim-codex/releases`

## CI/CD

- CI: GitHub Actions (`actions/workflows/ci.yml`, branch: master)
- Docker: GitHub Actions (`actions/workflows/docker.yml`)
- Coverage: Codecov (`codecov.io/gh/logos-storage/logos-storage-nim`)

## Contribution

- Open to contributions — open issues or PRs
- Discord: `discord.gg/CaJTh24ddQ`

## Related Notes

- [[codex-p2p-protocol]] — How the protocol works (what this code implements)
- [[codex-overview]] — High-level Codex context
- [[codex-use-cases]] — What to build with the API
