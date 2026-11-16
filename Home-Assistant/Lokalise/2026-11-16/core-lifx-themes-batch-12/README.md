# Home Assistant Core: LIFX-teman, batch 12

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Länder, världsdelar och rymdobjekt använder sina etablerade svenska namn. `Valentine's` avser högtiden och översätts därför med **Alla hjärtans dag**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
