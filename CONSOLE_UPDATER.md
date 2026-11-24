# TITAN FIX12 console updater (1.0.10)

Automatic metadata checks, user-selected installation, stable/pre-release releases and downgrade remain available. Standalone Kraken self-replacement is disabled; only TITAN releases are installed. FIX6 may need a manual transition after the repository rename.

## Console flow

- Initial metadata check 20 seconds after startup, then every 30 minutes, including
  when the web interface is closed. Checks never install or execute a payload.
- Open Updates in the interface on port 8097. Stable and pre-release releases are
  included by default; a checkbox hides pre-releases when desired.
- Choose a published tag. Download to console saves a verified ELF without changing
  the saved launch payload. Install selected version supports upgrades, downgrades
  and reinstalling the same version. Recent validation manifests provide version
  labels; older releases without a version manifest remain selectable by tag.
- The console downloads the selected ELF anew and verifies it before installation.
  Close games and finish PKG installation first. If the library scan owns the work
  mutex at publication time, installation defers with an error; retry afterwards.
- Installation prepares `/data/titan-core/titan-core.elf`, leaving the current
  process and resident services running. Fully restart the console and run the
  saved TITAN tile to activate it. Nothing forces a reboot, kills a game or changes
  its mounts.
- A previous saved ELF is retained at `/data/titan-core/titan-core.previous.elf`.
  This is a manual recovery copy, not an automatic boot rollback. Use a working
  ELF loader to run it if necessary. Downgrading to a release predating this
  updater also removes the updater UI until a newer ELF is loaded again.
- A stale ELF in Payload Manager or an external autoload source can overwrite the
  prepared saved copy on next launch. Update that source separately. The updater
  cannot identify or rewrite an arbitrary third-party loader configuration.

## Trust, storage and failure handling

Only the owner repository `grimmtroll2285-dot/TITAN` is queried.
The server accepts a validated release tag, never a browser-provided URL, path or
checksum. Only a single supported TITAN/TITAN-CORE outer ELF asset from a published release is
accepted. Tags and asset paths must match the exact owner repository. Drafts,
foreign assets, ambiguous ELFs and files larger than 64 MiB are rejected.

GitHub HTTPS uses the existing SceHttp/SceSsl certificate validation and pinned root
CA set. Each download is streamed in 64 KiB chunks, with a size limit and incremental
RustCrypto SHA-256. Its digest must match GitHub's asset SHA-256 or the release's
exact SHA256SUMS record; when both exist they must agree. Missing or conflicting
hashes fail closed. These are repository integrity checks, not an independent
publisher signature. A compromised repository/account remains a trust risk.

The completed file is re-read to check SHA-256 and ELF64/x86-64 structure, program
table bounds, load segment lengths and executable entry mapping. Internal free
space must cover staging, the next saved copy, the previous saved copy and 16 MiB
headroom. Downloaded staging is one owned slot at
`/data/titan-core/updates/downloaded.elf`; a newer successful download replaces it.

Before publication the updater rechecks game process visibility and installer
activity, acquires the library work mutex and the saved-payload mutex, copies and
syncs the new file, verifies it, copies/verifies the previous file, syncs directory
entries, then renames the new file atomically over the saved path. A post-rename
directory-sync failure is reported as a warning with prepared status. A failure
before final rename leaves the active saved ELF unchanged. This does not promise
power-loss safety on every console filesystem; hardware acceptance remains needed.

API mutations require JSON and `X-Titan-Updater: 1`; a supplied Origin must match
Host. No CORS permission is added. Only one check/download/install worker runs at
once. Status/progress is read-only. GitHub errors retain the previous release list
and are displayed. Up to 500 releases are listed; a truncation notice appears at
that bound. Version manifests are fetched for at most six recent releases to limit
network requests. No GitHub token is embedded or required.

Game packages, saves, AMPR overrides and cache contents are outside the updater's
file transaction. Previous payloads may interpret settings differently: review
their release notes before downgrading.

## Validation

Run `node --test review/update-policy.test.cjs review/updates-ui.test.cjs`, portable
Rust tests, PKG tests, localization embedding, JS syntax checks and the PS5 target
type check before building both ELF stages. Production SHA-256 and transaction
code are exercised by host tests, including corruption rejection and previous-file
preservation. Console HTTPS, download/installation/reboot, directory fsync behavior,
external loader interactions and game compatibility still require PS5 testing.

RustCrypto dependency versions, source archives, licenses and archive hashes are
recorded in `vendor/updater-dependencies/PROVENANCE.json`. Existing upstream credits,
GPL PlayGo source and component provenance are retained.
