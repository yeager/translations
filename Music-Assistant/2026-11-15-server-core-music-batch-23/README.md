# Music Assistant Server – musikkärna, batch 23

Datum: 2026-11-15

## Omfattning

24 svenska texter för bakgrundsjobb, import, synkronisering, dubblettspår,
databasåterställning, remastrade versioner samt musikkomponentens namn.

## Terminologi och kontext

- *Album*, *artist*, *ljudbok*, *poddsändning*, *radiostation*, *spår* och
  *spellista* följer befintlig svensk Music Assistant-terminologi.
- `Remastered 2009` bevaras som ett exempel på synlig medietitel.
- Platshållaren `{0}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träffar är det avsiktligt bevarade
  titelordet `Remastered` och termen *remaster*.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen täcker samtliga aktuella nycklar för `core.music`.
