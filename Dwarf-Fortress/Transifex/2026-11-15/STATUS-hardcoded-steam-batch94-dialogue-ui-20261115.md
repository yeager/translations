# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 94

- Scope: eleven complete dialogue and UI strings from the live untranslated queue.
- Context: only self-contained strings were selected. Sentence fragments and strings whose correct Swedish form depends on interpolated game data remain out of scope for this batch.
- Validation: the archived source IDs were matched against the live source strings; JSON parsing, markup parity, l10n-lint, svlang, Hunspell review, diff check and Gitleaks passed. `msgfmt` does not apply to this JSON delta.
- Upstream: all eleven entries were accepted through the Transifex API with HTTP 200 and authenticated direct readback exactly matched every archived Swedish target.
- Status: submitted and visible upstream. They remain unreviewed, which is a separate Transifex workflow state.
