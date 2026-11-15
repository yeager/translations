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

Arkiverad och pushad till `yeager/translations`.

Uppladdning har förberetts men kan inte utföras från den aktuella
Lokalise-behörigheten. API-tokenen kan läsa projektet, men både API-importen
och projektinställningarnas importvy svarar med HTTP 403. Tokenen saknar
rättigheten `Upload files`.

Ingen fil har därför laddats upp och inget importresultat, ingen
upstream-granskning eller integrering har verifierats.

## Manuell upstream-status

2026-11-15 sparades sex tidigare tomma, lokalt granskade strängar manuellt i
Lokalise-redigeraren: två etiketter och en beskrivning för inloggning med
enhetskod samt två etiketter och en beskrivning för QR-kodinloggning. Varje
sparning lästes tillbaka i redigeraren.
En kontrollsträng i samma delta fanns redan upstream med matchande svensk text.
Två andra kontroller hade redan svenska upstreamöversättningar med annan
formulering och lämnades därför orörda. Detta är inte en filimport; återstående
deltasträngar är inte inskickade eller verifierade.
