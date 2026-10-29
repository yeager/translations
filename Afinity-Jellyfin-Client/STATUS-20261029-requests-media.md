# Afinity: begäranden och mediedetaljer

Datum: 2026-10-29

## Aktuell kontroll

- Officiell release `v0.12.05-beta` publicerades 2026-10-19 och uppfyller
  48-månaderskravet.
- Hosted Weblate visar 3 115 av 3 115 översatta strängar (100 procent).
  Arton produktnamn är skrivskyddade och ingår redan i den kompletta
  översättningen.

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

## Uppladdning och slutkontroll

- Två granskade deltahäften under 1 000 strängar laddades upp via Weblate med
  läget att endast ändra oöversatta strängar. Det första uppdaterade 20 av 20
  poster. Det andra uppdaterade 25 av 26; den återstående posten hade fått en
  ändrad källsträng och sparades manuellt som `%1$d kanaler`.
- Sökningen `has:check` är tom efter slutgranskningen.
- Fyra giltiga kontroller avfärdades utan att ändra måltexten: två svenska
  pluraler där `spår` respektive formuleringen med `ytterligare` korrekt har
  samma form, samt produktnamnen `Tomatometer` och `Popcornmeter`.
