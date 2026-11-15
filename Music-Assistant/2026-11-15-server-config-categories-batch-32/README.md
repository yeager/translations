# Music Assistant Server – konfigurationskategorier, batch 32

Datum: 2026-11-15

## Omfattning

17 svenska etiketter för kvarvarande kategorier i Music Assistants
konfigurationsgränssnitt.

## Terminologi och kontext

- *Övertoning*, *köning*, *intelligent slumpning* och *insticksmoduler*
  följer projektets svenska terminologilista.
- Platshållarna `{0}` och `{1}` har bevarats exakt.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: *autouppspelning* är en korrekt svensk sammansättning
  som saknas i den aktuella ordlistan.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad eller inskickad upstream:
Lokalise-tokenen saknar rättigheten `Upload files`.
