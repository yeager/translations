# Home Assistant Core: LIFX-teman, batch 61

Åtta LIFX-teman har granskats i sitt gränssnittssammanhang. Kategorierna följer den etablerade svenska indelningen: `Bibliotek`, `Världsligt` och `Arkiv`. Länderna använder svenska landsnamn och temat *Turkey Dinner* har översatts som `Kalkonmiddag`, inte som landet Turkiet.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera egennamn och produktnamn som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla åtta översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
