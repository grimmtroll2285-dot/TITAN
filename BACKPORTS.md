# TITAN FIX12 catalog-backed backports

FIX12 (1.0.5) includes this feature on top of published FIX6. It excludes the
separate, unproven PKG/fakelib2 investigation changes. Both ELF stages are built
for the release; on-console download/boot/gameplay validation is still pending.
The product and repository are now named TITAN. Existing internal data paths
remain unchanged.

The project catalog is connected by default at
`https://raw.githubusercontent.com/grimmtroll2285-dot/TITAN/main/backports/catalog.json`.
It currently contains zero verified game patches. The UI separately links to
BackPork, PS5 Backport Toolkit and PS5 Game Updater as information/tools. The
latter's public verified seed was checked on 2026-11-18 and contained no entries.
These reference links do not impersonate compatible installable catalogs.

## What is implemented

The Backports tab lists the whole known console library. For native PS5 PKGs and
folders it matches catalogs by Title ID, exact three-part content version,
inclusive firmware range, source format and selected console model. Version
components compare numerically (`01.008.000` equals `1.8.0`). A different content
version, unknown firmware or unknown required console model cannot match.
Firmware comes from the console; model-specific patches require the user's
PS5/Slim or Pro selection. A library source claimed by ShadowMount is blocked.

Users can configure up to eight HTTPS GitHub catalog URLs, check immediately,
or import one small catalog JSON from a phone/PC. Import replaces the previous
locally imported catalog, leaving remote sources unchanged. Larger catalogs
use their URL. Console-side checks start after 35 seconds, then run every
30 minutes even when the browser is closed. Checks fetch metadata only.
Download and activation always require an explicit user action.

Every downloaded file has an exact size and SHA-256. Downloads stream to an
owned staging directory, have a 256 MiB per-file / 1 GiB per-pack limit and a
64 MiB free-space reserve. Publication requires verification of every file,
safe relative paths and, when included, matching Title ID/contentVersion in
`sce_sys/param.json`. Every active pack is rehashed at TITAN startup.

Installation records a pending selection. Only a **different kernel boot**
can activate it: restarting TITAN or reopening the browser is insufficient.
Rollback, disabling the managed selection and cancellation are available.
The pointer receipt is published by exclusive temporary-file creation, file
fsync, rename and directory fsync. A corrupt pending pack retains the previous
selection and reports an error. No original game/PKG or save is overwritten.

The native scanner selects a compatible managed pack ahead of legacy manual
backports. Native cache invalidation/rebuild remains the existing mechanism;
it preserves game-written cache files under the existing rules. A managed
backport's replacement libraries take priority over global AMPR/PlayGo modules;
TITAN fills missing modules and retains its mandatory streaming reader. A
managed pack cannot replace `libSceAmpr.sprx` or `libkernel.sprx`.
Global Settings → backports must be enabled. Installation also refuses when
game-library mode is Off. Disabling a managed selection restores the original
selection process, including any pre-existing legacy manual backport.

## Current limits and trust

* **The supplied catalog is empty.** No real game compatibility is inferred or
  advertised. Real patches need author/provenance, exact compatibility metadata,
  direct URLs and file hashes before being added. Yōtei's reported success from
  a user-supplied backport is not validation of this feature.
* Image entries are visible but installation for ShadowMount `.exfat`/FFPKG
  images is explicitly disabled. Their overlay and priority rules need a
  separate verified integration. This native feature does not modify the
  embedded resident ShadowMount binary.
* Supported initial hosts: `raw.githubusercontent.com`, `github.com`,
  `objects.githubusercontent.com`, `release-assets.githubusercontent.com`.
  HTML pages, captchas, advertising links and file-host verification are not
  download APIs. Checksums reject an HTML response masquerading as a module.
  Existing libSceHttp TLS roots and automatic redirect behavior are reused.
* A hash verifies bytes against the selected catalog; it is not an independent
  author signature or proof that compatibility claims are correct. Configure
  catalogs you trust. No website is scraped and no automatic conversion of
  arbitrary game executables/backports is attempted.
* It supports PS5 native PKG/folder patches, not PS4 CUSA patches, DLC/license
  repair, retail updates, arbitrary patch scripts or a guarantee for every game.
* No real console boot, download, game launch or rollback was hardware-tested.
  The PS5 browser may behave differently from desktop Chromium.
* Old immutable packs are retained for rollback, and power-loss staging may
  remain unreferenced. No automatic deletion/garbage collection is implemented.
  A receipt larger than 4 MiB is refused. Full patch history is not retained:
  Current and Previous are the two rollback selections.

## Files on the console

Under `/data/titan-core/backports/`:

* `settings.json`: catalog URLs and explicit model choice.
* `imported.json`: last explicitly imported local catalog.
* `packs/<manifest-sha256>/`: immutable files plus `manifest.json`.
* `installed.json`: per-title Current, Previous and Pending manifests and boot ID.

The source game's files stay at their original path. Catalog title matches are
for all native sources of that same title/version, not an arbitrary disk path.
If the game version/firmware no longer matches at boot, that managed patch is
not selected. No checksum can determine that two independently sourced game
builds are identical solely from their shared title/version: a catalog author
must document build-specific restrictions in its notes.

## Catalog schema 1

`catalog/catalog.json` is a valid empty catalog. A non-empty entry has:

```json
{
  "schema": 1,
  "entries": [{
    "id": "example-only",
    "revision": "1",
    "title_id": "PPSA12345",
    "name": "EXAMPLE ONLY",
    "author": "Original patch author",
    "page": "https://github.com/OWNER/REPOSITORY",
    "game_version": "01.008.000",
    "firmware_min": "13.60",
    "firmware_max": "13.60",
    "model": "any",
    "kind": "native",
    "notes": "Template; not a compatibility claim.",
    "files": [{
      "path": "fakelib/libSceExample.sprx",
      "url": "https://raw.githubusercontent.com/OWNER/REPOSITORY/main/files/REAL_HASH/libSceExample.sprx",
      "size": 123,
      "sha256": "REPLACE_WITH_64_HEX_DIGITS_FROM_THE_ACTUAL_FILE"
    }]
  }]
}
```

The above example intentionally has no real download/hash and is not installable.
`model` is `any`, `base` or `pro`; `kind` is `native`, `pkg` or `folder`.
Only `eboot.bin`, `sce_sys/param.json`, flat `fakelib/` or `fakelib2/` PRX/SPRX,
and PRX/SPRX under `sce_module/` are allowed. Absolute paths, traversal,
symlinks, duplicate case-folded paths, file/directory conflicts and protected
runtime names are refused. Per source and combined catalogs allow at most
512 entries / 4 MiB. Every entry ID in an individual catalog must be unique;
different revisions therefore need distinct IDs. Files per entry: 1–256.

## Prepare a patch-only folder or ZIP

Copy `catalog/metadata.example.json` and replace **all** sample compatibility
values with tested ones. Use only files you may publish, preserving authorship
and required notices. The input must contain patch files at its root, e.g.
`eboot.bin`, `fakelib/`, `sce_module/`; wrapper folders and unrelated files are
refused. This is a packaging tool, not a backport generator.

```text
python tools/backport_catalog.py --input PATCH.zip --metadata metadata.json --base-url https://raw.githubusercontent.com/OWNER/REPOSITORY/main/backports --output prepared-catalog
```

It writes `catalog.json` and `files/<sha256>/<filename>` into a new output
directory, without running executables, changing the input, or uploading files.
Publish that directory at the chosen base URL, then configure
`https://raw.githubusercontent.com/OWNER/REPOSITORY/main/backports/catalog.json`
in TITAN. To maintain several games, combine the entry arrays into one schema-1
catalog while preserving URLs and unique IDs. Known backports remain specific
to their game/build/firmware; the catalog mechanism is shared.

## Web API and verification

GET `/api/backports` returns metadata, library offers, incompatibility reasons,
progress, configuration and the installed-selection ledger.
POST `/api/backports/{check,settings,import,install,rollback,disable,cancel}`
requires same-origin JSON with `X-Titan-Updater: 1`, using the existing guard.
Install accepts only `{key,source_id}`; rollback/disable/cancel only a Title ID.
The server selects the stored validated manifest and rechecks source identity,
compatibility and running-game state. No browser-provided file path is used.
Downloads do not write active pack directories; the final receipt shares the
native work mutex. Installer/payload-update activity and running games block
download/scheduling. Busy backport work blocks a requested TITAN takeover.

Portable tests cover compatibility, path/URL limits, file corruption, symlinks,
staged identity mismatch, same-boot deferral, failed upgrades and rollback.
Python tests compare folder/ZIP output and reject unsafe members and identity
changes. JS tests cover absent/incompatible offers, literal remote text,
request scope, pending/rollback labels, edited sources and server errors.
`review/backports-preview.py` serves synthetic UI on loopback port 8772; its
buttons simulate operations and never download or install real patches.
New labels have authored Russian translations; other new technical labels
currently use explicit English fallback within the existing locale system.
