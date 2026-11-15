# Music Assistant Server – Yandex Music, autentisering och kvalitet, batch 89

Datum: 2026-11-15

Tjugo texter för Yandex Musics enhets- och QR-inloggning, autentisering,
Wave-förval, virtuella spellistor och kvalitetsval.

Terminologi: *verification URL* återges som *verifierings-URL*, *device code*
som *enhetskod*, *preset* som *förval*, *audio quality* som *ljudkvalitet* och
*base URL* som *API-basadress*. Produktnamn och synliga spellistnamn bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
