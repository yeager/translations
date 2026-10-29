# Open Shaders: bildgenerering, granskning 4

Det fjärde uppskalningshäftet innehåller 25 nycklar för bildgenerering,
bildfrekvensgränser och FSR4-reservvägar.

`Frame generation` har översatts med `bildgenerering`. DLSS, FSR, TAA, SDK
och varumärkesnamnen är avsiktligt bevarade. Körtidsfel uttrycks utan det
engelska ordet `fallback`: FSR3 används som reserv när FSR4 inte kan användas.
Formatmarkören `%.2f` för den uppmätta uppdateringsfrekvensen är oförändrad.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar enbart produktnamn, förkortningar och engelska delar av
  de officiella varumärkesnamnen.
- Filen kräver ny exportjämförelse före import till den fortfarande låsta
  Weblate-komponenten.
