# Warzone 2100 – svensk granskning: snabbchattens kärnfraser

**Datum:** 2026-11-13

**Komponent:** huvudspel, svensk PO-kandidat (`po/sv.po`)

## Omfattning

56 strängar har granskats rad för rad i snabbchattens mottagarval, kategorier, samordningsförslag, färdigstatus och vanliga spelarmedddelanden.

## Terminologibeslut

- *quick chat* blir **snabbchatt**.
- *ready* blir **klar** i väntrummet.
- *host* blir **värd**.
- *lobby* behålls som **lobby**, eftersom det är ett etablerat synligt UI-namn.

## Lokal kontroll

- `msgfmt --check --statistics --output-file=/dev/null po/sv.po`: godkänd, 1 904 översatta och 2 043 oöversatta meddelanden.
- `git diff --check`: godkänd.
- Gitleaks mot PO-filen: inga läckor.
- Kontroll av tre identiska konsonanter träffade endast engelska källsökvägar, inte svenska översättningar.

## Status

Deltafilen är arkiverad i `yeager/translations`. Den är endast lokalt granskad och inte uppladdad till Crowdin eller inskickad upstream.
