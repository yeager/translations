# Status – svensk granskning av Home Assistant Core

Senast uppdaterad: 2026-11-20.

## Omfattning och kontrollpunkt

- Granskning har genomförts rad för rad t.o.m. Lokalise-sida 730.
- Sida 731 är påbörjad; fem ändringar återlästes som sparade men har ännu inte förts in i TMX efter miljöåterställningen. En ytterligare referenssträng har ett dokumenterat, ännu ej verifierat förslag.
- Tidigare arbete fram till sida 614 finns i tidigare rapporter i denna katalog. Sidor 615–730 är fortsatt spårade genom Lokalise-ID:n och det kanoniska TMX-minnet; sidor 727–730 har kompletterande fullständig ändringsrapport.

## Kanoniskt Home Assistant-minne

- Fil: `yeager/swedish-tm/Home-Assistant/sv-home-assistant-core-lokalise-verified-20261120-canonical.tmx`.
- Senast verifierad nivå: **763** unika översättningsenheter, t.o.m. sida 730.
- XML-kontroll: unika `tuid`-värden och fullständig `source`-proveniens för varje post.
- Varje enhet har Lokalise-översättnings-ID i `tuid`, full nyckel som `source`, engelskt och svenskt segment samt statusen `saved-and-read-back`.

## Pågående uppföljning

| Nyckel | Status | Nästa säkra kontroll |
| --- | --- | --- |
| `component::script::services::toggle::name` | Förslag dokumenterat: `[%key:common::action::toggle%] skript`. | Återläs från Lokalise, kontrollera att referensen bevarats och lägg sedan till i TMX. |
| Sida 731, fem återlästa ändringar | Sparade och dokumenterade, men ännu inte tillagda i TMX. | Återanslut till Lokalise-API, hämta aktuell sida och synka endast de bekräftade Lokalise-ID:na. |

## Miljöstatus

Den tidigare autentiserade Lokalise-sessionen och dess API-hjälpare återställdes av miljön. Efter återställningen görs ingen Lokalise-skrivning. Fortsatt arbete använder inte `/tmp`; cache, rapporter och valideringsunderlag ska ligga i arbetsytan eller i respektive GitHub-repository.

## Referenser

- [Sparade ändringar på sidor 727–730](sparade-andringar-sidor-727-730.md)
- [Sida 731: granskning och kvarstående verifiering](granskning-sida-731-logbook-script.md)
