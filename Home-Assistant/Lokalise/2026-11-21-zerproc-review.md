# Home Assistant – Zerproc: svensk radgranskning

Datum: 2026-11-21  
Komponent: `zerproc`  
Omfattning: 1/1 aktuell källsträng

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::zerproc::config::step::confirm::description` | Do you want to start setup? | Vill du starta installationen? | Oförändrad | Korrekt och tydlig formulering. |

## Verifiering

- Den lokala källfilen använder referensen `[%key:common::config_flow::description::confirm_setup%]`; Lokalise API gav den upplösta aktuella engelska källtexten.
- `l10n-lint`: inga problem.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom den sparade översättningen redan är korrekt.

## Utökad export, 2026-11-21

Två ytterligare konfigurationssträngar fanns i den aktuella exporten. `no_devices_found` är korrekt. `component::zerproc::config::abort::single_instance_allowed` sparades som `Redan konfigurerad. Endast en konfiguration är möjlig.` i stället för `… kan göras.` och API-återlästes. TMX-manifest: `Home-Assistant/2026-11-21-zerproc-verified.json`.
