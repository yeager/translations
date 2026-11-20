# Foundation – slutförd svensk granskning: dlc_agriculture_general.json

Datum: 2026-11-20  
Omfattning: 423 av 423 aktuella strängar radgranskade via Crowdin API (offset 0–420; offset 430 verifierat tomt).

## Resultat

- 73 språk-, terminologi- och kompletthetsförbättringar sparades i Crowdin med API-svar 201.
- Alla oöversatta strängar som identifierades under granskningen fylldes i.
- Terminologi normaliserades bland annat för **skördefestival**, **festivalområde**, **festivalens attraktivitet** och **byäldstarna**.
- Dynamiska platshållare, markdown och radbrytningar bevarades.

## Spårbarhet

Samtliga ändringar med engelsk källa, tidigare svensk text, föreslagen svensk text och valideringsresultat finns i:

- `foundation-sv-agriculture-general-part1-20261120.md` till `foundation-sv-agriculture-general-part21-20261120.md`.

## Validering

- `l10n-lint --language sv`: utan fel eller varningar för varje förslagsbatch.
- `hunspell -d sv_SE`: inga stavningsanmärkningar för förslagen.
- En batch med platshållarledd svensk ordföljd gav endast tre informationsanmärkningar från lint; inga fel eller varningar.
