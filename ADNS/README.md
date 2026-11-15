# ADNS – svenska

Senast granskad: 15 november 2026

| Komponent | Omfattning | Lokal status | Upstreamstatus |
| --- | ---: | --- | --- |
| `adns-xml-strings` | 432/432 | Radgranskad | 16 förslag mottagna av Weblate, väntar på granskning |
| `nextdns-strings` | 200/774 | Batch 001–002 radgranskade | 4 förslag mottagna av Weblate, väntar på granskning |

ADNS v2.1.9 publicerades den 3 november 2026. Android-XML-komponenten har
granskats mot den engelska källfilen i fem avgränsade batcher. Batch 001
krävde ingen ändring; batch 002–005 innehåller sammanlagt 16 materiella
rättningar. Varje ändringsbatch har validerats som XML och med `l10n-lint`,
`git diff --check` och Gitleaks. `msgfmt` är inte tillämpligt på Android-XML;
Hunspell kördes inte för att begränsa CPU-belastningen.

Förslagen är mottagna av Hosted Weblate men inte godkända eller publicerade.
Deltafiler och kontrollanteckningar finns i katalogerna
`2026-11-15-adns-xml-batch-001/` till `2026-11-15-adns-xml-batch-005/`.
