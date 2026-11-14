# PCSX2: avflätning, 14 november 2026

Inställningsetiketten `Deinterlacing` förekommer både i helskärmsgränssnittet
och i Qt-inställningarna. Den väljer metod för att hantera den emulerade
konsolens sammanflätade bild. `Avflätning` är svensk fackterm för denna
bildbehandling och ersätter det onödiga engelska lånet i båda vyerna.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade deltan till projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning bekräftar kandidaten `450061` för sträng `8193`
och `450063` för sträng `5055`, båda med måltexten `Avflätning`.
Kandidaterna är inskickade upstream, men inte upstreamgranskade,
automatiskt godkända eller valda som aktiva översättningar.
