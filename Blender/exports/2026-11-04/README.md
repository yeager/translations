# Blender-exporter 2026-11-04

Detta är en rå, skrivskyddad arkivkopia av de svenska Blender-exporter som
hämtades den 4 november 2026. Ändra inte filerna direkt. Eventuella rättelser
ska först granskas i en delmängd och sedan skickas till rätt Blender
Translate-komponent.

## Källor och dubbletter

Tio filer hämtades. Tre av dem var byte-identiska web UI-exporter och sparas
en gång under namnet `blender-manual-manual-web-ui-4-5-sv.po`:

- `blender-manual-manual-web-ui-sv.po`
- `blender-manual-manual-web-ui-5-2-sv.po`
- `blender-manual-manual-web-ui-5-3-sv.po`

De har SHA-256
`fdf47859cac26b686cbcbf1e748f3846b0d685d3ccd3a70a5ea610dc9ea94524`.
Övriga filer nedan är skilda snapshots och har därför arkiverats var för sig.

| Fil | SHA-256 | PO-poster | Första automatiska resultat |
| --- | --- | ---: | --- |
| `blender-ui-ui-sv.po` | `2dff2e6f5a04d19041edb980faa2f7fad67293a9c54ef599b3e05916af7e398b` | 40 427 | l10n-lint: 0 fel, 50 varningar |
| `blender-manual-manual-4-5-sv.po` | `72c977e72c1701e871bad8be1e44206205c104b3895016d3f258b7ecccdaddce` | 41 880 | 26 fuzzy, 8 tomma; l10n-lint: 11 fel, 271 varningar |
| `blender-manual-manual-5-2-sv.po` | `21b5b0139826d8fb5fefab4dca7caeb003e864c936f7205e4722fb9c6332d3b9` | 46 699 | 4 633 fuzzy, 3 837 tomma; l10n-lint: 3 842 fel, 5 734 varningar |
| `blender-manual-manual-5-3-sv.po` | `d2e27c8f35b7e8800ad61dc2eeac4b02080bc116f752eb24a6eb7ef276e97c61` | 47 983 | 5 423 fuzzy, 4 714 tomma; l10n-lint: 4 722 fel, 6 703 varningar |
| `blender-manual-manual-sv.po` | `1b852be7ff62e5053a7875540491f4aa87861ffcc7052d51a504a4bd3f5d13ad` | 47 986 | 5 424 fuzzy, 4 716 tomma; l10n-lint: 4 724 fel, 6 704 varningar |
| `blender-manual-manual-web-ui-4-5-sv.po` | `e8e54ff6d75a6b79273eea5f75823e11b86d2e00b97d3fee929bc58d4e9fe511` | 14 | l10n-lint: inga träffar |
| `blender-manual-glossary-sv.tbx` | `2017f6fde28afdf964849ae8c31b5c33e852ffa0e72488bca58d186786456883` | 5 termposter | XML/TBX kan läsas |

L10n-lints felantal för manualerna omfattar främst fuzzy- och tomma poster.
De är granskningsunderlag, inte ett påstående om att varje träff är ett
språkfel.

## Smart versionsgranskning

Granskningen utgår från den senaste fulla katalogen, 5.3, och jämför sedan
endast unika eller avvikande poster i äldre versioner:

| Jämförelse | Poster bara i den äldre versionen | Gemensamma poster med avvikande måltext |
| --- | ---: | ---: |
| 4.5 jämfört med 5.3 | 4 167 | 53 |
| 5.2 jämfört med 5.3 | 476 | 0 |
| standardmanual jämfört med 5.3 | 4 | 1 |

Detta undviker att samma 46 000–48 000 manualposter granskas flera gånger.
Fuzzy- och tomma poster granskas först inom respektive unika mängd, därefter
språk-, format- och terminologiträffar i kontext.

## Formatavgränsning

`msgfmt` godkänner UI-filen och web UI-filen. Manualfilerna innehåller
export-/källrelaterade hinder som ska hållas isär från svensk språkgranskning:

- Manual 4.5, 5.2 och 5.3 har en `python-format`-flagga på en brödtext med
  `100 %`. Samma procenttal finns i både källa och mål; svensk text ska inte
  ändras för att kringgå en felaktig formatflagga.
- 5.2, 5.3 och standardmanualen innehåller dubblettdefinitioner enligt
  `msgfmt`. PO-posterna kan ändå läsas med kontextnyckel och jämförs på den
  nivån i granskningsarbetet.

Se [../../TERMINOLOGY.md](../../TERMINOLOGY.md) för den gemensamma
Blender-terminologin och [../../REVIEW-2026-11-04.md](../../REVIEW-2026-11-04.md)
för tidigare UI-granskning.
