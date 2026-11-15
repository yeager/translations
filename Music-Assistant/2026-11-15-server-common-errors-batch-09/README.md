# Music Assistant Server – vanliga fel, batch 09

Datum: 2026-11-15

## Omfattning

20 svenska felmeddelanden från `common.errors` för åtgärder, registrering,
ljudbearbetning, autentisering, anslutning, behörighet och ogiltiga värden.
Texterna används i Music Assistants gränssnitt och i dess konfigurations- och
uppspelningsflöden.

## Terminologi och kontext

- `provider` återges som *leverantör*, enligt befintlig svensk katalog.
- *Autentisering*, *åtkomsttoken* och *URI* behålls som etablerade tekniska
  termer i den kontext där de visas.
- Platshållarna `{0}` har bevarats exakt från engelsk källa.

## Kontroller

- Nycklar, engelska källtexter och platshållare har jämförts mot aktuell
  `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: enda träffen är den avsiktliga tekniska formen `URI:n`.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen ska förenas med den verifierade deltainskickningen
när Lokalise-åtkomsten fungerar igen.
