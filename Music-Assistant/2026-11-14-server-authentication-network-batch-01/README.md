# Music Assistant Server – autentisering och nätverk, batch 1

Datum: 2026-11-14

Komponent: `music-assistant/server`, filen
`music_assistant/translations/en.json`.

## Omfattning

Åtta strängar har granskats rad för rad i respektive konfigurationskontext:
inloggning med enhetskod, QR-kod för Yandex och serverns avancerade
nätverksbindning. IP-adressen, IPv4/IPv6 och radbrytningarna i den längre
beskrivningen är bevarade.

## Status

- Lokal granskning: klar.
- Arkivering: klar i denna katalog.
- Lokalise-uppladdning: väntande; ingen verifierbar API-token hittades under
  de etablerade nyckelringsnamnen.
- Lokalise-granskning, kodsynkronisering och release: ej verifierade.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är Yandex-appen och
  sammansättningen *enhetskod*.
- Radbrytningar: käll- och måltext har tre rader.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte gettext/PO.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den granskade lokala deltafilen finns i `reviewed.json`.
