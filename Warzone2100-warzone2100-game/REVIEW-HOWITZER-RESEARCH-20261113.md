# Warzone 2100 – svensk granskning: haubitsar och förfinad vapenforskning

**Datum:** 2026-11-13

**Komponent:** huvudspel, svensk PO-kandidat (`po/sv.po`)

## Omfattning

50 nya strängar har granskats rad för rad i sin statistik- och forskningskontext. Batchen omfattar haubitsar, brandhaubitsar, hyperhastighetskanoner, ammunition, materialuppgraderingar och sensorteknik.

## Terminologibeslut

- *howitzer* översätts konsekvent med **haubits**.
- *incendiary howitzer* översätts med **brandhaubits**.
- *hyper velocity cannon* översätts med **hyperhastighetskanon**.
- Produktnamn och synliga förkortningar, exempelvis Hurricane, Python, HVC, HVAPFSDS, Hardcrete och NEXUS, behålls där de fungerar som spelets egna namn.
- *rocket wire guidance* översätts med **trådstyrning för robotar**.

## Lokal kontroll

- `msgfmt --check --statistics --output-file=/dev/null po/sv.po`: godkänd, 1 708 översatta och 2 239 oöversatta meddelanden.
- `git diff --check`: godkänd.
- Gitleaks mot PO-filen: inga läckor.
- Kontroll av tre identiska konsonanter träffade endast engelska källsökvägar, inte svenska översättningar.

## Status

Deltafilen är arkiverad i `yeager/translations`. Den är endast lokalt granskad och inte uppladdad till Crowdin eller inskickad upstream.
