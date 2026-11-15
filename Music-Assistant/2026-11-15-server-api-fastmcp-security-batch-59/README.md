# Music Assistant Server – FastMCP-säkerhet, batch 59

Datum: 2026-11-15

Tio synliga säkerhets- och anslutningsinställningar för FastMCP-servern:
tokenmålgrupp, tillåtna Origin-värden, MCP-serverns monteringssökväg,
anslutningsguiden, autentisering och bekräftelse av åtgärder som kan radera
data.

Terminologi: MCP, RFC 8707, Origin, CSV, HTTP, OAuth-relaterade fält,
`base_url`, `publish_ip`, JWT- och klientnamn lämnas oförändrade. *DNS
rebinding* återges som *DNS-återbindning* och *reverse proxy* som *omvänd
proxy*.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
