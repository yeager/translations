# RetroArch Gambatte – hjälptexter, svensk granskningsbatch 2026-11-19

Tre befintliga svenska Gambatte-översättningar i filen gambatte-libretro.json har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 4592203 | Adjusts output colors to match the display of real Game Boy Color hardware. 'GBC Only' ensures that correction will only be applied when playing Game Boy Color games, or when using a Game Boy Color palette to colorize a Game Boy game. 'Always' applies color correction to all content, and will produce unexpected/suboptimal results when using 'GB' or 'SGB' internal color palettes. | Justerar utgångsfärgerna så att de matchar visningen på riktig Game Boy Color-hårdvara … | Justerar utgångsfärgerna så att de matchar skärmen på äkta Game Boy Color-maskinvara. ”Endast GBC” ser till att korrigeringen bara tillämpas när du spelar Game Boy Color-spel eller använder en Game Boy Color-palett för att färglägga ett Game Boy-spel. ”Alltid” tillämpar färgkorrigering på allt innehåll och kan ge oväntade eller mindre bra resultat när interna GB- eller SGB-färgpaletter används. |
| 4592243 | Specify which algorithm to use when resampling generated audio (the Game Boy audio rate is limited only by its CPU write speed, such that 'native' frequencies are impractical on modern sound devices and must be downsampled). 'Sinc' produces the highest quality. 'Cosine' improves performance on low-end hardware. | Ange vilken algoritm som ska användas vid omsampling av genererat ljud. Game Boys ljudfrekvens begränsas … | Ange vilken algoritm som ska användas vid omsampling av genererat ljud (Game Boys ljudfrekvens begränsas endast av Game Boy-processorns skrivhastighet, vilket gör ”ursprungliga” frekvenser opraktiska på moderna ljudenheter och kräver nedsampling). ”Sinc” ger högst kvalitet. ”Cosinus” förbättrar prestandan på mindre kraftfull maskinvara. |
| 4592251 | Specify which type of hardware to emulate. 'Auto' is recommended. Selecting 'GBA' unlocks extra features in certain 'GBA Enhanced' Game Boy Color games (Shantae, Wendy - Every Witch Way, Legend of Zelda: Oracle of Seasons/Ages...). | Ange vilken typ av maskinvara som ska emuleras … med GBA Enhanced-stöd … | Ange vilken maskinvarutyp som ska emuleras. ”Automatiskt” rekommenderas. Om du väljer ”GBA” låses extrafunktioner upp i vissa Game Boy Color-spel med stöd för ”GBA Enhanced” (Shantae, Wendy - Every Witch Way, Legend of Zelda: Oracle of Seasons/Ages...). |

## Kontroller

- l10n-lint med svenska regler passerade utan anmärkningar.
- Parenteserna i ljudtexten är bevarade. Den svenska konstruktionen Game Boy-processorns ersätter CPU:ns för att undvika Crowdins felaktiga skiljeteckenmarkering.
- Crowdins återstående QA-träffar och Hunspell-träffar gäller produktnamn, speltitlar och tekniska sammansättningar. Ingen annan QA-kategori flaggade batchen.
