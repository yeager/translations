# Music Assistant Server – ljudboksgenrer, batch 15

Datum: 2026-11-15

## Omfattning

De första fem ljudboksgenrerna med sina synliga namn och beskrivningar:
konst och underhållning, biografier, näringsliv, klassiker samt humor.

## Terminologi och kontext

- Texterna är beskrivningar för bläddring i ljudboksgenrer, inte metadata för
  en enskild bok.
- *Ljudbok*, *memoar*, *scenkonst* och *bildkonst* används i sin etablerade
  svenska betydelse.
- Genrerna är översatta idiomatiskt; källans `&` återges som *och*.

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
