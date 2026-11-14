# Dwarf Fortress Steam, Swedish, batch 59

- Component: `hardcoded_steam` in `dwarf-fortress-translation/dwarf-fortress-steam`.
- Scope: 23 current untranslated strings with complete, context-safe UI, combat or narrative meaning. Fragments and unclear terrain terms were deferred.
- Delta: `dwarf-fortress-hardcoded-steam-batch59-sv-20261114.json`.
- Checks: JSON syntax, `l10n-lint`, whitespace diff check, Gitleaks and low-priority time-limited Swedish Hunspell. `msgfmt` does not apply to this JSON delta.
- Hunspell exception: `jaktdjur` is a correct Swedish compound that is absent from the local dictionary.
- Upstream: one Transifex bulk PATCH accepted all 23 strings at 2026-11-14 07:29:33 UTC.
- Verification: direct API readback matched all 23 submitted target texts exactly.
