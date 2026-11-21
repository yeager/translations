# Home Assistant – AirVisual Pro: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `airvisual_pro`

## Underlag och verifiering

Alla tolv aktuella strängar jämfördes med `homeassistant/components/airvisual_pro/strings.json` och Lokalise API. `l10n-lint` godkände de komponentegna strängarna. Svlang/hunspell-träffar gäller produktnamnet AirVisual och sensorbeteckningen PM0,1, vilka bevaras.

## Resultat

- Konfigurationsreferenserna för enhet, anslutning, autentisering, värd och lösenord är korrekt upplösta på svenska.
- Den återanvända beskrivningen “Lösenordet finns i användargränssnittet för AirVisual Pro.” är korrekt i båda förekomsterna.
- “Värdnamnet eller IP-adressen för din AirVisual Pro-enhet.” är korrekt.
- “Index för luftkvalitet utomhus” är korrekt.
- `PM0,1` behålls: etiketten följer svensk decimalnotation, samtidigt som PM-beteckningen är igenkännbar.

Inga ändringar behövde sparas i Lokalise.