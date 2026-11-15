# Music Assistant Server – vanliga fel, batch 11

Datum: 2026-11-15

## Omfattning

20 svenska felmeddelanden från `common.errors` för resursstatus, roller,
självregistrering, installation, inloggning och ägarskap för musikkällor.

## Terminologi och kontext

- *Musikkälla*, *roll*, *administratör* och *behörighet* följer den svenska
  terminologin i befintlig Music Assistant-katalog.
- Produktnamnet Music Assistant och Home Assistant behålls.
- Platshållaren `{0}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: träffarna är produktnamnen Music Assistant och Home
  Assistant.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
