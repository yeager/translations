# Open Shaders: VR, dynamiskt närklippavstånd, häfte 99

Detta delta omfattar tolv strängar för VR-funktionens dynamiska
närklippavstånd. Källtexterna har jämförts med Open Shaders `dev` vid revision
`c1b1ef1` den 27 oktober 2026.

*Near clip* översätts konsekvent med *närklippavstånd*, vilket följer den
tidigare etablerade termen *klippavstånd*. *Depth probe* blir
*djupavkännare*. Produktnamnet Skyrim och namnet Exponentiell höjddimma
bevaras. Deltafilen får importeras först efter upplåsning och jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, nyckeljämförelse, `l10n-lint`, svensk språkgranskning,
Hunspell-genomgång, Gitleaks och Git-whitespacekontroll har körts.
`svlang` ger två felaktiga V2-varningar: den ena på ett sammansatt
gränssnittsbegrepp som subjekt och den andra på en korrekt relativ bisats.
Hunspell markerar endast produktnamn och tekniska fackord.
