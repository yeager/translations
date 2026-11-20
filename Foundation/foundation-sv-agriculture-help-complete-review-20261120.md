# Foundation – slutförd svensk granskning: dlc_agriculture_help.json

Datum: 2026-11-20  
Omfattning: 152 av 152 aktuella strängar radgranskade via Crowdin API (offset 0–150; offset 160 verifierat tomt).

## Resultat

- 41 språk-, terminologi- och formateringsförbättringar sparades i Crowdin med API-svar 201.
- Terminologi normaliserades för **skördefestival**, **festivalområde**, **festivalens attraktivitet**, **ståndsinbjudningar**, **Gemensam gård**, **delbyggnader** och **festunderhållare**.
- Markdown, platshållare och radbrytningar bevarades eller återställdes.

## Spårbarhet

Samtliga ändringar med källsträng, tidigare svensk text, förslag och valideringsresultat finns i:

- `foundation-sv-agriculture-help-part1-20261120.md` till `foundation-sv-agriculture-help-part14-20261120.md`.

## Validering

- `l10n-lint --language sv`: utan fel eller varningar för varje förslagsbatch.
- `hunspell -d sv_SE`: inga stavningsanmärkningar för förslagen.
- Två batcher gav endast informationsanmärkningar från lint om svensk ordföljd med inledande fetstil.
