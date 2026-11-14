# Music Assistant Server – ABC Radio Network, batch 4

Datum: 2026-11-14

Komponent: `music-assistant/server`, filen
`music_assistant/translations/en.json`.

## Omfattning

Tio strängar för ABC Radio Networks regionala direktströmmar har granskats
rad för rad. Stations- och nätverksnamn behålls. Svenska geografiska namn
används för de regionala valen där de har etablerade svenska former.

## Status

- Lokal granskning: klar.
- Arkivering: klar i denna katalog.
- Lokalise-uppladdning: väntande; ingen verifierbar API-token hittades under
  de etablerade nyckelringsnamnen.
- Lokalise-granskning, kodsynkronisering och release: ej verifierade.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är stationsnamn, ACT och
  geografiska namn.
- Aktuell källa: alla tio nycklar matchar den hämtade `en.json` exakt.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte gettext/PO.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den granskade lokala deltafilen finns i `reviewed.json`.
