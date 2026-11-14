# Home Assistant Core – Tuya, batch 32

Datum: 2026-11-14

Två svenska felindikeringar för Tuya sparades direkt i Lokalise och återlästes:

- `component::tuya::entity::binary_sensor::undervoltage::name`: **Underspänning**
- `component::tuya::entity::binary_sensor::power_outage::name`: **Strömavbrott**

Källsträngarna är korta sensornamn i Home Assistants enhetsgränssnitt. Termerna följer etablerad svensk elektroterminologi. Inga platshållare, URL:er eller em dash förekommer.

## Kontroller

- Sparade värden återlästa i Lokalise.
- Den misslyckade försöksredigeringen av en annan sträng med en osynlig riktmärkesmarkör avbröts och sparades inte.
- `msgfmt`, l10n-lint, svlang och hunspell-sv är inte tillämpliga på den här webbläsarbaserade redigeringen utan en lokal export.
- Diffkontroll och Gitleaks körs före arkivering.

## Upstreamstatus

Båda värdena är sparade i Lokalise. Lokalise-granskning, kodsynkronisering och release är inte verifierade.
