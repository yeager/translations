# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 96

- Scope: 19 complete dialogue and status strings from the live untranslated queue.
- Context: the selection excludes fragments and strings whose Swedish grammar depends on runtime data. Colour markup and source trailing spaces were preserved where present.
- Validation: every source ID was matched to the live source; JSON parsing, markup and trailing-space parity, l10n-lint, svlang, Hunspell review, diff check and Gitleaks passed. `msgfmt` does not apply to this JSON delta.
- Upstream: all 19 updates returned HTTP 200 through the Transifex API. Authenticated direct readback exactly matched the archived Swedish targets.
- Status: submitted and visible upstream; Transifex review remains a separate workflow state.
