# Music Assistant Server – ljudboksgenrer, batch 16

Datum: 2026-11-15

## Omfattning

Fem ljudboksgenrer med synliga namn och beskrivningar: drama och poesi,
fantasy och science fiction, skönlitteratur, främmande språk samt historia.

## Terminologi och kontext

- Texterna används vid bläddring bland ljudboksgenrer.
- *Skönlitteratur*, *språkinlärning* och *sceniska framträdanden* är valda
  utifrån svensk biblioteks- och kulturanvändning.
- Det etablerade genrenamnet *science fiction* behålls på svenska.

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
