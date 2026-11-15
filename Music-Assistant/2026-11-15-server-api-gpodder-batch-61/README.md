# Music Assistant Server – gPodder, batch 61

Datum: 2026-11-15

Tio svenska inställningstexter för synkronisering med gPodder-kompatibla
tjänster och Nextclouds gPodder Sync.

Terminologi: *feed* återges som *flöde*, *episode* som *avsnitt* och
*instance* som *instans*. Produkt- och formatnamnen gPodder, Nextcloud, URL
och token bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
