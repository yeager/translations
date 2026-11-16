# Home Assistant Core: LIFX-teman, batch 9

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Kategorierna översätts, medan geografiska namn och genrebeteckningen **Zombie** behålls. `Archives` återges som **Arkiv**, i enlighet med den etablerade svenska benämningen för sådana samlingar.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
