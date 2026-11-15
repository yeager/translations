# Music Assistant Server – MusicCast och MusicMe, batch 69

Datum: 2026-11-15

Tio inställningstexter för Yamaha MusicCast-grupper, MusicMe-konton och en
lokal NeteaseCloudMusicApi-kompatibel tjänst.

Terminologi: *zone* återges som *zon*, *source* som *källa*, *input* som
*ingång*, *multiroom playback* som *flerrumsuppspelning* och *base URL* som
*bas-URL*. Produkt- och API-namn bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
