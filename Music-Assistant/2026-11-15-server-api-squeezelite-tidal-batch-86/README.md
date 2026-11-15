# Music Assistant Server – Squeezelite, grupper, TheAudioDB och Tidal, batch 86

Datum: 2026-11-15

Tjugo texter för Squeezelite, Subsonic-historik, synkroniseringsgrupper,
TheAudioDB och Tidal-autentisering.

Terminologi: *visualization* återges som *visualisering*, *dynamic members*
som *dynamiska medlemmar*, *metadata* som *metadata* och *authentication*
som *autentisering*. PKCE, URL, token och produktnamn bevaras där de är
tekniska eller synliga namn.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
