# Music Assistant Server – lokal ljuduppspelning och låttexter, batch 66

Datum: 2026-11-15

Tio strängar för Last.fm, lokal ljuduppspelning, ljudstyrkeanalys och
LRCLib-låttexter.

Terminologi: *hardware* och *software* återges som *maskinvara* respektive
*programvara*, *volume scaling* som *volymskalning*, *loudness* som
*ljudstyrka* och *lyrics* som *låttexter*. Kod- och formatnamnen ALSA, PCM,
EBU R128, REPLAYGAIN_TRACK_GAIN och LRCLib bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
