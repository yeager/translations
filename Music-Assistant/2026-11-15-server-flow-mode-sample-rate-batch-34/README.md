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

En tidigare snabbkontroll var inte tillräcklig för att intyga radvis
verifiering. Fyra av tolv rader är rättade och sparade, och tre är verifierade
i Lokalise; fem återstår.
Arkivering och push sker efter varje ändring:
Lokalise-tokenen saknar rättigheten `Upload files`.
