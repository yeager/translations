# Music Assistant Server – Sonic, SoundCloud och Squeezelite, batch 85

Datum: 2026-11-15

Tjugo texter för Sonic Similarity, SoundCloud och Squeezelite.

Terminologi: *similar tracks* återges som *liknande spår*, *preset* som
*förval*, *authorization* som *auktorisering*, *discovery* som *upptäckt* och
*display support* som *bildskärmsstöd*. Produkt- och protokollnamn bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
