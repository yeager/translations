# RetroArch Swedish Crowdin submission — 2026-10-29

- Project: RetroArch, Swedish (`sv-SE`), Crowdin.
- Submitted by: `yeagersthlm`.
- Scope: the 19 strings in `retroarch-sv-untranslated-20261029.json`.
- Result: Crowdin confirmed **“Successfully added 19 translations”**.
- Verification: immediately after saving, the editor's **Untranslated** filter showed **0 STRINGS** and **No unsaved translations**.
- Local checks before submission: structural JSON validation, `svlang skrivregler`, `l10n-lint` on a source-to-target JSON projection, Hunspell review, scoped Gitleaks, and `git diff --check`.

Hunspell's remaining flags were accepted technical/product terms or identifiers: `04X`, `ABXY-inmatningsmetod`, `Cursor`, `DLSS`, `Hover`, `Moves`, `Originalhandkontroll`, `RetroArch`, `Stylus`, `Xbox`, `power-profiles-daemon`, `stylus`, `stylusen`, and `tuned-ppd`.

## Xemu/Vita3K batch 01 — 2026-11-03

- Scope: 50 context-reviewed strings from the Xemu and Vita3K core settings and package-management flow.
- Submission: Crowdin confirmed **“Successfully added 17 translations”** after the first 33 had saved; the editor then reported **“No unsaved translations”**.
- Archive: `retroarch-sv-xemu-vita3k-batch-01-20261103.json`.
- Checks: JSON structure, placeholder parity, `l10n-lint`, Hunspell review, and scoped Gitleaks. Hunspell's remaining flags are technical identifiers and product terms, including APU, DSP, DLAA, DLC, GiB, PKG, `.pup`, `param.sfo`, `vita3k`, `work.bin`, and `zRIF`.

## Xemu/Vita3K batch 02 — 2026-11-03

- Scope: 28 further context-reviewed Vita3K strings: package and archive errors, account controls, and Vulkan/GPU renderer options.
- Submission: the final Crowdin save reported **“Successfully added 17 translations”** and the editor reported **“No unsaved translations”**. This completed the saved entries in the two prepared Xemu/Vita3K batches.
- Archive: `retroarch-sv-xemu-vita3k-batch-02-20261103.json`.

## Vita3K format QA — 2026-11-03

- Corrected the two batch-01 labels whose English source deliberately lacks a terminal full stop.
- Verification: Crowdin now shows the corrected translations and **“No unsaved translations”**.

## Cemu review batch 01 — 2026-11-03

- Corrected the PowerPC CPU-mode explanation: it now distinguishes the game profile's mode from the profile itself and consistently uses the established `omkompilerare` terminology.
- Archive: `retroarch-sv-cemu-batch-01-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks. The remaining Hunspell flags are the Cemu product name and the established technical term `omkompileraren`.
- Submission: saved in Crowdin and verified as **“No unsaved translations”**.

## Cemu review batch 02 — 2026-11-03

- Clarified the TV-audio-channel behaviour and restored the literal `\\n` separators and parentheses that Crowdin checks for in account-entry and GPU-accuracy descriptions.
- Archive: `retroarch-sv-cemu-batch-02-20261103.json`.
- Checks: JSON structure, `l10n-lint`, control-symbol parity, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.
- Submission: saved in Crowdin and verified as **“No unsaved translations”**.

## Cemu review batch 03 — 2026-11-03

- Restored the parenthesized controller and sensor context in the dead-zone and GamePad-motion explanations, so the Swedish text retains both the factual detail and Crowdin's symbol parity.
- Archive: `retroarch-sv-cemu-batch-03-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, and scoped Gitleaks; product and controller names remain intentional Hunspell exceptions.
- Submission: saved in Crowdin and verified as **“No unsaved translations”**.

## Cemu review batch 04 — 2026-11-03

- Restored the source's parenthesized context in the internal-resolution, audio-thread, and audio-profiling explanations.
- Archive: `retroarch-sv-cemu-batch-04-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, and scoped Gitleaks. Crowdin's numeric comparison cannot parse Swedish decimal commas and multiplication signs, so its number warnings are false positives; the numeric values themselves are preserved.
- Submission: saved in Crowdin with **“Save Anyway”** for that false positive, then verified as **“No unsaved translations”**.

## Cemu component review complete — 2026-11-03

- All 153 strings in `cemu-libretro/cemu-libretro.json` were reviewed page by page in Crowdin.
- The final page contains only the approved `50%`, `100%`, and `Normal` values; no further change was warranted.

## Xenia review batch 01 — 2026-11-03

- Corrected the D3D9 half-pixel wording so it tells the user that the mode provides correct rendering for most games.
- Archive: `retroarch-sv-xenia-batch-01-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, and scoped Gitleaks.
- Submission: saved in Crowdin and verified as **“No unsaved translations”**.

## Xenia review batch 02 — 2026-11-03

- Replaced the English graphics term `vertex` with the established Swedish term `hörnpunkt` in the invalid-fetch-constants warning.
- Archive: `retroarch-sv-xenia-batch-02-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, and scoped Gitleaks.
- Submission: saved in Crowdin and verified as **“No unsaved translations”**.

## Xenia component review complete — 2026-11-03

- All 251 strings in `xenia-libretro/xenia-libretro.json` were reviewed page by page in Crowdin.
- Pages 2–6 contained no further high-confidence changes. Their remaining QA flags are intended technical terms, punctuation or number-parser false positives, and already-approved shared values.

## RPCS3 review batch 01 — 2026-11-03

- Submitted two context-checked strings in `rpcs3-libretro/rpcs3-libretro.json` through Crowdin.
- Restored source punctuation around the RPCS3 default-setting explanation and the PS3 BD-ROM speed (`9 MB/s`) without changing their emulator semantics.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.

## RPCS3 review batch 02 — 2026-11-03

- Submitted a context-corrected ReBAR explanation in `rpcs3-libretro/rpcs3-libretro.json` through Crowdin.
- The parenthetical now has an explicit subject: the setting is enabled by default in RPCS3 as well.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.

## RPCS3 review batch 03 — 2026-11-03

- Submitted three context-checked strings in `rpcs3-libretro/rpcs3-libretro.json` through Crowdin.
- Restored the Windows configuration-path parenthesis, split an ambiguous debugging warning into two complete Swedish sentences, and replaced the literal translation of a busy loop with the technical Swedish term `aktiv vänteloop`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.

## RPCS3 review batch 04 — 2026-11-03

- Submitted the database-override and audio-output descriptions in `rpcs3-libretro/rpcs3-libretro.json` through Crowdin.
- Restored the source parenthesis and clarified that the database contains game-specific corrections. The audio description now states accurately that the PS3 reports its available speakers to games and retains the game's own stereo/surround selection behaviour.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.

## RPCS3 review batch 05 — 2026-11-03

- Restored the source parenthesis in the exact double-precision fused-multiply-add explanation and made the default-setting subject explicit.
- Archive: `retroarch-sv-rpcs3-batch-05-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.

## RPCS3 review batch 06 — 2026-11-03

- Replaced the English term `vertex` with the established Swedish graphics term `hörnpunkt` in the vertex-cache label and description.
- Archive: `retroarch-sv-rpcs3-batch-06-20261103.json`.
- Checks: JSON structure, `l10n-lint`, `svlang skrivregler`, Hunspell review, and scoped Gitleaks.
