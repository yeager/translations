# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 93

- Scope: six complete in-game dialogue and tutorial strings.
- Context: the dialogue strings were self-contained. The tutorial string keeps every colour-control tag and its trailing space intact.
- Validation: JSON parsing, markup and newline parity, l10n-lint, svlang, Hunspell review, diff check and Gitleaks passed. `msgfmt` does not apply to this JSON delta.
- Upstream: Transifex's bulk endpoint returned HTTP 500 without importing this batch. The six entries were therefore submitted through the individual Transifex API endpoint; every request returned HTTP 200 and authenticated direct readback exactly matched the archived Swedish target.
- Status: submitted and visible upstream. They remain unreviewed, which is a separate Transifex workflow state.
