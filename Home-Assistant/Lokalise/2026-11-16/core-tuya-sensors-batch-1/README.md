# Home Assistant Core: Tuya-sensorer, batch 1

Tre sensorspecifika strängar för Tuya har granskats i sitt enhetssammanhang. *Inlet* och *outlet* avser vätskans eller gasens flödesriktning och blir därför `inlopp` respektive `utlopp`. *Reactive power* är den etablerade elkrafttermen `reaktiv effekt`.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts. Hunspell-sv kan markera facktermer som förväntade träffar.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla tre översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
