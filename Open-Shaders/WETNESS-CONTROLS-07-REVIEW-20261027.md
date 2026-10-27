# Våteffekter: reglage och status, häfte 07

## Omfattning

Häftet innehåller 16 oarkiverade nycklar för klimatförinställningarnas
status, funktionsbeskrivning och reglage.

## Språkval

- `preset` är konsekvent **förinställning** och `override` är konsekvent
  **åsidosättning**, enligt tidigare Open Shaders-häften.
- `shader state` blir **shaderläge**, ett etablerat tekniskt gränssnittsord
  som här är tydligare än en omskrivning med flera ord.
- `trails` återges som **rännilar** för vatten som rinner längs modeller;
  det skiljer företeelsen från spår i marken.
- `wet drops` är **våta droppar på karaktärer**, eftersom det är en
  reglageetikett och inte ett påstående om permanent fukt.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 8,8 av 10;
V2-varningen för uppmaningen `Välj … för att …` är en felträff. Hunspell
markerar endast `shaderläge`, ett medvetet tekniskt gränssnittsord.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
