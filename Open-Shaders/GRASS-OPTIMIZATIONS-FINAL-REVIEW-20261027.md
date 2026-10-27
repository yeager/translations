# Open Shaders: gräsoptimeringar, slutreglage, häfte 86

Detta häfte omfattar de nio sista tidigare oarkiverade nycklarna för
gräsoptimeringar: ocklusionsgallring, renderingsavstånd och förenklad
skuggning. Källtexterna har jämförts med Open Shaders `dev` vid revision
`c1b1ef1` den 27 oktober 2026 och med den svenska Weblate-exporten från
19 oktober 2026.

*Occlusion culling* blir *ocklusionsgallring* och *occlusion bias* blir
*ocklusionsförskjutning*. Förkortningarna NPC och INI samt
konfigurationsnycklarna i hjälptexten lämnas orörda.

`open-shaders-grass-optimizations-final-sv-20261027.json` är ett delta på nio
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar och
konfigurationsnycklar matchar den engelska katalogen. `svlang` rapporterar
två felaktiga V2-varningar och ett stavningsfel i den bevarade
konfigurationsnyckeln `fGrassStartFadeDistance`. Hunspell markerar bara
`NPC`, de bevarade konfigurationsnycklarna och tekniska sammansättningar.
