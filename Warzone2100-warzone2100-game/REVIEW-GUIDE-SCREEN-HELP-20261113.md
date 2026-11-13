# Warzone 2100 – svensk granskning: handledningens guidevyer

**Datum:** 2026-11-13

**Komponent:** huvudspel, svensk PO-kandidat (`po/sv.po`)

## Omfattning

11 strängar i spelguidens rubriker, interaktionshjälp och tangentbindningsreferenser har granskats rad för rad. Själva handledningens steg och kampanjens inledning var redan översatta i tidigare arkiverade batcher.

## Terminologibeslut

- *game guide* blir **spelguide**.
- *sidebar* blir **sidopanel**.
- *keymapping* blir **tangentbindning**.

## Lokal kontroll

- `msgfmt --check --statistics --output-file=/dev/null po/sv.po`: godkänd, 1 809 översatta och 2 138 oöversatta meddelanden.
- `git diff --check`: godkänd.
- Gitleaks mot PO-filen: inga läckor.
- Kontroll av tre identiska konsonanter träffade endast engelska källsökvägar, inte svenska översättningar.

## Status

Deltafilen är arkiverad i `yeager/translations`. Den är endast lokalt granskad och inte uppladdad till Crowdin eller inskickad upstream.
