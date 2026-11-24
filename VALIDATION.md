# Проверки TITAN FIX12 (1.0.10)

- PS5 target compilation and both optimized ELF stages built with Rust 1.99, LLVM 19 and SDK 0.43; at most two compiler jobs.
- 104 portable Rust tests, 8 package-reader tests and 27 JavaScript tests passed (139 in these suites). An additional host suite passed 94 tests; it overlaps the portable suite and is not added to a unique-test total.
- Multi-process lifetime-lock test: a second process cannot acquire the held lock; releasing ownership permits a new process despite stale PID text.
- Live SQLite registration tests reject freed rows/unrelated bytes and treat unreadable databases as errors.
- Synthetic Playwright browser checks: search, PKG overlay protection, native launch request, folder overlay change, last crash/text report, excluded-path save, and 390 px mobile viewport without horizontal overflow. These use fixtures, not a PS5. Screenshots were inspected locally.
- Stage1 and stage2 are ELF64 x86-64 ET_DYN with executable entry points. Exact embedded stage1, bundled UI, kstuff, isolated ShadowMount, PlayGo and official AMPR are verified. The real TITAN updater verification code accepts both stages. Release metadata and SHA-256 are generated from the actual uploaded build.

No FIX12 gameplay, save/exit validation or performance benchmarks were run on real PS5 hardware. Upstream AMPR release notes are not TITAN console test results. Native PKG mode remains experimental. The reported Forza Horizon 5 PKG crash is not confirmed fixed; Kraken upstream explicitly states that 0.3.2 does not fix it. Wait for Ready before launch; the existing game-start during cache-build race remains a limit.

Release workflow: .github/workflows/release-fix12.yml. Source reconstruction starts from the SHA-256-verified published FIX11 source, applies the reviewed patch, downloads pinned upstream runtime/source snapshots, builds, tests and publishes a stable release. See validation.json for actual artifact hashes and toolchain details. The full corresponding source is the named source ZIP asset, not GitHub's automatic repository archive.
