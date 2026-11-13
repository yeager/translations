# Warzone 2100 – svensk granskning: huvudmeny och spelstart

**Datum:** 2026-11-13

**Komponent:** huvudspel, svensk PO-kandidat (`po/sv.po`)

## Omfattning

90 strängar har granskats rad för rad i huvudmenyn, enspelar- och flerspelarvägarna, kampanjstarten, pausmenyn, spara/ladda-flödena och de tidiga inställningsmeddelandena.

## Terminologibeslut

- *single player* och *multiplayer* blir **enspelarläge** respektive **flerspelarläge**.
- *skirmish* blir **skärmytsling**.
- *display scale* blir **visningsskala**.
- *replay* blir **repris**.
- *Original Campaign* blir **Ursprunglig kampanj**.

## Lokal kontroll

- `msgfmt --check --statistics --output-file=/dev/null po/sv.po`: godkänd, 1 798 översatta och 2 149 oöversatta meddelanden.
- `git diff --check`: godkänd.
- Gitleaks mot PO-filen: inga läckor.
- Kontroll av tre identiska konsonanter träffade endast engelska källsökvägar, inte svenska översättningar.

## Status

Deltafilen är arkiverad i `yeager/translations`. Den är endast lokalt granskad och inte uppladdad till Crowdin eller inskickad upstream.
