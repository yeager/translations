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

## Scope and next batch

Crowdin currently lists 100%-translated Swedish components with widely varying approval coverage. The next batch is `obs-vst3.ini` (0% approved), followed by `win-asio.ini` (0% approved) and the remaining plugin components before the frontend catalog.

## Checks

- INI key parity was checked against the local OBS source tree.
- `git diff --check`: not applicable to this no-change batch; no patch exists.
- `msgfmt`: not applicable; OBS uses INI catalogs.
- `l10n-lint`: no OBS INI parser available.
- Hunspell was intentionally not run, following the current CPU constraint.
- Gitleaks: deferred until a changed batch produces an archive payload.
