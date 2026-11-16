# Home Assistant Core: LIFX-teman, batch 63

Åtta LIFX-teman har granskats i gränssnittskontext. Länderna använder svenska landsnamn. `Synthwave` är ett etablerat namn på en musikgenre och `Taps` är ett tvetydigt temanamn utan tillräcklig produktkontext för en säker semantisk översättning; båda behålls därför som synliga namn.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera egennamn och produktnamn som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla åtta översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
