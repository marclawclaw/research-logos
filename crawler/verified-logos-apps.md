# Verified Third-Party Logos Apps & Modules
_Last updated: 2026-03-25_

| Name | Repo | Author | Description | Last Commit | First Discovered |
|------|------|--------|-------------|-------------|-----------------|
| logos-notes | [xAlisher/logos-notes](https://github.com/xAlisher/logos-notes) | xAlisher | Encrypted, local-first notes app for the Logos ecosystem, using Status Keycard hardware for key derivation. Implements the Logos module plugin interface and installs into Logos Basecamp. | 2026-03-19 | 2026-03-25 |
| keycard-basecamp | [xAlisher/keycard-basecamp](https://github.com/xAlisher/keycard-basecamp) | xAlisher | Standalone Keycard smartcard authentication module for Logos Basecamp — provides smartcard auth primitives (BIP32 key derivation, PIN verification, session management) consumable via `logos.callModule("keycard", ...)`. | 2026-03-24 | 2026-03-25 |
| logos-legos | [corpetty/logos-legos](https://github.com/corpetty/logos-legos) | corpetty | Visual workflow builder (ComfyUI/n8n-style) for Logos Core modules — compose Logos protocol operations (chat, wallet, blockchain, storage) into executable pipelines via a node-graph editor. Uses logos-cpp-sdk and `mkLogosModule`. | 2026-03-18 | 2026-03-25 |
| logos-workflow-registry | [corpetty/logos-workflow-registry](https://github.com/corpetty/logos-workflow-registry) | corpetty | Native Logos module (part of Logos Legos v2) that discovers loaded Logos modules, introspects their Q_INVOKABLE methods, and produces node type definitions for the workflow canvas and engine. | 2026-03-20 | 2026-03-25 |
| logos-workflow-canvas | [corpetty/logos-workflow-canvas](https://github.com/corpetty/logos-workflow-canvas) | corpetty | Native Qt/QML Logos UI module providing a visual workflow editor (QuickQanava-based graph), part of the Logos Legos v2 native architecture. Serializes workflows to JSON for the engine to execute. | 2026-03-20 | 2026-03-25 |
| logos-workflow-engine | [corpetty/logos-workflow-engine](https://github.com/corpetty/logos-workflow-engine) | corpetty | Native Logos module for headless workflow execution — takes a serialized workflow graph, performs topological DAG sorting, and dispatches each node through LogosAPI in dependency order. | 2026-03-20 | 2026-03-25 |
| logos-workflow-scheduler | [corpetty/logos-workflow-scheduler](https://github.com/corpetty/logos-workflow-scheduler) | corpetty | Native Logos module that manages cron/webhook triggers for deployed workflows, triggering the workflow engine on schedule. Part of the Logos Legos v2 native architecture. | 2026-03-20 | 2026-03-25 |
| logos-storage-app-skeleton | [logos-storage/logos-storage-app-skeleton](https://github.com/logos-storage/logos-storage-app-skeleton) | logos-storage | CLI application skeleton for Logos Storage, using Logos Core — companion to the Logos Storage Module API tutorial, providing an `app_main` entry point with the `LogosModules` object and Qt synchronization primitives. | 2026-03-24 | 2026-03-25 |

---

## Rejected False Positives

The following 64 repos were found by the crawler (via `LogosResult` signal only) but are **not** built on the Logos protocol. The `LogosResult` string is a common pattern in TypeScript, C#, and other languages unrelated to Logos.

| Repo | Reason |
|------|--------|
| devtorque/earningswidget | generic-class |
| OshanKHZ/bitbadges | badge-generator |
| midday-ai/midday | invoicing-SaaS |
| ManzanoHerchelle/parish-church-system | church-management |
| adoslabsproject-gif/nothumanallowed | AI-security |
| nicholasandyweb/bootflare | HTML-template |
| rh0kzy/EdenWebSite | website |
| Alastairian/Lando_ian-ips | unrelated |
| unimaginative-artist/SOMA | local-AI |
| denniske/winget-ui | winget-UI |
| kalou906/AKIG | real-estate |
| Apezdr/nextjs-stream | media-server |
| Xignite/swaggerhub | finance-API |
| Yuva-Nagasai/Flowing-into-the-future | unrelated |
| InfiniteRasa/Rasa.NET | game-emulator |
| aziwar/AZ-Digital-Hub | portfolio |
| lenselinksander-coder/PRSYS-TaoGate-v10 | governance-AI |
| CenterBLC/N1904 | bible-text |
| saulocantanhede/tfgreek2 | bible-text |
| tripplej33/AmpedFieldOps | business-mgmt |
| mclendening/EverIntent-smart-sites | web-agency |
| MarcIlunga/driving_coach | driving-app |
| babylonlabs-io/babylon-toolkit | BTC-staking |
| KASPACOM/kaspacom-web-wallet | Kaspa-wallet |
| ErikDevCode/BackendAJE.Api | backend-API |
| x-dash-io/AI-Genius-Lab | AI-tools |
| New-Vision-Creatives/NVC-WEBSITE | company-website |
| ximu3/kisaki | media-management |
| adornodavid/HerbaxCosteo | cost-tracking |
| jdmlcloud/OnPointAdmin | admin-panel |
| adnansamirswe/UU_COVER_PAGE | cover-page |
| Karthik1404-h/Budget-bot | budget-bot |
| jjmaxwell4/xignite-swagger | finance-API |
| czd890/xignite-swaggerhub | finance-API |
| juliocesarmiranda893-ops/topsun-crm | CRM |
| harujagdl/panel-haruja-TN--v2 | HTML-panel |
| morpheusxx/MediaPortal-LogoManager | TV-logos |
| ASPaes/aspdoctorsaas | doctor-SaaS |
| Macakoloko/p4ms11te | unrelated |
| nine9188/-sports-web-community | sports-community |
| Snassy-icp/swaprunner | ICP-DEX |
| EdwardYambasu12/Git | unrelated |
| Cross-Atlantic-Software/collegefinder | college-finder |
| risefootballagency/fuelforfootball | football-nutrition |
| Hellares/backend | backend |
| AlexandriaDAO/lbry.fun | ICP-launchpad |
| CristianH2/Proyecto-DentalNova | dental-clinic |
| JesusAntonioEscobedoRamon/NUTRIWEB6.0 | nutrition-web |
| cesar050/Campeonato | sports-mgmt |
| nickhaidukou/leon-init | unrelated |
| najmus-sakib-hossain/WEBSITE | website |
| vortechpe/ajebackend | backend |
| LOHITH5506H/Budget-bot | budget-bot |
| maria162003/clinikdent-v2-0 | dental-clinic |
| aavilacxc/aria_prod_actual | unrelated |
| josecarmengonzalezmata/NutriUweb | nutrition-web |
| mtrejo30/CoronaSanitarios | sanitation-mgmt |
| danielgomezpascual/request_mobility | mobility-app |
| WerWolv/libsteam | Steam-library |
| TJ-Frederick/TheologAI | Bible-MCP |
| vaneebentos/Catalogo-backend | catalog-backend |
| jazminewrooman/PrutechGMX | unrelated |
| vladzaharia/apollo | unrelated |
| zehnm/integration.kodi | Kodi-integration (empty/unverified — `Q_INTERFACES(PluginInterface) Logos` signal but repo is empty) |
