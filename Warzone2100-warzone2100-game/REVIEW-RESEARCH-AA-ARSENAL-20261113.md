# Warzone 2100 – svensk granskning: luftvärn och vapenforskning

Datum: 2026-11-13

## Omfattning

97 forskningsnamn och forskningsmeddelanden för luftvärn, vapen och avancerade system. Källhänvisningarna går till respektive vapendefinition, forskningsobjekt eller spelskript.

## Terminologibeslut

- *AA* och *flak* → **luftvärn** och **luftvärnsflak**.
- *emplacement* → **ställning**, *hardpoint* → **värn**.
- *missile* → **robot**, medan *rocket* → **raket** i vapenklassificeringen.
- APDSB, APFSDS, HE och HEAP behålls som ammunitionsbeteckningar.
- Produktnamn som Angel, Archangel, Cyclone, Tornado, Stormbringer, Ripple, Scourge, Tank Killer och Flashlight behålls.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 1 116 översatta och 2 831 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.
- l10n-lint, svlang och hunspell-sv finns lokalt; den fullständiga semantiska körningen av l10n-lint redovisas separat eftersom katalogen fortfarande är ofullständig.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
