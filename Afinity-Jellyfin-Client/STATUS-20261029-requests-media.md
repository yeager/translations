# Afinity: begäranden och mediedetaljer

Datum: 2026-10-29

## Aktuell kontroll

- Officiell release `v0.12.05-beta` publicerades 2026-10-19 och uppfyller
  48-månaderskravet.
- Hosted Weblate visade 3 069 av 3 115 översatta strängar och 46 tomma,
  skrivbara poster. Arton produktnamn var skrivskyddade.
- Två deltakataloger med 20 respektive 26 strängar har skapats för de 46
  skrivbara, tomma posterna.

## Granskning

- `msgfmt --check --check-format`: godkänd; endast förväntade varningar om
  avsiktligt minimalistiskt deltahuvud.
- `l10n-lint`: inga fel eller varningar; två informationsposter om
  avsnittsbeteckningar som innehåller bokstaven `S`.
- `svlang skrivregler`: inga fel.
- `svlang check`: 10,0 av 10 i naturlighet. Tekniska platshållare och
  produktnamn markeras endast som ovanliga ord.
- Direktextraherade svenska måltexter gav bara varumärket `Tomatometer` i
  Hunspell efter att PO-huvud och formatplatshållare uteslutits; det är en
  avsiktligt oförändrad produktbeteckning.
- Terminologiminnet bekräftar bland annat `spellista`, `speltid`, `poäng` och
  `recension` i etablerad användning.

## Uppladdning

Filerna är under 1 000 strängar och kan laddas upp var för sig när aktuell
Weblate-måltext har jämförts igen. Likadana käll- och måltexter för tekniska
beteckningar (till exempel `S01E01` och `%1$.1f%%`) ska sparas individuellt
om Weblate avvisar dem vid filimport.
