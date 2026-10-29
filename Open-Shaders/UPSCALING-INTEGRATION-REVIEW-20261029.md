# Open Shaders: uppskalning, integrationsgranskning 2026-10-29

Samtliga 286 aktuella nycklar i `feature.upscaling` är nu granskade och
arkiverade i tolv små JSON-häften. En nyckeluppsättningsjämförelse mot den
lokala engelska katalogen visar 286 av 286 nycklar, utan saknade eller extra
nycklar.

Komponenten omfattar DLSS, FSR, bildgenerering, foveerad uppskalning, Reflex,
Neural Rendering och VR-reglage. Varumärken, DLL-namn, sökvägar och
formatmarkörer är bevarade där de är tekniska värden. Svenska termer omfattar
bland annat `uppskalningsförinställning`, `bildgenerering`, `bildfrekvensgräns`
och `foveerad uppskalning`.

Varje häfte har kontrollerats med JSON-syntax, nyckel- och
formatmarkörjämförelse, `l10n-lint`, `svlang skrivregler`, Hunspellgenomgång
och Gitleaks. De sammansatta fackorden och produktnamnen i Hunspell-utfallen
har bedömts manuellt.

Weblate-komponenten är fortfarande låst. Vid upplåsning ska varje häfte
jämföras mot en ny måltextexport före import, eftersom den lokala källan och
den äldre Weblate-statusen skiljer sig med fyra historiska nycklar.
