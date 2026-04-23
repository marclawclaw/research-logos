---
tags: [logos, module, lgx, nix, developer-experience, sdk]
source: https://github.com/logos-co/logos-module-builder
---

# Logos Module Builder

Logos Module Builder (`logos-co/logos-module-builder`) is a shared Nix flake library that provides reusable build functions for Logos modules. It dramatically reduces the boilerplate required to create a new module from approximately 600 lines of build configuration to approximately 70 lines, and from 5 configuration files to 2.

## Core concept

A Logos module is a plugin that implements the `PluginInterface` and is managed by the Logos runtime (`liblogos_core`). Modules are built as shared libraries (`.so` on Linux, `.dylib` on macOS) and distributed as `.lgx` packages. The module builder handles the full build pipeline: CMake configuration, dependency resolution, Nix packaging, and LGX output generation.

The module builder is used by virtually all Logos modules in the ecosystem, including the package manager, storage, delivery, accounts, and chat modules.

## Qt plugins, not QML plugins

Logos modules are **Qt plugins** (C++ plugin architecture), not QML plugins. This distinction matters.

A **Qt plugin** is a compiled C++ shared library (`.so`/`.dylib`) that implements a Qt plugin interface. It is discovered and loaded at runtime via `QPluginLoader`. The plugin system uses:

- `Q_OBJECT` macro — enables Qt's meta-object system (signals, slots, introspection)
- `Q_PLUGIN_METADATA(IID ... FILE "metadata.json")` — declares the class as a Qt plugin with a plugin interface ID
- `Q_DECLARE_INTERFACE(PluginInterface, ...)` — registers the interface with Qt's plugin system
- `Q_INVOKABLE` — marks methods as callable from Qt's runtime introspection

A **QML plugin** is a different thing: it registers QML types with a QML engine via `qmlRegisterType()` so they can be used in QML declarative UI files. QML plugins are written in QML/JS and loaded by the QML runtime, not by `QPluginLoader`.

The concrete evidence from `logos-delivery-module` (a real production module):

```cpp
class DeliveryModulePlugin : public QObject, public DeliveryModuleInterface
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID DeliveryModuleInterface_iid FILE "metadata.json")
    Q_INTERFACES(DeliveryModuleInterface PluginInterface)
    // ... Q_INVOKABLE methods
};
```

And `logos_module.h` (the module loading library):

```cpp
QPluginLoader* m_loader = nullptr;
// Loaded via: QPluginLoader::load() → qobject_cast<T*>(instance)
```

The `logos_module` static library (`logos-co/logos-module`) wraps this pattern: it finds plugins by scanning module directories, loads them via `QPluginLoader`, and provides introspection APIs to query methods and metadata without instantiating the plugin.

**The `ui_qml` module type** is the one exception that can involve QML: `mkLogosQmlModule` produces a C++ Qt plugin that implements `LogosProviderPlugin` (the new API) or `PluginInterface` (legacy), and additionally bundles QML view files. The QML files are loaded by the host application (basecamp or standalone app), not by the plugin itself. The C++ plugin runs in a separate `ui-host` subprocess and communicates with the QML view via Qt Remote Objects over a private socket.

## The LGX package format

LGX (Logos Package Format) is the archive format used to distribute both Logos Modules (core plugins) and UI Apps (Qt plugins). An `.lgx` file is a bundle containing platform-specific binaries and metadata.

There are two runtime variants of an LGX package:

| Variant | Suffix | Description |
|---------|--------|-------------|
| Dev | `-dev` (e.g. `darwin-arm64-dev`) | Dynamic libraries resolve from `/nix/store` at runtime. Not portable. Requires Nix to be present. |
| Portable | no suffix (e.g. `darwin-arm64`) | All non-system/non-Qt transitive dependencies are copied alongside the library and rpaths are rewritten to use `@loader_path` (macOS) or `$ORIGIN` (Linux). Fully self-contained. Works without Nix. |

The distinction is controlled by the `nix-bundle-lgx` bundler:

```bash
# Dev variant — requires /nix/store at runtime
nix bundle --bundler github:logos-co/nix-bundle-lgx .#lib

# Portable variant — self-contained, no nix/store dependency
nix bundle --bundler github:logos-co/nix-bundle-lgx#portable .#lib
```

The `logos-module-builder` produces both `lib` and `lib-portable` outputs automatically when building a module, and the `lgx` output bundles the `lib` output while `lgx-portable` bundles `lib-portable`.

### Why two variants matter

The dev variant is suitable for local development where Nix is available and iteration speed matters. The portable variant is suitable for distribution to end users or CI systems that do not have Nix installed. The `logos-basecamp` desktop application and the standalone app both support loading either variant.

## Module types

The builder supports three module types, controlled by the `type` field in `metadata.json`:

| Type | Builder | Description |
|------|---------|-------------|
| `core` | `mkLogosModule` | Backend/logic module with no UI. Runs as a headless plugin in an isolated `logos_host` subprocess. |
| `ui` (legacy) | `mkLogosModule` | Legacy C++ UI widget module. Loaded by the desktop app in-process. |
| `ui_qml` | `mkLogosQmlModule` | QML view module with optional C++ backend. The QML view runs in the host application; the C++ backend runs in a separate `ui-host` subprocess (process-isolated). |

For QML modules, communication between the QML view and the C++ backend uses Qt Remote Objects over a private socket.

## Module metadata

The single source of truth for module configuration is `metadata.json`:

```json
{
  "name": "my_module",
  "version": "1.0.0",
  "type": "core",
  "category": "general",
  "description": "My custom Logos module",
  "main": "my_module_plugin",
  "dependencies": ["waku_module"],
  "nix": {
    "packages": {
      "build": ["protobuf"],
      "runtime": ["zstd"]
    }
  }
}
```

The top-level fields are embedded into the Qt plugin binary at compile time via `Q_PLUGIN_METADATA`. The `nix` block is used only by the build system and is ignored by the Qt runtime.

## Build outputs

When you run `nix build` in a module that uses `logos-module-builder`, the following outputs are produced:

| Output | What it produces |
|--------|-----------------|
| `lib` | The raw shared library (`.so` or `.dylib`) with nix-store rpaths |
| `lib-portable` | The shared library with rewritten rpaths (`$ORIGIN`/`@loader_path`) |
| `lgx` | LGX package bundling the dev variant |
| `lgx-portable` | LGX package bundling the portable variant |
| `install` | Builds, packages as LGX dev, and installs via `lgpm` |
| `install-portable` | Builds, packages as LGX portable, and installs via `lgpm` |
| `integration-test` | For `ui_qml` modules: builds and runs QML integration tests |

## Architecture of the build pipeline

The builder is structured as follows:

```
logos-module-builder/
├── lib/
│   ├── mkLogosModule.nix      # Builder for core + legacy ui modules
│   ├── mkLogosQmlModule.nix   # Builder for ui_qml modules
│   ├── buildCppPlugin.nix     # Shared C++ plugin build pipeline
│   ├── mkStandaloneApp.nix    # apps.default for nix run
│   ├── mkModuleLib.nix        # Library builder
│   ├── mkModuleInclude.nix    # Header generator
│   ├── mkExternalLib.nix      # External library handler
│   └── parseMetadata.nix      # metadata.json parser
├── cmake/
│   └── LogosModule.cmake      # Reusable CMake module
├── templates/                  # Module templates (nix flake init)
└── docs/                      # Configuration reference, getting started, etc.
```

The builder integrates with `nix-bundle-lgx` (for LGX packaging) and `nix-bundle-dir` (for portable rpath rewriting) as flake inputs.

## Relationship to logos-basecamp

`logos-basecamp` is the desktop application shell that hosts Logos modules. It discovers modules by scanning directories at startup. Both embedded modules (bundled at build time) and user-installed modules (placed in the user-writable modules directory) are discovered the same way. LGX packages are installed by the `package_manager` Logos Module, which extracts the appropriate platform variant to the correct directory.

A module built with `logos-module-builder` does not need to be modified to work with basecamp. Once its LGX package is installed, it appears in the Core Modules tab.

## Relationship to logos-scaffold

`logos-scaffold` is a CLI tool that bootstraps a fully runnable Logos application environment. It provides a higher-level workflow on top of `logos-module-builder`, handling project scaffolding, module registration, and environment setup.

## External library support

Modules can depend on external C/C++ libraries (not other Logos modules) via the `nix.external_libraries` field in `metadata.json`. The builder auto-detects whether the library is a Nix derivation or raw source and handles the build accordingly.

For modules that need both dev and portable variants of an external library, the structured `externalLibInputs` format in the Nix call allows specifying per-variant package mappings. When this format is used, the builder produces both `lib` and `lib-portable` outputs linked against the corresponding external library variants.

## Quick reference

```bash
# Create a new module from template
nix flake init -t github:logos-co/logos-module-builder

# Build dev variant
nix build .#lgx

# Build portable variant
nix build .#lgx-portable

# Build and install dev
nix build .#install

# Build and install portable
nix build .#install-portable

# Run QML module in standalone app
nix run .

# Run integration tests
nix build .#integration-test -L
```

## Key repos

- [logos-module-builder](https://github.com/logos-co/logos-module-builder): The shared Nix build library
- [nix-bundle-lgx](https://github.com/logos-co/nix-bundle-lgx): The bundler that produces `.lgx` files (dev vs portable variants)
- [nix-bundle-dir](https://github.com/logos-co/nix-bundle-dir): Handles rpath rewriting for portable bundles
- [logos-basecamp](https://github.com/logos-co/logos-basecamp): Desktop application shell
- [logos-standalone-app](https://github.com/logos-co/logos-standalone-app): Minimal host app for `nix run` of QML modules
- [logos-scaffold](https://github.com/logos-co/logos-scaffold): CLI bootstrapping tool
