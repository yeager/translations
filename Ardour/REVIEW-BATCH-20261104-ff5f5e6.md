# Ardour – grupp-, navigerings- och spellisteåtgärder

| Fält | Uppgift |
| --- | --- |
| Datum | 2026-11-04 |
| Kandidatcommit | `ff5f5e6` |
| Komponent | `gtk2_ardour/po/sv.po` |
| Ändrade strängar | 5 |
| Upstream | Inte inskickad: Ardour PR #1150 är öppen och en parallell PR skulle skapa konflikt. |

## Rättningar

- `Gain` i en grupps kanalreglage är **förstärkning**, inte ekonomisk **vinst**.
- Den brutna genvägstexten i navigeringstidslinjen använder nu svenska uppmaningar och behåller samtliga tangentplatshållare.
- Det felaktiga `o` efter kanalnumret är borttaget ur polaritetsverktygstipset.
- `Clear Current` används i den aktuella spellistans meny och är därför **Töm aktuell spellista**, inte **Klar ström**.

## Verifiering

- `msgfmt --check --statistics`: godkänt, 4 039 översatta meddelanden.
- `l10n-lint`: endast den tidigare dokumenterade, avsiktliga avvikelsen i översättarkrediterna.
- Hunspell: körd för de berörda orden.
- `git diff --check`: godkänt.
- Gitleaks: inga hemligheter hittades.
