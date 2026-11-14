# PrusaSlicer: svensk katalogavgränsning

Datum: 14 november 2026

## Underlag

Den aktuella huvudgrenen kontrollerades vid commit `e6c85c5`, daterad
6 november 2026. Den enda svenska PO-filen i arkivet är
`resources/localization/wx_locale/sv.po`.

Katalogens huvud visar `Project-Id-Version: wxWidgets 3.1` och dess
källhänvisningar går till wxWidgets, exempelvis `../src/common/` och
`../src/richtext/`. Den innehåller inte PrusaSlicers egna användargränssnitt.

## Resultat

Katalogen har 1 672 översatta poster, 123 tomma och 96 luddiga. Dessa tal är
en status för den medföljande wxWidgets-översättningen, inte för
PrusaSlicers svenska UI. En massrättning här skulle därför ha fel
projektomfattning och har inte gjorts.

`msgfmt --check` passerar trots dessa historiska ofärdiga poster.
l10n-lint rapporterar bland annat format-, snabbtangents- och
tomsträngsproblem i ramverkskatalogen. Ingen svensk PrusaSlicer-text har
ändrats, ingen upstreamändring är inskickad och ingen upstreamstatus påstås.

## Nästa steg

Identifiera först PrusaSlicers etablerade kanal för dess egna svenska UI och
hämta den aktuella resursen därifrån. Därefter kan en kontextgranskad batch
tas fram.
