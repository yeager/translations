# Music Assistant Server – KION Music och Last.fm, batch 65

Datum: 2026-11-15

Tio inställningstexter för KION Musics ljudströmning och Last.fm:s
rekommendationer och scrobbling.

Terminologi: *transport* återges som *transportläge*, *fallback* som
*reservläge*, *lossless* som *förlustfri* och *endpoint* som *slutpunkt*.
Koderna `raw`, `encraw`, AES-CTR, FLAC och produktnamnen bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
