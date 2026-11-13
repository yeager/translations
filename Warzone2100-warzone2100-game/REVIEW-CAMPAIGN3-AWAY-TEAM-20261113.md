# Warzone 2100 – kampanj 3, svensk granskningsbatch

**Datum:** 2026-11-13

**Projekt och komponent:** Warzone 2100, huvudspel, kampanj 3 (`cam3strings.txt:43–118`)

**Omfattning:** 40 nya svenska meddelanden. Kandidaten innehåller nu 225 av 3 947 översatta meddelanden.

## Kontext

Batchen är berättelse- och uppdragsinformation om insatsgruppen, Grupp Alfa, Grupp Gamma och NEXUS. Källans avsiktligt ofullständiga punktrader bevaras i svensk översättning; endast synlig text är översatt.

## Lokala kontroller

- `msgfmt --check --statistics`: godkänd, 225 översatta och 3 722 oöversatta meddelanden.
- Diffkontroll och Gitleaks för `po/sv.po`: godkända.
- Kontroll av tre lika konsonanter i följd: inga träffar i batchens svenska måltexter.
- Hunspell: enbart granskade spelnamn, förkortningar och sammansättningar.
- svlang: `skrivregler` godkänd. Naturlighetsverktygets V2-varningar är falska positiva för rubriker och korrekta svenska satser.
- l10n-lint: full katalog har väntade `missing-translation`-diagnoser; den kan inte godkännas som helhet innan katalogen är komplett.
- Projektets svenska TM/TBX saknas tills svenska aktiveras i Crowdin.

## Status

- Lokal radgranskning: färdig för denna batch.
- Arkivering och push: färdig när filerna är synliga på `main`.
- Crowdin-uppladdning, upstream-inskick, upstream-granskning och merge: har inte skett.