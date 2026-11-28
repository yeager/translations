# WebKitGTK — svenska, `main/po`

Granskad 2026-11-28 mot den aktuella POT-filen från GNOME Damned Lies. Gren: `main`.

- [GNOME-katalogens aktivitetssida](https://l10n.gnome.org/vertimus/webkit/main/po/sv/)
- [Aktuell POT](https://l10n.gnome.org/POT/webkit.main/webkit.main.pot)
- [Aktuell svensk PO](https://l10n.gnome.org/POT/webkit.main/webkit.main.sv.po)
- Hämtad POT SHA-256: `9033eb72b62067662b616937ec92775791a5b55065e6482630c775282228e4d0`
- Hämtad PO SHA-256: `7e4c94034e5276ee1c416e74afe7b4250396331864f768f3cdcf0e9d7b544ca6`

## Resultat

| Mätning | Före | Efter lokal granskning |
|---|---:|---:|
| Aktiva strängar enligt POT | 517 | 517 |
| Översatta | 516 | 517 |
| Fuzzy | 1 | 0 |
| Oöversatta | 0 | 0 |
| Ändrade översättningstexter | — | 170 |
| Tidigare fuzzy-poster radgranskade | — | 1 |

Ingen sträng var helt tom från början. En fuzzy-markerad post har granskats, korrigerats och avmarkerats. De återstående ändringarna rättar bland annat acceleratorplacering, webb- och hjälpmedelstermer, mediekontroller, typografi, inställningsbeskrivningar och grammatik. Termen för accessibility/a11y följer instruktionen att använda **hjälpmedel**.

## Kontroller

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy`: godkänd mot aktuell POT.
- Egen kontroll mot POT: 0 strukturella fel; alla 517 poster översatta; 0 fuzzy och 0 oöversatta. Platshållare, pluralformer, markup, URL:er och acceleratorantal stämmer. Inga acceleratorer använder `å`, `ä` eller `ö`.
- `l10n-lint --language sv --no-terminology`: 0 fel, 0 varningar. Informationsmeddelandena gäller mnemonicens flytt inom översatta etiketter och längden på tre korta kommandon som behöver längre svenska formuleringar.
- `hunspell-sv` kördes på katalogen. Rimliga tekniska och sammansatta ord dokumenteras i [`hunspell-exceptions.md`](hunspell-exceptions.md); full utdata finns i [`hunspell-output.txt`](hunspell-output.txt).
- Översättningsminnet `swedish-tm` konsulterades; se [`tm-check.md`](tm-check.md). Osäkra eller mindre idiomatiska äldre TM-träffar användes inte.

## Inskickning

Ingen ändring har skickats till GNOME Damned Lies.
