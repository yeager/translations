# Home Assistant Core: LIFX-teman, batch 96

Åtta LIFX-teman har granskats i sitt gränssnittssammanhang. Tidigare fastställda svenska formuleringar används för kategorier och återkommande teman. `Cyberpunk` behålls som etablerad genre; länderna har svenska namn.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera egennamn och genrebeteckningar som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla åtta översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
