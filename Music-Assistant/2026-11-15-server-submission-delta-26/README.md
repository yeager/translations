# Music Assistant Server – svensk inskickningsdelta 26

Datum: 2026-11-15

## Omfattning

- 369 unika, lokalt godkända svenska strängar för Music Assistant Server.
- Deltan samlar de tidigare väntande 85 strängarna samt de godkända batcherna
  för vanliga fel, spelaralternativ, ljudboksgenrer, mediemappar, lagring,
  webbserver, musikkärna och ljudströmmar.
- Filen är avsedd för en enda JSON-import i Lokalise och ersätter inte någon
  hel katalog.

## Konfliktlösning

Tre överlappande äldre spelarvärden normaliserades enligt den senare
radgranskningen: `common.player_options.mono_mode.name`,
`common.player_options.speech_enhancement.name` och
`common.player_options.surround_mode.name`. Inga motstridiga värden återstår i
`sv_SE.delta.json`.

## Kontroller

- 369 måltexter; inga tomma värden.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: träffarna är granskade produktnamn, format, protokoll,
  förkortningar, kodvärden och facktermer.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Arkiverad och pushad till vårt arkiv. Inte uppladdad, inskickad, granskad eller
integrerad upstream. API-token saknas i de avsedda Nyckelring-posterna, och
den sparade Lokalise-sessionen kan inte öppna redigeraren via automatiseringen
på grund av en CDP-timeout. Importresultat kan därför inte verifieras ännu.
