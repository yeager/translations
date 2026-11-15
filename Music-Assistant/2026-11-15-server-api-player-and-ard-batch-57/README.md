# Music Assistant Server – spelarstyrning och ARD Audiothek, batch 57

Datum: 2026-11-15

Tio svenska konfigurationstexter som sparades via Lokalise API: spelarens
ljudavstängning och strömstyrning, en URL till en klocksignal före meddelanden,
och ARD Audiotheks ljudström- och kontoinställningar.

Terminologi: *native* återges som *inbyggd*, *power control* som
*strömstyrning*, och *pre-announcement chime* som *klocksignal före
meddelanden*. ARD och URL behålls som namn respektive teknisk förkortning.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för varje sträng.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
