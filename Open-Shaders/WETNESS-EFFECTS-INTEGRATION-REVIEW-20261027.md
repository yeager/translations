# Våteffekter: sammanslagen granskning 2026-10-27

## Omfattning

De 13 separata våteffektshäftena har slagits samman temporärt och jämförts
mot den aktuella engelska källkatalogen. De omfattar samtliga 201 aktuella
nycklar i `feature.wetness_effects`.

## Resultat

- Arkivet innehåller 201 av 201 källnycklar.
- Inga nycklar saknas och inga främmande nycklar finns i den sammanslagna
  katalogen.
- Samtliga formatmarkörer, bokstavliga procenttecken och radbrytningar är
  identiska med källan.
- JSON-syntax, `l10n-lint` och Gitleaks är godkända för den sammanslagna
  katalogen.
- `svlang` ger 0,0 av 10 för den sammanslagna UI-katalogen, eftersom
  frekvenslistan markerar 188 tekniska UI-ord som ovanliga och tio korrekta
  V2-konstruktioner som möjliga fel. Varje delta har dessutom granskats
  separat; språkpoängen där ligger mellan 7,6 och 10,0.
- Hunspell markerar formatfragment, produktnamn och tekniska
  sammansättningar som `pölbildning`, `regnväta`, `strandväta`, `ytväta`,
  `ytgrovhet` och `shaderläge`. De har kontrollerats manuellt och behålls.

## Upstreamstatus

Komponenten är lokalt komplett, men ingen import har gjorts. Hosted Weblate
har fortfarande komponenten låst. Efter upplåsning måste en ny export
jämföras innan de separata deltafilerna importeras.
