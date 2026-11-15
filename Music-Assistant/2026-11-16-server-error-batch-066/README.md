# Music Assistant Server – kontobyte och tjänstfel, batch 66

Datum: 2026-11-16

Två nya svenska servertexter för ett konto som inte stämmer med den tidigare
leverantörskonfigurationen och för ett tjänstfel. Platshållaren `{0}` i
tjänstfelet är bevarad exakt.

Terminologi: *provider* återges som *leverantör*, i linje med den synliga
inställningskontexten. Texterna använder direkt tilltal och beskriver nästa
åtgärd utan onödigt fackspråk.

Status: båda posterna uppdaterades via Lokalise API och lästes tillbaka med
samma översättnings-ID:n. API:t bekräftar `is_untranslated: 0` och
`is_fuzzy: false` för båda. En full ny genomräkning av Music Assistant Servers
4 098 svenska poster gav 0 tomma och 0 oöversatta värden. Arkivposten är
pushad till vårt arkiv; detta är inte ett upstream-godkännande eller en
release.

Kontroller: JSON, källnycklar, platshållare, l10n-lint, svlang, Hunspell,
kontroll av tre identiska tecken i följd, diffkontroll och Gitleaks. `msgfmt`
är inte tillämpligt på JSON-kataloger.
