# Music Assistant Server – Yandex Smart Home och OAuth, batch 92

Datum: 2026-11-15

Tjugo texter för Yandex Smart Home: exponerade spelare, engångskoder,
instansnamn och manuell OAuth-konfiguration.

Terminologi: *one-time password* återges som *engångslösenord*, *instance
name* som *instansnamn*, *authorization URL* som *auktoriserings-URL* och
*client secret* som *klienthemlighet*. Namn på externa fält och tekniska
identifierare bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
