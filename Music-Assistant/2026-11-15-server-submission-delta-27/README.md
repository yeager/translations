# Music Assistant Server – svensk inskickningsdelta 27

Datum: 2026-11-15

## Omfattning

- 394 unika, lokalt godkända svenska strängar för Music Assistant Server.
- Ersätter inskickningsdelta 26 genom att även inkludera den färdiggranskade
  ljudströmsbatchen 25.
- Filen är avsedd för en enda JSON-import i Lokalise och ersätter inte någon
  hel katalog.

## Kontroller

- 394 måltexter; inga tomma värden.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska är kontrollerad i de ingående batcherna; återstående
  träffar är dokumenterade produktnamn, format, protokoll, kodvärden och
  facktermer.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Arkiverad och pushad till vårt arkiv. Inte uppladdad, inskickad, granskad eller
integrerad upstream. API-token saknas i de avsedda Nyckelring-posterna, och
den sparade Lokalise-sessionen kan inte öppna redigeraren via automatiseringen
på grund av en CDP-timeout. Importresultat kan därför inte verifieras ännu.
