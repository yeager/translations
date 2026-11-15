# Music Assistant Server – FastMCP och leverantörer, batch 60

Datum: 2026-11-15

Tio strängar för FastMCP-servern och leverantörerna Fully Kiosk, Genius Lyrics
och gPodder. Texterna täcker bekräftelse av raderande åtgärder, TLS/HTTPS,
ljuduppspelning och externa autentiseringsflöden.

Terminologi: MCP, TLS, HTTPS, API och produktnamnen Fully Kiosk, Android,
Genius, gPodder, opodsync och Nextcloud bevaras. *Fingerprint* översätts som
*fingeravtryck* och *lyrics* som *låttexter*.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
