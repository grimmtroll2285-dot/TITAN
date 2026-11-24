> FIX12 uses PlayGo Stub 0.6 unchanged. Disabling a folder game’s entire library overlay also disables injected PlayGo for that game. PKGs retain mandatory AMPR; per-game PlayGo selection remains separate.

# Embedded PlayGo compatibility (1.0.4-playgo.1 pre-release)

Base: published Fix5 1.0.3. Owner authorized both ELF stages and pre-release publication on 2026-11-18.
The existing AMPR 0.4.1, ShadowMount beta12 and kstuff binaries are unchanged.
drakmor's pgo_stub 0.6 (GPL-3.0) is embedded byte-for-byte, including its
source archive, license, SHA-256 and provenance in vendor/playgo.

## Policy

playgo_enabled defaults to true. With inject_ampr enabled, native PS5 titles
receive PlayGo Stub 0.6 after their own game/backport libraries are composed.
The stub answers PlayGo installation-state queries; AMPR still reads real data.
It is not a license repair, decoder, driver or verified performance improvement.

playgo_exclude remains the backward-compatible stored array of PPSA title IDs.
The Settings -> PlayGo section now presents named native library games with
checkboxes and search instead of a manual Title ID textarea. Checked means
PlayGo is allowed for the title. Existing exclusions, including those on an
offline drive, survive inventory refreshes and edits to other games. The list
deduplicates by Title ID and excludes YouTube, PS4 and ShadowMount-owned sources.
New native games retain the existing default of PlayGo allowed. The global
PlayGo and injection switches remain authoritative. Save Settings to apply;
editing a checkbox alone does not write the console config. Excluded titles
keep their original game/backport PlayGo,
subject to the existing game_fakelib setting. Disabling playgo_enabled applies
the same rule to all native titles. Disabling inject_ampr disables this injection.
YouTube host IDs, PS4 titles, the TITAN launcher, and ShadowMount-owned image
titles are not injected by this path. Existing ShadowMount ownership remains.

A manual libScePlayGo.sprx in /data/titan-core/ampr takes priority. Canonical
spelling is preferred; other case variants are sorted deterministically. Manual
files are retained on disk when disabled. Case variants are copied to the canonical
runtime filename. All non-PlayGo manual runtime files retain the existing rules.

The per-title AMPR snapshot records the selected builtin hash or manual metadata.
A policy change refreshes fakelib only; it does not re-extract a whole package.
Package originals, game-written files, saves and source metadata stay intact.
Source cache composition uses existing idle scanning: close games and wait for
Ready before launching. The previously identified mid-build launch race is not
fixed by this feature and remains a separate task. No forced unmount is added.

## Validation boundary

Host tests/type checks and ELF validation are recorded separately. No console run,
performance result, 007/MGS4/Yotei fix, or majority-of-games compatibility is
claimed. Keep the upstream implementation unchanged until game-specific traces
demonstrate a reason for changing it. The logging upstream variant remains
available for future on-console diagnosis.

UI verification (2026-11-18): four selection-model tests, full bundled-script
syntax check, and synthetic Chromium checkbox/save/reload round-trip. A saved
checkbox change produced the expected playgo_exclude array without deleting
another title's existing choice. Desktop and 390-pixel layout checked. This UI change is included in the two-stage FIX12 release build; no console
gameplay or actual console settings round-trip is claimed.


FIX12: automatic injection checks eboot imports; unknown existing game modules stay. Known Stub 0.4/0.5 upgrades to 0.6. Named selection and manual AMPR override remain. PKG AMPR reader is required regardless of inject_ampr; optional PlayGo still follows its configured gates. See KRAKEN_0_3_0_UPGRADE.md.
