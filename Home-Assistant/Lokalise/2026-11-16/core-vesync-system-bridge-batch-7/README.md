# Home Assistant Core: VeSync och System Bridge, batch 7

Åtta aktuella svenska luckor har granskats mot komponentnyckel och föregående VeSync-batcher. Tillagning används konsekvent för fritösfunktionerna, även i knapparna per korg. System Bridge och VeSync är produktnamn och lämnas oförändrade.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; produktnamn och platshållaren är dokumenterade undantag.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
