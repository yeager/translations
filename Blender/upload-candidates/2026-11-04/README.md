# Blender Manual – uppladdningskandidater 5 november 2026

Källa: de radvis granskade deltafilerna
`../../blender-manual-sv-review-batch-20261104-01.po` till och med
`../../blender-manual-sv-review-batch-20261104-69.po`.

`create-manual-upload-batches.py` bygger först en samlad PO med `msgcat
--use-first --no-location` och delar sedan den i Weblate-säkra filer. Den
sammanlagda katalogen innehåller 868 översatta meddelanden enligt `msgfmt`.

| Fil | Översatta meddelanden | Status |
| --- | ---: | --- |
| `blender-manual-sv-reviewed-01.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-02.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-03.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-04.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-05.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-06.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-07.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-08.po` | 100 | Ingår i den samlade, importerade filen |
| `blender-manual-sv-reviewed-09.po` | 68 | Ingår i den samlade, importerade filen |

## Kontroller

- Varje kandidat och den samlade katalogen passerar `msgfmt --check`.
- Varje kandidat har körts genom l10n-lint, svlang och Hunspell. Inga fel
  hittades. Kvarvarande varningar är dokumenterade kontextundantag:
  maskinläsbara glTF/USD/SPDX-värden, kodliteral som `startup.blend`, URL:er
  med `issues` eller `features`, `scope-namn` i GPU-felsökning, bokstavliga
  datumformat och den avsiktliga menystigen `Visa --> Visa skjutreglage`.
- `git diff --check` passerar för generatorn och kandidatfilerna.
- Gitleaks har skannat hela kandidatkatalogen utan träffar.
- Terminologin är avstämd mot den aktuella Blender-dokumentationen,
  Blender-UI-katalogen, projektets svenska översättningsminne och
  `Blender/TERMINOLOGY.md`. Rigify använder här bland annat *underrigg*,
  *finjusteringskontroll*, *vridpunkt*, *nyckelbildruta* och
  *Child Of-begränsning*.
- Råexporten i `../../exports/2026-11-04/` har inte ändrats. Den innehåller
  58 dubbla PO-definitioner och kan därför inte valideras direkt med
  `msgattrib`; de separata deltafilerna och de genererade kandidaterna är
  däremot giltiga och har validerats med `msgfmt`.

För en samlad uppladdning används
`blender-manual-sv-reviewed-all.po` till den **generiska**
Manual-komponenten, inte till versionskomponenterna 4.5, 5.2 eller 5.3.
Den innehåller 868 granskade meddelanden och ersätter de numrerade filerna
som uppladdningsunderlag.

## Verifierad importstatus

Den samlade filen importerades den 5 november 2026 till den generiska
Manual-komponenten via Blender Translate i läget *Lägg till som översättning*.
Historiken visar 868 bearbetade meddelanden: 856 uppdaterade, 11 hoppade över
och 1 hittades inte. En efterföljande dubblettimport uppdaterade 0
meddelanden, hoppade över 867 och hittade inte samma 1 meddelande.

Den enda saknade nyckeln ska identifieras från en färsk export. Resultatet
gäller denna deltaimport; det innebär inte att hela Manual-komponenten är
färdiggranskad eller uppströmsgranskad.
