# Home Assistant Core – Fibaro

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/fibaro/strings.json`  
Lokalise: läsning av `component::fibaro`; inga skrivningar har gjorts.

## Resultat

Samtliga **16 aktuella** källsträngar har lästs i Lokalise och jämförts med den
aktuella Core-källan. Inga ändringsförslag har identifierats. Svenska texter,
referenser, platshållaren `{username}` och produkttermerna är korrekta i sitt
sammanhang.

Kontrollerat omfattning:

- konfigurationsfel och redan-konfigurerad-avbrott;
- användaruppgifter och beskrivningar, inklusive hubbens URL och import av
  Fibaro-plugins/quickapps;
- återautentisering, inklusive lösenordsbeskrivning och `{username}`.

## Historisk Lokalise-rad

`component::fibaro::config::abort::reauth_successful` visas fortfarande i
Lokalise, men saknas i aktuell `strings.json`. Den behandlas som historisk och
har varken föreslagits för ändring eller förts in i TMX som en aktuell
Lokalise-verifierad post.

## TMX och Lokalise

Inga värden har sparats eller återlästs som ändrade i Lokalise. Därför görs
ingen ändring i Home Assistant-TMX:en; den ska fortsätta skilja mellan
verifierade sparade värden och lokala granskningsförslag.
