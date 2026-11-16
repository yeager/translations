# Home Assistant Core: LIFX-teman, batch 78

Åtta LIFX-teman har granskats i gränssnittskontext. Länderna använder svenska landsnamn. Person- och konstnärsnamnen Molly Malone, Mondrian och Monet behålls som egennamn.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera egennamn och produktnamn som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla åtta översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
