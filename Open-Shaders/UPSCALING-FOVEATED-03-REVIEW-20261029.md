# Open Shaders: foveerad uppskalning, granskning 3

Det tredje uppskalningshäftet innehåller 25 nycklar för visning i periferin,
områdesmasker och foveerad finjustering i VR.

`Foveerad rendering` används i svensk VR-facktext och ligger till grund för
den konsekventa formen `foveerad uppskalning`. `Upscaler` har översatts med
`uppskalningsmetod`; `Periphery AA` med `kantutjämning i periferin`.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga facktermer och förkortningar, bland
  annat DLSS, FSR, VR och `foveerad`.
- `svlang check` ger V2-markeringar för giltiga bisatser, etiketter och
  imperativ. Dessa har granskats manuellt; verktygets frekvenslista är inte
  representativ för GPU- och VR-terminologi.
- Filen måste jämföras mot en ny Weblate-export före import.
