# HP Printer: batcherna 41–45 är klara

Datum: 2026-11-14

Detta underlag är arkiverat för spårbarhet. Samtliga strängar i batch 41–45
är nu sparade eller separat verifierade i Lokalise.

| Batch | Omfattning | Slutstatus |
| --- | ---: | --- |
| 41 | 2 etiketter för pappersstopp | En sparad, en redan korrekt. |
| 42 | 4 grundläggande sidräknare | Samtliga redan korrekta. |
| 43 | 7 räknare för ark, dokumentmatare och skannerglas | Tre sparade, fyra redan korrekta. |
| 44 | 4 räknare för svartvitt och färg | Två sparade, två redan korrekta. |
| 45 | 10 skrivarstatusvärden | Tre sparade, sju redan korrekta. |

Käll- och termkontroll:

- Home Assistants HP Printer-dokumentation bekräftar att integreringen visar
  skrivarets lokala status och räknare.
- Dokumentationen anger uttryckligen att `scanner_jams` gäller pappersstopp i
  dokumentmataren. Därför används “Pappersstopp i dokumentmataren”.
- Samtliga batcher har passerat l10n-lint, individuell svlang-kontroll,
  Hunspell-sv, diffkontroll och Gitleaks. `skannerglaset` är ett avsiktligt
  sammansatt fackord som Hunspell-sv inte känner igen.

Varje ändrad måltext sparades i Lokalise och lästes därefter tillbaka separat.
Oförändrade texter kontrollerades också mot sin exakta nyckel.
