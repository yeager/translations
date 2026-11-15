# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 97

- Scope: 41 complete UI and dialogue strings from the live untranslated queue.
- Context: the batch excludes sentence fragments and dynamic grammar. Existing Dwarf Fortress terminology was used for `ballista`, `Bågmakarverkstad` and interface labels.
- Validation: source IDs, markup and source trailing spaces were checked against the live resource; JSON parsing, l10n-lint, svlang, diff check and Gitleaks passed. Hunspell reports only `Bågmakarverkstad` and `ballista`, both intentional terms. `msgfmt` does not apply to this JSON delta.
- Upstream: all 41 updates were accepted by the Transifex API. Authenticated direct readback exactly matched every archived Swedish target.
- Status: submitted and visible upstream; Transifex review remains a separate workflow state.
