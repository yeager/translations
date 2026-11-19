# Foundation – jordbruks-DLC: upplåsningar, full radgranskning 2026-11-19

Samtliga 51 strängar i `dlc_agriculture_unlockables.json` granskades via Crowdin API. Tjugo förbättringsförslag identifierades; övriga 31 bedömdes korrekta.

## Sammanfattning av förslag

- `Harvest Festival` och samtliga berörda beskrivningar använder konsekvent **skördefestival** i stället för *skördefest*.
- `Festival Grounds` blir **festivalområdet**.
- `Additional Minstrels` blir **Ytterligare trubadurer**, och den tillhörande beskrivningen använder *trubadurer*.
- `{1} Folk Game` använder svensk gemen: **{1} folklek**.

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` har bevarats.
- Förslagen har inte skickats till Crowdin efter den senaste uttryckliga sparåtgärden.
