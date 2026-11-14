# PCSX2: källidentiska UI-etiketter, 14 november 2026

Tre måltexter i den nedladdade XLIFF-exporten har orelaterat innehåll trots
att källans UI-kontext anger att värdet ska behållas:

| Sträng-ID | Kontext | Korrekt måltext |
| ---: | --- | --- |
| `5003` | Val av grafikmotor | `Vulkan` |
| `5291` | Visning av inmatningsinspelning | `%1 [%2]` |
| `5869` | Kortplats för minneskort | `%1 [%2]` |

Källidentisk text är här avsiktlig: `Vulkan` är ett synligt API-namn och de
två formatsträngarna består endast av platshållare och syntax. Deltafilen
innehåller bara dessa tre poster.

XML-validering, l10n-lint, svlang, lågprioriterad Hunspell-SV,
diffkontroll och Gitleaks passerade. `msgfmt` är inte tillämpligt på XLIFF.
Upstream-resultat dokumenteras här först efter verifierat API-svar.
