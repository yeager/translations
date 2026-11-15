# Music Assistant Server – AI och meddelandevolym, batch 33

Datum: 2026-11-15

## Omfattning

11 svenska texter för AI-motorns konfiguration, inloggning med webbkakor,
meddelandevolym och övertoning mellan olika samplingsfrekvenser.

## Terminologi och kontext

- *AI-motor*, *insticksmodul*, *webbkakor*, *övertoning* och
  *samplingsfrekvens* är konsekventa med projektets terminologilista.
- Produktnamnet Home Assistant och domännamnet `passport.yandex.ru` bevaras.
- Det administrativa tilltalet är direkt och tydligt; inga inloggningsuppgifter
  eller värden har lagts till.

## Kontroller

- Källtext, nycklar och radbrytningar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är Home Assistant och
  `passport.yandex.ru`.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Samtliga elva strängar verifierades i Lokalise 2026-11-15. De fanns redan som
svenska upstream-översättningar och lämnades orörda. Arkivering och push pågår:
Lokalise-tokenen saknar rättigheten `Upload files`.
