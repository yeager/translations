# Home Assistant Core – Airzone MQTT, svenska

Datum: 2026-11-15

Tre Airzone-strängar har granskats som en sammanhängande inställningsgrupp,
sparats i Lokalise och återlästs i den svenska målspråkskolumnen.

| Källa | Svenska |
| --- | --- |
| MQTT topic prefix configured on the Airzone WebServer. Leave empty to disable MQTT updates. | MQTT-ämnesprefix som har konfigurerats på Airzone-webbservern. Lämna tomt om du vill inaktivera MQTT-uppdateringar. |
| MQTT topic prefix | MQTT-ämnesprefix |
| Enter a valid MQTT topic prefix without wildcards. | Ange ett giltigt MQTT-ämnesprefix utan jokertecken. |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad i Lokalise: klar, tre strängar.
- Återläst i Lokalise: klar, tre strängar.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot den arkiverade
  kontrollfilen i denna batch.
- `msgfmt`: ej tillämpligt; Lokalise-källan är JSON-baserad och ingen PO-fil
  har exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.
