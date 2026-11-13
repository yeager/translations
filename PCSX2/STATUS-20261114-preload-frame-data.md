# PCSX2: förinläsning av bildrutedata, 14 november 2026

Två UI-etiketter för `Preload Frame Data` använde den inkonsekventa formen
`Förladdning av ramdata`. I grafik- och gränssnittskontexten används
`bildruta`, och PCSX2:s terminologilista anger `förinläsning` för `preload`.
Den korta åtgärdsformen `Förinläs bildrutedata` är lämplig för båda
etiketterna.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade filen till projekt `561203`, fil `15`, språk
`sv-SE`: 2 strängar och 6 ord importerades, 0 godkändes automatiskt och 0
hoppades över. Direkt återläsning bekräftar de ogranskade kandidaterna
`450033` för sträng `9907` och `450035` för sträng `4811`. Kandidaterna är
inskickade upstream, men inte upstreamgranskade eller valda som aktiva
översättningar.
