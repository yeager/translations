# Home Assistant Core: VeSync, Samsung ExLink och Plex, batch 5

Åtta aktuella svenska luckor har granskats mot komponentnyckel och tidigare Home Assistant-översättningar. Tillståndet `Standby` översätts konsekvent med **Vänteläge**. I VeSync avser `basket` fritöskorgen och benämns därför **korg**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; VeSync, ExLink, Plex och platshållaren är tekniska eller egna namn.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
