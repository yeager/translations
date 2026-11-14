# PrusaSlicer: svensk katalogavgränsning

Datum: 14 november 2026

## Underlag

Den aktuella huvudgrenen kontrollerades vid commit `e6c85c5`, daterad
6 november 2026. Den enda svenska PO-filen i arkivet är
`resources/localization/wx_locale/sv.po`.

Katalogens huvud visar `Project-Id-Version: wxWidgets 3.1` och dess
källhänvisningar går till wxWidgets, exempelvis `../src/common/` och
`../src/richtext/`. Den innehåller inte PrusaSlicers egna användargränssnitt.
PrusaSlicers egen lokaliseringsguide anger i stället språkmappar med filer som
`resources/localization/<språk>/PrusaSlicer_<språk>.po`. Någon svensk sådan
katalog finns inte i den aktuella huvudgrenen.

## Resultat

Katalogen har 1 672 översatta poster, 123 tomma och 96 luddiga. Dessa tal är
en status för den medföljande wxWidgets-översättningen, inte för
PrusaSlicers svenska UI. Projektets guide säger uttryckligen att de
wxWidgets-poster som följer med inte ska ändras, eftersom de återställs vid
nästa synkning. En massrättning här skulle därför ha fel projektomfattning
och har inte gjorts.

`msgfmt --check` passerar trots dessa historiska ofärdiga poster.
l10n-lint rapporterar bland annat format-, snabbtangents- och
tomsträngsproblem i ramverkskatalogen. Ingen svensk PrusaSlicer-text har
ändrats, ingen upstreamändring är inskickad och ingen upstreamstatus påstås.

## Nästa steg

Eftersom en svensk PrusaSlicer-katalog saknas behöver svenskt språkstöd
initieras som en egen, större insats från den aktuella POT-filen. Det kräver
en separat prioritering och en komplett kontextgranskning före inskick.
