# Music Assistant Server – spelaralternativ, batch 14

Datum: 2026-11-15

## Omfattning

26 svenska namn på återstående spelaralternativ: lägen, högtalare,
statusbelysning, subwoofer, surround, tonkontroll och pekstyrning.

## Terminologi och kontext

- Detta är korta synliga etiketter i spelarinställningarna.
- Loudness, Pure Direct och Trueplay behålls som etablerade synliga
  ljudfunktionsnamn.
- *Surround*, *subwoofer* och *equalizer* används som etablerade svenska
  ljudtermer i detta gränssnitt.

## Kontroller

- Nycklar och källtexter kontrollerade mot aktuell `en.json` och
  `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är avsiktliga produktnamn,
  förkortningar och etablerade ljudtermer.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Tillsammans med batch 13 täcker den hela komponenten
`common.player_options` i den aktuella engelska katalogen.
