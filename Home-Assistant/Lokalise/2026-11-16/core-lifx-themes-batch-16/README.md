# Home Assistant Core: LIFX-teman, batch 16

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Teman och kategorier har idiomatiska svenska benämningar, till exempel **Stjärnstoft**, **Sommarskymning** och **Stormfront**. Helgdagen följer svensk förkortning i **S:t Patricks dag**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
