# Home Assistant Core: Xiaomi Miio — entitetsetiketter

Tio tydliga språk- och sammansättningsrättningar sparades via Lokalise API och återlästes:

- `delay_off_countdown`: svensk formulering i stället för engelska `delay off`.
- `favorite_rpm` och två LED-ljusstyrkeetiketter: korrekta sammansättningar.
- `air_quality`: `Luftkvalitet`.
- Rengöringsområde och tre städtidsetiketter: korrekt böjning och kompakta etiketter.
- Två DnD-etiketter: `Start för Stör ej` respektive `Slut för Stör ej`.

Fullständiga nycklar och värden finns i `Home-Assistant/2026-11-21-xiaomi-miio-entities-verified.json`; TMX validerad till 2 498 poster.

## Sammansättningar, tillägg

`filter_hours_used`, `load_power` och `purify_volume` sparades därefter som `Filteranvändning`, `Lasteffekt` respektive `Rengöringsvolym`. De är API-återlästa och spåras i `Home-Assistant/2026-11-21-xiaomi-miio-compounds-verified.json`.

## Underhållsetiketter, tillägg

Nio filter-, borste- och användningstidsetiketter har normaliserats till korrekta uttryck för återstående livslängd. Fullständig spårning finns i `Home-Assistant/2026-11-21-xiaomi-miio-maintenance-verified.json`; samtliga är API-återlästa.
