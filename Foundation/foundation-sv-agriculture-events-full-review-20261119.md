# Foundation – jordbruks-DLC: händelser, full radgranskning 2026-11-19

Samtliga 93 strängar i `dlc_agriculture_events.json` granskades via Crowdin API. 27 förbättringsförslag identifierades och dokumenteras rad för rad i tre batchrapporter.

| Batch | Omfattning | Rapport |
| --- | --- | --- |
| I | Festivalintroduktion och första uppdrag | [händelser I](foundation-sv-agriculture-events-part1-review-20261119.md) |
| II | Gårdar, trubadurens uppdrag och festivalstatus | [händelser II](foundation-sv-agriculture-events-part2-review-20261119.md) |
| III | Kungabesök och underhållare | [händelser III](foundation-sv-agriculture-events-part3-review-20261119.md) |

## Kontroller

- Varje förslagsbatch passerade `l10n-lint --language sv`.
- Varje förslagsbatch passerade `hunspell -d sv_SE`.
- Styckebrytningar, formatmarkörer och terminologin *Harvest Festival* → *skördefestival* har verifierats.
- Förslagen har inte skickats till Crowdin.
