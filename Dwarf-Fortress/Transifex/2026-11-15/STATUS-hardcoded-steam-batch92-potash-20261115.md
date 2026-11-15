# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 92

- Scope: one complete in-game tutorial string about producing pottaska.
- Context: the source is a self-contained instructional paragraph. Its colour markup was preserved exactly and terms follow the project terminology: pottaska, askverkstad, vattenkälla and hink.
- Validation: JSON parsing, markup and newline parity, l10n-lint, svlang, Hunspell review, diff check and Gitleaks passed. Hunspell marks `askverkstaden`, a context-correct project compound. `msgfmt` does not apply to this JSON delta.
- Upstream: the Transifex API accepted the update with HTTP 200. Direct authenticated readback exactly matched the archived Swedish target.
- Status: submitted and visible upstream. It remains unreviewed, which is a separate Transifex workflow state.
