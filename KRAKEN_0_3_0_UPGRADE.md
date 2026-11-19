# TITAN FIX8 / Kraken Mount 0.3.0

Upstream tag v0.3.0: e1e784560fe3a56e3b5ffd579f47ed5b2cf194f7.
https://github.com/quer3q/kraken-mount/compare/v0.2.1...v0.3.0

Ported save-module filtering (ordinary fakelib only), required PKG AMPR injection, preservation of newer game AMPR, conditional PlayGo import detection with known 0.4/0.5 upgrades, source stability checks, missing-source auto-unregister, console-language titles, title sounds and guarded USB eject. The unmodified PlayGo 0.6 binary is identical to FIX7. No bundled dlc_emu 0.3 is added: upstream documents unresolved RPC bugs in that release. Existing game-supplied DLC libraries remain under the existing fakelib policy.

TITAN retains installed PKGs in place, internal-source priority, selected managed backports, per-game PlayGo selection, manual PlayGo precedence, update/downgrade and the isolated ShadowMount service. Auto-unregister is on, 300 seconds by default, configurable in Settings. It requires a full scan, proven absent source, cache ownership, no game/installer/backport operation, and no real installed PKG, protected YouTube host or ShadowMount ownership. Cache stays; source return registers again. Unreadable sources are not proof of removal. USB eject is refused during worker operations or when foreign ShadowMount folders/images are registered; it never force-unmounts. Firmware IPMI behavior remains a hardware acceptance check.

The scanner retains TITAN's in-memory two-second PKG stability guard in addition to the configurable upstream modification-time window. It keeps TITAN source priority rather than upstream's folder-first duplicate rule. PlayGo explicit manual overrides and selected catalog libraries remain authoritative. Unknown game-supplied PlayGo modules are preserved; automatic detection searches eboot only.

No console gameplay or real USB-eject result is asserted by source/build tests. Close games and wait for Ready before launching.
