# Inkscape Weblate: svensk komponentinventering

Datum: 13 november 2026. Underlaget är direktavläst från Inkscape Weblate API.

## UI och terminologi

| Komponent | Status |
| --- | --- |
| Inkscape (dev) | 11 245 av 11 245 översatta, 0 fuzzy. Radgranskad; 340 Weblate-kontroller är kategoriserade utan verifierade fel. |
| Inkscape (1.4.x) | 10 913 av 10 913 översatta, 0 fuzzy. Unika poster har radgranskats mot utvecklingsgrenen; 331 Weblate-kontroller är kategoriserade utan verifierade fel. |
| Inkscape-glossarium | 0 svenska poster i API-svaret. Projektterminologin underhålls i `TERMINOLOGY.md`. |
| Windows store | Ingen svensk resurs exponerades av API:t. |

## Dokumentation

Komponenterna `man`, `keys` och handledningarna basic, advanced, calligraphy, elements, interpolate, shapes, tips, tracing och tracing-pixelart finns för både utvecklingsgrenen och 1.4.x. Den gemensamma svenska katalogen har nu granskats rad för rad lokalt; gemensamma strängar mellan versionerna har inte dubbelgranskats.

Nybörjarguiden omfattar 71 svenska PO-filer och handledningarna 11. Samtliga 82 lokala PO-filer har lästs rad för rad och har inga fuzzy-poster. `msgfmt` och `git diff --check` har passerat. `l10n-lint` har kvar varningar som måste tolkas per kontext, främst om avsiktliga UI-etiketter och dokumentationsmarkup.
