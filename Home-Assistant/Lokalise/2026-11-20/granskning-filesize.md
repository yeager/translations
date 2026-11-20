# Home Assistant Core – Filesize

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/filesize/strings.json`  
Lokalise: läsning av `component::filesize`; inga skrivningar har gjorts.

## Resultat

Samtliga **10 aktuella** källsträngar har lästs i Lokalise och jämförts med
aktuell Core-källa. Inga ändringsförslag har identifierats.

- `Sökväg till filen`, `Sökvägen är inte giltig` och `Sökvägen är inte
  tillåten` återger källan idiomatiskt och konsekvent.
- Sensorbenämningarna `Skapad`, `Senast uppdaterad`, `Storlek` och `Storlek i
  byte` är korrekta i kontexten.
- `Filstorlek` är en etablerad och lämplig komponenttitel.
- Den delade `file_path`-referensen och den delade
  `already_configured_service`-referensen är intakta.

`hunspell-sv` gav inga träffar för de fria svenska översättningarna och
`svlang` godkände kontrollmeningen `Sökvägen är inte tillåten.`.

## Historisk Lokalise-rad

`component::filesize::config::abort::reconfigure_successful` finns i
Lokalise men inte i aktuell `strings.json`. Den är därför historisk och ingår
inte i den aktiva omfattningen eller i TMX som Lokalise-verifierat aktuellt
värde.

## TMX och Lokalise

Inga värden har sparats eller återlästs som ändrade i Lokalise. Home
Assistant-TMX:en ändras därför inte.
