# Music Assistant Server – Pandora och Party, batch 76

Datum: 2026-11-15

Tio texter för Pandora-ljudkvalitet, proxy, uppspelningsövertagande och
kontouppgifter samt två Party-inställningar.

Terminologi: *stream* återges som *ström*, *rate limiting* som
*hastighetsbegränsning* och *duplicate tracks* som *dubblettspår*. SOCKS,
formatnamnen och exemplen `ip_address:port` respektive `socks5://` bevaras som
tekniska värden. Radbrytningar och HTML-kodtaggar är bevarade i proxytexten.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
