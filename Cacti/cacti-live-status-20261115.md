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

Cacti Translates Weblate visar komponenter och API-data, men uppladdningsvyn svarade upprepade gånger med Cloudflare-fel 520 den 2026-11-15. Weblate API fungerar däremot och användes för Mactrack, Syslog och MikroTik. I MikroTik-batch 01 förekom `End Date Selector` i två delbatcher; den deduplicerades före importen, medan rådeltafilerna bevarades oförändrade.
