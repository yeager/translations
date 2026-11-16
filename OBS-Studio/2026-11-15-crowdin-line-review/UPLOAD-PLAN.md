# Crowdin submission plan

Status: 1 correction sent and read back (`App/Plugins/VLC Video`); 549 remain pending.

2026-11-16: a single XML-validated XLIFF was prepared for the 298 distinct
`App/Core` and `App/Frontend Tools` corrections. It is not recorded as
uploaded: Crowdin's import dialog was reached, but the browser interface could
not attach a local file to its native file selector.

OBS maintainers confirmed on 2026-11-15 that translations are accepted through
Crowdin, not GitHub pull requests. This plan is therefore the only upstream
submission path for the reviewed catalogs, including ASIO Output UI, Windows
ASIO and VST3.

The archive contains 550 validated Swedish changes. They must be applied to
the current live Crowdin strings, not uploaded as whole INI catalogs: the
local OBS checkout can lag behind Crowdin and a full-file upload could replace
newer translations.

## Submission units

- `App/Core`: 91 changes, one component batch.
- `App/Frontend`: 206 changes, split into three batches of at most 100
  strings while preserving the current live string IDs.
- Each remaining component: one component batch (at most 30 changes).

After each component batch, read back the saved translations and compare the
string IDs, source text, placeholders and target values with its delta file.
Mark a translation reviewed only when Crowdin confirms the saved value.

No API token, session secret or exported credentials belong in this directory.
