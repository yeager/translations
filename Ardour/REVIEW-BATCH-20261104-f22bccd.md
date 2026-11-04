# Ardour – export- och insticksmodulsterminologi

| Fält | Uppgift |
| --- | --- |
| Datum | 2026-11-04 |
| Kandidatcommit | `f22bccd` |
| Komponent | `gtk2_ardour/po/sv.po` |
| Ändrade strängar | 17 |
| Upstream | Inte inskickad: Ardour PR #1150 är öppen och en parallell PR skulle skapa konflikt. |

## Terminologiska beslut

- `plugin` är konsekvent **insticksmodul** i dialogtitlar, hjälptexter, fel och parameterdialoger.
- `range` i Ardours redigeringsläge är **intervall**, vilket följer den redan etablerade termen **intervallverktyg**.
- `Grab Mode` följer den befintliga UI-beteckningen **Flyttläge**.
- `tail` för reverb- och processorljud är **svans** i den förklarande hjälptexten.

## Språkrättningar

- Sju export- och importstatusar använder nu svenska **av** i stället för engelska `of`.
- `Encoding` beskriver en åtgärd och är **Kodning av**.
- SoundCloud-statusen är rättad från `bbyte` till **byte** och korrekt svensk räkneordsfras.

## Verifiering

- `msgfmt --check --statistics`: godkänt, 4 039 översatta meddelanden.
- `l10n-lint`: endast den tidigare dokumenterade, avsiktliga avvikelsen i översättarkrediterna.
- Hunspell: sammansättningar som `flerkanalsinsticksmodul` och `separeringsåtgärd` är korrekta facktermer trots att grundordlistan saknar dem.
- `git diff --check`: godkänt.
- Gitleaks: inga hemligheter hittades.
