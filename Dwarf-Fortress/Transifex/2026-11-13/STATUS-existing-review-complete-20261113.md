# Dwarf Fortress 50.* `text_set`: befintlig svenska, komplett granskning

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`

## Omfattning

Samtliga 186 svenska strängar som var översatta vid granskningstillfället
hämtades från Transifex och granskades rad för rad i 15 arkiverade urval.
Detta omfattar både verkstitlar, dynamiska namnmallar och dialog.

## Resultat

- 181 strängar behölls efter kontext- och språkgranskning.
- 5 strängar korrigerades: två hotfulla dialogrepliker, en boktitel med
  singular/plural-fel och två titlar med fel betydelse.
- Samtliga fem ändringar skickades i tre samlade Transifex API-anrop och
  återlästes individuellt med exakt matchning.

## Kontroller

Varje ändringsdelta kontrollerades med JSON, l10n-lint, svlang, Hunspell-sv,
taggparitet där taggar förekommer, `git diff --check` och Gitleaks. Hunspell
rapporterade endast förväntade dynamiska taggvariabler. `msgfmt` är inte
tillämpligt eftersom resursen hanteras som Transifex-strängar och JSON-delta.

## Status

Den befintliga svenska delen av `text_set` är lokalt granskad, arkiverad och
pushad till `yeager/translations`. De fem korrigeringarna är inskickade och
verifierade i Transifex. Projektgranskning och publicering i en utgåva är inte
verifierad. Oöversatta `text_set`-strängar återstår och hanteras som separat
kompletteringsarbete.
