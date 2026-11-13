# PCSX2: primitivrensning för bildbuffert, 14 november 2026

Sträng `8285` är etiketten för en grafikinställning som framtvingar en
primitivrensning när en bildbuffert också används som inmatningstextur. Den
aktiva texten hade fel ordföljd och behöll `framebuffer` på engelska. Den
granskade formuleringen använder den svenska grafiktermen `bildbuffert` och
det tekniska `primitivrensning`, i linje med den längre hjälptexten för samma
inställning.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade filen till projekt `561203`, fil `15`, språk
`sv-SE`: 1 sträng och 12 ord importerades, 0 godkändes automatiskt och 0
hoppades över. Direkt återläsning bekräftar den ogranskade kandidaten
`450037`. Kandidaten är inskickad upstream, men inte upstreamgranskad eller
vald som aktiv översättning.
