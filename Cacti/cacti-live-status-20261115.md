# Cacti, svensk live-status 2026-11-15

Källa: Cacti Translates offentliga Weblate-API och komponentexporter.

## Verifierad komponentstatus

- `routerconfigs`: 381/381 översatta efter tre importerade batcher.
- `wmi`: 168/168 översatta efter två importerade batcher.
- `mactrack`: deltafil med fyra korrigeringar importerad via Weblate API;
  importsvaret accepterade 4/4 strängar och en uppdaterad sträng återlästes
  ur den aktuella PO-exporten.
- `syslog`: deltafil med sex korrigeringar importerad via Weblate API;
  importsvaret accepterade 6/6 strängar och tidsstämpelprecisionen
  återlästes ur den aktuella PO-exporten.
- `mikrotik`: tre deduplicerade API-importer accepterade 17 + 17 + 5
  strängar. `Presets`, `End Date Selector` och `No Health Sensors Found`
  återlästes ur den aktuella PO-exporten.
- Övriga komponenter: 100 % översatta enligt aktuell API-avläsning.

## Färdiga men väntande Weblate-importer

| Komponent | Deltafiler | Strängar | Status |
| --- | --- | ---: | --- |
| – | – | – | Inga väntande Cacti-importer i denna batch. |

## Upstreamblockerare

Cacti Translates Weblate visade tidigare Cloudflare-fel 520 i uppladdningsvyn
den 15 november 2026. API:t svarar nu normalt och användes för omkontroll av
de redan arkiverade deltabatcherna. Ingen aktuell API-blockerare kvarstår.

## Verifierad API-import, 15 november 2026 kl. 16:01–16:02

Följande tidigare validerade deltafiler skickades separat via Weblate API med
läget `translate` och konflikthanteringen `replace-translated`:

| Komponent | Deltafil | Behandlade | Överhoppade | Uppdaterade | Saknade |
| --- | --- | ---: | ---: | ---: | ---: |
| Mactrack | `cacti-mactrack-sv-vendor-list-20261026.delta.po` | 2 | 2 | 0 | 0 |
| Syslog | `cacti-syslog-sv-batch01-20261115.po` | 6 | 6 | 0 | 0 |
| MikroTik | `cacti-mikrotik-sv-batch01-20261115.po` | 34 | 34 | 0 | 0 |
| MikroTik | `cacti-mikrotik-sv-batch01b-20261115.po` | 18 | 18 | 0 | 0 |

Weblate bekräftade HTTP 200 för varje import. Alla 60 översättningar var
redan identiska med den aktuella svenska upstreamtexten. Inget skickades som
en ny serverändring och inga källsträngar saknades. Batchernas `msgfmt`,
`l10n-lint`, `svlang`, diffkontroll och Gitleaks är godkända; `msgfmt` varnar
för avsiktligt minimala deltafilshuvuden i Syslog och MikroTik, inte för
översättningssyntax eller format.
