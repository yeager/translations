# Ardour – tidskod, I/O och omprovtagning

| Fält | Uppgift |
| --- | --- |
| Datum | 2026-11-04 |
| Kandidatcommit | `fd8a6e5` |
| Komponent | `libs/ardour/po/sv.po` |
| Ändrade strängar | 4 |
| Upstream | Inte inskickad: Ardour PR #1150 är öppen och en parallell PR skulle skapa konflikt. |

## Terminologiska beslut

- `rate/drop` i en inkommande MTC-ström avser MTC:s bildfrekvens och drop-frame-flagga, därför **bildfrekvens-/drop-frame-värde**.
- Den efterfrågade monitoranslutningen hämtas från `get_monitor_bus_preferred_bundle()`. `I/O` avser alltså en namngiven **I/O-bunt**, inte en abstrakt I/O-operation.
- `in/%2 out configuration` beskriver kanalantal och blir **%1 ingångar/%2 utgångar**.
- `resampling` är **omprovtagning**. Frekvensen skrivs med mellanrum före `kHz` enligt svensk typografi.

## Verifiering

- `msgfmt --check --statistics`: godkänt, 854 översatta meddelanden.
- `l10n-lint`: 0 fel.
- Hunspell: ordlistan saknar de sammansatta facktermerna `drop-frame-värde` och `omprovtagning`; de har godkänts efter kontextkontroll.
- `git diff --check`: godkänt.
- Gitleaks: inga hemligheter hittades.
