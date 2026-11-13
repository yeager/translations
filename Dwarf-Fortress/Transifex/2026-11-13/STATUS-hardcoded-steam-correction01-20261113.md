# Dwarf Fortress Steam – hardcoded_steam – Swedish correction 01

- Date: 2026-11-13
- Source: Transifex resource `dwarf-fortress-steam / hardcoded_steam`
- Scope: one grammatical correction found in a previously submitted batch.
- Rationale: the English source is a third-person present-tense predicate. Swedish uses the finite form `hänger`, not the infinitive `hänge`.
- Validation: `jq`, `l10n-lint`, `gitleaks`, and Git whitespace validation are required before archiving. `msgfmt` does not apply because this is a JSON delta.
- Upstream submission: sent as one Transifex API request; the server recorded the correction.
- Upstream verification: direct API readback matched `hänger sig skickligt åt författarens fantasier` exactly.
- Upstream review and release: not verified; the returned record is not marked reviewed, proofread, or finalized.
