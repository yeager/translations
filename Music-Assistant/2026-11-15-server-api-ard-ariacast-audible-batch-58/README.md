# Music Assistant Server – ARD Audiothek, AriaCast och Audible, batch 58

Datum: 2026-11-15

Tio svenska konfigurationstexter som sparades via Lokalise API. Batchen
omfattar interna ARD Audiothek-identifierare, val av AriaCast-spelare och
Audibles autentiseringsflöde.

Terminologi: ARD:s synliga interna fältnamn `token`, `token_expiry` och `uid`
behålls oförändrade. Produkt- och protokollnamnen ARD, AriaCast, Audible,
Music Assistant och WebSocket behålls. *Authentication* återges som
*autentisering*.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
