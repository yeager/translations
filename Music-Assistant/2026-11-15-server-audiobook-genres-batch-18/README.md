# Music Assistant Server – ljudboksgenrer, batch 18

Datum: 2026-11-15

## Omfattning

De återstående sex ljudboksgenrerna med synliga namn och beskrivningar:
vetenskap, självhjälp, talare och berättare, sport, teknik samt resor och
äventyr.

## Terminologi och kontext

- Texterna används för kategorisering och bläddring bland ljudböcker.
- *Friluftsliv*, *reseskildring*, *självhjälp* och *personlig utveckling*
  följer etablerad svensk användning i biblioteks- och förlagskontext.

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
integrerad upstream. Tillsammans med batch 15–17 täcker den samtliga aktuella
nycklar för `common.media.audiobook_genre`.
