# Music Assistant Server – spelarens ljudfunktioner, batch 3

Datum: 2026-11-14

Komponent: `music-assistant/server`, filen
`music_assistant/translations/en.json`.

## Omfattning

18 namnetiketter för spelarens ljudfunktioner har granskats rad för rad:
fördröjning, balans, mono, surround, högtalare, subwoofer, statuslampor och
pekkontroller. Produktnamnet `Trueplay` och etablerade synliga ljudtermer
`Loudness`, `Mono` och `IR-repeater` bevaras avsiktligt.

## Status

- Lokal granskning: klar.
- Arkivering: klar i denna katalog.
- Lokalise-uppladdning: väntande; ingen verifierbar API-token hittades under
  de etablerade nyckelringsnamnen.
- Lokalise-granskning, kodsynkronisering och release: ej verifierade.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är avsiktligt bevarade
  ljudtekniska UI-namn och `Trueplay`.
- Aktuell källa: alla 18 nycklar matchar den hämtade `en.json` exakt.
- `msgfmt`: ej tillämpligt; resursen är JSON, inte gettext/PO.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den granskade lokala deltafilen finns i `reviewed.json`.
