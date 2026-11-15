# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 82

- **Date:** 2026-11-15
- **Scope:** 24 current, untranslated menu labels and gameplay terms: actions, terrain, facilities, material handling, combat, creatures and access settings.
- **Terminology:** Swedish UI terms retain the component's established imperative style. `Wood Furnace` is translated as `Vedugn`, `Lye Making` as `Lutframställning`, and `Monster slayer` as `Monsterdräpare`. Intentional identity translation: `Terrarium`.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell reported the valid compounds `Lutframställning` and `Monsterdräpare`. `svlang`'s only English-source hit comes from parsing the JSON wrapper. `l10n-lint` cannot parse the wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 24 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 24/24.
- **Status:** Submitted and verified upstream. Transifex has not marked the entries reviewed.
