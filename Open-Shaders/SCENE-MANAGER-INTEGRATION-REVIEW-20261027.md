# Scene Manager — integrationsgranskning 2026-10-27

## Täckning

De elva komponenthäftena har sammanfogats temporärt och jämförts med den
aktuella engelska källkatalogen. Resultatet är **170 av 170** nycklar, utan
saknade eller extra nycklar och utan motstridiga dubbletter.

## Automatiska kontroller

- JSON-syntax: godkänd.
- `l10n-lint`: inga fel.
- Gitleaks: inga hemligheter.
- Formatmarkörer, bokstavliga procenttecken och radbrytningar: identiska med
  källan för alla 170 nycklar.
- Hunspell: återstående träffar är dokumenterade produkttermer,
  förkortningar, platshållaren `{target}` och korrekt bildade
  sammansättningar, exempelvis `åsidosättningsfiler`.

## Språkgranskning

Alla batcher har granskats radvis. Den sammanslagna UI-katalogen får 0/10 av
`svlang` eftersom dess frekvensbaserade mått tolkar korta etiketter och
tekniska sammansättningar som ovanliga. De tolv specifika V2-varningarna är
grammatiskt korrekta imperativ, etikettfragment eller vanliga svenska
huvudsatser. Anglicismträffen gäller platshållaren `{feature}`. Ingen av
träffarna kräver ändring.

## Upstreamläge

Komponenten är klar lokalt men fortfarande låst i Hosted Weblate. Jämför med
en färsk export när låsningen har hävts innan de elva små deltafilerna importeras.
