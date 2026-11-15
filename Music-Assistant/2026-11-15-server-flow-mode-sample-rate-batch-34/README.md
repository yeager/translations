# Music Assistant Server – köflödeslägets samplingsfrekvens, batch 34

Datum: 2026-11-15

## Omfattning

12 svenska texter för samplingsfrekvens i köflödesläge: alternativ, etiketter
och förklaringar av omprovtagning, bandbredd och sömlös uppspelning.

## Terminologi och kontext

- *Köflödesläge*, *samplingsfrekvens*, *sampla om*, *övertoning* och
  *sömlös uppspelning* följer projektets fastlagda terminologi.
- Kodenheterna 48 kHz och 96 kHz samt alternativet *Bitperfekt* är oförändrade
  där det krävs för begripligheten.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: *köflödesläge* är en projektfastlagd sammansättning som
  saknas i den aktuella ordlistan.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad eller inskickad upstream:
Lokalise-tokenen saknar rättigheten `Upload files`.
