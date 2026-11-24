# Historical integration notes

Archived attribution and component history through FIX11. Version claims below describe historical builds; see CREDITS.md for FIX12.

# Development, thanks and licenses

## TITAN CORE вЂ” devchmod

TITAN CORE is maintained by **[devchmod](https://github.com/devchmod)**, following six months of independent research. Project work includes the TITAN CORE interface and branding, multilingual navigation, USB FPKG installer, installed-package preparation and legacy import recovery, diagnostics and reporting, and integration of the resident services.

**Installed-PKG launch handling is a TITAN CORE addition:** the earlier workflow brought supported Debug Settings/Overdrive installs into a playable homebrew library without retaining another complete PKG, with successful console use reported by the maintainer on firmware 13.60. Current versions keep eligible packages at their original system path and recover receipt-proven earlier imports, while retaining the native cache and launch engine. The maintainer confirmed original-path launch and full System storage sizes on the development console with 0.5.7-beta.1; see docs/USER_HARDWARE_CONFIRMATION.md. Native cache uses additional space.

Development also addresses package discovery and duplicate library filters. Build checks and documented tests are included in this repository; see [validation](docs/VALIDATION.md) for their scope.

## Thanks to the upstream developers

Thank you to **quer3q**, **EchoStretch**, **drakmor**, the **PS5 payload SDK contributors**, and the wider homebrew community for sharing their code, tools and research. Their contributions support the components listed below. TITAN CORE development and integration are described above; each upstream project retains credit for its own code.

## Included components

| Component | Upstream | Role |
|---|---|---|
| Kraken Mount 0.3.0 (TITAN integration) | [quer3q/kraken-mount](https://github.com/quer3q/kraken-mount) | Native FPKG/folder mounting, cache, registration and launch code used and adapted in TITAN CORE |
| ampr-emu-ng 0.4.1 | [quer3q/ampr-emu-ng](https://github.com/quer3q/ampr-emu-ng/tree/v0.4.1) | Packed-game runtime; custom launch notice `PLAY NO LIMIT` (component UI label `chmod v0.1`) |
| kstuff-lite 1.11 | [EchoStretch/kstuff-lite](https://github.com/EchoStretch/kstuff-lite/releases/tag/v1.11) | Pinned resident payload, embedded unchanged |
| ShadowMountPlus 1.7beta10 | [drakmor/ShadowMountPlus](https://github.com/drakmor/ShadowMountPlus/releases/tag/1.7beta10) | Pinned image service, embedded unchanged |
| PS5 Dump Forge | [quer3q/ps5-dump-forge](https://github.com/quer3q/ps5-dump-forge) | Toolchain/workflow references and attributed sparse-format reader reference |
| ps5-payload-sdk | [ps5-payload-dev/sdk](https://github.com/ps5-payload-dev/sdk) | Payload build toolchain and PS5 libraries |

## Source and notices

- Root license: GPL-3.0-or-later; see [LICENSE](LICENSE).
- Existing dependency notices: [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES).
- Pinned service versions, original source snapshots, component licenses and hashes: [vendor/unified](vendor/unified).
- Original AMPR 0.4.0 binary/source and custom display-only runtime source: [vendor/ampr-emu-ng](vendor/ampr-emu-ng), including [branding explanation](vendor/ampr-emu-ng/TITAN_BRANDING.md).
- Sparse-format port attribution and exact source reference: [vendor/format-reference](vendor/format-reference).
- TITAN CORE artwork provenance: [docs/branding/PROVENANCE.md](docs/branding/PROVENANCE.md).

The current custom AMPR source changes only the launch-notice text to PLAY NO LIMIT. Compatible filenames, exported runtime identity and underlying engine version remain upstream 0.4.0. Upstream credits in source archives are preserved. Additional third-party code retains its own license terms; consult the included notices/source for each component.

## Reader and decoder source references

The renamed `crates/titan-core-pkg/src/layout.rs` is the existing layout reader previously named `kraken.rs`. It ports the upstream `VF/kraken_image.rs:728-1036` describe logic and `FP/mount.rs:35-283` block/layout logic. Its sparse handling references `vendor/ps5upload-fpkg/src/kraken_image.rs` (GPL-3.0-or-later). The decoder ports the Kraken block decoder vendored by ps5-dump-forge: `kraken.rs` (bit reader, arrays and LZ), `kraken/huff.rs` (Huffman helpers) and `kraken_image.rs::decode_described`. Neutral local names do not change the compression format or its authorship. AMPR codec-2 index encoding follows the upstream `ng/KRAKEN.md` contract.

## Local Kraken 0.2.1 integration

This fork incorporates Kraken Mount commit 029386534988d7f70ba3eb2e01d4c285336e5611 and ampr-emu-ng v0.4.1 commit 8b61a06048717f9241a2d09e3db86031417d6d99. All upstream authorship and licenses are retained. TITAN-specific source discovery, installed-package access recording, UI, native-service coordination and game-library mode settings remain. See docs/KRAKEN_0_2_1_UPGRADE.md for the integration boundaries and validation.

The current runtime source is vendor/ampr-emu-ng/play-no-limit-v0.4.1-source.zip. The only runtime production change from v0.4.1 is the existing TITAN launch notice; the upstream identity and engine version remain unchanged. The original v0.4.1 binary is retained alongside it. Earlier v0.4.0 source archives are historical.

Local build attribution and runtime launch notice: SirenaGoloviy. The notice reads PLAY NO LIMIT by SirenaGoloviy. This attribution does not replace the upstream component credits.

Local icons.2 revision: the bundled ShadowMount is now a source-built 1.7beta10-titan-no-auto-uninstall variant, not the unmodified original. It disables the two background auto-uninstall call sites and retains explicit user API uninstall. The original binary and source are retained; modified source is sources/shadowmountplus-a8e4004-titan-safe.zip under vendor/unified. SQLite 3.46.1 is linked into TITAN for live, read-only registration queries; its public-domain source and build provenance are in vendor/sqlite.

## Local isolated3 integration
Custom ShadowMountPlus variant: targeted registration API, per-boot native ownership and YouTube host guards. Original GPL authorship and notices remain; see docs/FIX3.md and vendored source/TITAN_CHANGES.md. Runtime AMPR unchanged from branded0.4.1.

## PlayGo compatibility source update
PlayGo Stub 0.6 by drakmor, GPL-3.0, is included unchanged. Binary, full corresponding upstream source archive, license and SHA-256 provenance are in vendor/playgo. TITAN adds only integration policy and settings; majority-of-games compatibility is not yet tested.

## FIX6 on-console updater
RustCrypto sha2 0.10.9 supplies streaming SHA-256. Dependency source, original
licenses and lockfile hashes are retained in vendor/updater-dependencies.
Local release/download/downgrade integration: SirenaGoloviy fork. Upstream
TITAN, Kraken, PlayGo, AMPR, kstuff and ShadowMount authorship remains unchanged.

## Backports catalog source feature

The TITAN/SirenaGoloviy catalog format, packaging tool, UI and native managed-overlay integration are local additions after FIX6. No third-party game backport or Sony module is bundled by this feature; metadata must retain each patch author and source. Existing GPL and upstream credits remain unchanged. See docs/BACKPORTS.md.

## TITAN FIX7 branding

The owner renamed the current distribution and UI to TITAN and its repository to grimmtroll2285-dot/TITAN. The original TITAN CORE project authorship above is retained. Internal data paths and engine identifiers stay compatible; vendor binaries and PlayGo remain unchanged.

## Kraken Mount 0.3.0 integration

FIX8 incorporates selected runtime, scanner, registration, USB and metadata changes from quer3q/kraken-mount v0.3.0 (e1e784560fe3a56e3b5ffd579f47ed5b2cf194f7), retaining GPL-3.0 authorship. See docs/KRAKEN_0_3_0_UPGRADE.md for exact integration boundaries, including the excluded dlc_emu binary. No new PlayGo binary or AMPR binary is substituted.
