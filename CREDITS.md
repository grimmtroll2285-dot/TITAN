# TITAN — authors, components and licenses

TITAN / **PLAY NO LIMIT by SirenaGoloviy** is the local distribution and integration. Original **TITAN CORE by devchmod** authorship and contributions remain credited: interface, multilingual navigation, installation, installed-package preparation, diagnostics and service integration. See [historical notices](CREDITS_HISTORY.md).

Thank you to **quer3q**, **EchoStretch**, **drakmor**, the PS5 payload SDK contributors and the homebrew community. Thank you to PS5 testers **@ImN3k1t** and **Владимир Барсук (@script_durova)** for reports and testing earlier builds. This acknowledgement does not imply they tested FIX12.

| FIX12 component | Upstream | Distribution/adaptation |
|---|---|---|
| Kraken Mount 0.3.2 | [quer3q/kraken-mount](https://github.com/quer3q/kraken-mount/releases/tag/v0.3.2) | Native mount/cache/registration/launch code adapted to TITAN safety, UI and updater |
| ampr-emu-ng 0.5.1 | [quer3q/ampr-emu-ng](https://github.com/quer3q/ampr-emu-ng/releases/tag/v0.5.1) | Official unmodified release binary; TITAN launch notice is separate in `src/launch.rs` |
| kstuff-lite 1.11 | [EchoStretch/kstuff-lite](https://github.com/EchoStretch/kstuff-lite/releases/tag/v1.11) | Unchanged embedded resident payload |
| ShadowMountPlus 1.7beta12-titan-isolated4 | [drakmor/ShadowMountPlus](https://github.com/drakmor/ShadowMountPlus) | Source-built TITAN adaptation: isolated ownership/registration and protected hosts; earlier automatic uninstall call sites disabled |
| PlayGo Stub 0.6 | [drakmor/pgo_stub](https://github.com/drakmor/pgo_stub) | Unchanged bundled library with TITAN integration and game selection |
| PS5 Dump Forge | [quer3q/ps5-dump-forge](https://github.com/quer3q/ps5-dump-forge) | Format/decoder and build workflow references |
| ps5-payload-sdk 0.43 | [ps5-payload-dev/sdk](https://github.com/ps5-payload-dev/sdk) | Payload build libraries and toolchain |
| SQLite 3.46.1 | [sqlite.org](https://sqlite.org/) | Registration database access, public domain |
| RustCrypto sha2 0.10.9 | [RustCrypto/hashes](https://github.com/RustCrypto/hashes) | Streaming integrity checks; dependency licenses retained |

Root license is GPL-3.0-or-later; see [LICENSE](LICENSE). Full corresponding TITAN source, vendored service sources, official AMPR source, component licenses, third-party notices and provenance are in the release asset **TITAN-SirenaGoloviy-fix12-source.zip**. GitHub's automatic Source code archive contains this distribution repository and is not the full payload source.

Original authorship and notices are retained. Historical custom-branded AMPR archives remain for provenance; FIX12 does not run those older binaries. No third-party game backport or Sony module is bundled by the catalog feature. Sparse/index/codec reader attributions remain in the full source and THIRD_PARTY_NOTICES.
