# Music Assistant Server – NeteaseCloudMusic, batch 70

Datum: 2026-11-15

Tio inställningstexter för NeteaseCloudMusicApi: anslutning, QR-inloggning,
autentisering och val av ljudkvalitet.

Terminologi: *API base URL* återges som *API-basadress*, *authentication* som
*autentisering* och *preferred quality* som *föredragen kvalitet*. QR, URL och
produktnamnen NeteaseCloudMusicApi, Exhigh, Hi-Res och JY Effect bevaras som
tekniska eller synliga namn.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
