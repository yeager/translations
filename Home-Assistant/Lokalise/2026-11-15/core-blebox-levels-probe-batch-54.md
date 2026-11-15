# Home Assistant Core – Blebox nivåer och givare, svenska

Datum: 2026-11-15

Sex Blebox-entiteter och feltexter har granskats i sammanhanget för nivå- och
givarsensorer, sparats via Lokalise API och återlästs via API.

| Källa | Svenska |
| --- | --- |
| Fill level | Fyllnadsnivå |
| Gauge pressure | Manometertryck |
| Liquid height | Vätskenivå |
| Volume | Volym |
| `{device_name}: {sensor_name} probe not configured` | `{device_name}: givaren {sensor_name} är inte konfigurerad` |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, sex översättningar.
- API-återläsning: klar. Rätt nyckel och översättnings-ID, målspråk `sv` och
  `is_unverified=false` för samtliga sex.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot kontrollfilen.
- `msgfmt`: ej tillämpligt; katalogen är JSON-baserad och ingen PO-fil har
  exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.
