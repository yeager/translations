# Dwarf Fortress Steam, Swedish, batch 60

- Component: `hardcoded_steam` in `dwarf-fortress-translation/dwarf-fortress-steam`.
- Scope: 22 current untranslated strings with complete and safe UI, combat, world-generation or narrative context. Ambiguous fragments were deferred.
- Delta: `dwarf-fortress-hardcoded-steam-batch60-sv-20261114.json`.
- Checks: JSON syntax, `l10n-lint`, whitespace diff check, Gitleaks and low-priority time-limited Swedish Hunspell. `msgfmt` does not apply to this JSON delta.
- Hunspell exception: `Vapensmedsgrop` is a deliberate Swedish compound for the named location type.
- Upstream: one Transifex bulk PATCH accepted all 22 strings at 2026-11-14 07:32:48 UTC.
- Verification: direct API readback matched all 22 submitted target texts exactly.
