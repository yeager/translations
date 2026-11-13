# Warzone 2100 – kampanj 2–3, svensk granskningsbatch

**Datum:** 2026-11-13

**Projekt och komponent:** Warzone 2100, huvudspel – slutet av kampanj 2 och inledningen av kampanj 3 (`cam2strings.txt:111–153`, `cam3strings.txt:4–40`)

**Omfattning:** 42 nya svenska meddelanden. Den lokala kandidaten innehåller nu 185 av 3 947 översatta meddelanden.

## Kontext och terminologi

Blocket innehåller satellitkommunikation, SAM-luftvärn, evakuering, missilavfyrning och den norra sektorn. Synliga förkortningar och namn som **NEXUS**, **NASDA**, **SAM**, **LZ** och **Bas Beta** behålls. Speltermer är bland annat *satellitlänksplats*, *luftvärnsrobotställning*, *säker zon*, *robotsilo* och *stridsspets*.

## Lokala kontroller

- `msgfmt --check --statistics`: godkänd, **185 översatta** och 3 762 oöversatta meddelanden.
- Diffkontroll: `git diff --check` samt whitespacekontroll av den otrackade PO-filen är godkända.
- Gitleaks: godkänd utan träffar för `po/sv.po`.
- Kontroll av tre lika konsonanter i följd: inga träffar i batchens svenska måltexter.
- Hunspell: träffar gäller granskade namn, förkortningar och sammansättningar, exempelvis `Satellitlänksplats`, `NASDA-satelliterna` och `robotsilon`.
- svlang: `skrivregler` godkänd; naturlighetskontrollens V2-varningar är granskade som falska positiva.
- l10n-lint: helkatalogen har kvar väntade `missing-translation`-diagnoser och kan därför inte godkännas som helhet före färdigställande.
- Projektets svenska TM/TBX saknas tills svenska aktiveras i Crowdin.

## Status

- Lokal radgranskning: färdig för denna batch.
- Arkivering och push: färdig och verifierad genom GitHubs API-svar.
- Crowdin-uppladdning, upstream-inskick, upstream-granskning och merge: har inte skett.