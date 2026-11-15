# Music Assistant Server – ljudboksgenrer, batch 17

Datum: 2026-11-15

## Omfattning

Fem ljudboksgenrer med synliga namn och beskrivningar: barn och unga vuxna,
mystik, facklitteratur, religion och andlighet samt romantik.

## Terminologi och kontext

- Texterna används för kategorisering och bläddring bland ljudböcker.
- *Facklitteratur*, *pusseldeckare* och *ungdomsroman* följer etablerad svensk
  biblioteks- och förlagsanvändning.
- Den engelska marknadsföringstonen i `steamy reads` uttrycks neutralt som
  *berättelser med erotiska inslag*.

## Kontroller

- Nycklar och källtexter kontrollerade mot aktuell `en.json` och
  `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: inga kvarvarande träffar.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
