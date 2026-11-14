# PCSX2: assemblerkod i felsökaren, 14 november 2026

Felsökaren har både en dockningsbar vy och en egen fönsterrubrik med namnet
`Disassembly`. Källkoden visar att det är samma vy som visar
processorinstruktioner i assemblerform. `Assemblerkod` beskriver innehållet
direkt, fungerar som kort fliktext och undviker en krystad direktöversättning
av processen.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade deltan till projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning bekräftar kandidaten `450065` för sträng `13532`
och `450067` för sträng `13554`, båda med måltexten `Assemblerkod`.
Kandidaterna är inskickade upstream, men inte upstreamgranskade,
automatiskt godkända eller valda som aktiva översättningar.
