# Music Assistant Server – QQ Music, Roku och Snapcast, batch 82

Datum: 2026-11-15

Tjugo texter för QQ Music, Roku Media Assistant, Samsung WAM, SiriusXM och
Snapcast.

Terminologi: *automatic discovery* återges som *automatisk upptäckt*,
*priority order* som *prioriteringsordning*, *buffer size* som
*buffertstorlek*, *chunk size* som *segmentstorlek* och *control port* som
*styrport*. Produkt-, format- och tekniska ID-namn bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
