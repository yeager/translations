# PCSX2: EE-cykelöverhoppning och jämn sprite-position, 14 november 2026

`EE Cycle Skipping` används som etikett för samma fartinställning i Qt och i
helskärmsgränssnittet. Den ena svenska formen var den oidiomatiska
`Hoppning av EE-cykler`, medan den andra fortfarande var engelsk.
`EE-cykelöverhoppning` gör inställningen kort, konsekvent och tydlig.

`Force Even Sprite Position` är en kryssruta i grafikkorrigeringarna. Den var
redan korrekt översatt som `Tvinga jämn sprite-position` i två andra vyer men
inte i den vanliga Qt-inställningen. Samma svenska etikett används därför i
alla tre vyerna.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast de nya måltexterna, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade deltan till projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning bekräftar kandidaterna `450043` för sträng
`16537`, `450045` för sträng `8133` och `450047` för sträng `11552`.
Kandidaterna är inskickade upstream, men inte upstreamgranskade,
automatiskt godkända eller valda som aktiva översättningar.
