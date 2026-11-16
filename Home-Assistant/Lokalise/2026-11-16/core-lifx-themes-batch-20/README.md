# Home Assistant Core: LIFX-teman, batch 20

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Länder och planeter använder etablerade svenska namn. Det engelska genrenamnet `Sci Fi` skrivs ut som **Science fiction**, medan övriga teman har naturliga svenska titlar som **Tomteverkstad**, **Skrikdrottning** och **Oas för egenvård**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
