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

## Reviewed batch 8 — pending upstream save

Component: `Frontend` (first wording batch)

Seventeen context-sensitive frontend messages were reviewed against their English counterparts. All 17 have clear Swedish UI corrections in `frontend-phrasing.delta.json`: direct dialog wording in place of repeated *Var god*, one exposed English audio term, a definite-form correction and a connection error rewritten into natural Swedish. Placeholders, line breaks, product names and the source ellipses are preserved where present.

This is not a claim that the full 1,382-key local frontend snapshot has been reviewed. It is one bounded, archived batch.

## Reviewed batch 9 — pending upstream save

Component: `Frontend` (output and audio batch)

Twelve output, encoder and audio strings were reviewed against the English source. `frontend-output-audio.delta.json` contains the resulting corrections: Swedish compounds and agreement, an actual typo, the standard `i stället`, technical encoder terminology and clearer audio-warning wording. It preserves `%1` through `%3`, HTML markup and all source line breaks. The remaining frontend catalog is outside this batch.

## Reviewed batch 10 — pending upstream save

Component: `Frontend` (system-message batch)

Seven system and integration messages were reviewed. `frontend-system-messages.delta.json` corrects a Wine warning typo, restores the Advanced Audio Properties route, tightens the resource-leak error, fixes Swedish punctuation and retains placeholders, markup, menu names, versions and line breaks.

## Reviewed batch 11 — pending upstream save

Component: `Frontend` (output-settings batch)

Eleven output-settings strings were reviewed. `frontend-output-settings.delta.json` corrects bitrate warning wording, ambiguous pronouns, codec terminology, FFmpeg settings grammar and the split-file labels. Every source placeholder and line break is retained.

## Reviewed batch 12 — pending upstream save

Component: `obs-outputs`

The local snapshot has 27 English keys and 25 Swedish keys. The two absent Swedish keys are newer local-source drift (`RTMPStream.BindIP` and `MP4Output.StartChapter`); they are already translated in Crowdin and therefore are not recreated from this outdated export. The 25 matching keys were reviewed. `obs-outputs.delta.json` contains ten corrections for timeout semantics, networking terms, binding instructions and Swedish compounds.

## Reviewed batch 13 — pending upstream save

Component: `Frontend` (core UI, keys 1–180 in local source order)

The first 180 local English source keys were compared one by one with Swedish. Five corrections are recorded in `frontend-core-ui.delta.json`: one spelling error, an already-running recovery message, consistent `felsäkert läge`, and a complete automatic-configuration priority label. Keys missing only from the older local Swedish snapshot are documented but not reconstructed; Crowdin has Swedish at 100% completion.

## Reviewed batch 14 — pending upstream save

Component: `Frontend` (auto-configuration, status and undo UI; keys 181–360 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-autoconfig-status-undo.delta.json` contains 34 repairs to source meaning, Swedish grammar, terminology, typos and punctuation. It retains all placeholders, markup and source line structure. Newer keys absent from the local Swedish snapshot are deliberately excluded.

## Reviewed batch 15 — pending upstream save

Component: `Frontend` (output, remux and scene UI; keys 361–540 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-output-remux-scene.delta.json` contains 23 corrections: output errors, remux workflow text, macOS permission text, scene-collection recovery and source controls. It also removes one unintended invisible U+2063 character after a placeholder. Placeholders, markup and source line structure are retained.

## Reviewed batch 16 — pending upstream save

Component: `Frontend` (properties, transforms and main menus; keys 541–720 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-properties-transform-menu.delta.json` records 18 corrections for properties terminology, reconnecting status text, transform modes, virtual-camera choices and menus. Placeholders and access-key markup remain present.

## Reviewed batch 17 — pending upstream save

Component: `Frontend` (general, streaming and output settings; keys 721–900 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-general-stream-settings.delta.json` contains 25 corrections for general preferences, snapping, system-tray wording, multiview layouts, stream settings and fragmented-recording tooltips. Placeholders, markup, line breaks and menu paths are retained.

## Reviewed batch 18 — pending upstream save

Component: `Frontend` (output, video and audio settings; keys 901–1080 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-output-video-audio.delta.json` contains 13 corrections for FFmpeg wording, screenshots, video settings and audio-meter terminology. Existing prepared changes for the same output settings are not duplicated.

## Reviewed batch 19 — pending upstream save

Component: `Frontend` (advanced settings, audio mixer and hotkeys; keys 1081–1260 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-advanced-audio-hotkeys.delta.json` contains 16 corrections for advanced video/network settings, TCP pacing, audio monitorering, hotkey status and output warnings. Placeholders and line breaks are retained.

## Reviewed batch 20 — pending upstream save

Component: `Frontend` (about, import, YouTube and plugin manager; keys 1261–1440 in local source order)

The next 180 local English source keys were compared one by one with Swedish. `frontend-youtube-plugins.delta.json` contains 19 corrections for source meaning, product capitalization, direct UI wording, YouTube broadcasts and plugin-manager messages. Placeholders and markup are retained.

## Reviewed batch 21 — pending upstream save

Component: `Frontend` (NVENC diagnostics; keys 1441–1459 in local source order)

The final 19 local English source keys were compared one by one with Swedish. `frontend-nvenc-diagnostics.delta.json` contains six diagnostics-wording corrections. The earlier `i stället` correction for the Kepler message remains in the existing frontend system-message batch and is intentionally not duplicated.

## Local frontend review complete

All 1,459 keys in the local English frontend snapshot were compared line by line. This proves the scope of the local snapshot only: it has 1,382 Swedish keys, while Crowdin contains newer Swedish keys and remains the authoritative upstream catalog. The archived delta files must be applied to current Crowdin strings individually or by an API flow that can list and verify the target translations; the raw local snapshot must not be uploaded wholesale.

The archive now contains 342 prepared corrections across all reviewed OBS components. None has been saved to Crowdin in this work session.

2026-11-16: reviewed the live `Stores/Steam/Store Page` component line by line in Crowdin (23 strings). Prepared 9 context-checked corrections in `store-steam.delta.json`; none has been saved upstream.

2026-11-16: reviewed the live `Stores/Steam/Short Description` component in its Crowdin store context (1 string, 0% approved). The current Swedish `Kostnadsfri programvara med öppen källkod för videoinspelning och direktsändning` is accurate, idiomatic and within Steam's displayed 300-character limit; no change was prepared.

2026-11-16: reviewed the live `Stores/Flathub/Metadata` component line by line in Crowdin (15 strings). Prepared 9 context-checked corrections in `store-flathub.delta.json`; none has been saved upstream.

2026-11-16: reviewed the live `App/Plugins/Frontend/Frontend Tools` component line by line in Crowdin (48 strings). Prepared 5 context-checked corrections in `frontend-tools.delta.json`; none has been saved upstream.

2026-11-16: reviewed page 1 of the live `App/Core` component line by line in Crowdin (50 of 1,428 strings). Most applicable corrections were already present in `frontend-core-ui.delta.json`, `frontend-system-messages.delta.json` and `frontend-autoconfig-status-undo.delta.json`; 3 additional corrections are in `core-page-01.delta.json`. None has been saved upstream.

2026-11-16: reviewed page 2 of the live `App/Core` component line by line in Crowdin (100 of 1,428 strings). Most applicable corrections were already present in `frontend-output-audio.delta.json`, `frontend-output-remux-scene.delta.json`, `frontend-phrasing.delta.json` and `frontend-autoconfig-status-undo.delta.json`; 4 additional corrections are in `core-page-02.delta.json`. None has been saved upstream.

2026-11-16: reviewed page 3 of the live `App/Core` component line by line in Crowdin (150 of 1,428 strings). Most applicable corrections were already present in `frontend-system-messages.delta.json`, `frontend-output-remux-scene.delta.json` and `frontend-properties-transform-menu.delta.json`; 5 additional corrections are in `core-page-03.delta.json`. None has been saved upstream.

2026-11-16: reviewed page 4 of the live `App/Core` component line by line in Crowdin (200 of 1,428 strings). Most applicable corrections were already present in `frontend-general-stream-settings.delta.json` and `frontend-properties-transform-menu.delta.json`; 3 additional corrections are in `core-page-04.delta.json`. None has been saved upstream.

2026-11-16: reviewed page 5 of the live `App/Core` component line by line in Crowdin (250 of 1,428 strings). All identified wording, terminology and grammar corrections were already recorded in `frontend-general-stream-settings.delta.json`, `frontend-output-audio.delta.json`, `frontend-output-settings.delta.json` and `frontend-output-video-audio.delta.json`; no duplicate delta was created. None has been saved upstream.

2026-11-16: reviewed page 6 of the live `App/Core` component line by line in Crowdin (300 of 1,428 strings). The necessary corrections already existed in `frontend-output-settings.delta.json`, `frontend-output-audio.delta.json`, `frontend-output-video-audio.delta.json`, `frontend-system-messages.delta.json` and `frontend-advanced-audio-hotkeys.delta.json`. The VST term in the existing surround-sound warning was aligned with the terminology list (`VST-insticksmoduler`); no additional delta was created. None has been saved upstream.

2026-11-16: reviewed page 7 of the live `App/Core` component line by line in Crowdin (350 of 1,428 strings). Corrections already present in `frontend-phrasing.delta.json` and `frontend-advanced-audio-hotkeys.delta.json` cover audio ducking, stream delay, TCP pacing, mixer layout, audio monitorering and hotkey wording. `core-page-07.delta.json` adds 9 distinct corrections for the monitoring-device label, mixer layout actions and the numeric-keypad label. None has been saved upstream.

2026-11-16: reviewed page 8 of the live `App/Core` component line by line in Crowdin (400 of 1,428 strings). Existing corrections in `frontend-advanced-audio-hotkeys.delta.json` and `frontend-youtube-plugins.delta.json` cover output warnings, Browser Source, about text, importer labels and YouTube authorization. `core-page-08.delta.json` adds 16 distinct corrections for numeric-keypad labels, monitorering, the empty-sources guidance and a channel-information error. None has been saved upstream.

2026-11-16: reviewed page 9 of the live `App/Core` component line by line in Crowdin (450 of 1,428 strings). Existing corrections in `frontend-phrasing.delta.json`, `frontend-system-messages.delta.json`, `frontend-youtube-plugins.delta.json` and `frontend-advanced-audio-hotkeys.delta.json` cover YouTube, multitrack-video, plugin-manager and streaming-error wording. `core-page-09.delta.json` adds 2 distinct encoder-configuration corrections. None has been saved upstream.

2026-11-16: reviewed page 10 of the live `App/Core` component line by line in Crowdin (500 of 1,428 strings). The NVENC diagnostics, Kepler guidance and dropped-frames label are already corrected in `frontend-nvenc-diagnostics.delta.json`, `frontend-system-messages.delta.json` and `frontend-core-ui.delta.json`. Generic approved UI labels were retained. No duplicate delta was created and none has been saved upstream.

2026-11-16: reviewed page 11 of the live `App/Core` component line by line in Crowdin (550 of 1,428 strings). Projector, transition, timing, clipboard and Studio Mode labels were already accurate in their UI context. `core-page-11.delta.json` corrects the missing ellipsis on the New menu item. None has been saved upstream.

2026-11-16: reviewed page 12 of the live `App/Core` component line by line in Crowdin (600 of 1,428 strings). Existing deltas already cover direct plugin wording and the established term `felsäkert läge`. `core-page-12.delta.json` adds two distinct corrections: singular agreement for removing a selected scene and a descriptive title for the dockable-window warning. None has been saved upstream.

2026-11-16: reviewed page 13 of the live `App/Core` component line by line in Crowdin (650 of 1,428 strings). Existing deltas already cover authentication-status and account-disconnection wording. `core-page-13.delta.json` adds three distinct corrections for the live-broadcast choice and grammatically complete frame-rate preference options. None has been saved upstream.

2026-11-16: reviewed page 14 of the live `App/Core` component line by line in Crowdin (700 of 1,428 strings). Existing deltas already cover the main auto-configuration test wording, disk-space label, updater guidance and integrity-check text. `core-page-14.delta.json` adds seven distinct corrections for wizard alternatives, network-test status, updater errors and quick transitions. None has been saved upstream.

2026-11-16: reviewed page 15 of the live `App/Core` component line by line in Crowdin (750 of 1,428 strings). Existing work already corrects the filter-changes history label. `core-page-15.delta.json` adds six distinct corrections for paste, centering and audio-history wording. None has been saved upstream.

2026-11-16: reviewed page 16 of the live `App/Core` component line by line in Crowdin (800 of 1,428 strings). Existing deltas already cover safe-mode and direct-dialog wording. `core-page-16.delta.json` adds six distinct corrections for grouping and live-broadcast actions. None has been saved upstream.

2026-11-16: reviewed page 17 of the live `App/Core` component line by line in Crowdin (850 of 1,428 strings). Existing work already corrects the access-granted spelling. `core-page-17.delta.json` adds two distinct corrections for missing-file matching and the established macOS input-monitoring permission term. None has been saved upstream.

2026-11-16: reviewed page 18 of the live `App/Core` component line by line in Crowdin (900 of 1,428 strings). Dialog prompts, preview status and reconnection wording are already covered by `frontend-phrasing.delta.json`, `frontend-output-remux-scene.delta.json` and `frontend-properties-transform-menu.delta.json`. No duplicate delta was created and none has been saved upstream.

2026-11-16: reviewed page 19 of the live `App/Core` component line by line in Crowdin (950 of 1,428 strings). `core-page-19.delta.json` adds four distinct corrections for transform-window labels and the established actions for starting and ending a live broadcast. None has been saved upstream.

2026-11-16: reviewed page 20 of the live `App/Core` component line by line in Crowdin (1,000 of 1,428 strings). `core-page-20.delta.json` adds three distinct corrections for live-broadcast status/actions and the preview-scaling menu label. None has been saved upstream.

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
- Final delta audit: all 376 proposed changes pass JSON parsing plus placeholder, markup and escaped-line-break parity checks; `git diff --check` and Gitleaks pass.
- svlang: run on the combined delta text. Its aggregate score and 74 warnings are false positives caused by concatenated UI fragments, code/format tokens, product names and markup; each delta remains reviewed in source context. It has no INI parser.
