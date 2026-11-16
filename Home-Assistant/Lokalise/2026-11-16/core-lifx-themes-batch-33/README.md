# Home Assistant Core: LIFX-teman, batch 33

Denna batch fortsätter de svenska namnen på LIFX-teman. `Lo-fi` är en etablerad svensk form för musikstilen. Övriga teman får svenska ord och etablerade svenska landnamn; `Lucky Shamrock` blir **Lyckoklöver**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera egennamn och produktnamn som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla åtta översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
