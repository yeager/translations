# Music Assistant Server – ORF Radiothek och Pandora, batch 75

Datum: 2026-11-15

Tio konfigurations- och beskrivningstexter för ORF Radiothek och Pandora.

Terminologi: *protocol* återges som *protokoll*, *quality* som *kvalitet*,
*on-demand* som *på begäran* och *live stream* som *direktsändning*.
Tekniska nycklar och formatvärden, inklusive `hideFromStations`, `bundle.json`,
HLS, Shoutcast och q-värden, bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
