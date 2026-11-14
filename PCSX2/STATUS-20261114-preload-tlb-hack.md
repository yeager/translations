# PCSX2: förinläs TLB-hack, 14 november 2026

Kryssrutan `Preload TLB Hack` förekommer både i helskärmsgränssnittet och i
Qt-inställningarna. Båda använde tidigare `Förladdning TLB Hack`, en form som
varken följer PCSX2:s svenska terminologi eller fungerar väl som en kort
åtgärdsetikett. Källkoden bekräftar att det är samma kryssruta i båda
gränssnitten. `Förinläs TLB-hack` följer befintliga etiketter som `Hoppa över
MPEG-hack`, använder den svenska sammansättningen `TLB-hack` och undviker
onödigt lån av `load`.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade deltan till projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning bekräftar de nya kandidaterna `450039` för
sträng `8705` och `450041` för sträng `9995`, båda med exakt måltext
`Förinläs TLB-hack`. Kandidaterna är inskickade upstream, men inte
upstreamgranskade, automatiskt godkända eller valda som aktiva översättningar.
