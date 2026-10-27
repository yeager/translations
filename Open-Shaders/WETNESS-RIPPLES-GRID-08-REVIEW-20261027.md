# Våteffekter: krusningar och rutnät, häfte 08

## Omfattning

Häftet omfattar 16 oarkiverade reglage och hjälptexter för krusningar, stänk,
väta och regndropparnas rumsliga rutnät.

## Språkval

- `ripples` är **krusningar** och `splashes` är **stänk**. De betecknar olika
  vatteneffekter och hålls därför isär.
- `vanilla` är **ursprunglig**, i enlighet med övriga funktionsprofiler.
- Grafikparametern `roughness` är **ytgrovhet**, inte en allmän beskrivning
  av gräsets utseende.
- `wetness effect` är **våteffekt**, med långt å. `väteffekt` skulle betyda
  en effekt som hör till väte och är därför fel i sammanhanget.
- Formattal och enheter behålls exakt: `%.2f m (%.1f enheter)`.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 10,0 av 10.
Hunspell markerar formatfragmenten `.1f` och `.2f` samt fackorden
`våteffekt` och `ytgrovhet`; de ska behållas.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
