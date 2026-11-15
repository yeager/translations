# Music Assistant Server – Plex-betyg och Plex Connect, batch 80

Datum: 2026-11-15

Tjugo Plex-strängar för betyg och favoriter samt Plex Connects enhetstyp och
spelarpresentation.

Terminologi: *rating* återges som *betyg*, *favorite* som *favorit*, *like*
som *gilla*, *device class* som *enhetsklass* och *remote client* som
*fjärrklient*. Plex, MA, PC, SSL och enhetstyper bevaras eller översätts enligt
synlig UI-kontext.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
