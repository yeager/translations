# Status – svensk granskning av Home Assistant Core

Senast uppdaterad: 2026-11-20.

## Omfattning och kontrollpunkt

- Granskning har genomförts rad för rad t.o.m. Lokalise-sida 730.
- Sida 731 är granskad och dess sex sparade ändringar har återlästs och förts in i TMX-minnet.
- Tidigare arbete fram till sida 614 finns i tidigare rapporter i denna katalog. Sidor 615–730 är fortsatt spårade genom Lokalise-ID:n och det kanoniska TMX-minnet; sidor 727–730 har kompletterande fullständig ändringsrapport.

## Kanoniskt Home Assistant-minne

- Fil: `yeager/swedish-tm/Home-Assistant/sv-home-assistant-core-lokalise-verified-20261120-canonical.tmx`.
- Senast verifierad nivå: **769** unika översättningsenheter, t.o.m. sida 731.
- XML-kontroll: unika `tuid`-värden och fullständig `source`-proveniens för varje post.
- Alla 769 enheter har full nyckel som `source`, engelskt och svenskt segment samt statusen `saved-and-read-back`.
- 572 senare poster använder `lokalise:<översättnings-id>` som `tuid`. De 197 historiska posterna använder i stället den fullständiga källnyckeln som `tuid`; deras Lokalise-ID behöver hämtas från API:t innan de kan migreras säkert.

## Pågående uppföljning

| Nyckel | Status | Nästa säkra kontroll |
| --- | --- | --- |
| Nya tomma HotSpring-poster och följdposter | 14 förslag dokumenterade utan Lokalise-skrivning. | Kontrollera att HotSpring-källan publicerats i Core före ett eventuellt sparbeslut. |
| `component::timer_list` | 35 tomma strängar granskade mot aktuell Core-källa och dokumenterade som förslag. | Fortsätt från `services::finish_timer`; behåll förslagsstatus tills ett sparbeslut finns. |
| 197 historiska TMX-enheter | Strukturellt giltiga men saknar Lokalise-ID i `tuid`. | Slå upp varje fullständig `source`-nyckel via Lokalise-API:t och ersätt `tuid` först efter en unik matchning. |

## Miljöstatus

Den tidigare autentiserade Lokalise-sessionen och dess API-hjälpare återställdes av miljön, men en läsbehörig Lokalise-yta har återetablerats. Ingen Lokalise-skrivning görs. Fortsatt arbete använder inte `/tmp`; cache, rapporter och valideringsunderlag ska ligga i arbetsytan eller i respektive GitHub-repository.

## Källkontroll efter sessionens återställning

- Home Assistant Core kontrollerades mot uppströms-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12` (2026-11-20).
- `homeassistant/components/logbook/strings.json` och `homeassistant/components/script/strings.json` innehåller fortfarande de engelska källtexter som sida 731 granskades mot, inklusive `Log activity`, `Reload scripts` och `Toggle script`.
- Detta bekräftar att de dokumenterade sida-731-förslagen inte bygger på föråldrad engelsk källtext. Det ersätter inte Lokalise-återläsningen av de svenska målvärdena och ger därför inte underlag för TMX-synkning.

## Verktygsaudit

- `svlang`, `hunspell-sv`, `swedish-foss-terminology` och `swedish-tm` har kontrollerats från rena arbetskopior i arbetsytan.
- Python-källorna kompilerar och `swedish-foss-terminology` kan starta sin export-CLI. Fulla pytest-sviter är inte körda eftersom den återställda miljön saknar `pytest`.
- Hunspell markerar `klimatprofilsindex`, trots att beståndsdelarna accepteras. Termen kommer från den aktuella Home Assistant-kontexten men saknar här en oberoende generell ordbokskälla. Enligt `hunspell-sv`-policyn läggs den därför inte in som en global enskild katalogterm; träffen är en granskningssignal, inte ett automatiskt verktygsfel.
- `swedish-tm` innehåller från commit `fac51ee` den beroendefria valideraren `scripts/validate_home_assistant_core_tmx.py`. Den validerar XML, språksegment, källproveniens och review-status samt rapporterar skillnaden mellan Lokalise-ID och historiska nyckelbaserade `tuid`-värden. Dess strikta migrationsläge är avsiktligt rött tills ID-rekonstruktionen kan verifieras via API:t.

## Referenser

- [Sparade ändringar på sidor 727–730](sparade-andringar-sidor-727-730.md)
- [Sida 731: granskning och kvarstående verifiering](granskning-sida-731-logbook-script.md)
- [Nya tomma HotSpring-strängar och följdposter](granskning-nya-tomma-strangar-hotspring.md)
- [Timer list: fortsatt granskning av tomma strängar](granskning-timer-list-fortsattning.md)
- [Timer list: återstående granskade tjänststrängar](granskning-timer-list-tjanster.md)
