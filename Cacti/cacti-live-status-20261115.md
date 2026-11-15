# Cacti, svensk live-status 2026-11-15

Källa: Cacti Translates offentliga Weblate-API och komponentexporter.

## Verifierad komponentstatus

- `routerconfigs`: 381/381 översatta efter tre importerade batcher.
- `wmi`: 168/168 översatta efter två importerade batcher.
- `mactrack`: deltafil med fyra korrigeringar importerad via Weblate API;
  importsvaret accepterade 4/4 strängar och en uppdaterad sträng återlästes
  ur den aktuella PO-exporten.
- Övriga komponenter utom `mikrotik` och `syslog`: 100 % översatta enligt aktuell API-avläsning.

## Färdiga men väntande Weblate-importer

| Komponent | Deltafiler | Strängar | Status |
| --- | --- | ---: | --- |
| `syslog` | `cacti-syslog-sv-batch01-20261115.po` | 6 | Lokalt validerad och arkiverad; ej importerad. |
| `mikrotik` | `cacti-mikrotik-sv-batch01a-20261115.po`, `cacti-mikrotik-sv-batch01b-20261115.po`, `cacti-mikrotik-sv-batch02-20261115.po` | 39 | Lokalt validerad och arkiverad i tre små importer; ej importerad. |

## Upstreamblockerare

Cacti Translates Weblate visar komponenter och API-data, men uppladdningsvyn svarade upprepade gånger med Cloudflare-fel 520 den 2026-11-15. Weblate API fungerar däremot och användes för Mactrack. Syslog och MikroTik ska importeras komponentvis via samma API och läsas tillbaka efter varje import.
