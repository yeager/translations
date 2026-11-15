# Music Assistant Server – svensk inskickningsdelta 31

Datum: 2026-11-15

## Omfattning

- 434 unika, lokalt granskade svenska strängar för Music Assistant Server.
- Ersätter delta 29 genom att även inkludera den färdiggranskade
  Audiobookshelf-konfigurationen.
- Avsedd för en enda JSON-import i Lokalise och ersätter inte en hel katalog.

## Kontroller

- 434 måltexter; inga tomma värden.
- `l10n-lint --language sv`, `svlang`, JSON- och diffkontroll: godkända.
- Hunspell-svenska: granskad i de ingående batcherna; kvarvarande träffar är
  produktnamn, format, protokoll, kodvärden och etablerade facktermer.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom formatet är JSON.

## Status

Arkiverad lokalt. Uppladdning, importresultat, granskning och integrering
upstream ska verifieras separat.
