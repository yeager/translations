# Music Assistant Server – nätverk och innehåll, batch 2

Datum: 2026-11-14

Komponent: `music-assistant/server`, filen
`music_assistant/translations/en.json`.

## Omfattning

20 strängar har granskats rad för rad: TCP-bindning, konfiguration av ansluten
enhet, återställning av autentisering, OAuth-klient-ID, exponerade spelare och
medieinnehåll. Översättningarna följer den befintliga projektspecifika
terminologin, bland annat *insticksmodul*, *spelare*, *övertoning* och
*samplingsfrekvens*.

## Status

- Lokal granskning: klar.
- Arkivering: klar i denna katalog.
- Lokalise-uppladdning: väntande; ingen verifierbar API-token hittades under
  de etablerade nyckelringsnamnen.
- Lokalise-granskning, kodsynkronisering och release: ej verifierade.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är Music Assistant och OAuth.
- Aktuell källa: alla 20 nycklar matchar den hämtade `en.json` exakt.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte gettext/PO.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den granskade lokala deltafilen finns i `reviewed.json`.
