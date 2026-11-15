# OBS Studio — Swedish Crowdin line review

Date: 2026-11-15  
Project: [OBS Studio on Crowdin](https://crowdin.com/project/obs-studio)  
Locale: `sv-SE`  
Source release observed: OBS Studio 33.0.1, published 2026-10-29.

## Upstream state before review

Crowdin reports Swedish as **100% translated** and **31% approved** (0 untranslated words). The outstanding work is therefore a quality review of existing translations, not completion of missing strings.

## Reviewed batch 1

Component: `App/Plugins/asio-output-ui.ini`  
Crowdin component URL: <https://crowdin.com/editor/obs-studio/771/enus-sv>

| Source key | Source | Swedish | Result |
| --- | --- | --- | --- |
| `AsioOutput.Menu` | ASIO Output | ASIO-utmatning | Correct; no change. |
| `AsioOutput.Disabled` | No ASIO audio driver was detected in your system. ASIO monitoring is disabled. | Ingen ASIO-ljuddrivrutin hittades på ditt system. ASIO-monitorering har inaktiverats. | Correct in the DAW/ASIO context; no change. |

Two strings were reviewed in their Crowdin component. No source or Swedish value was changed, so no upload was required. Crowdin exposes the entries as translated; the current account has no visible approve action in this component.

## Reviewed batch 2

| Component | Strings | Result |
| --- | ---: | --- |
| `obs-vst3.ini` | 8 | All keys, one-to-one UI terminology, line break and technical tokens are correct. No change. |
| `win-asio.ini` | 15 | All keys, `%i` placeholders and ASIO/driver terminology are correct in context. No change. |

`ASIO-monitorering`, `ASIO-utmatning`, `ASIO-ingång`, `samplingsfrekvens` and `värdprogram` are retained as established audio-software wording. The driver-reload instruction deliberately retains the full operational caveat from the source rather than shortening it.

## Reviewed batch 3 — pending upstream save

| Component | Reviewed strings | Result |
| --- | ---: | --- |
| `Jack` | 3 | Two wording corrections prepared in `jack.delta.json`; one translation is already correct. |
| `Mac Virtualcam` | 10 | Four idiomatic Swedish corrections prepared in `mac-virtualcam.delta.json`; six translations are correct. |

The pending deltas have not been saved to Crowdin. Raw Crowdin exports remain unchanged.

Crowdin API check: the stored token can read project `51028` (`OBS Studio`), but `GET /api/v2/projects/51028/files` returns HTTP 403 for each available Crowdin API credential. It therefore cannot safely list or submit the target strings through the API. The browser editor remains the available upstream route.

## Reviewed batch 4 — pending upstream save

Component: `NVENC`
Reviewed strings: 60 (two pages in Crowdin)

Fifteen changes are prepared in `nvenc.delta.json`. They correct bitrate-versus-speed terminology, technical compounds, Swedish grammar, a `Windows Game DVR` typo, the Swedish spelling `kodek`, and a misleading technical tooltip. The remaining 45 strings are contextually correct and unchanged. Markup, `%1`, product names, encoder names and example options are retained byte-for-byte where required.

## Reviewed batch 5 — pending upstream save

Component: `NVIDIA Filters`
Reviewed strings: 22

Thirteen changes are prepared in `nvidia-filters.delta.json`. They correct brand possessives, restore the every-N-frames meaning, and normalize GPU and blur-strength terminology. The other nine strings are correct in the filter UI context.

## Terminology

`TERMINOLOGY.md` records the decisions already applied to ASIO, VST3, virtual-camera, NVENC and NVIDIA Filters UI. It is the source of truth for remaining OBS component batches.

## Reviewed batch 6 — pending upstream save

Component: `Desktop Entry`

Both strings are reviewed. `desktop-entry.delta.json` contains two word-order and UI-style corrections; the component's translation state is otherwise complete.

## Reviewed batch 7 — pending upstream save

Component: `Filters`

The local source snapshot contains 133 English keys and 122 Swedish keys. The 11 missing keys are newer than that snapshot and are already translated in Crowdin; they are kept outside this local delta until a current Crowdin export is available. The 122 matching keys were reviewed. `filters.delta.json` records 25 terminology and natural-language corrections, chiefly for dynamics processors, blending modes and video-filter labels.

## Scope and next batch

Crowdin currently lists 100%-translated Swedish components with widely varying approval coverage. The next batch is the 0%-approved `Jack`, `Mac Virtualcam`, `NVENC`, `NVIDIA Filters` and Steam metadata components, followed by the remaining plugins before the frontend catalog.

## Checks

- INI key parity was checked against the local OBS source tree; batch 2 has 8/8 and 15/15 matching keys, with no missing or extra keys and no `%i` mismatch.
- `git diff --check`: passed for the archive batch.
- `msgfmt`: not applicable; OBS uses INI catalogs.
- `l10n-lint`: no OBS INI parser available (reported unsupported translation-file format).
- svlang: the installed CLI only accepts plain text through `svlang check`; it has no INI parser. The translations were reviewed in their source/UI context instead.
- Hunspell was intentionally not run, following the current CPU constraint.
- Gitleaks: passed for the archive payload.
