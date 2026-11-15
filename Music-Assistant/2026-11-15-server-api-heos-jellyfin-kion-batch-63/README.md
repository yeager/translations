# Music Assistant Server – HEOS, Jellyfin och KION Music, batch 63

Datum: 2026-11-15

Tio svenska konfigurationstexter för HEOS-spelare, Jellyfin-servrar och KION
Musics API-autentisering.

Terminologi: *remote server* återges som *fjärrserver*, *stream* som
*strömma*, *credentials* som *autentiseringsuppgifter* och *base URL* som
*API-bas-URL*. Produkt- och protokollnamn bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
