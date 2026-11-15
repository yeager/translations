# Music Assistant Server – Party, Phishin och Plex, batch 78

Datum: 2026-11-15

Tio texter för Party-åtkomst, Phishin och Plex-autentisering.

Terminologi: *guest access* återges som *gäståtkomst*, *rate limiting* som
*hastighetsbegränsning*, *live audience recordings* som *liveinspelningar
gjorda av publiken* och *authenticate* som *autentisera*. Produktnamnen Plex,
MyPlex och Phish bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
