# Foundation – slutförd svensk granskning: village_event.json

Datum: 2026-11-20  
Omfattning: 31 av 31 aktuella strängar radgranskade via Crowdin API (offset 0–30; offset 40 verifierat tomt).

## Sparade ändringar

| Sträng-ID | Föreslagen svenska |
|---|---|
| 26052 | Skördefestivalboden måste byggas och alla resurser som krävs för att bygga {1} måste placeras i den. |
| 26060 | {1} ståndsinbjudning(ar) intjänade |
| 26096 | Möt {1} |

Samtliga ändringar är sparade i Crowdin med API-svar 201 och dokumenterade i delrapporterna 1–3.

## Validering

- `l10n-lint --language sv`: utan problem för varje förslagsbatch.
- `hunspell -d sv_SE`: inga stavningsanmärkningar för förslagen.
- Platshållaren `{1}` har bevarats i samtliga berörda strängar.
