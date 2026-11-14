# Voice Support, batch 28

Åtta värden i `component::voice_support` sparades direkt i Home Assistant Core-projektet på Lokalise och återlästes 2026-11-14.

| Nyckel | Svenska efter återläsning |
| --- | --- |
| `config::step::manual::data::port` | Port |
| `config::step::manual::data::host` | Värd |
| `config::flow_title` | `{name}` |
| `config::error::unsupported_version` | Voice-appen använder en protokollversion som den här Home Assistant-installationen inte stöder. Uppdatera appen eller Home Assistant. |
| `config::error::cannot_connect` | Det gick inte att ansluta |
| `config::abort::single_instance_allowed` | Redan konfigurerad. Endast en konfiguration är möjlig. |
| `config::abort::cannot_connect` | Det gick inte att ansluta |
| `config::abort::already_configured` | Tjänsten är redan konfigurerad |

Källorna använder i flera fall Lokalise-nyckelreferenser till etablerade gemensamma Home Assistant-värden. Referenserna sparades i stället för att duplicera deras synliga engelska text, och den svenska upplösningen återlästes i redigeraren. `{name}` är en avsiktligt bevarad platshållare.

Kontroll: värdena sparades i Lokalise och återlästes. `msgfmt`, l10n-lint, svlang och Hunspell är inte tillämpliga på denna direktredigerade, exportlösa JSON-batch. Arkivets diffkontroll och Gitleaks kördes före push.

Status: sparad i projektets etablerade upstreamkanal. Granskning, synkronisering och release är inte verifierade.
