# Home Assistant Core – Tuya, batch 35

Datum: 2026-11-14

En svensk statusindikering för Tuya sparades direkt i Lokalise och återlästes:

- `component::tuya::entity::binary_sensor::overload::name`: **Överbelastning**

Källsträngen är ett kort statusnamn i Home Assistants enhetsgränssnitt. Den
svenska termen är etablerad inom elteknik. Inga platshållare, URL:er eller em
dash förekommer.

## Kontroller

- Sparat värde återläst i Lokalise.
- `msgfmt`, l10n-lint, svlang och hunspell-sv är inte tillämpliga på den här
  webbläsarbaserade redigeringen utan en lokal export.
- Diffkontroll och Gitleaks körs före arkivering.

## Upstreamstatus

Värdet är sparat i Lokalise. Lokalise-granskning, kodsynkronisering och release
är inte verifierade.
