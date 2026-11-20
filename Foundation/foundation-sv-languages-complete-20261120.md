# Foundation svenska — languages.json slutförd

Datum: 2026-11-20  
Projekt: Crowdin Foundation (306855), språk `sv-SE`  
Komponent: `languages.json` (fil-ID 34)

Alla 11 aktuella strängar radgranskades via Crowdin API. Slutkontroll med `GET /strings?fileId=34&limit=20&offset=20` returnerade 0 strängar.

Språkbenämningar rättades från adjektiv till svenska språknamn. Sex ändringar sparades (HTTP 201) och tre förslag fanns redan i Crowdin som identiska dubbletter (HTTP 400). Fullständig logg: `foundation-sv-languages-part1-20261120.md`.

Samtliga förslag passerade `l10n-lint --language sv` och `hunspell -d sv_SE` utan anmärkningar.
