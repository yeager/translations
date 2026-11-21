# Home Assistant – Abode: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `abode`

## Underlag

- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 27/27 exakta komponentnycklar med både engelsk källa och svensk måltext.
- Ingen tidigare Abode-rapport hittades i `yeager/translations`; granskningen återanvänder alltså inga odokumenterade förslag.

## Resultat

Samtliga 27 svenska strängar kontrollerades mot aktuell engelsk källa och sitt nyckelsammanhang. Ingen ändring behövde sparas.

Särskilt kontrollerade uttryck omfattar `MFA-kod`, `Abode-konto`, `Entitets-ID`, `Abode-systeminställning`, `bildtagning` och `automatisering`. De är begripliga, konsekventa med Home Assistant-termer och bevarar produktnamnet Abode.

Platshållarkontrollen för hela komponenten gav 0 avvikelser; `{error}` är bevarad i `component::abode::exceptions::change_setting_failed::message`.

## Verktyg

- `hunspell-sv`: träffar endast Abode, MFA, `{error}` och sammansättningar med produktnamnet; inga svenska stavningsfel.
- `svlang check`: 10,0/10. Abode är en förväntad produktnamnsträff.
- Manuell format- och platshållarkontroll: inga avvikelser.

## Status

Inga lokala, osparade svenska förslag finns för Abode. Komponenten är dokumenterad som granskad mot dagens Lokalise-data.