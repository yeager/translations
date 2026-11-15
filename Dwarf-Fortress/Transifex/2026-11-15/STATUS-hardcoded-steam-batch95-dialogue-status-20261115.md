# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 95

- Scope: 22 complete dialogue and status strings from the live untranslated queue.
- Context: only standalone source strings were selected. Fragmented text and strings that require agreement with runtime data were deliberately deferred.
- Validation: every archived source ID was checked against the live source; JSON parsing, l10n-lint, svlang, Hunspell review, diff check and Gitleaks passed. `msgfmt` does not apply to this JSON delta.
- Upstream: each update was accepted by the Transifex API with HTTP 200. Authenticated direct readback exactly matched all 22 archived Swedish targets.
- Status: submitted and visible upstream; Transifex review remains a separate workflow state.
