# Warzone 2100 – svensk granskning: aktivt spelgränssnitt och order

**Datum:** 2026-11-13

**Komponent:** huvudspel, svensk PO-kandidat (`po/sv.po`)

## Omfattning

39 strängar har granskats rad för rad i bygg- och produktionspanelen, enhetsgrupper, underrättelsevyn och enhetsordrarna som används under spelets första uppdrag.

## Terminologibeslut

- *fire-at-will* blir **eld efter eget omdöme**.
- *fire support* blir **eldunderstöd**.
- *build progress* och *construction progress* skiljs åt som **byggförlopp** respektive **tillverkningsförlopp**.
- *recycle* blir **återvinn** i orderkontexten.

## Lokal kontroll

- `msgfmt --check --statistics --output-file=/dev/null po/sv.po`: godkänd, 1 848 översatta och 2 099 oöversatta meddelanden.
- `git diff --check`: godkänd.
- Gitleaks mot PO-filen: inga läckor.
- Kontroll av tre identiska konsonanter träffade endast engelska källsökvägar, inte svenska översättningar.

## Status

Deltafilen är arkiverad i `yeager/translations`. Den är endast lokalt granskad och inte uppladdad till Crowdin eller inskickad upstream.
