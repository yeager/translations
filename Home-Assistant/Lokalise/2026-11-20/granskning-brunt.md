# Home Assistant Core – Brunt

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/brunt/strings.json`  
Lokalise: läsning av `component::brunt`; inga skrivningar har gjorts.

## Resultat

Samtliga **10 aktuella** källsträngar har lästs i Lokalise och jämförts med
aktuell Core-källa. Inga ändringsförslag har identifierats.

- `Konfigurera din Brunt-integration` är idiomatisk och korrekt.
- `Ange lösenordet för {username} på nytt.` återger återautentiseringsflödet
  korrekt och behåller platshållaren.
- De övriga åtta aktiva nycklarna är delade referenser och är intakta.

`svlang` godkände den fria återautentiseringstexten. Hunspell-träffen gäller
endast platshållaren `{username}`.

## Historisk Lokalise-rad

`component::brunt::config::abort::reauth_successful` finns i Lokalise men
saknas i aktuell `strings.json`. Den behandlas som historisk.

## TMX och Lokalise

Inga värden har sparats eller återlästs som ändrade i Lokalise. Home
Assistant-TMX:en ändras därför inte.
