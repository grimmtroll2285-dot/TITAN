# Kraken Mount 0.3.2 / AMPR 0.5.1 — TITAN FIX12

Stable TITAN version: **1.0.10**, tag **fix12**, based on the published FIX11 source archive.

## Integrated changes

- Kraken Mount v0.3.2 native scanner, cache layout v3/additional ELF extraction outside `decrypted/`, launch lifecycle, immediate owned-nullfs cleanup, same-title ELF transition grace and sandbox font/source remounts.
- Last-crash records in `/data/titan-core/crashes.json` and plain-text `GET /api/report/<TID>`.
- Library search, drive filtering, ready-title launch, queued-rebuild button handling, path exclusions and per-folder `overlay_off` with cache fingerprint invalidation.
- Playden API v1 subset via **POST /api/v1/** on 8097: `version`, `games`, `scan`, `manual/add`, `manual/remove`, `games/uninstall`, `games/fakelib`. It covers the native library, not the entire ShadowMount service API. Uninstall retains sources/cache and rejects installed system titles or foreign registrations.
- FW 12+ launcher tile staging via batched registration; live app.db row check; web-server rebind after rest mode.
- Official unmodified ampr-emu-ng v0.5.1, SHA-256 `7ca61afc444f0b44d2f005506dde16cb43e74dae4b1e045323b291b8db1c3d5d`. Corresponding source is retained as `vendor/ampr-emu-ng/upstream-v0.5.1-source.zip` in the full source archive.

## TITAN adaptations

The existing TITAN updater remains the only payload updater: stable/pre-release selection, downgrade, integrity checks and activation after full restart. Upstream standalone Kraken self-replacement is deliberately disabled so it cannot overwrite TITAN with a different product. The Payload Manager catalog points to FIX12.

Keep installed-PKG receipt compatibility, in-place packages, YouTube guards, native/ShadowMount ownership, exact external `homebrew` allowlist, no-force-unmount policy, game-written cache files, PlayGo game selection and backport manager. Busy cleanup remains paused and retries; foreign layers are never forced off. A fallback process disappearance is reported with unknown exit status rather than inventing a successful exit code.

AMPR upstream release notes list save/exit and directory-read fixes for several games; these are integrated upstream changes, not new TITAN hardware test results. PKG mode remains experimental. Wolverine confirmation is still pending upstream. Performance numbers from upstream are not TITAN benchmarks.

## Sources

- [Kraken Mount v0.3.2](https://github.com/quer3q/kraken-mount/releases/tag/v0.3.2), commit dbe78a7 (full snapshot retained in source provenance).
- [AMPR v0.5.1 release](https://github.com/quer3q/ampr-emu-ng/releases/tag/v0.5.1).
- [Exit-spawn lifecycle work, PR 109](https://github.com/quer3q/kraken-mount/pull/109).

See VALIDATION.md and validation.json for actual checks; no FIX12 hardware testing is claimed. Existing build/game-start race limits remain: wait for Ready.

## Additional FIX12 hardening

A kernel-held lifetime lock at `/data/titan-core.instance.lock` prevents competing FIX12 processes even if the HTTP socket is lost. Its PID text is diagnostic; kernel ownership expires with the process, so a stale file never requires deleting. Close/stop and fully reboot to transition from earlier payloads without this lock. Registration status uses a live SQLite SELECT, never freed database bytes.

Forza Horizon 5 PKG launch crashes are not declared fixed. Upstream explicitly confirmed that Kraken 0.3.2 does not fix this crash: https://github.com/quer3q/kraken-mount/issues/59#issuecomment-7127681835. A matching symptom does not prove the same cause on another console. Capture kernel logs/core dump before diagnosing the executable or AMPR.
