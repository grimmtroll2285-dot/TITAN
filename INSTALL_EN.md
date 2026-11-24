# TITAN FIX12 — installation and use

Version 1.0.10, stable release. Primary target: PS5 13.60 with a working jailbreak and ELF Loader. The PS5 ELF is not a Windows application.

### Install and use

1. Download **TITAN-SirenaGoloviy-fix12.elf** from the [FIX12 release](https://github.com/grimmtroll2285-dot/TITAN/releases/tag/fix12). Use the outer ELF, not stage1 or GitHub's automatic Source code archive.
2. Close games, fully reboot the console, run your jailbreak and load the ELF through a compatible Payload Manager or ELF Loader. Replace older autoload copies too.
3. Open the TITAN tile or `http://PS5_IP:8097` from a computer/phone on the same network. Wait for services and the game's **Ready** status.
4. Put external archive PKGs in the drive-root `homebrew` folder, e.g. `/mnt/usb0/homebrew/Game.pkg`, including subfolders. Internal sources may use `/data/homebrew`. Do not move system-installed PKGs manually.
5. Open a library card and select **Play**, or launch the registered title from the PS5 home screen. Search and the drive filter sit above game cards.

**PlayGo:** Settings → PlayGo game selection → check games → Save. **Overlay:** per-folder-game switch in game details; unavailable for PKGs. **Reports:** Game report link in the card. **Updates:** select a stable release or pre-release to upgrade, reinstall or downgrade, then fully restart the console.

The first FIX12 scan upgrades older cache layouts to extract additional ELF files. Wait for Ready. Game-written cache files outside TITAN's generated-file list are retained. See [INSTALL_EN.md](INSTALL_EN.md) for the complete guide.

## Storage and compatibility

TITAN saves its launchable copy as `/data/titan-core/titan-core.elf`; settings, logs and caches retain `/data/titan-core/`. kstuff-lite 1.11 and the adapted ShadowMountPlus 1.7beta12-titan-isolated4 service are embedded. Wait for service readiness and avoid running competing standalone mount engines for the same library.

Supported formats depend on the bundled components. Arbitrary encrypted retail PKGs are unsupported. Installer copies and verifies a selected compatible PKG at the chosen destination while retaining the original. Check the destination and free space first. Use safe USB ejection only after games have closed.

Missing-source cleanup unregisters owned missing tiles after the configured delay; it does not delete source packages, user cache data, YouTube or system-installed games. External archive PKGs must remain inside the drive-root `homebrew` tree even when custom scan paths are used.

## New FIX12 controls

Excluded source paths accepts absolute file/folder paths, one per line. It excludes the path and descendants from native discovery, preserving data and existing registrations. A sibling sharing only a text prefix is unaffected. Playden manual/remove uses the same list.

The per-folder-game library overlay switch disables cached library substitution, including AMPR/PlayGo and library content supplied by a selected backport. Use it only when the folder game does not require those libraries. Enable it again and wait for Ready if needed. PKG overlay disabling is rejected because the package reader is mandatory. ShadowMount images keep their own engine settings.

## Updates, backports and troubleshooting

Updates automatically checks metadata; installation requires your action. Select the version to upgrade, reinstall or downgrade, then fully reboot and launch the saved TITAN copy. Replace older Payload Manager/autoload copies separately. FIX6 may require a manual upgrade after the repository rename.

Backports require an accessible compatible catalog matching the exact title, game version, firmware and source format. PlayGo/AMPR do not replace required backports or restore missing licenses.

For launch/exit problems, export Game report and Diagnostics logs immediately, including kernel logs when available. Include firmware, Title ID, game version, format and source path. A last-crash entry requires a matching console dump; no entry is not proof that no crash happened. See [validation](VALIDATION.md) for test scope. FIX12 has not been tested on PS5 hardware.
