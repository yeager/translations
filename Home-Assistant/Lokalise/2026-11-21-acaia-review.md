# Home Assistant – Acaia: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `acaia`

## Underlag

- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 17/17 exakta komponentnycklar med engelsk källa och svensk måltext.
- Ingen tidigare Acaia-rapport hittades i `yeager/translations`.

## Sparad och återläst ändring

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::acaia::entity::button::tare::name` | Tare | Nollställ | Tarera | Funktionen på en våg tarerar vikten; ”Nollställ” är mindre exakt och kan förväxlas med återställning. |

Ändringen skickades via Lokalise API och lästes tillbaka från samma nyckel.

## Övrig kontroll

Resterande 16 strängar kontrollerades mot aktuell källa. `Acaia-våg`, `Tidsgräns för frånkoppling vid inaktivitet`, `Starta/stoppa timer` och platshållaren `{name}` är korrekta. Inga ytterligare säkra ändringar identifierades.

## Status

Komponenten är granskad mot aktuell Lokalise-data. Inga lokala, osparade svenska förslag återstår.