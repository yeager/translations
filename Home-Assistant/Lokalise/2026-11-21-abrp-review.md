# Home Assistant – ABRP: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `abrp`

## Underlag

- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 31/31 exakta komponentnycklar, med engelskt källvärde och svensk måltext.
- Ingen tidigare ABRP-rapport hittades i `yeager/translations`.

## Sparad och återläst ändring

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::abrp::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen för {name} har upphört | Autentiseringen för {name} har upphört att gälla | Det tidigare värdet var en ofullständig svensk sats. Platshållaren `{name}` bevarades. |

Ändringen skickades via Lokalise API och lästes tillbaka från samma nyckel.

## Övrig kontroll

Termerna `batterikapacitet`, `batteritemperatur`, `laddningsstatus`, `vägmätare`, `räckvidd`, `OAuth2-åtkomsttoken` och `A Better Routeplanner-konto` bedömdes korrekta i sitt sammanhang. Inga övriga säkra ändringar identifierades.

## Status

Komponenten är granskad mot aktuell Lokalise-data. Inga lokala, osparade svenska förslag återstår.