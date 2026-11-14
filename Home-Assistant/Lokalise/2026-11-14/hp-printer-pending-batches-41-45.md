# HP Printer: lokalt granskade, väntande batcher 44–45

Datum: 2026-11-14

Detta underlag är arkiverat för spårbarhet. Strängarna är **inte** sparade
upstream i Lokalise ännu och får inte räknas som uppladdade eller återlästa.

| Batch | Omfattning | Status |
| --- | ---: | --- |
| 44 | 4 räknare för svartvitt och färg | Lokal QA godkänd; väntar på sparning och återläsning. |
| 45 | 10 skrivarstatusvärden | Lokal QA godkänd; väntar på sparning och återläsning. |

Sammanlagt: 14 lokalt granskade strängar.

Käll- och termkontroll:

- Home Assistants HP Printer-dokumentation bekräftar att integreringen visar
  skrivarets lokala status och räknare.
- Dokumentationen anger uttryckligen att `scanner_jams` gäller pappersstopp i
  dokumentmataren. Därför används “Pappersstopp i dokumentmataren”.
- Samtliga batcher har passerat l10n-lint, individuell svlang-kontroll,
  Hunspell-sv, diffkontroll och Gitleaks. `skannerglaset` är ett avsiktligt
  sammansatt fackord som Hunspell-sv inte känner igen.

Före sparning krävs fortfarande exakt nyckelkontroll, sparning i Lokalise och
separat återläsning av varje måltext. Batch 41–43 är sparade eller verifierade
upstream och dokumenteras i respektive batchfil.
