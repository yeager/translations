# Crowdin submission plan

Status: prepared locally; not sent.

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
