# Music Assistant Server – Plex-bibliotek och lokala servrar, batch 79

Datum: 2026-11-15

Tjugo Plex-strängar för MyPlex-autentisering, samlingar, GDM-upptäckt,
musikbibliotek och lokal anslutning.

Terminologi: *collection* återges som *samling*, *hub* som *nav*, *library*
som *bibliotek*, *discover* som *hitta* och *verify certificate* som
*verifiera certifikat*. GDM, IP, SSL och HTTPS bevaras som tekniska namn.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
