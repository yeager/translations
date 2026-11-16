# Cataclysm-DDA, svenska: batch 70

Tio aktuella oöversatta strängar om bioniska implantats hygien, kompatibilitet
och installationskrav. `CBM` återges konsekvent som `bioniskt implantat`.

## Kontroller före API-inskick

- Platsmarkörer och varningsmarkeringar ska bevaras.
- `l10n-lint --language sv --json-format auto`, Hunspell-SV och svlang granskas.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt för
  enskilda JSON-översättningar via Transifex API.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En oberoende GET-återläsning jämförde därefter varje målsträng med batchens
underlag: 10 av 10 stämde exakt.

`l10n-lint` och svlang passerade utan avvikelser. Hunspell-SV markerar endast
`bioniska`, en etablerad böjning av projektets tekniska term `bionisk`.
