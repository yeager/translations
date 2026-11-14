# Home Assistant Core, Lokalise, svenska: Voice-batch 2

Datum: 2026-11-14

Fem sammanhängande strängar för den nya röstfunktionen har granskats i sin
Lokalise-kontext, sparats direkt upstream och återlästs i redigeraren:

- `component::voice_support::preview_features::next_generation_voice::disable_confirmation`
  - Nästa generations röst stängs av. Om Home Assistant installerade Voice-appen säkerhetskopieras och avinstalleras den, och integrationsposten tas bort.
- `component::voice_support::preview_features::next_generation_voice::description`
  - Aktiverar nästa generations röstsystem i Home Assistant. På system med Home Assistant OS eller Supervised installeras appen när funktionen aktiveras.
- `component::voice_support::issues::app_setup_failed::title`
  - Det gick inte att konfigurera Voice-appen
- `component::voice_support::config::step::start_app::title`
  - Startar appen
- `component::voice_support::config::step::on_supervisor::title`
  - Välj anslutningsmetod

Kontroller: diffkontroll och Gitleaks för arkivändringen. `msgfmt`,
`l10n-lint`, `svlang` och Hunspell-sv är inte tillämpliga på direkt sparade
Lokalise-strängar utan en exporterad resursfil. Home Assistant Core 2026.11.1
släpptes 2026-11-09 och uppfyller därmed aktualitetskravet.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad
batch, inte en fullständig genomgång av projektet.
